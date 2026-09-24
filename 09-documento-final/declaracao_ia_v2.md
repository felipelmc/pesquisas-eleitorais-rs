# Declaração complementar de uso de IA: versão do artigo de 24/09/2026

RASCUNHO NÃO VALIDADO: 18 pendências humanas abertas.

Esta declaração complementa a declaração gerada do *log* (`07-relatorio/declaracao_uso_ia.md`), que não registra os agentes desta versão porque nenhum comando `rs` foi rodado nela. Ela lista os agentes que prepararam o artigo, o suplemento, o resumo em linguagem simples e a vitrine, a partir dos arquivos do projeto e sem nenhuma análise nova. Coordenação: `claude-opus-5-5`, no Claude Code. Todos os subagentes foram Opus ou Sonnet; nenhum foi Fable. Nenhum leu PDF de estudo incluído. As leituras de exemplares, das revisões anteriores e das normas brasileiras usaram só fontes abertas e legítimas: PMC, páginas oficiais, repositórios institucionais e o Internet Archive para páginas oficiais do TSE com acesso direto bloqueado.

Os *prompts* estão em `09-documento-final/prompts_v2/`. As versões instanciadas (`_prompt_*.md`) substituem só os campos {{PAPEL}}, {{ARQUIVO}}, {{PASSE}}, {{PDF}} e {{NOME}}. O SHA256 abaixo é do arquivo como está no commit desta versão.

| Prompt | Papel | Modelo | SHA256 (início) |
|---|---|---|---|
| `prompt_abertura.md` | abertura e resumo em linguagem simples | claude-opus-5-5 | `7801a66645366259…` |
| `prompt_arquiteto.md` | especificação do artigo (spec_v2.md) | claude-opus-5-5 | `0da27e7c34e5e6a8…` |
| `prompt_checklists.md` | listas de conferência do suplemento (S11) | claude-opus-5-5 | `a96b1c3f538aee3e…` |
| `prompt_correcoes_finais.md` | correções finais da verificação e da revisão visual | claude-opus-5-5 | `6a9be5ddb4e3c0ce…` |
| `prompt_correcoes_tecnicas.md` | correções técnicas da verificação | claude-opus-5-5 | `645f3824b5ae4251…` |
| `prompt_estilo_v2.md` | passes de voz (my-voice) e anti-IA (tirar-cara-de-ia) | claude-opus-5-5 | `760c329e644ee871…` |
| `prompt_exemplares.md` | movimentos das revisões exemplares e rubrica | claude-opus-5-5 | `274006471e8e25c8…` |
| `prompt_figuras.md` | figuras do artigo | claude-opus-5-5 | `818984a268ea136b…` |
| `prompt_garritty_revisoes.md` | recomendações de Garritty 2024 e revisões anteriores | claude-opus-5-5 | `5b18876801a327b5…` |
| `prompt_leituras_criticas.md` | leituras críticas simuladas por IA (L1 métodos, L2 ciência política) | claude-opus-5-5 | `6da8e199d6161478…` |
| `prompt_livro_regras.md` | regras do livro para o relato e auditoria final | claude-opus-5-5 | `941a8c11bb8eb843…` |
| `prompt_qa_visual_pdf.md` | revisão visual dos PDFs | claude-opus-5-5 (artigo); claude-sonnet-5 (suplemento) | `76c67f287fc828a1…` |
| `prompt_redator_v2.md` | redação do corpo do artigo | claude-opus-5-5 | `be5fa236142d951c…` |
| `prompt_referencias_metodo.md` | referências metodológicas conferidas no Crossref | claude-sonnet-5 | `81f91b78d31f70ba…` |
| `prompt_revisao_pareceres.md` | revisão depois das leituras críticas | claude-opus-5-5 | `9a65800cfbeb77f5…` |
| `prompt_rubrica.md` | rubrica cega v1 × v2 | claude-opus-5-5 | `b82bd8dd5853d2ba…` |
| `prompt_tabelas_montagem.md` | referências, tabelas, montagem e suplemento | claude-opus-5-5 | `df7fb46ef385b6da…` |
| `prompt_travas.md` | travas da reescrita, células e números derivados | claude-opus-5-5 | `8140aba6e7f65bf6…` |
| `prompt_verificacao_final.md` | verificação final e auditoria | claude-opus-5-5 | `a5a87e7f9e66b318…` |
| `prompt_verificacao_v2.md` | verificação independente e auditoria | claude-opus-5-5 | `ee55809d49d30c84…` |
| `prompt_vitrine.md` | vitrine interativa | claude-opus-5-5 | `d97f25516596655a…` |

Houve também um agente Sonnet, com *prompt* escrito na própria chamada, que conferiu as regras brasileiras do dia da eleição (`insumos/contexto_brasil.md`, seção 7).

Nenhuma dessas etapas valida o conteúdo. As leituras críticas e as verificações são de IA e não são revisão por especialista humano. A responsabilidade pelo conteúdo é do autor, que ainda não revisou este texto (P038).
