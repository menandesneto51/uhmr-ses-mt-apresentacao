# UHMR — SES-MT

Apresentação executiva e pacote documental da **Unidade Hospitalar Modular de Resposta a Emergências**, proposta para a Secretaria de Estado de Saúde de Mato Grosso.

## Acessos da versão publicada

- `index.html` — apresentação executiva em formato de slides;
- `projeto.html` — síntese institucional do projeto;
- `documentos.html` — biblioteca para download dos documentos;
- arquivos `00` a `06` — pacote técnico-administrativo original;
- `PACOTE_COMPLETO_UHMR_SES_MT_2026_v1_0.zip` — conjunto completo da versão 1.0.

## Desenvolvimento v2

A versão 2 está sendo estruturada com documentação-fonte versionada, rastreabilidade de requisitos, base legal, matriz de riscos, requisitos sanitários, engenharia, recursos humanos, custos, SLA/KPI, fiscalização, consulta ao mercado e agentes de validação.

### Documentos-fonte

- `docs/00_GOVERNANCA_DOCUMENTAL_UHMR_SES_MT.md`
- `docs/01_BASE_LEGAL_E_NORMATIVA_UHMR_SES_MT.md`
- `docs/02_DFD_UHMR_SES_MT_v2.md`
- `docs/03_MATRIZ_RISCOS_UHMR_v2.md`
- `docs/04_MATRIZ_REQUISITOS_SANITARIOS_ASSISTENCIAIS_UHMR.md`
- `docs/05_PLANO_GESTAO_E_FISCALIZACAO_CONTRATUAL_UHMR.md`
- `docs/06_RFI_CONSULTA_ESTRUTURADA_AO_MERCADO_UHMR.md`
- `docs/07_MATRIZ_SLA_KPI_ACEITE_UHMR.md`
- `docs/08_CHECKLIST_CONFORMIDADE_PRE_EDITAL_UHMR.md`
- `docs/09_PLANO_TRANSICAO_PACOTE_00_06_PARA_V2.md`
- `docs/10_PADRAO_VISUAL_E_EDITORIAL_SES_MT_UHMR.md`
- `docs/11_MATRIZ_MESTRE_REQUISITOS_UHMR.md`
- `docs/12_PLANO_PROTECAO_DADOS_E_SEGURANCA_UHMR.md`
- `docs/13_PLANO_CONTINUIDADE_CONTINGENCIA_UHMR.md`
- `docs/14_ETP_UHMR_SES_MT_v2_FONTE.md`
- `docs/15_TERMO_DE_REFERENCIA_UHMR_v2_FONTE.md`
- `docs/16_MINUTA_EDITAL_UHMR_v2_FONTE.md`
- `docs/17_MINUTA_CONTRATUAL_UHMR_v2_FONTE.md`
- `docs/18_CADERNO_ENGENHARIA_INFRAESTRUTURA_UHMR.md`
- `docs/19_MATRIZ_EQUIPAMENTOS_ENGENHARIA_CLINICA_UHMR.md`
- `docs/20_MATRIZ_RECURSOS_HUMANOS_UHMR.md`
- `docs/21_MODELO_ECONOMICO_E_CUSTOS_UHMR.md`
- `docs/22_PLANO_TREINAMENTO_EXERCICIOS_UHMR.md`
- `docs/23_PLANO_DESMOBILIZACAO_RECOMPOSICAO_UHMR.md`
- `docs/24_REGISTRO_DECISOES_ABERTAS_UHMR.md`

## Cursor e agentes

O Cursor é o ambiente padrão de manutenção técnica.

- regras obrigatórias: `.cursor/rules/uhmr-v2.mdc`;
- agentes: `agents/`;
- validador documental: `scripts/validate_documentation.py`;
- CI: `.github/workflows/validate-docs.yml`.

## Escopo

A proposta contempla prontidão, transporte, implantação, operação, manutenção e desmobilização de capacidade hospitalar temporária modular, com níveis acumulativos N0–N4.

Os quantitativos da versão 1.0 permanecem parâmetros preliminares e deverão ser confirmados por memória de cálculo, dados estaduais, consulta ao mercado, validações sanitárias, engenharia e análise de custo.

## Situação

Minuta para validação técnica, assistencial, sanitária, de engenharia, logística, tecnológica, orçamentária, administrativa e jurídica.

A documentação v2 não substitui atos formais da SES-MT, análise da SEPLAG/PGE quando aplicável, autorizações sanitárias ou aprovação da autoridade competente.

## Identidade visual

A UHMR deverá possuir seus próprios assets oficiais em `assets/`. A dependência atual de imagens hospedadas no repositório CIATOX será removida após incorporação e validação das cópias locais.

## Publicação

A versão pública atual permanece em GitHub Pages. A v2 somente substituirá a versão publicada após auditoria documental, QA visual e promoção controlada para `main`.
