# GOVERNO DO ESTADO DE MATO GROSSO
## SECRETARIA DE ESTADO DE SAÚDE - SES-MT
### UHMR - Unidade Hospitalar Modular de Resposta a Emergências

**Documento:** Governança Documental e Padrão Institucional  
**Código:** UHMR-GOV-001  
**Versão:** 2.0 - minuta técnica  
**Data-base:** setembro de 2026  
**Situação:** em validação técnica, administrativa, sanitária, orçamentária e jurídica  
**Classificação:** documento de planejamento - não autoriza contratação

---

## 1. Finalidade

Estabelecer a arquitetura documental oficial do projeto UHMR, o padrão de identificação dos documentos, as regras de versionamento, os papéis de validação e a relação de dependência entre os artefatos de planejamento, contratação, operação e fiscalização.

A governança documental busca evitar divergências entre ETP, Termo de Referência, edital, contrato, planilhas, caderno operacional e apresentação executiva.

## 2. Princípios

1. uma única fonte técnica para cada requisito;
2. rastreabilidade entre necessidade, requisito, evidência, custo, risco, SLA e critério de aceite;
3. linguagem institucional, objetiva e verificável;
4. separação entre requisito obrigatório, requisito desejável e hipótese sujeita à validação;
5. nenhuma especificação restritiva sem justificativa técnica;
6. nenhuma quantidade definitiva sem memória de cálculo;
7. nenhuma referência normativa sem identificação da fonte e checagem de vigência;
8. nenhuma informação clínica individualizada em documentos públicos;
9. compatibilidade com os fluxos SES-MT, SEPLAG, PGE, Vigilância Sanitária e áreas técnicas competentes;
10. versionamento de todas as mudanças relevantes.

## 3. Padrão de cabeçalho

Todos os documentos oficiais ou minutas devem conter:

- Governo do Estado de Mato Grosso;
- Secretaria de Estado de Saúde - SES-MT;
- nome do projeto UHMR;
- título do documento;
- código documental;
- versão;
- data-base;
- unidade responsável;
- situação do documento;
- indicação de que a minuta não substitui aprovação da autoridade competente, quando aplicável.

## 4. Identificação e versionamento

Padrão de código:

**UHMR-[DOMÍNIO]-[NÚMERO]**

Domínios mínimos:

- GOV - governança;
- DFD - formalização da demanda;
- ETP - estudo técnico preliminar;
- TR - termo de referência;
- LEG - base legal;
- RSK - riscos;
- SAN - requisitos sanitários;
- ENG - engenharia e infraestrutura;
- OPS - operação;
- SLA - desempenho e níveis de serviço;
- FIN - custos e orçamento;
- FIS - fiscalização;
- RFI - consulta ao mercado;
- DAT - dados e indicadores;
- LGPD - privacidade e segurança da informação.

Versões:

- 0.x - rascunho de trabalho;
- 1.x - minuta consolidada;
- 2.x - versão tecnicamente revisada;
- Aprovado - somente após validações formais registradas no processo.

## 5. Arquitetura documental

### Bloco A - Planejamento

1. Documento de Formalização da Demanda - DFD;
2. Estudo Técnico Preliminar - ETP;
3. Matriz de necessidades e cenários;
4. memória de cálculo de dimensionamento;
5. pesquisa/consulta estruturada ao mercado;
6. análise de alternativas;
7. matriz de riscos;
8. estimativa de custos e modelo econômico.

### Bloco B - Especificação

9. Termo de Referência ou Projeto Básico, conforme enquadramento;
10. caderno técnico de requisitos sanitários e assistenciais;
11. caderno de engenharia e infraestrutura;
12. matriz de equipamentos e tecnologias;
13. matriz de recursos humanos;
14. matriz de consumíveis;
15. matriz SLA/KPI/aceite;
16. plano de mobilização, implantação, operação e desmobilização.

### Bloco C - Seleção e contratação

17. minuta de edital;
18. minuta contratual;
19. requisitos de habilitação técnica e econômico-financeira justificados;
20. critérios de julgamento;
21. matriz de responsabilidades;
22. matriz de riscos contratual, quando cabível;
23. checklist de conformidade jurídica e administrativa.

### Bloco D - Execução e fiscalização

24. plano de fiscalização;
25. ordem de mobilização;
26. checklist de site assessment;
27. termo de comissionamento;
28. termo de aceite;
29. relatório diário de operação;
30. registro de incidentes;
31. medição e ateste;
32. relatório de desmobilização;
33. lições aprendidas.

## 6. Fonte única de requisitos

Deve ser criada uma matriz mestre com os campos:

| Campo | Descrição |
|---|---|
| ID | identificador único |
| domínio | assistencial, sanitário, engenharia, TI etc. |
| requisito | descrição objetiva |
| natureza | obrigatório / desejável / opcional |
| fundamento | norma, evidência ou decisão técnica |
| documento de origem | ETP, TR, RFI etc. |
| critério de aceite | evidência necessária |
| SLA/KPI | indicador aplicável |
| custo associado | CAPEX/OPEX/prontidão/ativação |
| risco associado | ID na matriz de riscos |
| responsável | área técnica |
| status | proposto, validado, aprovado, suspenso |

## 7. Fluxo de validação

A aprovação documental deve ocorrer por domínio, sem presumir competência de área diversa.

Validações mínimas, conforme o conteúdo:

- área demandante;
- assistência hospitalar;
- Vigilância Sanitária;
- engenharia/infraestrutura;
- engenharia clínica;
- tecnologia da informação e segurança;
- regulação;
- logística;
- orçamento/finanças;
- aquisições e contratos;
- controle interno, quando aplicável;
- Procuradoria-Geral do Estado, nos casos submetidos à análise jurídica.

## 8. Regra para documentos públicos

Materiais publicados no GitHub ou GitHub Pages devem conter apenas informações adequadas à publicidade. Credenciais, informações pessoais, dados clínicos identificáveis, especificações de segurança sensíveis e documentos internos restritos não devem ser publicados.

## 9. Regra Cursor

O Cursor será o ambiente padrão de manutenção técnica do projeto. Toda alteração estrutural deverá:

1. identificar os documentos impactados;
2. atualizar a matriz mestre de requisitos;
3. verificar referências normativas;
4. executar validações automáticas de consistência;
5. registrar a alteração no CHANGELOG;
6. gerar pacote candidato a revisão;
7. somente depois atualizar os artefatos finais.

## 10. Status

Este documento estabelece o padrão da versão 2.0 e deve ser utilizado como referência para a revisão dos arquivos 00 a 06 existentes.
