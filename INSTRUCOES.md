# Posts do Zubiaurre & Riela Advogados Associados: como gerar, aprovar e publicar

Este repositório guarda tudo o que a tarefa agendada precisa para fazer os posts do escritório
(Instagram @zr.adv e página "Zubiaurre & Riela - Advogados Associados" no Facebook) e as artes de cada post publicado.
O Instagram puxa as imagens daqui, pelo link público.

Calendário: **sexta-feira, 1 post por semana, carrossel informativo**, sempre com aprovação do Alexandre antes de publicar.

## Regra fixa: publicidade da advocacia (OAB)

Isto vem antes de tudo. Um post que fere estas regras **não vai para aprovação**: reescreva.
Base: Provimento 205/2021 do CFOAB e Código de Ética e Disciplina (arts. 39 a 47).
A responsabilidade pela publicidade é do advogado, não da automação.

A publicidade tem que ser sóbria, discreta e informativa, sem captação de clientela nem mercantilização.

| Pode | Não pode |
|---|---|
| Explicar a lei, prazos e mudanças (conteúdo técnico e informativo) | Citar honorários, forma de pagamento, gratuidade ou desconto |
| Impulsionar post informativo | Oferecer serviço ou chamar para contratar ("fale com a gente", "agende", "chame no WhatsApp") |
| Logo, identidade visual e foto dos advogados e do escritório | Contar caso concreto, cliente ou resultado obtido |
| Site e redes como contato, como num cartão | Prometer resultado ("multa cancelada", "processo ganho") |
| Títulos e qualificações verdadeiros e comprováveis | Expressões persuasivas, de autoengrandecimento ou comparação com colegas ("o melhor", "líder", "referência") |
| Lives, vídeos e palestras com conteúdo informativo | Anunciar especialidade sem título; ostentação; usar símbolos da OAB |

Na prática, 5 regras do conteúdo:

1. **O post ensina, não vende.** Explica a regra e para aí. Nada de "a gente resolve", "conte com a gente", "procure um advogado especialista".
2. **Fechamento neutro.** O último slide é uma assinatura (escritório, advogado, OAB e site), como um cartão.
   Explicar o tema e terminar oferecendo o serviço é tratado por parte da OAB como captação disfarçada.
   Frases permitidas para fechar: "Conteúdo de caráter informativo.", "Acompanhe as próximas publicações."
3. **Sem medo vendido.** Urgência só quando é fato (um prazo que vence, uma lei que entrou em vigor), dita com sobriedade.
   Nada de "cuidado!", "você pode perder tudo", emoji de alerta.
4. **Sem caso real**, nem anonimizado de um jeito reconhecível. Exemplos são sempre hipóteses ("imagine um produtor que...").
5. **Nome e OAB sempre.** O art. 44 do Código de Ética exige o nome do advogado ou da sociedade e o número de inscrição
   na OAB em toda publicidade. Já está no modelo das artes (slide final e rodapé da imagem única) e vai no fim de toda legenda.
   **Contato: só o site** (zradvogados.com.br). Sem telefone, sem WhatsApp, sem "link na bio para agendar".

Checagem obrigatória antes de mandar para aprovação: ler cada slide e a legenda contra a tabela acima
e dizer ao Alexandre, numa linha, que a checagem foi feita e se algo ficou no limite.

## Quem é o escritório

Zubiaurre & Riela Advogados Associados. Sócios: Alexandre Juliani Riela (OAB/RS 110.261) e
Luiz Paulo Zubiaurre Pereira (OAB/RS 110.389). Site: zradvogados.com.br.
Os posts automáticos tratam da prática ambiental e agrária, conduzida pelo Alexandre, e são assinados por ele.

## Público e tom

- Quem lê: produtores rurais, empresas e consultores ambientais do Noroeste gaúcho que lidam com órgão ambiental,
  autuação e regularização de imóvel. Entendem da atividade deles, não de processo.
- Tom: professor que explica bem. Claro, sem juridiquês, sem sensacionalismo. Termo técnico só explicado na mesma frase.
- Gancho da capa: até **8 palavras**, informativo ("O prazo de defesa começa antes do que você pensa"), nunca de venda.
  Tipos que funcionam: distinção que confunde (X não é Y), mito x regra, pergunta frequente, lei nova explicada.
- Escrever em terceira pessoa ou impessoal. Evitar "a gente", "nós resolvemos", "nossa equipe".

## Os 8 pilares (rodízio; não repetir o pilar do último post)

1. Autos de infração e defesa administrativa (prazos, intimação, edital, conversão de multa)
2. Crimes ambientais (Lei 9.605/1998: o que é crime e o que é só infração)
3. Licenciamento e a Lei Geral do Licenciamento (Lei 15.190/2025)
4. Código Florestal: CAR, Reserva Legal, APP, PRA
5. Direito agrário: georreferenciamento, SIGEF, posse, contratos agrários
6. Água e outorga do ponto de vista jurídico
7. Lei nova e decisões dos tribunais, explicadas sem caso do escritório
8. Dúvidas frequentes e mitos ("multa prescreve?", "posso cortar árvore no meu terreno?")

Antes de escolher o tema, ler `historico.md`: não repetir o pilar do último post nem tema dos últimos 12.
Dê preferência ao que está acontecendo agora (lei nova, prazo que vence, decisão recente do STJ/STF/TJRS/TRF4).

## Regras de conteúdo

- Toda lei, artigo, prazo, súmula ou número é **conferido em fonte oficial antes** (planalto.gov.br, stj.jus.br,
  stf.jus.br, al.rs.gov.br, sema.rs.gov.br, fepam.rs.gov.br, diário oficial). Se a página não abrir direto,
  procurar com WebSearch e abrir o link do resultado. **Sem confirmação, não cita**; fale da regra em termos gerais.
  Lei nova (2025 e 2026) pede cuidado redobrado: conferir se está em vigor e se não foi alterada ou vetada.
- Sem estatística inventada, sem caso real, sem promessa, sem parecer pelo post.
- Sem imagem gerada por IA. Artes só com tipografia, cores e logo do escritório (modelo em `sistema/render.py`).
- Cada slide de texto que cita norma leva o campo `fonte` (ex.: "Lei 12.651/2012, art. 12, II").
- Legenda: 600 a 1.200 caracteres, parágrafos curtos, primeira linha = gancho, cita a norma entre parênteses.
  Termina sempre com:

  ```
  Conteúdo de caráter informativo.

  Zubiaurre & Riela Advogados Associados
  Alexandre Juliani Riela · OAB/RS 110.261
  zradvogados.com.br
  ```

  e 4 a 6 hashtags informativas (ex.: #direitoambiental #direitoagrario #codigoflorestal #licenciamentoambiental #trespassos).

## Identidade visual (já está no modelo; não mudar sem o Alexandre pedir)

Terceira identidade, sóbria, que não pode lembrar as outras marcas:
PRUMO é escuro, sem serifa, "de sistema", com selo em pílula; Santa Rute é creme quente, verde e dourado, com cara de campo.

- Fundo branco-gelo frio e liso, filetes finos cinza, monograma ZR bem clarinho em marca-d'água no canto.
- Cabeçalho: monograma ZR (da logo do papel timbrado) + "ZUBIAURRE & RIELA / ADVOGADOS ASSOCIADOS" em caixa-alta espaçada.
- Títulos em serifa clássica (EB Garamond) grafite; palavras de destaque em dourado discreto itálico.
- Texto corrido em Lato, cinza-grafite. Numeração dos slides em algarismos romanos dourados (I, II, III...).
- Rótulo do tema: traço dourado + caixa-alta espaçada cinza (sem selo, sem pílula).
- Rodapé: filete, site à esquerda, número do slide à direita.
- Slide final (`assinatura`): fundo grafite liso com moldura fina, logo completa em prata, título curto neutro,
  nome do advogado, OAB e site. **Sem botão e sem chamada para contato.**
- Sem foto de banco de imagem, sem fundo degradê, sem emoji nas artes.

A logo fica em `sistema/logo-mascara.png` (completa) e `sistema/monograma-mascara.png` (só o ZR), tiradas do papel
timbrado do escritório. Se chegar uma versão melhor da logo, troque esses dois arquivos (PNG em tons de cinza: branco = logo).

## Formato

**Sexta: carrossel informativo (6 slides).** `capa` → 3 a 5 `texto` → `assinatura`.
(Imagem única, `unico`, fica disponível se o Alexandre pedir.)

Modelo do `post.json` (exemplo real em `posts/2026-11-27-app-e-reserva-legal/post.json`):

```json
{
  "pilar": "Código Florestal",
  "formato": "carrossel",
  "slides": [
    {"tipo": "capa", "selo": "Código Florestal", "titulo": "...", "destaque": ["palavras", "em", "dourado"], "sub": "..."},
    {"tipo": "texto", "num": 1, "titulo": "...", "destaque": ["..."], "texto": "...", "fonte": "Lei 12.651/2012, art. 4º"},
    {"tipo": "assinatura", "titulo": "Conteúdo informativo", "texto": "Cada caso tem particularidades que dependem de análise própria. Acompanhe as próximas publicações."}
  ],
  "legenda": "..."
}
```

Imagem única: `{"tipo": "unico", "selo": "...", "titulo": "...", "destaque": [...], "sub": "..."}`.
Capa e imagem única aceitam `"tamanho"` (padrão 100) para diminuir o título se sobrar palavra sozinha na última linha.

Tamanhos que cabem bem: título da capa até ~45 caracteres; título de slide `texto` até ~35 (uma linha);
texto do slide até ~230; título da `assinatura` até ~30; texto da `assinatura` até ~120.

Gerar as artes: `python3 sistema/render.py posts/AAAA-MM-DD-slug/post.json posts/AAAA-MM-DD-slug`
(precisa de Pillow; não precisa de cairosvg). Sempre abrir as imagens e conferir: texto cortado, sobreposição,
palavra sozinha na última linha, acentos. Ajustar o texto e renderizar de novo.

A pasta do post leva a data da sexta da publicação.

## Aprovação

1. Mandar ao Alexandre as artes (SendUserFile, status proactive) e, em mensagem, a legenda completa, o pilar,
   de onde saiu cada lei ou número (com link da fonte oficial) e a linha da checagem da OAB.
2. Mandar notificação no celular avisando que o post do escritório está esperando aprovação.
3. Esperar a resposta. Ajustes pedidos mexem só no que foi pedido.
4. **Só publicar com aprovação explícita** ("aprovado", "pode publicar"). Sem resposta, não publica.

## Publicação (só depois do OK)

1. Commit da pasta `posts/AAAA-MM-DD-slug/` (post.json + JPGs) e push para `main`.
2. Links das imagens, sempre com o hash do commit (evita imagem antiga em cache):
   `https://raw.githubusercontent.com/alexandrejriela-PRUMO/zr-conteudo/<HASH>/posts/AAAA-MM-DD-slug/slide_01.jpg`
   Conferir com curl que cada link responde 200 image/jpeg.
3. Instagram (Zapier, "Instagram for Business" → Publish Photo(s)):
   conta **Zubiaurre & Riela - Advogados Associados** `instagramPageId = 17841447724064518` (@zr.adv);
   `media` = lista de links na ordem; `caption` = legenda.
4. Facebook (Zapier, "Facebook Pages" → Create Page Photo), sempre pela conexão
   `0256a435-af26-8f47-a14c-fcfddde245af` ("alexandrejriela@gmail.com #2"):
   página **Zubiaurre & Riela - Advogados Associados** `page = 727184393814727`; `source` = **só o link do slide_01**;
   `message` = legenda.
5. Pegar o link do post no Instagram (Instagram for Business → Make API GET Request em
   `https://graph.facebook.com/v23.0/<id>?fields=permalink`) e responder ao Alexandre com ele.
6. Acrescentar a linha em `historico.md`, commit e push.

Se algo falhar (Zapier fora, erro de publicação), avisar o Alexandre do que faltou, com as artes prontas
para postar à mão. Nunca publicar na conta ou página de outra marca (PRUMO, Santa Rute, Repiso Imóveis).

## O que a automação não faz

- Não responde comentários nem mensagens (a OAB veda resposta automática e indiscriminada a não clientes).
- Não impulsiona post. Impulsionamento, se houver, é decisão do Alexandre, só de post informativo.
- Não coloca neste repositório nada além do que vai ser publicado: nada de peça, documento ou dado de cliente.
