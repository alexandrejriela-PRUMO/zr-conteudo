"""Renderiza os slides do Zubiaurre & Riela Advogados Associados (1080x1350, JPEG).

Uso: python3 sistema/render.py posts/AAAA-MM-DD-slug/post.json posts/AAAA-MM-DD-slug
O post.json segue o modelo descrito em INSTRUCOES.md.

Identidade própria do escritório (diferente do PRUMO, escuro e "de sistema", e da Santa Rute,
creme, verde e com cara de campo):
- fundo branco-gelo frio, liso, com filetes finos: cara de publicação jurídica, sóbria;
- logo ZR (tirada do papel timbrado do escritório) em grafite, monograma no cabeçalho;
- títulos em serifa clássica (EB Garamond), grafite; destaque em dourado discreto itálico;
- texto corrido em Lato, cinza-grafite; numeração dos slides em algarismos romanos dourados;
- sem selo, sem botão, sem chamada de venda: o slide final é uma assinatura, como um cartão
  (nome do escritório, advogado, OAB e site), exigência do art. 44 do Código de Ética da OAB.
"""
import os, re, sys, json
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
W, H = 1080, 1350
FD = os.path.join(BASE, "fontes") + "/"
# EB Garamond (variável): o "peso" vai junto com o caminho, ex.: (arquivo, 600)
SERIF_B = (FD + "EBGaramond[wght].ttf", 600)
SERIF_SB = (FD + "EBGaramond[wght].ttf", 500)
SERIF_I = (FD + "EBGaramond-Italic[wght].ttf", 600)
SERIF_M = (FD + "EBGaramond[wght].ttf", 500)
SANS_R, SANS_B, SANS_I = FD + "Lato-Regular.ttf", FD + "Lato-Bold.ttf", FD + "Lato-Italic.ttf"

# Cores
FUNDO = (242, 243, 244)       # branco-gelo, frio (a Santa Rute é creme quente)
GRAFITE = (35, 39, 43)        # títulos e logo
TEXTO = (68, 74, 80)          # texto corrido
CINZA = (128, 134, 140)       # rótulos, rodapé
FILETE = (200, 203, 207)      # linhas finas
OURO = (163, 130, 76)         # dourado discreto (destaques, números)
OURO_CLARO = (201, 172, 120)
GRAFITE_FUNDO = (30, 33, 37)  # slide de assinatura
PRATA = (214, 217, 221)

ESCRITORIO = "Zubiaurre & Riela Advogados Associados"
ADVOGADO = "Alexandre Juliani Riela"
OAB = "OAB/RS 110.261"
SITE = "zradvogados.com.br"
M = 80  # margem lateral


_cache = {}


def font(p, s):
    chave = (p, s)
    if chave not in _cache:
        if isinstance(p, tuple):
            f = ImageFont.truetype(p[0], s)
            f.set_variation_by_axes([p[1]])
        else:
            f = ImageFont.truetype(p, s)
        _cache[chave] = f
    return _cache[chave]


# ---------- logo ----------

def _mascara(nome, alvo_h=None, alvo_w=None):
    m = Image.open(os.path.join(BASE, nome)).convert("L")
    r = (alvo_h / m.height) if alvo_h else (alvo_w / m.width)
    return m.resize((max(1, int(m.width * r)), max(1, int(m.height * r))), Image.LANCZOS)


def por_marca(im, nome, cor, x, y, alvo_h=None, alvo_w=None, opacidade=1.0):
    m = _mascara(nome, alvo_h, alvo_w)
    if opacidade < 1:
        m = m.point(lambda v: int(v * opacidade))
    camada = Image.new("RGBA", m.size, cor + (255,))
    camada.putalpha(m)
    im.alpha_composite(camada, (int(x), int(y)))
    return m.size


def cabecalho(im, d):
    """Monograma ZR + nome do escritório em caixa-alta espaçada, filete fino embaixo."""
    w, h = por_marca(im, "monograma-mascara.png", GRAFITE, M, 70, alvo_h=62)
    d.rectangle([M + w + 26, 74, M + w + 27, 128], fill=FILETE)
    espacado(d, M + w + 52, 78, "ZUBIAURRE & RIELA", font(SANS_B, 21), GRAFITE, 0.24)
    espacado(d, M + w + 52, 108, "ADVOGADOS ASSOCIADOS", font(SANS_R, 17), CINZA, 0.28)
    d.rectangle([M, 168, W - M, 168], fill=FILETE)


def rodape(d, esquerda, direita):
    y = H - 104
    d.rectangle([M, y, W - M, y], fill=FILETE)
    f = font(SANS_R, 22)
    espacado(d, M, y + 34, esquerda, f, CINZA, 0.12)
    fb = font(SANS_B, 22)
    larg = sum(d.textlength(c, font=fb) + fb.size * 0.12 for c in direita) - fb.size * 0.12
    espacado(d, W - M - larg, y + 34, direita, fb, OURO, 0.12)


# ---------- texto ----------

def quebra(texto, f, larg, d):
    linhas = []
    for par in texto.split("\n"):
        atual = ""
        for p in par.split():
            teste = (atual + " " + p).strip()
            if d.textlength(teste, font=f) <= larg:
                atual = teste
            else:
                linhas.append(atual)
                atual = p
        linhas.append(atual)
    return linhas


def espacado(d, x, y, texto, f, cor, track=0.2):
    cx = x
    for ch in texto:
        d.text((cx, y), ch, font=f, fill=cor)
        cx += d.textlength(ch, font=f) + f.size * track
    return cx


def bloco(d, x, y, texto, f, cor, larg, entre=1.45, centro=False):
    for ln in quebra(texto, f, larg, d):
        cx = (W - d.textlength(ln, font=f)) / 2 if centro else x
        d.text((cx, y), ln, font=f, fill=cor)
        y += int(f.size * entre)
    return y


def altura_bloco(d, texto, f, larg, entre=1.45):
    return len(quebra(texto, f, larg, d)) * int(f.size * entre)


def titulo(d, x, y, texto, tam, larg, destaque=None, cor=GRAFITE, cor_dest=OURO, entre=1.02, centro=False):
    """Título em serifa; palavras de destaque em dourado itálico."""
    destaque = [w.lower() for w in (destaque or [])]
    f, fi = font(SERIF_B, tam), font(SERIF_I, tam)
    for ln in quebra(texto, f, larg, d):
        palavras = ln.split(" ")
        dest = [re.sub(r"[^\wÀ-ú]", "", p).lower() in destaque for p in palavras]
        larg_ln = sum(d.textlength(p + " ", font=fi if e else f) for p, e in zip(palavras, dest)) - d.textlength(" ", font=f)
        cx = (W - larg_ln) / 2 if centro else x
        for p, e in zip(palavras, dest):
            ff = fi if e else f
            d.text((cx, y), p, font=ff, fill=cor_dest if e else cor)
            cx += d.textlength(p + " ", font=ff)
        y += int(tam * entre)
    return y


def altura_titulo(d, texto, tam, larg, entre=1.02):
    return len(quebra(texto, font(SERIF_B, tam), larg, d)) * int(tam * entre)


def rotulo(d, x, y, texto):
    """Rótulo do tema: traço dourado curto + caixa-alta espaçada em cinza."""
    d.rectangle([x, y + 13, x + 40, y + 15], fill=OURO)
    espacado(d, x + 58, y, texto.upper(), font(SANS_B, 22), CINZA, 0.26)


def romano(n):
    tab = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in tab:
        while n >= v:
            out += s
            n -= v
    return out


def base():
    im = Image.new("RGBA", (W, H), FUNDO + (255,))
    # monograma bem clarinho, cortado no canto inferior direito
    por_marca(im, "monograma-mascara.png", GRAFITE, W - 560, H - 520, alvo_h=470, opacidade=0.035)
    d = ImageDraw.Draw(im)
    cabecalho(im, d)
    return im, d


# ---------- slides ----------

def slide_capa(s, n, total):
    im, d = base()
    tam = s.get("tamanho", 100)
    fs = font(SANS_R, 36)
    h = 70 + altura_titulo(d, s["titulo"], tam, W - 2 * M) + (60 + altura_bloco(d, s.get("sub", ""), fs, W - 2 * M - 40) if s.get("sub") else 0)
    y0 = max(260, 190 + (H - 120 - 190 - h) // 2)
    rotulo(d, M, y0, s["selo"])
    y = titulo(d, M, y0 + 70, s["titulo"], tam, W - 2 * M, s.get("destaque"))
    if s.get("sub"):
        d.rectangle([M, y + 26, M + 90, y + 28], fill=OURO)
        bloco(d, M, y + 60, s["sub"], fs, TEXTO, W - 2 * M - 40)
    rodape(d, SITE, f"{n} / {total}")
    return im


def slide_texto(s, n, total):
    im, d = base()
    ft = font(SANS_R, 39)
    tam = 72
    h = 130 + altura_titulo(d, s["titulo"], tam, W - 2 * M) + 48 + altura_bloco(d, s["texto"], ft, W - 2 * M)
    if s.get("fonte"):
        h += 90
    y0 = max(240, 190 + (H - 120 - 190 - h) // 2)
    num = romano(int(s["num"]))
    d.text((M - 4, y0 - 18), num, font=font(SERIF_SB, 110), fill=OURO)
    d.rectangle([M, y0 + 112, W - M, y0 + 112], fill=FILETE)
    y = titulo(d, M, y0 + 140, s["titulo"], tam, W - 2 * M, s.get("destaque"))
    y = bloco(d, M, y + 44, s["texto"], ft, TEXTO, W - 2 * M)
    if s.get("fonte"):
        f = font(SANS_I, 25)
        d.rectangle([M, y + 44, M + 3, y + 78], fill=OURO)
        d.text((M + 20, y + 46), "Fonte: " + s["fonte"], font=f, fill=CINZA)
    rodape(d, SITE, f"{n} / {total}")
    return im


def slide_assinatura(s, n, total):
    """Fechamento: assinatura do escritório, como um cartão. Sem chamada para contratar."""
    im = Image.new("RGBA", (W, H), GRAFITE_FUNDO + (255,))
    d = ImageDraw.Draw(im)
    d.rectangle([40, 40, W - 40, H - 40], outline=(70, 66, 58), width=1)
    lw, lh = _mascara("logo-mascara.png", alvo_w=560).size
    por_marca(im, "logo-mascara.png", PRATA, (W - lw) // 2, 190, alvo_w=560)
    y = 190 + lh + 80
    d.rectangle([W / 2 - 50, y, W / 2 + 50, y + 2], fill=OURO_CLARO)
    y += 60
    if s.get("titulo"):
        y = titulo(d, 0, y, s["titulo"], 60, 860, s.get("destaque"), cor=(240, 241, 243), cor_dest=OURO_CLARO, centro=True)
        y += 10
    if s.get("texto"):
        y = bloco(d, 0, y + 10, s["texto"], font(SANS_R, 33), (190, 195, 200), 800, 1.45, centro=True)
    y = max(y + 70, H - 380)
    fn = font(SERIF_SB, 46)
    d.text(((W - d.textlength(ADVOGADO, font=fn)) / 2, y), ADVOGADO, font=fn, fill=(240, 241, 243))
    fo = font(SANS_B, 26)
    larg = sum(d.textlength(c, font=fo) + fo.size * 0.2 for c in OAB) - fo.size * 0.2
    espacado(d, (W - larg) / 2, y + 70, OAB, fo, OURO_CLARO, 0.2)
    fs = font(SANS_R, 30)
    d.text(((W - d.textlength(SITE, font=fs)) / 2, y + 134), SITE, font=fs, fill=PRATA)
    return im


def slide_unico(s, n, total):
    """Imagem única: frase em serifa + linha de apoio; a legenda carrega a explicação."""
    im, d = base()
    tam = s.get("tamanho", 100)
    fs = font(SANS_R, 37)
    h = (70 if s.get("selo") else 0) + altura_titulo(d, s["titulo"], tam, W - 2 * M) + (60 + altura_bloco(d, s.get("sub", ""), fs, W - 2 * M - 40) if s.get("sub") else 0)
    y0 = max(260, 190 + (H - 120 - 190 - h) // 2)
    if s.get("selo"):
        rotulo(d, M, y0, s["selo"])
        y0 += 70
    y = titulo(d, M, y0, s["titulo"], tam, W - 2 * M, s.get("destaque"))
    if s.get("sub"):
        d.rectangle([M, y + 26, M + 90, y + 28], fill=OURO)
        bloco(d, M, y + 60, s["sub"], fs, TEXTO, W - 2 * M - 40)
    rodape(d, f"{ADVOGADO} · {OAB}", SITE)
    return im


def render(slides, pasta):
    os.makedirs(pasta, exist_ok=True)
    fn = {"capa": slide_capa, "texto": slide_texto, "assinatura": slide_assinatura, "unico": slide_unico}
    out = []
    for i, s in enumerate(slides, 1):
        p = f"{pasta}/slide_{i:02d}.jpg"
        fn[s["tipo"]](s, i, len(slides)).convert("RGB").save(p, "JPEG", quality=92, optimize=True)
        out.append(p)
    return out


if __name__ == "__main__":
    dados = json.load(open(sys.argv[1]))
    print(render(dados["slides"], sys.argv[2]))
