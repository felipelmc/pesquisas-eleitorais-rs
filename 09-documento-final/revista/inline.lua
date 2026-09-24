-- Filtro do artigo (pre-quarto). No Typst:
--   ::: {.resumo}               -> #resumo[ ... ]
--   ::: {.mensagens-principais} -> #mensagens[ ... ]
--   ::: {.tabela-larga} / {.figura-larga} -> #largura-total[ ... ]
--   [⊕⊕◯◯]{.grade}              -> #grade("⊕⊕◯◯")
--   [texto]{.enunciado cel="C01"} -> texto (o span só serve às travas)
--   `código` inline             -> Fira Mono com pontos de quebra depois de / _ .
-- No HTML: .tabela-larga / .figura-larga ganham a classe column-body-outset (nunca escrita no .qmd,
-- porque no Typst qualquer column-* liga a geometria de margem).

local function tem(el, c)
  return el.classes and el.classes:includes(c)
end

local function typst_str(s)
  return '"' .. s:gsub('\\', '\\\\'):gsub('"', '\\"') .. '"'
end

local function envolve(abre, conteudo, fecha)
  local out = { pandoc.RawBlock("typst", abre) }
  for _, b in ipairs(conteudo) do table.insert(out, b) end
  table.insert(out, pandoc.RawBlock("typst", fecha))
  return out
end

function Div(el)
  if quarto.doc.is_format("typst") then
    if tem(el, "resumo") then
      local lang = el.attributes["lang"]
      if lang then
        return envolve("#resumo[#set text(lang: \"" .. lang:sub(1, 2) .. "\")", el.content, "]")
      end
      return envolve("#resumo[", el.content, "]")
    elseif tem(el, "mensagens-principais") then
      return envolve("#mensagens[", el.content, "]")
    elseif tem(el, "figura-larga") then
      return envolve("#figura-larga[", el.content, "]")
    elseif tem(el, "tabela-larga") then
      return envolve("#largura-total[", el.content, "]")
    end
  elseif quarto.doc.is_format("html") then
    if tem(el, "tabela-larga") or tem(el, "figura-larga") then
      el.classes:insert("column-body-outset")
      return el
    end
  end
  return nil
end

function Span(el)
  if tem(el, "grade") and quarto.doc.is_format("typst") then
    return pandoc.RawInline("typst", "#grade(" .. typst_str(pandoc.utils.stringify(el)) .. ")")
  end
  if tem(el, "enunciado") and not quarto.doc.is_format("html") then
    return el.content
  end
  return nil
end

function Code(el)
  if quarto.doc.is_format("typst") then
    local t = el.text:gsub('\\', '\\\\'):gsub('"', '\\"')
    -- ponto de quebra (U+200B) depois de / _ .
    t = t:gsub("([/_%.%-])", "%1\u{200B}")
    return pandoc.RawInline("typst", '#text(font: ("Fira Mono", "STIX Two Math"), size: 0.86em, lang: "en", hyphenate: false, "' .. t .. '")')
  end
  return nil
end
