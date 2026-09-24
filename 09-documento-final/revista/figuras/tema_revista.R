# Tema comum das figuras do artigo (09-documento-final/revista/figuras/).
# Carregado por gerar_figuras.R com source(). Só define fonte, tamanhos, paleta, formatação de números e a
# função de gravação; não lê dados.

suppressPackageStartupMessages({
  library(ggplot2)
  library(systemfonts)
})

# ---------------------------------------------------------------- fonte
# Fira Sans do sistema (mesma família das fontes do projeto). Só registra as OTF de revista/fontes/otf se a
# família não existir no sistema.
FONTE <- "Fira Sans"
if (!FONTE %in% systemfonts::system_fonts()$family) {
  otf <- file.path(DIR_REVISTA, "fontes", "otf")
  systemfonts::register_font(
    name = FONTE,
    plain = file.path(otf, "FiraSans-Regular.otf"), bold = file.path(otf, "FiraSans-Bold.otf"),
    italic = file.path(otf, "FiraSans-Italic.otf"), bolditalic = file.path(otf, "FiraSans-BoldItalic.otf")
  )
  message("Fira Sans registrada a partir de revista/fontes/otf")
}

# ---------------------------------------------------------------- tamanhos (em pt na largura final)
CORPO <- 7.5          # corpo do texto das figuras
CORPO_MIN <- 6.5      # menor corpo permitido
pt_mm <- function(p) p / ggplot2::.pt                    # tamanho de texto em pt -> unidade de geom_text (mm)
lw <- function(p) p / (ggplot2::.pt * 72.27 / 96)        # espessura em pt -> linewidth do ggplot2
LINHA <- lw(0.3)      # linhas de 0,3 pt (eixos, grades, contornos)
LINHA_DADO <- lw(0.5) # marcas de dado (setas, barras de IC)
LARGURA <- c(texto = 140, larga = 170)                  # mm

# ---------------------------------------------------------------- paleta
COR <- list(
  a_favor = "#2a78d6",   # a favor, bandwagon, viabilidade, momentum a favor, mobilização
  contra = "#eb6834",    # contra, underdog, desmobilização
  misto = "#52514e",     # losango cinza-escuro
  nulo = "#898781",      # anel cinza (nulo por ±δ)
  tinta = "#23221f",     # texto principal
  tinta2 = "#52514e",    # texto secundário
  tinta3 = "#898781",    # texto terciário, notas
  grade = "#d9d7d0",     # grades e filetes
  fundo_caixa = "#f4f3ef", # preenchimento neutro de caixas
  confundidor = "#b9b7b0"  # contorno dos confundidores no modelo lógico
)
# Risco de viés: paleta "colourblind" do robvis 0.3.1 instalado (rob_summary/rob_traffic_light), versão de 4
# níveis usada para ROBINS-I e ROB1: baixo #fef0d9, algumas preocupações/moderado/incerto #fdcc8a,
# alto/grave #fc8d59, crítico #d7301f. O robvis 0.3.1 não define cor de "sem informação"; nenhum julgamento
# consolidado desta revisão tem esse valor.
COR_ROB <- c(`1` = "#fef0d9", `2` = "#fdcc8a", `3` = "#fc8d59", `4` = "#d7301f")
SIMBOLO_ROB <- c(`1` = "+", `2` = "−", `3` = "×", `4` = "!")  # símbolos do robvis (+, -, x, !)

# ---------------------------------------------------------------- números pt-BR
num_br <- function(acc = 0.01) {
  scales::label_number(accuracy = acc, decimal.mark = ",", big.mark = ".", style_negative = "minus")
}
pct_br <- function(acc = 1) scales::label_percent(accuracy = acc, decimal.mark = ",", big.mark = ".")

# ---------------------------------------------------------------- palavras estrangeiras em itálico (plotmath)
ESTRANGEIRAS <- c("bandwagon", "underdog", "momentum", "Momentum", "survey", "post hoc")
# Converte um rótulo em expressão plotmath com as palavras estrangeiras em itálico (negrito = TRUE para títulos).
# No SVG, cada pedaço vira um <text> com textLength, e o leitor de SVG do Typst descarta espaço inicial ou final
# e estica o resto; por isso o espaço na borda de um pedaço vira espaço não separável (U+00A0), que ele mantém.
# (O operador "~" do plotmath não serve: gera um <text> na fonte Symbol.)
italicizar <- function(x, negrito = FALSE) {
  f_n <- if (negrito) "bold" else "plain"
  f_i <- if (negrito) "bolditalic" else "italic"
  vapply(x, function(s) {
    padrao <- paste0("(", paste(ESTRANGEIRAS, collapse = "|"), ")")
    partes <- regmatches(s, gregexpr(padrao, s), invert = NA)[[1]]
    partes <- partes[partes != ""]
    partes <- sub("^ ", "\u00a0", sub(" $", "\u00a0", partes))
    toks <- vapply(partes, function(p) paste0(if (p %in% ESTRANGEIRAS) f_i else f_n, "(", deparse(p), ")"),
                   character(1))
    paste(toks, collapse = " * ")
  }, character(1), USE.NAMES = FALSE)
}
rotulador_italico <- function(labels) {
  lapply(labels, function(v) lapply(italicizar(as.character(v)), function(e) parse(text = e)[[1]]))
}

# ---------------------------------------------------------------- tema
tema_revista <- function(base = CORPO, grade_x = FALSE, grade_y = FALSE) {
  t <- theme_minimal(base_size = base, base_family = FONTE, base_line_size = LINHA, base_rect_size = LINHA) %+replace%
    theme(
      text = element_text(family = FONTE, colour = COR$tinta, size = base),
      plot.background = element_rect(fill = "transparent", colour = NA),
      panel.background = element_rect(fill = "transparent", colour = NA),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_blank(),
      axis.line.x = element_line(colour = COR$tinta2, linewidth = LINHA),
      axis.ticks = element_line(colour = COR$tinta2, linewidth = LINHA),
      axis.ticks.length = unit(1.2, "mm"),
      axis.text = element_text(size = base - 0.5, colour = COR$tinta2),
      axis.title = element_text(size = base, colour = COR$tinta),
      legend.background = element_rect(fill = "transparent", colour = NA),
      legend.key = element_rect(fill = "transparent", colour = NA),
      legend.text = element_text(size = base - 0.5),
      legend.title = element_text(size = base),
      strip.background = element_rect(fill = "transparent", colour = NA),
      strip.text = element_text(face = "bold", hjust = 0, size = base, margin = margin(2, 0, 2, 0)),
      plot.tag = element_text(face = "bold", size = base + 1.5, family = FONTE),
      plot.caption = element_text(hjust = 0, size = CORPO_MIN, colour = COR$tinta2, margin = margin(t = 4)),
      plot.title = element_text(face = "bold", size = base, hjust = 0, margin = margin(b = 3)),
      plot.title.position = "plot",
      plot.caption.position = "plot",
      plot.margin = margin(3, 3, 3, 3)
    )
  if (grade_x) t <- t + theme(panel.grid.major.x = element_line(colour = COR$grade, linewidth = LINHA))
  if (grade_y) t <- t + theme(panel.grid.major.y = element_line(colour = COR$grade, linewidth = LINHA))
  t
}

# ---------------------------------------------------------------- gravação (SVG com svglite, PNG com ragg a 300 dpi)
gravar_figura <- function(p, nome, largura = c("texto", "larga"), altura_mm) {
  largura <- match.arg(largura)
  w <- LARGURA[[largura]]
  dir.create(DIR_SAIDA, showWarnings = FALSE, recursive = TRUE)
  svg <- file.path(DIR_SAIDA, paste0(nome, ".svg"))
  png <- file.path(DIR_SAIDA, paste0(nome, ".png"))
  svglite::svglite(svg, width = w / 25.4, height = altura_mm / 25.4, bg = "transparent")
  print(p)
  invisible(dev.off())
  ragg::agg_png(png, width = w, height = altura_mm, units = "mm", res = 300, background = "transparent")
  print(p)
  invisible(dev.off())
  message(sprintf("%s: %d x %d mm", nome, w, round(altura_mm)))
  invisible(c(largura_mm = w, altura_mm = altura_mm))
}
