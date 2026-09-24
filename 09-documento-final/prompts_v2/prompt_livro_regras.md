# Regras do livro para o relato (etapa 0b)

Você extrai do livro *Revisão sistemática de ponta a ponta* (Felipe Lamarca; <https://felipelamarca.com/Systematic-Review/metodo/>) as regras que valem para escrever e revisar o artigo final desta revisão sistemática rápida (tipo efetividade com SWiM, GRADE, RoB 2, ROBINS-I V2 e EPOC). Raiz do projeto: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Escreva só `09-documento-final/insumos/livro_regras.md`.

## Leitura (WebFetch; peça ao WebFetch o texto integral e literal da seção, não um resumo; se ele resumir, peça de novo por subseção)
- `10-relato-divulgacao.html` (cap. 11): §11.1 (produtos e sumário executivo), §11.2 (estrutura do relatório no formato OQF), §11.4 (resumo em linguagem simples, *policy brief*, mapa de evidências), §11.5 (auditoria final / checklist), §11.8 (licenças, o que publicar), §11.10 (frases-modelo), e o "Como relatar".
- `09-certeza-evidencia-pratica.html` (cap. 10): §10.1 (frases de certeza, regras de Santesso), tabela de proporcionalidade dos verbos, SoF, EtD-lite/TRANSFER, "ausência de evidência".
- `08a-sintese-quantitativa.html` (cap. 8): SWiM, vote counting, teste de sinal e ressalvas obrigatórias, *forest plot*, *effect direction plot*, *harvest plot*, intervalo de predição (quando mostrar), metas com poucos estudos.
- `06-qualidade-risco-vies.html`: §6.6 (como relatar e visualizar risco de viés).
- `11-ia-na-revisao.html`: §12.15 (declaração de IA) e o que relatar sobre IA.
- `apendice-b-reprodutibilidade.html`: item 27 (dados e código).

## Saída: `09-documento-final/insumos/livro_regras.md`
Organize por uso, cada regra com (i) a regra em uma frase, (ii) a citação literal curta entre aspas, (iii) a URL com âncora da seção:
1. Estrutura e ordem do relatório (§11.1, §11.2).
2. Resumo, resumo executivo e mensagens principais.
3. Resumo em linguagem simples (padrão Campbell).
4. Métodos ("diz o que esta revisão fez").
5. Resultados: frases de certeza, SoF, SWiM (itens), figuras e legendas (o que cada figura deve conter).
6. Discussão, limitações (23b × 23c), implicações (verbos proporcionais, transferibilidade).
7. Informações adicionais: registro, financiamento, conflitos, dados e código, declaração de IA.
8. Auditoria final §11.5, **item a item, numerada**, pronta para virar checklist de aceite.
9. Frases-modelo (§11.10).
Se uma seção não existir com esse número, diga qual existe e use-a. Não invente regra que não esteja no livro.

Responda com UMA linha: `OK livro_regras.md: <n> regras, auditoria com <n> itens`.
