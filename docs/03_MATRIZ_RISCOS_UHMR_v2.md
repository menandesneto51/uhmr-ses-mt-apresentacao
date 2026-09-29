# SES-MT - UHMR
## Matriz de Riscos de Planejamento, Contratação e Operação

**Código:** UHMR-RSK-001
**Versão:** 2.1 - minuta técnica
**Escala:** Probabilidade (P) e Impacto (I): 1 a 5. Nível inicial = P x I.
**Nota:** a matriz contratual final deve observar o enquadramento da contratação e o Decreto Estadual nº 1.525/2022.

| ID | Risco | Fase | P | I | Nível | Tratamento mínimo | Responsável primário |
|---|---|---|---:|---:|---:|---|---|
| R01 | demanda mal caracterizada | planejamento | 3 | 5 | 15 | DFD + evidências + validação multidisciplinar | área demandante |
| R02 | solução superdimensionada | planejamento | 3 | 4 | 12 | cenários e memória de cálculo | planejamento |
| R03 | solução subdimensionada | planejamento | 3 | 5 | 15 | cenários críticos + expansão modular | assistência |
| R04 | especificação restritiva | contratação | 3 | 5 | 15 | requisitos funcionais + RFI + justificativas | aquisições/técnica |
| R05 | pesquisa de preços inadequada | contratação | 3 | 5 | 15 | metodologia documentada + fontes múltiplas | compras |
| R06 | baixa competição | contratação | 3 | 4 | 12 | consulta ao mercado e revisão de barreiras | comissão |
| R07 | fornecedor sem capacidade logística | execução | 3 | 5 | 15 | prova documental + teste/exercício | fiscalização |
| R08 | atraso de mobilização | operação | 4 | 5 | 20 | SLA, marcos, penalidades e simulações | contratada/gestor |
| R09 | site inadequado | operação | 3 | 5 | 15 | protocolo de site assessment | engenharia |
| R10 | energia insuficiente | operação | 3 | 5 | 15 | redundância, teste de carga e combustível | engenharia |
| R11 | falha em gases medicinais | operação | 2 | 5 | 10 | redundância, alarmes e plano de contingência | engenharia clínica |
| R12 | água/WASH insuficientes | operação | 3 | 5 | 15 | reserva, qualidade e contingência | infraestrutura |
| R13 | climatização inadequada | operação | 3 | 5 | 15 | parâmetros técnicos e monitoramento | engenharia |
| R14 | falha de isolamento/fluxos | operação | 3 | 5 | 15 | validação sanitária e testes | VISA/assistência |
| R15 | equipamentos sem manutenção | prontidão | 3 | 5 | 15 | plano de manutenção e rastreabilidade | engenharia clínica |
| R16 | falta de consumíveis | operação | 4 | 4 | 16 | estoque mínimo e reposição por SLA | logística |
| R17 | recursos humanos insuficientes | operação | 4 | 5 | 20 | dimensionamento por configuração + banco de contingência | assistência |
| R18 | falha de integração com regulação | operação | 3 | 5 | 15 | fluxo pré-definido e simulação | regulação |
| R19 | incidente de segurança do paciente | operação | 3 | 5 | 15 | protocolos, NSP/arranjo equivalente e notificação | assistência |
| R20 | infecção relacionada à assistência | operação | 3 | 5 | 15 | PCIH/CCIH aplicável, fluxos e vigilância | assistência/VISA |
| R21 | tratamento inadequado de dados | operação | 3 | 5 | 15 | perfis, logs, minimização e plano LGPD | TI/encarregado |
| R22 | medição sem evidência | execução | 3 | 4 | 12 | matriz de aceite + registros auditáveis | fiscalização |
| R23 | pagamento por capacidade não disponível | execução | 2 | 5 | 10 | testes periódicos de prontidão | gestor |
| R24 | desmobilização insegura | encerramento | 2 | 5 | 10 | checklist, descontaminação e inventário | contratada/fiscal |
| R25 | dependência exclusiva do fornecedor | ciclo de vida | 3 | 4 | 12 | padrões abertos, portabilidade e documentação | planejamento |
| R26 | licença/autorização não obtida | implantação | 2 | 5 | 10 | matriz de autorizações e responsáveis | gestor/VISA |
| R27 | requisito normativo desatualizado | planejamento | 3 | 4 | 12 | verificação normativa em cada release | conformidade |
| R28 | acidente ocupacional | operação | 3 | 5 | 15 | NR aplicável, treinamento e EPI/EPC | SES/contratada |
| R29 | incêndio | operação | 2 | 5 | 10 | PPCI/segurança, detecção, extinção e treinamento | engenharia |
| R30 | expansão N4 inviável no prazo | operação | 3 | 4 | 12 | teste de escalonamento e reserva logística | logística |

## Critério de tratamento

- 20-25: crítico - não aceitar sem plano específico e responsável;
- 15-19: alto - mitigação obrigatória e monitoramento;
- 8-14: moderado - controles documentados;
- 1-7: baixo - aceitar ou monitorar conforme justificativa.

## Campos obrigatórios na versão operacional

A versão de execução deverá acrescentar:

- causa;
- consequência;
- controles existentes;
- ação preventiva;
- ação contingencial;
- gatilho;
- prazo;
- responsável nominal/função;
- risco residual;
- evidência de fechamento.


## Revisão de prontidão e acionamento em 28 de setembro de 2026

Incluir riscos de acionamento sem autorização do Secretário, módulos desnecessários, dupla cobrança, indisponibilidade durante manutenção, vencimento e quebra de cadeia de frio. A contratada responde pela manutenção e perdas sob sua responsabilidade; fiscalização registra evidências e aplica o tratamento contratual.

Referência transversal: [Diretrizes de prontidão e acionamento](26_DIRETRIZES_PRONTIDAO_ACIONAMENTO_UHMR.md). Situação: minuta para validação institucional.


## Complementação técnica e normativa — revisão 2.1

### 9. Matriz de riscos e continuidade

Atribuir à empresa falha ordinária de equipamento, manutenção vencida, conservação inadequada e perda por vencimento sob sua gestão; prever substituição e recomposição sem preço adicional ordinário. Identificar separadamente acesso bloqueado, sítio inadequado, falha de utilidades locais, demanda simultânea e atraso de licença, com responsável, prevenção, contingência, evidência e consequência contratual. A imputação dependerá da causa documentada e da alocação pactuada. Para assistência, prever referência e transporte seguro de pacientes; para laboratório, rede de apoio; para medicamentos, fornecedor e rota alternativos autorizados. O encerramento exige transferência assistencial, reconciliação de estoques e liberação do sítio.

Fontes, limites de aplicação e requisitos complementares: [Caderno de fundamentação e controles](27_FUNDAMENTACAO_E_CONTROLES_UHMR.md).
