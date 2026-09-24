#show: doc => article(
$if(title)$
  title: [$title$],
$endif$
$if(subtitle)$
  subtitle: [$subtitle$],
$endif$
$if(by-author)$
  authors: (
$for(by-author)$
$if(it.name.literal)$
    ( name: [$it.name.literal$],
      affiliation: [$for(it.affiliations)$$it.name$$sep$, $endfor$],
      email: [$it.email$] ),
$endif$
$endfor$
    ),
$endif$
$if(date)$
  date: [$date$],
$endif$
$if(lang)$
  lang: "$lang$",
$endif$
$if(region)$
  region: "$region$",
$endif$
$if(fontsize)$
  fontsize: $fontsize$,
$endif$
$if(section-numbering)$
  sectionnumbering: "$section-numbering$",
$endif$
$if(keywords)$
  keywords: ($for(keywords)$"$keywords$",$endfor$),
$endif$
$if(revista.masthead)$
  masthead: [$revista.masthead$],
$endif$
$if(revista.cabeca)$
  cabeca: [$revista.cabeca$],
$endif$
$if(revista.nota-ia)$
  nota-ia: [$revista.nota-ia$],
$endif$
$if(revista.ultima-busca)$
  ultima-busca: [$revista.ultima-busca$],
$endif$
$if(rascunho)$
  rascunho: true,
$endif$
  doc,
)
