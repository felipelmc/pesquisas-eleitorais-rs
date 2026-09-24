// Template do artigo (Typst, via Quarto template-partials). Tipografia de revista acadêmica, sem imitar
// nenhuma revista real: sem nome, logo, ISSN, DOI, volume ou datas de recebimento/aceite.
// Atenção: este arquivo passa pelo motor de templates do Pandoc; um cifrão literal precisa ser escrito duplicado.

#let acento = rgb("#1f4e79")
#let verm = rgb("#b91c1c")
#let ambar = rgb("#b45309")
#let ambar-fundo = rgb("#fff6e8")
#let cinza-fundo = luma(245)
#let serif = ("STIX Two Text", "STIX Two Math")
#let sans = ("Fira Sans", "STIX Two Math")
#let mono = ("Fira Mono", "STIX Two Math")

// ---------------------------------------------------------------- caixas
#let pendente(titulo: "Pendente de revisão humana", body) = block(
  width: 100%, breakable: true, above: 1.1em, below: 1.1em,
  inset: (left: 9pt, right: 8pt, y: 7pt), fill: ambar-fundo,
  stroke: (left: 2.2pt + ambar))[
  #set text(font: sans, size: 8.4pt)
  #set par(first-line-indent: 0pt, justify: false, leading: 0.5em, spacing: 0.6em)
  #text(weight: "semibold", fill: ambar, tracking: 0.03em, upper(titulo)) \
  #body
]

#let caixa-rascunho(titulo, body) = block(
  width: 100%, breakable: true, above: 1em, below: 1em,
  inset: 9pt, radius: 1.5pt, stroke: 0.9pt + verm, fill: verm.lighten(96%))[
  #set text(font: sans, size: 8.4pt)
  #set par(first-line-indent: 0pt, justify: false, leading: 0.5em, spacing: 0.6em)
  #text(weight: "bold", fill: verm, titulo) \
  #body
]

#let destaque(titulo, body) = block(
  width: 100%, breakable: true, above: 1.1em, below: 1.1em,
  inset: (x: 10pt, y: 9pt), fill: cinza-fundo, stroke: (top: 1.6pt + acento))[
  #set text(font: sans, size: 8.8pt)
  #set par(first-line-indent: 0pt, justify: false, leading: 0.52em, spacing: 0.65em)
  #if titulo != none and titulo != [] [#text(weight: "semibold", fill: acento, tracking: 0.03em, upper(titulo)) \ ]
  #body
]

// callout do Quarto redefinido: despacho pelo título; ícones ignorados (sem Font Awesome no PDF)
#let callout(body: [], title: "", background_color: none, icon: none, icon_color: none, body_background_color: none) = {
  let t = content-to-string(title)
  if t.contains("Pendente de revisão humana") { pendente(body) }
  else if t.contains("RASCUNHO") { caixa-rascunho(title, body) }
  else { destaque(title, body) }
}

// blocos de classe (inline.lua): .resumo, .mensagens-principais
#let resumo(titulo: none, body) = block(
  width: 100%, breakable: true, above: 1.2em, below: 1.2em,
  inset: (x: 11pt, y: 10pt), fill: cinza-fundo, stroke: (top: 0.8pt + acento, bottom: 0.8pt + acento))[
  #set text(font: sans, size: 8.6pt)
  #set par(first-line-indent: 0pt, justify: true, leading: 0.5em, spacing: 0.62em)
  #show heading: it => block(above: 0em, below: 0.7em, text(size: 9pt, weight: "semibold", fill: acento, tracking: 0.05em, upper(it.body)))
  #body
]

#let mensagens(body) = block(
  width: 100%, breakable: true, above: 1.2em, below: 1.2em,
  inset: (x: 11pt, y: 10pt), stroke: (left: 2.4pt + acento), fill: acento.lighten(94%))[
  #set text(font: sans, size: 8.8pt)
  #set par(first-line-indent: 0pt, justify: false, leading: 0.52em, spacing: 0.7em)
  #show heading: it => block(above: 0em, below: 0.7em, text(size: 9.2pt, weight: "semibold", fill: acento, tracking: 0.05em, upper(it.body)))
  #set list(indent: 0pt, body-indent: 0.6em, spacing: 0.75em, marker: text(fill: acento)[▪])
  #body
]

#let largura-total(body) = pad(x: -14mm, body)
#let grade(s) = box(text(font: "STIX Two Math", size: 1.02em, fill: acento, tracking: 0.02em, s))

// ---------------------------------------------------------------- artigo
#let article(
  title: none,
  subtitle: none,
  authors: none,
  keywords: (),
  date: none,
  abstract-title: none,
  abstract: none,
  thanks: none,
  cols: 1,
  lang: "pt",
  region: "BR",
  font: none,
  fontsize: 10pt,
  title-size: 1.5em,
  subtitle-size: 1.25em,
  heading-family: none,
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  mathfont: none,
  codefont: none,
  linestretch: 1,
  sectionnumbering: none,
  linkcolor: none,
  citecolor: none,
  filecolor: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  masthead: none,
  cabeca: none,
  nota-ia: none,
  ultima-busca: none,
  rascunho: false,
  pendencias: none,
  doc,
) = {
  set document(title: if rascunho [#title (RASCUNHO NÃO VALIDADO)] else { title }, keywords: keywords)
  set document(
    author: authors.map(author => content-to-string(author.name)).join(", ", last: " & "),
  ) if authors != none and authors != ()

  set page(
    paper: "a4",
    margin: (x: 35mm, top: 27mm, bottom: 25mm),
    header: context {
      if here().page() > 1 {
        set text(font: sans, size: 7.2pt, fill: luma(80))
        grid(columns: (1fr, auto), align: (left, right),
          cabeca,
          if rascunho { text(fill: verm, weight: "semibold", tracking: 0.04em)[RASCUNHO NÃO VALIDADO] })
        v(-4pt)
        line(length: 100%, stroke: 0.35pt + luma(150))
      }
    },
    footer: context align(center, text(font: sans, size: 7.2pt, fill: luma(80),
      counter(page).display("1 / 1", both: true))),
    background: if rascunho { context place(center + horizon, rotate(-38deg,
      text(font: sans, size: 50pt, weight: "bold", fill: verm.transparentize(94%))[RASCUNHO NÃO VALIDADO])) },
  )

  set text(font: serif, size: fontsize, lang: lang, region: region, hyphenate: true,
           number-type: "lining", costs: (hyphenation: 70%, widow: 100%, orphan: 100%))
  set par(justify: true, leading: 0.6em, spacing: 0.6em,
          first-line-indent: (amount: 1.2em, all: false))
  show regex("\\b(bandwagon|underdog|momentum|survey|surveys|leave-one-out|forest plot|harvest plot)\\b"): it => text(lang: "en", it)
  show raw: set text(font: mono, size: 0.88em)
  show math.equation: set text(font: "STIX Two Math")

  set heading(numbering: sectionnumbering)
  show heading: set text(font: sans, fill: acento, weight: "semibold", hyphenate: false)
  show heading: set par(justify: false)
  show heading.where(level: 1): it => block(above: 1.7em, below: 0.8em, text(size: 11.5pt, it))
  show heading.where(level: 2): it => block(above: 1.3em, below: 0.6em, text(size: 10pt, it))
  show heading.where(level: 3): it => block(above: 1.1em, below: 0.5em, text(size: 9.5pt, weight: "medium", style: "italic", it))

  // listas e notas
  set list(indent: 0.6em, body-indent: 0.5em, spacing: 0.6em)
  set enum(indent: 0.6em, body-indent: 0.5em, spacing: 0.6em)
  show footnote.entry: set text(font: serif, size: 8pt)

  // figuras e tabelas
  show figure.caption: it => {
    set text(font: sans, size: 7.9pt)
    set par(justify: true, first-line-indent: 0pt, leading: 0.48em)
    align(left)[#text(weight: "semibold", fill: acento)[#it.supplement #context it.counter.display(it.numbering).] #it.body]
  }
  show figure: set block(above: 1.4em, below: 1.4em)
  show figure: set align(left)
  show figure.where(kind: "quarto-float-tbl"): set block(breakable: true)
  show figure.where(kind: "quarto-float-tbl"): set figure.caption(position: top)
  show figure.where(kind: "quarto-float-qdr"): set block(breakable: true)
  show figure.where(kind: "quarto-float-qdr"): set figure.caption(position: top)
  show table: set text(font: sans, size: 7.6pt, number-width: "tabular", hyphenate: true)
  show table: set par(justify: false, first-line-indent: 0pt, leading: 0.45em)
  set table(inset: (x: 3.5pt, y: 3.2pt), stroke: (x, y) => if y == 0 { (top: 0.8pt, bottom: 0.4pt) })
  show table: it => block(width: 100%, stroke: (bottom: 0.8pt), it)
  show table.cell.where(y: 0): set text(weight: "semibold")

  // referências bibliográficas (citeproc): corpo menor, recuo pendente
  show <refs>: set text(size: 8.8pt)
  show <refs>: set par(hanging-indent: 1.4em, first-line-indent: 0pt, justify: false, leading: 0.5em, spacing: 0.55em)

  // links e referências cruzadas
  show link: set text(fill: acento)
  show ref: set text(fill: acento)

  // ------------------------------------------------ bloco de título (página 1)
  block(width: 100%, below: 1.4em)[
    #set par(first-line-indent: 0pt, justify: false)
    #if masthead != none {
      text(font: sans, size: 7.2pt, weight: "medium", tracking: 0.08em, fill: luma(70), upper(masthead))
      if date != none { text(font: sans, size: 7.2pt, weight: "medium", tracking: 0.08em, fill: luma(70))[ · #date] }
      v(-2pt)
      line(length: 100%, stroke: 1.4pt + acento)
    }
    #v(1.1em)
    #text(font: sans, size: 19pt, weight: "semibold", fill: luma(15))[#title]
    #if subtitle != none {
      v(0.25em)
      text(font: serif, size: 12pt, style: "italic", fill: luma(40), subtitle)
    }
    #v(0.9em)
    #if authors != none and authors != () {
      text(font: sans, size: 9.6pt)[
        #authors.map(a => [#text(weight: "semibold", a.name)#if a.affiliation != [] [ · #a.affiliation]]).join([; ])
      ]
    }
    #if ultima-busca != none {
      linebreak()
      text(font: sans, size: 8pt, fill: luma(80))[Última busca: #ultima-busca]
    }
    #if nota-ia != none {
      v(0.5em)
      text(font: sans, size: 7.8pt, style: "italic", fill: luma(70), nota-ia)
    }
  ]

  doc
}
