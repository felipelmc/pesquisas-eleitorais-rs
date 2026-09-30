# Desenha as 7 figuras do artigo a partir de figuras/dados/*.csv (gerados por preparar_dados_figuras.py).
#
# USO (de qualquer pasta)
#   Rscript 09-documento-final/revista/figuras/gerar_figuras.R            # todas
#   Rscript 09-documento-final/revista/figuras/gerar_figuras.R rob metas  # só algumas
#
# Só lê os CSV de figuras/dados/ e, para os rótulos autor-ano, revista/rotulos_autor_ano.json (gerado por
# citeproc com o CSL da revista). Se o JSON não existir, monta o rótulo a partir de 07-relatorio/incluidos.csv
# com a regra do CSL APSA (um a três sobrenomes; "et al." a partir de quatro autores; sufixo de ano quando o
# mesmo rótulo e ano se repetem) e avisa que o rótulo final virá do citeproc.
# Grava figuras/saida/<nome>.svg (svglite) e <nome>.png (ragg, 300 dpi), com fundo transparente.

suppressPackageStartupMessages({
  library(ggplot2)
  library(patchwork)
})

arg_arquivo <- sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE))
DIR_FIG <- if (length(arg_arquivo)) dirname(normalizePath(arg_arquivo)) else getwd()
DIR_REVISTA <- dirname(DIR_FIG)
RAIZ <- dirname(dirname(DIR_REVISTA))
DIR_DADOS <- file.path(DIR_FIG, "dados")
DIR_SAIDA <- file.path(DIR_FIG, "saida")
source(file.path(DIR_FIG, "tema_revista.R"))

ler <- function(nome) {
  utils::read.csv(file.path(DIR_DADOS, nome), encoding = "UTF-8", stringsAsFactors = FALSE,
                  na.strings = "", check.names = FALSE)
}
larg_mm <- function(txt, p = CORPO, negrito = FALSE, italico = FALSE) {
  systemfonts::string_width(txt, family = FONTE, size = p, res = 72, weight = if (negrito) "bold" else "normal",
                            italic = italico) * 25.4 / 72
}
# quebra um texto em linhas que caibam em `largura` mm
quebrar <- function(txt, largura, p = CORPO, negrito = FALSE) {
  palavras <- strsplit(txt, " ", fixed = TRUE)[[1]]
  linhas <- character(0)
  atual <- ""
  for (w in palavras) {
    cand <- if (atual == "") w else paste(atual, w)
    if (atual != "" && larg_mm(cand, p, negrito) > largura) {
      linhas <- c(linhas, atual)
      atual <- w
    } else {
      atual <- cand
    }
  }
  c(linhas, atual)
}

# ---------------------------------------------------------------- rótulos autor-ano
ROTULO_PROVISORIO <- FALSE
rotulos_autor_ano <- local({
  cand <- c(file.path(DIR_REVISTA, "rotulos_autor_ano.json"), file.path(DIR_FIG, "rotulos_autor_ano.json"))
  f <- cand[file.exists(cand)]
  if (length(f)) {
    j <- jsonlite::fromJSON(f[1], simplifyVector = FALSE)
    rot <- vapply(j, function(v) {
      if (is.list(v)) v <- v[["rotulo"]] %||% v[[1]]
      as.character(v)
    }, character(1))
    rot <- sub("^\\((.*)\\)$", "\\1", trimws(rot))                    # tira parênteses externos
    rot <- sub("^(.*[^(]) (\\d{4}[a-z]?)$", "\\1 (\\2)", rot)          # "Autor 2017" -> "Autor (2017)"
    message("rótulos autor-ano: ", f[1])
    rot
  } else {
    ROTULO_PROVISORIO <<- TRUE
    inc <- utils::read.csv(file.path(RAIZ, "07-relatorio", "incluidos.csv"), encoding = "UTF-8",
                           stringsAsFactors = FALSE)
    sobren <- lapply(strsplit(inc$autores, " | ", fixed = TRUE), function(a) trimws(sub(",.*$", "", a)))
    curto <- vapply(sobren, function(s) {
      if (length(s) >= 4) paste(s[1], "et al.")
      else if (length(s) == 3) paste0(s[1], ", ", s[2], " e ", s[3])
      else if (length(s) == 2) paste(s[1], "e", s[2])
      else s[1]
    }, character(1))
    suf <- rep("", nrow(inc))
    grupo <- paste(curto, inc$ano)
    for (g in unique(grupo[duplicated(grupo)])) {
      i <- which(grupo == g)
      i <- i[order(tolower(inc$titulo[i]))]
      suf[i] <- letters[seq_along(i)]
    }
    message("AVISO: revista/rotulos_autor_ano.json não existe; rótulos autor-ano provisórios (o final vem do citeproc)")
    stats::setNames(paste0(curto, " (", inc$ano, suf, ")"), inc$chave)
  }
})
`%||%` <- function(a, b) if (is.null(a)) b else a
autor_ano <- function(chaves) {
  faltam <- setdiff(unique(chaves), names(rotulos_autor_ano))
  if (length(faltam)) stop("chaves sem rótulo autor-ano: ", paste(faltam, collapse = ", "))
  unname(rotulos_autor_ano[chaves])
}

# ================================================================ 1. modelo lógico
fig_modelo_logico <- function() {
  d <- ler("dados_modelo_logico.csv")
  ar <- ler("dag_arestas.csv")
  nos <- d[d$elemento == "no", ]
  mods <- d[d$elemento == "moderador", ]
  # layout manual (mm; origem no canto inferior esquerdo). Nós identificados pelo nome do .mmd.
  pos <- data.frame(
    nome = c("divulgacao_enviesada", "apoio_latente", "pesquisa_t1", "interesse_politico", "preferencia_previa",
             "exposicao", "percepcao_viabilidade", "calculo_estrategico", "heuristica_consenso", "conformidade",
             "simpatia_azarao", "emocoes", "complacencia", "apoio_ao_lider", "desmobilizacao",
             "resposta_ao_survey", "pesquisa_t2"),
    x = c(15, 15, 42, 15, 15,
          42, 68, 93, 68, 68,
          68, 68, 68, 117, 93,
          117, 121),
    y = c(94, 80, 80, 60, 42,
          60, 86, 86, 73, 61,
          49, 37, 17, 61, 17,
          29, 86),
    stringsAsFactors = FALSE
  )
  faltam <- setdiff(nos$nome, pos$nome)
  if (length(faltam)) stop("nós do DAG sem posição: ", paste(faltam, collapse = ", "))
  nos <- merge(nos, pos, by = "nome")
  p_no <- 7
  nos$linhas <- lapply(nos$rotulo, quebrar, largura = 19, p = p_no)
  nos$n_lin <- lengths(nos$linhas)
  nos$w <- pmax(vapply(nos$linhas, function(l) max(larg_mm(l, p_no)), numeric(1)) + 4.5, 18)
  nos$h <- nos$n_lin * 3.1 + 2.8
  nos$txt <- vapply(nos$linhas, paste, character(1), collapse = "\n")
  AZUL_CLARO <- "#e3edf9"; ROSA <- "#f6e3dd"
  nos$borda <- ifelse(nos$papel == "confundidor", COR$confundidor, COR$tinta2)
  nos$fundo <- ifelse(nos$papel %in% c("exposicao", "desfecho"), AZUL_CLARO,
               ifelse(nos$papel == "colisor", ROSA, "transparent"))
  nos$cor_txt <- ifelse(nos$papel == "confundidor", COR$tinta2, COR$tinta)
  # nós com palavra estrangeira (ex.: "resposta ao survey"): cada linha é desenhada em pedaços, com a palavra
  # estrangeira em itálico e os pedaços lado a lado, centrados no nó (larguras medidas na fonte; 1 mm = U unidades
  # no eixo x, porque o grafo tem 170 unidades em LARGURA["larga"] mm). Os demais nós seguem num texto só.
  U <- 170 / LARGURA[["larga"]]
  LS <- p_no * 0.92 * 1.2 / 72 * 25.4          # passo entre linhas do texto de várias linhas (lineheight 0.92), em mm
  rx_estr <- paste0("^(", paste(ESTRANGEIRAS, collapse = "|"), ")$")
  tem_estr <- vapply(nos$linhas, function(l) any(grepl(rx_estr, unlist(strsplit(l, " ")))), logical(1))
  esp <- (larg_mm("a b", p_no) - larg_mm("ab", p_no)) * U
  ped <- do.call(rbind, lapply(which(tem_estr), function(i) {
    ls <- nos$linhas[[i]]
    do.call(rbind, lapply(seq_along(ls), function(j) {
      w <- unlist(strsplit(ls[j], " "))
      it <- grepl(rx_estr, w)
      grp <- cumsum(c(TRUE, it[-1] != it[-length(it)]))
      segs <- vapply(split(w, grp), paste, character(1), collapse = " ")
      seg_it <- vapply(split(it, grp), `[`, logical(1), 1)
      larg <- vapply(seq_along(segs), function(k) larg_mm(segs[k], p_no, italico = seg_it[k]) * U, numeric(1))
      x0 <- nos$x[i] - (sum(larg) + esp * (length(segs) - 1)) / 2
      data.frame(x = x0 + c(0, cumsum(larg + esp))[seq_along(segs)],
                 y = nos$y[i] + ((length(ls) - 1) / 2 - (j - 1)) * LS,
                 txt = segs, face = ifelse(seg_it, "italic", "plain"), cor = nos$cor_txt[i])
    }))
  }))
  nos$lt <- ifelse(nos$tracejado == 1, "22", "solid")
  B <- split(nos, nos$nome)
  F <- 0.7  # folga entre a ponta da seta e a caixa
  topo <- function(n, x = B[[n]]$x) c(x, B[[n]]$y + B[[n]]$h / 2 + F)
  base <- function(n, x = B[[n]]$x) c(x, B[[n]]$y - B[[n]]$h / 2 - F)
  esq <- function(n, y = B[[n]]$y) c(B[[n]]$x - B[[n]]$w / 2 - F, y)
  dir <- function(n, y = B[[n]]$y) c(B[[n]]$x + B[[n]]$w / 2 + F, y)
  # ponto da borda da caixa na direção de (tx, ty)
  borda <- function(b, tx, ty) {
    dx <- tx - b$x; dy <- ty - b$y
    sx <- if (dx != 0) (b$w / 2 + F) / abs(dx) else Inf
    sy <- if (dy != 0) (b$h / 2 + F) / abs(dy) else Inf
    s <- min(sx, sy)
    c(b$x + dx * s, b$y + dy * s)
  }
  # rotas ortogonais para as arestas longas (confundidores -> apoio; exposição -> resposta ao survey)
  Y1 <- "apoio_ao_lider"
  rota <- list(
    "apoio_latente>apoio_ao_lider" = list(esq("apoio_latente"), c(3.6, 80), c(3.6, 99.6), c(106, 99.6), topo(Y1, 106)),
    "interesse_politico>apoio_ao_lider" = list(esq("interesse_politico"), c(2.3, 60), c(2.3, 101.1), c(108.2, 101.1),
                                               topo(Y1, 108.2)),
    "preferencia_previa>apoio_ao_lider" = list(esq("preferencia_previa"), c(1, 42), c(1, 102.6), c(110.4, 102.6),
                                               topo(Y1, 110.4)),
    "exposicao>resposta_ao_survey" = list(base("exposicao", 39.5), c(39.5, 26.5), esq("resposta_ao_survey", 26.5)),
    "apoio_ao_lider>resposta_ao_survey" = list(base(Y1, 117), topo("resposta_ao_survey", 117)),
    "apoio_ao_lider>pesquisa_t2" = list(topo(Y1, 121), base("pesquisa_t2", 121)),
    "pesquisa_t1>exposicao" = list(base("pesquisa_t1"), topo("exposicao")),
    "apoio_latente>pesquisa_t1" = list(dir("apoio_latente"), esq("pesquisa_t1")),
    "interesse_politico>exposicao" = list(dir("interesse_politico"), esq("exposicao"))
  )
  # leque da exposição: sai da borda direita (alturas escalonadas) e chega à borda esquerda de cada nó
  X <- B[["exposicao"]]
  for (m in ar$para[ar$de == "exposicao"]) {
    if (m == "resposta_ao_survey") next
    if (m == "complacencia") {  # sai da base, para não se sobrepor à seta das emoções
      rota[[paste0("exposicao>", m)]] <- list(base("exposicao", X$x + X$w / 2 - 3), esq(m))
      next
    }
    dy <- max(min((B[[m]]$y - X$y) * 0.16, X$h / 2 - 0.9), -(X$h / 2 - 0.9))
    rota[[paste0("exposicao>", m)]] <- list(dir("exposicao", X$y + dy), esq(m))
  }
  segs <- list()
  for (i in seq_len(nrow(ar))) {
    chave <- paste0(ar$de[i], ">", ar$para[i])
    pts <- rota[[chave]]
    if (is.null(pts)) {
      a <- B[[ar$de[i]]]; b <- B[[ar$para[i]]]
      caminho <- rbind(borda(a, b$x, b$y), borda(b, a$x, a$y))
    } else {
      caminho <- do.call(rbind, pts)
    }
    segs[[i]] <- data.frame(aresta = i, x = caminho[, 1], y = caminho[, 2], tipo = ar$tipo[i],
                            confund = B[[ar$de[i]]]$papel == "confundidor")
  }
  segs <- do.call(rbind, segs)
  cor_seg <- tapply(segs$confund, segs$aresta, function(v) if (v[1]) COR$confundidor else COR$tinta2)
  # rótulos dos elos (E1 a E8, tabela por elo da teoria) em etiquetas sobre a borda superior dos nós
  elo_no <- c(percepcao_viabilidade = "E1", calculo_estrategico = "E2", heuristica_consenso = "E3",
              conformidade = "E4", simpatia_azarao = "E5", emocoes = "E6", complacencia = "E7",
              divulgacao_enviesada = "E8")
  for (k in names(elo_no)) {
    e <- unique(ar$elo[!is.na(ar$elo) & ar$para == k])            # elo da aresta que chega ao nó
    if (!length(e)) e <- unique(ar$elo[!is.na(ar$elo) & ar$de == k]) # ou, na falta, da que sai dele
    if (!identical(e, elo_no[[k]])) stop("elo do nó ", k, " não bate com dag_arestas.csv: ", paste(e, collapse = ","))
  }
  el_pos <- do.call(rbind, lapply(names(elo_no), function(k) {
    b <- B[[k]]
    data.frame(x = b$x - b$w / 2 + 3.4, y = b$y + b$h / 2, elo = elo_no[[k]],
               fundo = if (b$fundo == "transparent") "white" else b$fundo)
  }))

  # quadro de moderadores
  mx0 <- 134; mx1 <- 170; my1 <- 102.6
  # marcador e texto em colunas separadas (sem espaço inicial no texto: o SVG estica o que sobra)
  mod <- do.call(rbind, lapply(mods$rotulo, function(r) {
    l <- quebrar(r, 29, p = CORPO_MIN)
    data.frame(texto = l, marcador = c(TRUE, rep(FALSE, length(l) - 1)))
  }))
  mod_y <- my1 - 9.5 - (seq_len(nrow(mod)) - 1) * 3.05
  my0 <- min(mod_y) - 3

  # legenda
  ly <- 3.5
  leg_txt <- data.frame(x = c(9, 50, 88, 111, 134),
                        txt = c("elo esperado (E1 a E6)", "efeito indesejado (E7, E8)", "confundidor", "colisor",
                                "exposição e desfecho principal"))
  leg_seg <- data.frame(x = c(1, 42), xend = c(7.5, 48.5), y = ly, tipo = c("solida", "tracejada"))
  leg_box <- data.frame(xmin = c(81, 104, 127), xmax = c(86.5, 109.5, 132.5), ymin = ly - 1.6, ymax = ly + 1.6,
                        fundo = c("transparent", ROSA, AZUL_CLARO), borda = c(COR$confundidor, COR$tinta2, COR$tinta2))

  y0 <- ly - 3; y1 <- 104
  seta <- arrow(length = unit(1.3, "mm"), type = "closed", angle = 22)
  g <- ggplot() +
    geom_path(data = segs, aes(x, y, group = aresta, linetype = tipo, colour = factor(aresta)),
              linewidth = LINHA_DADO * 0.8, arrow = seta, lineend = "butt", linejoin = "mitre") +
    scale_colour_manual(values = cor_seg, guide = "none") +
    scale_linetype_manual(values = c(solida = "solid", tracejada = "22"), guide = "none") +
    geom_rect(data = nos, aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2),
              fill = nos$fundo, colour = nos$borda, linetype = nos$lt, linewidth = LINHA) +
    geom_text(data = nos[!tem_estr, ], aes(x, y, label = txt), colour = nos$cor_txt[!tem_estr], family = FONTE,
              size = pt_mm(p_no), lineheight = 0.92) +
    geom_text(data = ped, aes(x, y, label = txt), colour = ped$cor, fontface = ped$face, hjust = 0, family = FONTE,
              size = pt_mm(p_no)) +
    geom_rect(data = el_pos, aes(xmin = x - 2.3, xmax = x + 2.3, ymin = y - 1.2, ymax = y + 1.2), fill = el_pos$fundo,
              colour = NA) +
    geom_text(data = el_pos, aes(x, y, label = elo), family = FONTE, size = pt_mm(CORPO_MIN), colour = COR$tinta2,
              fontface = "bold") +
    annotate("rect", xmin = mx0, xmax = mx1, ymin = my0, ymax = my1, fill = COR$fundo_caixa, colour = NA) +
    annotate("text", x = mx0 + 2, y = my1 - 3.4, label = "Moderadores (fora do grafo)", hjust = 0, family = FONTE,
             fontface = "bold", size = pt_mm(7), colour = COR$tinta) +
    annotate("text", x = mx0 + 4.4, y = mod_y, label = mod$texto, hjust = 0, family = FONTE, size = pt_mm(CORPO_MIN),
             colour = COR$tinta) +
    annotate("text", x = mx0 + 2, y = mod_y[mod$marcador], label = "\u2022", hjust = 0, family = FONTE,
             size = pt_mm(CORPO_MIN), colour = COR$tinta) +
    geom_segment(data = leg_seg, aes(x = x, xend = xend, y = y, yend = y, linetype = tipo), colour = COR$tinta2,
                 linewidth = LINHA_DADO * 0.8, arrow = seta) +
    geom_rect(data = leg_box, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = leg_box$fundo,
              colour = leg_box$borda, linewidth = LINHA) +
    geom_text(data = leg_txt, aes(x = x, y = ly, label = txt), hjust = 0, family = FONTE, size = pt_mm(CORPO_MIN),
              colour = COR$tinta2) +
    coord_cartesian(xlim = c(0, 170), ylim = c(y0, y1), expand = FALSE, clip = "off") +
    theme_void(base_family = FONTE) +
    theme(plot.background = element_rect(fill = "transparent", colour = NA), plot.margin = margin(0, 0, 0, 0))
  gravar_figura(g, "modelo_logico", "larga", altura_mm = y1 - y0)
}

# ================================================================ 2. PRISMA
fig_prisma <- function() {
  d <- ler("dados_prisma.csv")
  P <- 7          # corpo das caixas
  LH <- 3.15      # altura de linha (mm)
  PAD <- 1.6
  IND <- 2.4      # recuo dos itens (o marcador fica na coluna do recuo zero)
  # colunas (mm)
  X0 <- 8
  larg_ramo <- (170 - X0) / 2
  col <- list(b = c(X0 + 0.5, X0 + 38), bs = c(X0 + 43, X0 + larg_ramo - 2),
              o = c(X0 + larg_ramo + 2, X0 + larg_ramo + 39.5), os = c(X0 + larg_ramo + 44.5, 169.6))
  caixa_col <- c(b_ident = "b", b_removidos = "bs", b_triados = "b", b_excl_triagem = "bs", b_buscados = "b",
                 b_nao_rec = "bs", b_avaliados = "b", b_excl_tc = "bs",
                 o_ident = "o", o_removidos = "os", o_triados = "o", o_excl_triagem = "os", o_buscados = "o",
                 o_nao_rec = "os", o_avaliados = "o", o_excl_tc = "os")
  caixa_linha <- c(ident = 1, removidos = 1, triados = 2, excl_triagem = 2, buscados = 3, nao_rec = 3,
                   avaliados = 4, excl_tc = 4)
  caixas <- unique(d$caixa[d$estilo != "seta"])
  txt <- list(); lin <- list()
  for (cx in setdiff(caixas, "incluidos")) {
    cl <- col[[caixa_col[[cx]]]]
    w <- cl[2] - cl[1] - 2 * PAD
    x <- d[d$caixa == cx, ]
    ls <- character(0); es <- character(0); ind <- numeric(0); mk <- logical(0)
    for (i in seq_len(nrow(x))) {
      item <- x$estilo[i] == "normal"
      q <- quebrar(gsub("(n = ", "(n\u00a0=\u00a0", x$texto[i], fixed = TRUE), w - if (item) IND else 0, P)
      ls <- c(ls, q); es <- c(es, rep(x$estilo[i], length(q)))
      ind <- c(ind, rep(if (item) IND else 0, length(q))); mk <- c(mk, item & seq_along(q) == 1)
    }
    lin[[cx]] <- data.frame(caixa = cx, texto = ls, estilo = es, indent = ind, marcador = mk, stringsAsFactors = FALSE)
  }
  n_lin <- vapply(lin, nrow, integer(1))
  # altura de cada faixa = maior caixa da faixa
  faixa_de <- function(cx) caixa_linha[[sub("^[bo]_", "", cx)]]
  alt_faixa <- vapply(1:4, function(f) max(n_lin[vapply(names(n_lin), faixa_de, numeric(1)) == f]) * LH + 2 * PAD,
                      numeric(1))
  GAP <- 6
  CAB <- 7      # cabeçalhos dos ramos
  topo <- 0
  y_cab <- c(topo - CAB, topo)
  y_top <- numeric(4); y_bot <- numeric(4)
  cur <- topo - CAB - GAP + 2
  for (f in 1:4) { y_top[f] <- cur; y_bot[f] <- cur - alt_faixa[f]; cur <- y_bot[f] - GAP }
  inc <- d[d$caixa == "incluidos", ]
  h_inc <- nrow(inc) * LH + 2 * PAD
  y_inc <- c(cur - h_inc - 2, cur - 2)
  retang <- do.call(rbind, lapply(names(lin), function(cx) {
    cl <- col[[caixa_col[[cx]]]]; f <- faixa_de(cx)
    h <- n_lin[[cx]] * LH + 2 * PAD
    # caixas laterais centradas na faixa; principais ocupam a faixa toda
    lateral <- caixa_col[[cx]] %in% c("bs", "os")
    yt <- if (lateral) (y_top[f] + y_bot[f]) / 2 + h / 2 else y_top[f]
    yb <- if (lateral) yt - h else y_bot[f]
    data.frame(caixa = cx, xmin = cl[1], xmax = cl[2], ymin = yb, ymax = yt)
  }))
  inc_x <- c(col$b[1] + 12, col$o[2] - 12)
  retang <- rbind(retang, data.frame(caixa = "incluidos", xmin = inc_x[1], xmax = inc_x[2], ymin = y_inc[1],
                                     ymax = y_inc[2]))
  R_ <- split(retang, retang$caixa)
  # texto das caixas
  tx <- do.call(rbind, lapply(names(lin), function(cx) {
    r <- R_[[cx]]; l <- lin[[cx]]
    ymid <- (r$ymin + r$ymax) / 2
    y0 <- ymid + (nrow(l) - 1) * LH / 2
    data.frame(x = r$xmin + PAD + l$indent, y = y0 - (seq_len(nrow(l)) - 1) * LH, texto = l$texto,
               estilo = l$estilo, marcador = l$marcador)
  }))
  marc <- tx[tx$marcador, ]
  marc$x <- marc$x - IND
  tx$marcador <- NULL
  r <- R_[["incluidos"]]
  tx <- rbind(tx, data.frame(x = (r$xmin + r$xmax) / 2, y = (r$ymin + r$ymax) / 2 + (nrow(inc) - 1) * LH / 2 -
                               (seq_len(nrow(inc)) - 1) * LH, texto = inc$texto, estilo = "incl"))
  tx$hjust <- ifelse(tx$estilo == "incl", 0.5, 0)
  tx$cor <- ifelse(tx$estilo == "normal", COR$tinta2, COR$tinta)
  tx$face <- ifelse(tx$estilo == "incl", "bold", "plain")
  # setas
  cx <- function(k) (R_[[k]]$xmin + R_[[k]]$xmax) / 2
  cy <- function(k) (R_[[k]]$ymin + R_[[k]]$ymax) / 2
  setas <- list()
  for (p in c("b", "o")) {
    s <- function(a, b) paste0(p, "_", c(a, b))
    for (par in list(c("ident", "triados"), c("triados", "buscados"), c("buscados", "avaliados"))) {
      k <- s(par[1], par[2])
      setas[[length(setas) + 1]] <- data.frame(x = cx(k[1]), y = R_[[k[1]]]$ymin, xend = cx(k[1]), yend = R_[[k[2]]]$ymax)
    }
    for (par in list(c("ident", "removidos"), c("triados", "excl_triagem"), c("buscados", "nao_rec"),
                     c("avaliados", "excl_tc"))) {
      k <- s(par[1], par[2])
      setas[[length(setas) + 1]] <- data.frame(x = R_[[k[1]]]$xmax, y = cy(k[2]), xend = R_[[k[2]]]$xmin, yend = cy(k[2]))
    }
  }
  setas <- do.call(rbind, setas)
  # avaliados -> incluídos (com o número de relatos incluídos de cada ramo)
  seta_inc <- rbind(
    data.frame(x = cx("b_avaliados"), y = R_[["b_avaliados"]]$ymin, xend = cx("b_avaliados"), yend = y_inc[2]),
    data.frame(x = cx("o_avaliados"), y = R_[["o_avaliados"]]$ymin, xend = cx("o_avaliados"), yend = y_inc[2])
  )
  rot_inc <- data.frame(x = seta_inc$x + 1.5, y = (seta_inc$y + seta_inc$yend) / 2,
                        texto = c(d$texto[d$caixa == "b_seta_incl"], d$texto[d$caixa == "o_seta_incl"]))
  # cabeçalhos dos ramos e faixas de fase
  cab <- data.frame(xmin = c(col$b[1], col$o[1]), xmax = c(col$bs[2], col$os[2]), ymin = y_cab[1], ymax = y_cab[2],
                    texto = c("Busca em bases de dados", "Busca por citações (outros métodos)"))
  fases <- data.frame(ymin = c(y_bot[1], y_bot[4], y_inc[1]), ymax = c(y_cab[1] - 1, y_top[2], y_top[2] - 0) ,
                      texto = c("Identificação", "Triagem", "Inclusão"))
  fases$ymin <- c(y_bot[1] - GAP / 2 + 0.5, y_bot[4] - GAP / 2 + 0.5, y_inc[1])
  fases$ymax <- c(y_cab[1] - 1, y_top[2] + GAP / 2 - 0.5, y_bot[4] - GAP / 2 - 0.5)

  g <- ggplot() +
    geom_rect(data = cab, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = COR$fundo_caixa, colour = NA) +
    geom_text(data = cab, aes(x = xmin + PAD, y = (ymin + ymax) / 2, label = texto), hjust = 0, family = FONTE,
              fontface = "bold", size = pt_mm(P), colour = COR$tinta) +
    geom_rect(data = fases, aes(xmin = 0, xmax = X0 - 3, ymin = ymin, ymax = ymax), fill = COR$fundo_caixa, colour = NA) +
    geom_text(data = fases, aes(x = (X0 - 3) / 2, y = (ymin + ymax) / 2, label = texto), angle = 90, family = FONTE,
              fontface = "bold", size = pt_mm(P), colour = COR$tinta) +
    geom_segment(data = setas, aes(x = x, y = y, xend = xend, yend = yend), colour = COR$tinta2, linewidth = LINHA_DADO * 0.8,
                 arrow = arrow(length = unit(1.3, "mm"), type = "closed", angle = 22)) +
    geom_segment(data = seta_inc, aes(x = x, y = y, xend = xend, yend = yend), colour = COR$tinta2,
                 linewidth = LINHA_DADO * 0.8, arrow = arrow(length = unit(1.3, "mm"), type = "closed", angle = 22)) +
    geom_text(data = rot_inc, aes(x, y, label = texto), hjust = 0, family = FONTE, size = pt_mm(CORPO_MIN), colour = COR$tinta2) +
    geom_rect(data = retang, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
              fill = ifelse(retang$caixa == "incluidos", "#e3edf9", "transparent"), colour = COR$tinta2, linewidth = LINHA) +
    geom_text(data = tx, aes(x, y, label = texto, hjust = hjust), colour = tx$cor, fontface = tx$face, family = FONTE,
              size = pt_mm(P)) +
    geom_text(data = marc, aes(x, y), label = "\u2022", hjust = 0, colour = COR$tinta2, family = FONTE,
              size = pt_mm(P)) +
    coord_cartesian(xlim = c(0, 170), ylim = c(y_inc[1] - 1, 0.5), expand = FALSE, clip = "off") +
    theme_void(base_family = FONTE) +
    theme(plot.background = element_rect(fill = "transparent", colour = NA), plot.margin = margin(0, 0, 0, 0))
  gravar_figura(g, "prisma", "larga", altura_mm = 0.5 - (y_inc[1] - 1))
}

# letra de painel: entra no próprio título, em negrito, na mesma linha de base (a etiqueta do patchwork ficava meia
# linha acima do título ou numa linha própria)
com_letra <- function(letra, titulo) paste0(letra, "\u00a0\u00a0", titulo)

# ================================================================ 3. risco de viés
fig_rob <- function() {
  d <- ler("dados_rob.csv")
  GL <- c(dominio = "domínios", geral = "geral", `com grupo de comparação` = "com grupo de comparação",
          `série temporal interrompida` = "série temporal interrompida")
  painel <- function(f, grupos, titulo, larg_rot = 40, legenda = TRUE) {
    x <- d[d$ferramenta == f & d$grupo %in% grupos, ]
    dom <- unique(x[, c("dominio", "dominio_rotulo", "ordem", "grupo", "total")])
    dom <- dom[order(dom$ordem), ]
    dom$rot <- vapply(dom$dominio_rotulo, function(r) paste(quebrar(r, larg_rot, 7), collapse = "\n"), character(1))
    x$y <- factor(x$dominio, levels = rev(dom$dominio))
    dom$y <- factor(dom$dominio, levels = rev(dom$dominio))
    x$grupo_f <- factor(x$grupo, levels = grupos, labels = GL[grupos])
    dom$grupo_f <- factor(dom$grupo, levels = grupos, labels = GL[grupos])
    niv <- unique(d[d$ferramenta == f, c("nivel", "julgamento_rotulo")])
    niv <- niv[order(niv$nivel), ]
    x$nivel_f <- factor(x$nivel, levels = niv$nivel)
    p <- ggplot(x, aes(x = proporcao, y = y, fill = nivel_f)) +
      geom_col(width = 0.72, colour = COR$tinta2, linewidth = LINHA, position = position_stack(reverse = TRUE)) +
      geom_text(data = dom, aes(x = 1.03, y = y, label = paste0("n = ", total)), inherit.aes = FALSE, hjust = 0,
                family = FONTE, size = pt_mm(CORPO_MIN), colour = COR$tinta2) +
      scale_fill_manual(values = COR_ROB[as.character(niv$nivel)], labels = niv$julgamento_rotulo, name = NULL,
                        drop = FALSE) +
      scale_x_continuous(labels = pct_br(), breaks = seq(0, 1, 0.5), expand = c(0, 0)) +
      scale_y_discrete(labels = stats::setNames(dom$rot, dom$dominio)) +
      facet_wrap(~grupo_f, ncol = 1, scales = "free_y", space = "free_y") +
      coord_cartesian(xlim = c(0, 1), clip = "off") +
      labs(title = titulo, x = NULL, y = NULL) +
      tema_revista() +
      theme(legend.position = if (legenda) "bottom" else "none", legend.location = "plot",
            legend.justification = "left", legend.key.size = unit(2.6, "mm"), legend.key.spacing.x = unit(1.2, "mm"),
            legend.text = element_text(size = CORPO_MIN, margin = margin(l = 2.5, r = 3)),
            legend.margin = margin(t = 0, l = 0), legend.box.margin = margin(t = -3, l = 0),
            plot.margin = margin(2, 27, 2, 2), axis.text.y = element_text(colour = COR$tinta, size = 7, lineheight = 0.9),
            axis.text.x = element_text(size = CORPO_MIN),
            strip.text = element_text(face = "plain", colour = COR$tinta2, size = CORPO_MIN, hjust = 0,
                                      margin = margin(1.5, 0, 1, 0)),
            strip.clip = "off", panel.spacing.y = unit(1.2, "mm"))
    if (!f %in% "epoc") p <- p + theme(strip.text = element_blank(), panel.spacing.y = unit(2, "mm"))
    p
  }
  a <- painel("rob2", c("dominio", "geral"), com_letra("a", "RoB 2 (randomizados)"))
  b <- painel("robins_i", c("dominio", "geral"), com_letra("b", "ROBINS-I V2 (não randomizados)"))
  c1 <- painel("epoc", "com grupo de comparação", com_letra("c", "EPOC (não randomizados)"), larg_rot = 50)
  c2 <- painel("epoc", c("série temporal interrompida", "geral"), "\u00a0", larg_rot = 38, legenda = FALSE)
  g <- (a | b) / (c1 | c2) + plot_layout(heights = c(7.3, 10)) +
    plot_annotation(caption = paste0("Julgamentos de IA não validados por humano. Unidade: resultado avaliado (estudo \u00d7 desfecho).",
                                     "\n\u2020 Critério fora do julgamento geral do EPOC (Emenda 4a)."),
                    theme = theme(plot.caption = element_text(family = FONTE, size = CORPO_MIN, colour = COR$tinta2,
                                                              hjust = 0),
                                  plot.background = element_rect(fill = "transparent", colour = NA)))
  gravar_figura(g, "rob", "larga", altura_mm = 128)
}

# ================================================================ 4. células
fig_celulas <- function() {
  d <- ler("dados_celulas.csv")
  d$y <- -d$ordem
  blocos <- unique(d[, c("bloco", "bloco_rotulo", "bloco_sentido")])
  blocos$lab <- italicizar(paste0(blocos$bloco_rotulo, " (", blocos$bloco_sentido, ")"), negrito = TRUE)
  d$bloco_f <- factor(d$bloco, levels = blocos$bloco, labels = blocos$lab)
  rot_linha <- stats::setNames(d$rotulo_linha, d$y)
  pr <- d[d$marca == "proporcao", ]
  pr$cor <- unlist(COR[ifelse(pr$maioria == "empate", "misto", pr$maioria)])
  # chave de cor (revisão visual, item 15): a cor do ponto e do IC diz para que lado aponta a maioria dos estudos
  ROT_MAIORIA <- c(a_favor = "a favor", contra = "contra", empate = "empate")
  if (!all(pr$maioria %in% names(ROT_MAIORIA))) stop("dados_celulas.csv: maioria fora de a_favor/contra/empate")
  pr$maioria_f <- factor(ROT_MAIORIA[pr$maioria], levels = ROT_MAIORIA)
  X_XY <- 1.10; X_C <- 1.44; X_W <- 1.615
  circ <- do.call(rbind, lapply(which(!is.na(d$certeza_nivel)), function(i) {
    data.frame(y = d$y[i], bloco_f = d$bloco_f[i], x = X_C + 0.015 + (0:3) * 0.037, cheio = (1:4) <= d$certeza_nivel[i])
  }))
  marca <- d[d$marca != "proporcao", ]
  g <- ggplot(d, aes(y = y)) +
    geom_vline(xintercept = c(0, 0.25, 0.75, 1), colour = COR$grade, linewidth = LINHA) +
    geom_vline(xintercept = 0.5, colour = COR$tinta3, linewidth = LINHA, linetype = "22") +
    geom_linerange(data = pr, aes(xmin = ic_inf, xmax = ic_sup), colour = pr$cor, linewidth = LINHA_DADO) +
    geom_point(data = pr, aes(x = proporcao, shape = classe_rotulo, fill = maioria_f), colour = "white", size = 2.3,
               stroke = 0.35) +
    geom_point(data = marca[marca$marca == "nulo", ], aes(x = 0.5), shape = 21, fill = NA, colour = COR$nulo,
               size = 2.2, stroke = 0.7) +
    geom_text(data = marca[marca$marca == "nulo", ], aes(x = 0.535, label = rotulo_marca), hjust = 0, family = FONTE,
              size = pt_mm(CORPO_MIN), colour = COR$tinta2) +
    geom_text(data = marca[marca$marca == "vazia", ], aes(x = 0.535, label = rotulo_marca), hjust = 0, family = FONTE,
              fontface = "italic", size = pt_mm(CORPO_MIN), colour = COR$tinta3) +
    geom_text(aes(x = X_XY, label = rotulo_xy), hjust = 0, family = FONTE, size = pt_mm(7), colour = COR$tinta) +
    geom_point(data = circ, aes(x = x), shape = ifelse(circ$cheio, 10, 1), size = 1.9, stroke = 0.45,
               colour = COR$tinta) +
    geom_text(aes(x = X_W, label = certeza_texto), hjust = 0, family = FONTE, size = pt_mm(7),
              colour = ifelse(is.na(d$certeza_nivel), COR$tinta3, COR$tinta)) +
    scale_shape_manual(values = c(randomizado = 21, `não randomizado` = 22), breaks = c("randomizado", "não randomizado"),
                       name = "Classe de desenho") +
    scale_fill_manual(values = stats::setNames(c(COR$a_favor, COR$contra, COR$misto), ROT_MAIORIA), drop = FALSE,
                      name = "Cor: maioria dos estudos") +
    scale_x_continuous(limits = c(-0.02, 1.83), breaks = seq(0, 1, 0.25), labels = num_br(0.01),
                       expand = c(0, 0),
                       sec.axis = dup_axis(breaks = c(0, X_XY, X_C), name = NULL,
                                           labels = c("proporção a favor (IC 95%)", "x de y", "certeza (GRADE)"))) +
    scale_y_continuous(breaks = function(l) d$y[d$y >= l[1] & d$y <= l[2]],
                       labels = function(b) unname(rot_linha[as.character(b)]),
                       expand = expansion(add = 0.62)) +
    facet_wrap(~bloco_f, ncol = 1, scales = "free_y", space = "free_y", labeller = label_parsed) +
    labs(x = "proporção dos estudos com direção definida que apontam a favor", y = NULL) +
    guides(x = guide_axis(cap = "both"), x.sec = guide_axis(cap = "none"),
           shape = guide_legend(order = 1, override.aes = list(fill = COR$tinta2, colour = "white", size = 2.3)),
           fill = guide_legend(order = 2, override.aes = list(shape = 21, colour = "white", size = 2.3))) +
    tema_revista() +
    theme(axis.text.y = element_text(colour = COR$tinta, size = 7, hjust = 1),
          axis.text.x.top = element_text(colour = COR$tinta, size = 7, hjust = 0),
          axis.ticks.x.top = element_blank(), axis.line.x.top = element_blank(),
          axis.title.x = element_text(hjust = 0, size = 7, colour = COR$tinta2, margin = margin(t = 2)),
          legend.position = "bottom", legend.justification = "left", legend.key.size = unit(3, "mm"),
          legend.box = "vertical", legend.box.just = "left", legend.spacing.y = unit(0.6, "mm"),
          legend.margin = margin(t = -2), legend.title = element_text(size = 7),
          panel.spacing.y = unit(1.5, "mm"), strip.text = element_text(size = 7.5, hjust = 0,
                                                                        margin = margin(3, 0, 1.5, 0)),
          plot.margin = margin(2, 2, 2, 2))
  gravar_figura(g, "celulas", "larga", altura_mm = 132)
}

# ================================================================ 5. direção por estudo
# legenda desenhada item a item, com larguras medidas (quebra de linha quando passa da largura)
legenda_itens <- function(itens, x0 = 1.5, larg = 168, gap = 4.5, p = CORPO_MIN) {
  x <- x0; y <- 0; out <- list()
  for (it in itens) {
    w <- (if (it$tipo == "titulo") 0 else 3) + larg_mm(gsub("[*]", "", it$texto), p)
    if ((x + w > larg || it$tipo == "titulo") && x > x0) { x <- x0; y <- y - 1 }
    out[[length(out) + 1]] <- data.frame(x = x, y = y, tipo = it$tipo, chave = it$chave, texto = it$texto)
    x <- x + w + gap
  }
  do.call(rbind, out)
}

fig_direcao <- function() {
  d <- ler("dados_direcao.csv")
  d$estudo <- autor_ano(d$chave)
  d$estudo[d$excluido_critico == 1] <- paste0(d$estudo[d$excluido_critico == 1], " \u2020")
  RH <- 3.1    # altura de linha (mm)
  XC <- c(comp = 1.5, classe = 54, estudo = 76, glifo = 134.5, dir = 138.5, rob = 163)
  forma <- c(a_favor = 24, contra = 25, misto = 23, nulo = 21)
  montar <- function(pn) {
    x <- d[d$painel == pn, ]
    x <- x[order(x$ordem), ]
    linhas <- list(); cab <- list(); y <- -1.1; bloco_ant <- ""; cls_ant <- ""; cel_ant <- ""
    for (i in seq_len(nrow(x))) {
      if (x$bloco[i] != bloco_ant) {
        if (bloco_ant != "") y <- y - 0.45
        cab[[length(cab) + 1]] <- data.frame(y = y, texto = x$bloco_rotulo[i])
        bloco_ant <- x$bloco[i]; cls_ant <- ""; cel_ant <- ""
        y <- y - 1.05
      }
      id_cel <- paste(x$classe[i], x$rotulo_celula[i], x$celula_id[i])
      nova_cls <- x$classe[i] != cls_ant
      linhas[[i]] <- cbind(x[i, ], yy = y, mostra_cls = nova_cls, mostra_cel = id_cel != cel_ant,
                           filete = if (cel_ant == "") "nenhum" else if (nova_cls) "classe" else if (id_cel != cel_ant) "celula" else "nenhum")
      cls_ant <- x$classe[i]; cel_ant <- id_cel
      y <- y - 1
    }
    list(L = do.call(rbind, linhas), C = do.call(rbind, cab), y_min = y + 0.4)
  }
  painel <- function(pn, titulo) {
    m <- montar(pn); L <- m$L; C <- m$C
    L$cor <- unlist(COR[L$glifo])
    L$fill <- ifelse(L$glifo == "nulo", NA, L$cor)
    L$face_dir <- ifelse(L$italico == 1, "italic", "plain")
    fil <- L[L$filete != "nenhum", ]
    cabecalho <- data.frame(x = XC[c("comp", "classe", "estudo", "dir", "rob")], hjust = c(0, 0, 0, 0, 0.5),
                            texto = c("comparação", "classe", "estudo", "direção", "risco de viés"))
    g <- ggplot() +
      geom_segment(data = fil, aes(x = ifelse(filete == "classe", XC[["comp"]], XC[["comp"]]), xend = 168,
                                   y = yy + 0.5, yend = yy + 0.5),
                   colour = ifelse(fil$filete == "classe", COR$tinta3, COR$grade), linewidth = LINHA) +
      geom_text(data = C, aes(x = XC[["comp"]], y = y, label = italicizar(texto, negrito = TRUE)), parse = TRUE,
                hjust = 0, family = FONTE, size = pt_mm(7.2), colour = COR$tinta) +
      geom_segment(data = C, aes(x = XC[["comp"]], xend = 168, y = y - 0.58, yend = y - 0.58), colour = COR$tinta2,
                   linewidth = LINHA) +
      geom_text(data = L[L$mostra_cel, ], aes(x = XC[["comp"]], y = yy, label = rotulo_celula), hjust = 0,
                family = FONTE, size = pt_mm(7), colour = COR$tinta) +
      geom_text(data = L[L$mostra_cls, ], aes(x = XC[["classe"]], y = yy, label = classe_rotulo), hjust = 0,
                family = FONTE, size = pt_mm(7), colour = COR$tinta2) +
      geom_text(data = L, aes(x = XC[["estudo"]], y = yy, label = estudo), hjust = 0, family = FONTE, size = pt_mm(7),
                colour = COR$tinta) +
      geom_point(data = L, aes(x = XC[["glifo"]], y = yy, shape = glifo), fill = L$fill, colour = L$cor, size = 2,
                 stroke = 0.6) +
      geom_text(data = L, aes(x = XC[["dir"]], y = yy, label = direcao_rotulo), fontface = L$face_dir, hjust = 0,
                family = FONTE, size = pt_mm(7), colour = COR$tinta) +
      geom_point(data = L, aes(x = XC[["rob"]], y = yy), shape = 21, fill = COR_ROB[as.character(L$rob_nivel)],
                 colour = COR$tinta2, size = 2.6, stroke = 0.3) +
      geom_text(data = L, aes(x = XC[["rob"]], y = yy - 0.03, label = SIMBOLO_ROB[as.character(rob_nivel)]),
                family = FONTE, fontface = "bold", size = pt_mm(CORPO_MIN), colour = COR$tinta) +
      geom_text(data = cabecalho, aes(x = x, y = -0.2, label = texto, hjust = hjust), family = FONTE,
                size = pt_mm(CORPO_MIN), colour = COR$tinta2) +
      scale_shape_manual(values = forma, guide = "none") +
      scale_x_continuous(limits = c(0, 170), expand = c(0, 0)) +
      scale_y_continuous(limits = c(m$y_min, 0.5), expand = c(0, 0)) +
      labs(title = parse(text = italicizar(titulo, negrito = TRUE))[[1]]) +
      theme_void(base_family = FONTE) +
      theme(plot.title = element_text(family = FONTE, size = 7.5, hjust = 0, margin = margin(b = 1.5, l = 4),
                                      colour = COR$tinta),
            plot.title.position = "plot",
            plot.background = element_rect(fill = "transparent", colour = NA), plot.margin = margin(1, 0, 5, 0))
    list(g = g, n = 0.5 - m$y_min)
  }
  a <- painel("principal", com_letra("a", "Síntese principal (contagem por direção da SWiM)"))
  b <- painel("fora", com_letra("b", "Fora da contagem (agrupamento amplo, post hoc): estudos e células que não entram na síntese principal"))
  itens <- list(
    list(tipo = "glifo", chave = "a_favor", texto = "a favor (bandwagon, viabilidade, momentum a favor, mobilização) ou positivo"),
    list(tipo = "glifo", chave = "contra", texto = "contra (underdog, contra a viabilidade, momentum contra, desmobilização)"),
    list(tipo = "glifo", chave = "misto", texto = "misto"),
    list(tipo = "glifo", chave = "nulo", texto = "nulo por \u00b1\u03b4"),
    list(tipo = "texto", chave = "\u2020", texto = "risco crítico, fora do teste de sinal"),
    list(tipo = "titulo", chave = "", texto = "Risco de viés:"),
    list(tipo = "rob", chave = "1", texto = "baixo"),
    list(tipo = "rob", chave = "2", texto = "algumas preocupações ou moderado"),
    list(tipo = "rob", chave = "3", texto = "alto ou grave"),
    list(tipo = "rob", chave = "4", texto = "crítico")
  )
  lg <- legenda_itens(itens)
  lg$x[lg$tipo == "titulo"] <- lg$x[lg$tipo == "titulo"] - 2.3
  lg$lab <- italicizar(lg$texto)
  gl <- lg[lg$tipo == "glifo", ]; gl$cor <- unlist(COR[gl$chave]); gl$fill <- ifelse(gl$chave == "nulo", NA, gl$cor)
  rb <- lg[lg$tipo == "rob", ]; tx <- lg[lg$tipo == "texto", ]
  n_leg <- 1 - min(lg$y)
  leg <- ggplot() +
    geom_point(data = gl, aes(x = x, y = y, shape = chave), fill = gl$fill, colour = gl$cor, size = 2, stroke = 0.6) +
    geom_point(data = rb, aes(x = x, y = y), shape = 21, fill = COR_ROB[rb$chave], colour = COR$tinta2, size = 2.6,
               stroke = 0.3) +
    geom_text(data = rb, aes(x = x, y = y - 0.03, label = SIMBOLO_ROB[chave]), family = FONTE, fontface = "bold",
              size = pt_mm(CORPO_MIN)) +
    geom_text(data = tx, aes(x = x, y = y, label = chave), family = FONTE, size = pt_mm(7)) +
    geom_text(data = lg, aes(x = x + 2.3, y = y, label = lab), parse = TRUE, hjust = 0, family = FONTE,
              size = pt_mm(CORPO_MIN), colour = COR$tinta) +
    scale_shape_manual(values = forma, guide = "none") +
    scale_x_continuous(limits = c(0, 170), expand = c(0, 0)) +
    scale_y_continuous(limits = c(min(lg$y) - 0.5, 0.5), expand = c(0, 0)) +
    theme_void() + theme(plot.background = element_rect(fill = "transparent", colour = NA),
                         plot.margin = margin(3, 0, 0, 0))
  g <- a$g / b$g / leg + plot_layout(heights = c(a$n, b$n, n_leg)) +
    plot_annotation(theme = theme(plot.background = element_rect(fill = "transparent", colour = NA)))
  gravar_figura(g, "direcao", "larga", altura_mm = (a$n + b$n + n_leg) * RH + 17)
}

# ================================================================ 6. metas exploratórias
fig_metas <- function() {
  d <- ler("dados_metas.csv")
  d$rotulo <- "Estimativa combinada (CHE + RVE)"
  d$rotulo[d$tipo == "efeito"] <- autor_ano(d$chave[d$tipo == "efeito"])
  tem_extra <- !is.na(d$rotulo_extra) & d$rotulo_extra != ""
  d$rotulo[tem_extra] <- paste0(d$rotulo[tem_extra], ", ", d$rotulo_extra[tem_extra])
  # "g (IC)" já formatado em preparar_dados_figuras.py, com arredondamento decimal meio para cima (0,975 -> 0,98);
  # a ordem das linhas (menor erro-padrão no topo) também vem do CSV
  if (!"rotulo_valor" %in% names(d) || anyNA(d$rotulo_valor)) stop("dados_metas.csv sem rotulo_valor")
  d$txt <- d$rotulo_valor
  painel <- function(pn) {
    x <- d[d$painel == pn, ]
    x$y <- rev(seq_len(nrow(x)))
    x$y[x$tipo == "combinado"] <- x$y[x$tipo == "combinado"] - 0.35
    delta <- x$delta[1]
    ef <- x[x$tipo == "efeito", ]; cb <- x[x$tipo == "combinado", ]
    dia <- data.frame(x = c(cb$ic_inf, cb$estimativa, cb$ic_sup, cb$estimativa),
                      y = cb$y + c(0, 0.32, 0, -0.32))
    lim <- range(c(x$ic_inf, x$ic_sup, -delta, delta))
    lim <- c(floor(lim[1] * 2) / 2, ceiling(lim[2] * 2) / 2)
    ggplot(x, aes(y = y)) +
      annotate("rect", xmin = -delta, xmax = delta, ymin = -Inf, ymax = Inf, fill = COR$grade, alpha = 0.9) +
      geom_vline(xintercept = 0, colour = COR$tinta2, linewidth = LINHA) +
      geom_hline(yintercept = min(ef$y) - 0.6, colour = COR$grade, linewidth = LINHA) +
      geom_linerange(data = ef, aes(xmin = ic_inf, xmax = ic_sup), colour = COR$tinta, linewidth = LINHA_DADO) +
      geom_point(data = ef, aes(x = estimativa), shape = 15, size = 1.9, colour = COR$tinta) +
      geom_polygon(data = dia, aes(x = x, y = y), fill = NA, colour = COR$tinta, linewidth = LINHA_DADO) +
      scale_x_continuous(limits = lim, breaks = scales::breaks_width(0.5), labels = num_br(0.1),
                         expand = expansion(mult = 0.02)) +
      scale_y_continuous(breaks = x$y, labels = x$rotulo, expand = expansion(add = 0.6),
                         sec.axis = dup_axis(labels = x$txt, name = NULL)) +
      labs(title = com_letra(pn, x$painel_titulo[1]), x = parse(text = italicizar("g de Hedges (positivo = bandwagon)"))[[1]], y = NULL) +
      guides(x = guide_axis(cap = "both")) +
      tema_revista() +
      theme(axis.text.y.left = element_text(colour = COR$tinta, size = 7, hjust = 0),
            axis.text.y.right = element_text(colour = COR$tinta, size = 7, hjust = 0),
            axis.ticks.y = element_blank(),
            axis.title.x = element_text(size = 7, colour = COR$tinta2, margin = margin(t = 2)),
            plot.margin = margin(2, 2, 4, 2))
  }
  a <- painel("a"); b <- painel("b")
  na <- sum(d$painel == "a"); nb <- sum(d$painel == "b")
  g <- a / b + plot_layout(heights = c(na, nb)) +
    plot_annotation(theme = theme(plot.background = element_rect(fill = "transparent", colour = NA)))
  gravar_figura(g, "metas", "larga", altura_mm = (na + nb) * 5.2 + 34)
}

# ================================================================ 7. realismo
fig_realismo <- function() {
  d <- ler("dados_realismo.csv")
  niveis <- c("hipotetico", "induzido", "real")
  rot_niv <- c(hipotetico = "hipotético", induzido = "induzido", real = "real")
  ordem_glifo <- c("a_favor", "misto", "nulo", "contra")
  d$glifo_ord <- match(d$glifo, ordem_glifo)
  d <- d[order(d$tabela, d$classe, d$realismo, d$excluido_critico, d$glifo_ord, d$chave), ]
  d$pos <- stats::ave(seq_len(nrow(d)), d$tabela, d$classe, d$realismo, FUN = seq_along)
  d$yv <- match(d$realismo, rev(niveis))
  d$desf_f <- factor(d$tabela, levels = c("T9", "T14"),
                     labels = c("Apoio a quem aparece à frente (célula principal)", "Comparecimento"))
  d$classe_f <- factor(d$classe_rotulo, levels = c("randomizado", "não randomizado"))
  d$cat <- ifelse(d$excluido_critico == 1, paste0(d$glifo, "_critico"), d$glifo)
  preench <- c(a_favor = COR$a_favor, contra = COR$contra, misto = COR$misto, nulo = "white",
               contra_critico = "#f7c3ae", a_favor_critico = "#a9c9ef")
  borda <- c(a_favor = COR$a_favor, contra = COR$contra, misto = COR$misto, nulo = COR$nulo,
             contra_critico = COR$contra, a_favor_critico = COR$a_favor)
  rot_cat <- c(a_favor = "a favor (bandwagon; mobilização)", contra = "contra (underdog; desmobilização)",
               misto = "misto", nulo = "nulo por ±δ", contra_critico = "contra, risco crítico (fora do teste)",
               a_favor_critico = "a favor, risco crítico (fora do teste)")
  cats <- intersect(names(preench), unique(d$cat))
  tot <- stats::aggregate(pos ~ tabela + classe + realismo + desf_f + classe_f + yv, data = d, FUN = max)
  rot_leg <- lapply(italicizar(rot_cat[cats]), function(e) parse(text = e)[[1]])
  painel <- function(tb, titulo, eixo_x) {
    x <- d[d$tabela == tb, ]
    tt <- tot[tot$tabela == tb, ]
    ggplot(x) +
      geom_tile(aes(x = pos - 0.5, y = yv, fill = cat, colour = cat), width = 0.9, height = 0.62,
                linewidth = LINHA * 1.6, linetype = ifelse(x$excluido_critico == 1, "22", "solid")) +
      geom_text(data = tt, aes(x = pos + 0.12, y = yv, label = pos), hjust = 0, family = FONTE, size = pt_mm(7),
                colour = COR$tinta2) +
      scale_fill_manual(values = preench[cats], labels = rot_leg, name = NULL, breaks = cats, limits = cats,
                        drop = FALSE) +
      scale_colour_manual(values = borda[cats], breaks = cats, limits = cats, guide = "none", drop = FALSE) +
      scale_x_continuous(limits = c(0, 6), breaks = 0:5, expand = c(0, 0), labels = num_br(1)) +
      scale_y_continuous(breaks = 1:3, labels = rot_niv[rev(niveis)], limits = c(0.5, 3.5), expand = c(0, 0)) +
      facet_wrap(~classe_f, nrow = 1, drop = FALSE) +
      labs(title = titulo, x = if (eixo_x) "estudos \u00d7 célula (um bloco por estudo em cada célula)" else NULL,
           y = NULL) +
      guides(fill = guide_legend(nrow = 2, override.aes = list(colour = borda[cats], linewidth = LINHA * 1.6)),
             x = guide_axis(cap = "both")) +
      tema_revista() +
      theme(strip.text.x = element_text(face = "plain", colour = COR$tinta2, size = 7, hjust = 0),
            axis.text.y = element_text(colour = COR$tinta, size = 7),
            axis.title = element_text(size = 7, colour = COR$tinta2),
            panel.spacing.x = unit(6, "mm"),
            panel.grid.major.x = element_line(colour = COR$grade, linewidth = LINHA),
            legend.position = "bottom", legend.justification = "left", legend.location = "plot",
            legend.key.size = unit(3, "mm"), legend.text = element_text(size = CORPO_MIN), legend.margin = margin(t = -1))
  }
  a <- painel("T9", "Apoio a quem aparece à frente (célula principal)", FALSE)
  b <- painel("T14", "Comparecimento", TRUE)
  if (!all(cats %in% d$cat[d$tabela == "T14"])) stop("a legenda do painel de comparecimento não cobre todas as categorias")
  g <- (a + theme(legend.position = "none")) / b
  gravar_figura(g, "realismo", "larga", altura_mm = 92)
}

# ================================================================ principal
FIGURAS <- list(modelo_logico = fig_modelo_logico, prisma = fig_prisma, rob = fig_rob, celulas = fig_celulas,
                direcao = fig_direcao, metas = fig_metas, realismo = fig_realismo)
alvo <- commandArgs(trailingOnly = TRUE)
if (!length(alvo)) alvo <- names(FIGURAS)
desconhecidas <- setdiff(alvo, names(FIGURAS))
if (length(desconhecidas)) stop("figuras desconhecidas: ", paste(desconhecidas, collapse = ", "))
for (nm in alvo) FIGURAS[[nm]]()
if (ROTULO_PROVISORIO) message("NOTA: rótulos autor-ano provisórios; rode de novo quando revista/rotulos_autor_ano.json existir")
