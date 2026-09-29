# GOVERNO DO ESTADO DE MATO GROSSO
## SECRETARIA DE ESTADO DE SAÚDE - SES-MT
# Relatório de QA dos artefatos binários — UHMR revisão 2.2

**Código:** UHMR-QA-002  
**Versão:** 2.2 — 29/09/2026  
**Situação:** verificação técnica de consistência e renderização; não substitui aprovação institucional.

## 1. Escopo

Após a atualização das fontes controladas da revisão 2.2, foram regenerados e conferidos os artefatos Word, PDF e Excel do pacote UHMR.

## 2. Documentos Word/PDF verificados

| Documento | Páginas PDF | Resultado |
|---|---:|---|
| 00 — Índice e guia | 8 | aprovado no QA visual |
| 01 — ETP consolidado | 37 | aprovado no QA visual |
| 02 — Termo de Referência | 16 | aprovado no QA visual |
| 03 — Minuta de Edital | 14 | aprovado após correção do campo de paginação |
| 04 — Minuta Contratual | 10 | aprovado no QA visual |
| 06 — Caderno Operacional e Formulários | 15 | aprovado no QA visual |
| 07 — Caderno de Fundamentação e Controles | 4 | aprovado no QA visual |
| 08 — Benchmark FN-SUS | 1 | aprovado no QA visual |
| 09 — Matriz de Responsabilidades e Custos | 1 | aprovado no QA visual |
| 10 — Relatório de Validação por Agentes | 1 | aprovado no QA visual |

Foi mantido também o alias `ETP_UHMR_SES_MT_2026_CONSOLIDADO`, idêntico ao documento 01.

## 3. Método de QA documental

- renderização dos DOCX para PDF;
- inspeção visual das páginas alteradas e de páginas de controle;
- comparação das páginas não alteradas com a revisão 2.1;
- verificação de cortes, sobreposições, quebras indevidas e tabelas;
- preflight dos PDFs;
- renderização independente de PDFs para conferência de paridade visual.

As páginas não modificadas mantiveram o layout da revisão anterior. Não foram observados cortes ou sobreposições nas páginas de controle.

## 4. Correção específica

A minuta de edital possuía problema legado no rodapé, exibindo a palavra “Página” sem o número. O campo PAGE do Word foi reconstruído e a renderização posterior confirmou a numeração correta.

## 5. Planilha de dimensionamento e custos

A planilha da revisão 2.2 foi atualizada com:

- benchmark FN-SUS;
- itens de FAT/SAT e recondicionamento;
- custos modulares de posições críticas, laboratório, centro cirúrgico e medicamentos/insumos;
- novas fontes e referências;
- novos riscos;
- indicadores adicionais de SLA;
- abas `Benchmark FN-SUS` e `Responsabilidades 2.2`;
- identificação de itens cujo preço permanece bloqueado por ausência de pesquisa de mercado atual.

Foi executada varredura de erros de fórmulas sem ocorrência de erros identificados.

## 6. Estado de publicação

Os artefatos binários estão coerentes com a revisão 2.2 para fins de planejamento, RFI, pesquisa de preços e análise institucional.

O QA de apresentação não elimina os gates do Auditor Final. Permanecem bloqueadores de publicação do edital:

- pesquisa de preços atual e suficiente;
- quantitativos/tetos finais;
- SLAs definitivos;
- memórias de cálculo de utilidades;
- matriz de responsabilidades institucionalmente aprovada;
- parcelamento e critério de julgamento;
- modelo de RH e responsabilidades assistenciais;
- licenciamento;
- competência formal de acionamento;
- validação jurídica e autorização da autoridade competente.

## 7. Pacote consolidado

Foi gerado o pacote `PACOTE_UHMR_SES_MT_REVISAO_2_2.zip`, contendo Word, PDF, Excel e guia da revisão.

A Biblioteca de trabalho mantém os documentos originais atualizados e uma pasta específica `Hospital de campanha/Revisao 2.2` para os novos artefatos e pacote consolidado.
