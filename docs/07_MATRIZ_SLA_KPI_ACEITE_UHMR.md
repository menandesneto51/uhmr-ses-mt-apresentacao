# SES-MT - UHMR
## Matriz SLA, KPI e Critérios de Aceite

**Código:** UHMR-SLA-001
**Versão:** 2.1 - parâmetros para validação
**Importante:** valores numéricos definitivos devem ser confirmados pelo ETP, consulta ao mercado e área técnica.

| ID | Evento/Serviço | Indicador | Método de medição | Meta preliminar | Evidência |
|---|---|---|---|---|---|
| SLA01 | prontidão | disponibilidade documental | itens válidos / itens exigidos | a definir | checklist |
| SLA02 | equipamentos | disponibilidade técnica | equipamentos aptos / previstos | a definir | inventário/manutenção |
| SLA03 | acionamento | tempo de confirmação | acionamento -> confirmação | a definir por configuração | log |
| SLA04 | mobilização | tempo de saída | confirmação -> saída | a definir | log/transporte |
| SLA05 | deslocamento | aderência ao plano | realizado x estimado | por missão | rastreamento |
| SLA06 | implantação | tempo de montagem | chegada -> montagem concluída | a definir por configuração | log |
| SLA07 | comissionamento | tempo até aceite | chegada -> aceite técnico | a definir por configuração | termo |
| SLA08 | energia | disponibilidade | minutos disponíveis / minutos operação | alta disponibilidade | monitoramento |
| SLA09 | gases | disponibilidade | minutos disponíveis / minutos operação | alta disponibilidade | alarmes/log |
| SLA10 | climatização | conformidade ambiental | medições conformes / total | conforme faixa aprovada | sensores |
| SLA11 | manutenção | tempo de resposta | abertura -> início atendimento | a definir por criticidade | OS |
| SLA12 | manutenção | tempo de solução | abertura -> restabelecimento | a definir por criticidade | OS |
| SLA13 | reposição | tempo de reposição | solicitação -> reposição | a definir por classe | estoque/log |
| SLA14 | TI | disponibilidade de sistemas | uptime | a definir | monitoramento |
| SLA15 | expansão | tempo de escalonamento | ordem -> capacidade adicional disponível | a definir | termo |
| SLA16 | desmobilização | tempo de encerramento | ordem -> área liberada | a definir | termo |
| SLA17 | recomposição | retorno à prontidão | retorno -> N0 restabelecido | a definir | checklist |

## 1. Critérios de aceite

Todo requisito crítico deverá ser classificado como:

- A - aceite documental;
- B - aceite visual/inspeção;
- C - teste funcional;
- D - teste de carga/desempenho;
- E - simulação operacional;
- F - evidência assistencial/sanitária;
- G - aceite por autoridade competente.

## 2. Criticidade

- C1: suporte;
- C2: relevante;
- C3: crítico;
- C4: missão/vida.

Requisitos C4 devem possuir contingência documentada e teste de falha.

## 3. Glosa e penalidade

A fórmula de glosa/penalidade deverá ser definida no TR/contrato somente após:

- estimativa de impacto;
- proporcionalidade;
- possibilidade de mensuração;
- distinção entre indisponibilidade parcial e total;
- exclusões justificadas;
- procedimento de contraditório.

## 4. Regra

Nenhum SLA deve ser incluído no edital sem:

- evento inicial e final claros;
- fonte de tempo;
- responsável pelo registro;
- tolerância, se houver;
- forma de comprovação;
- consequência prevista.


## Revisão de prontidão e acionamento em 28 de setembro de 2026

Medir disponibilidade N0 por item e período; preventivas realizadas no prazo sobre preventivas devidas; calibrações válidas sobre equipamentos que as exigem; entregas completas e tempestivas por OA; conformidade de lote, validade e temperatura quando aplicável. Metas e glosas serão definidas no contrato após validação, sem percentuais inventados. Fornecimento isolado usa aceite de produtos, não TLO hospitalar.

Referência transversal: [Diretrizes de prontidão e acionamento](26_DIRETRIZES_PRONTIDAO_ACIONAMENTO_UHMR.md). Situação: minuta para validação institucional.


## Complementação técnica e normativa — revisão 2.1

### 8. Indicadores e tratamento da indisponibilidade

Proposta de indicadores: disponibilidade por componente = horas de capacidade disponível e comprovada / horas de capacidade contratada; manutenção preventiva no prazo = intervenções concluídas no prazo / intervenções devidas; entrega conforme = unidades aceitas / unidades entregues. Denominador zero será registrado como não aplicável. Registrar também tempo da OA ao recebimento, tempo até liberação e falhas críticas. Metas, janelas de apuração, tolerâncias, substituição e regra proporcional de medição devem ser validadas antes do edital. Não fixar percentuais de glosa arbitrários nem confundir redução por serviço não prestado com sanção administrativa. Impedimentos atribuíveis à SES ou a terceiros serão registrados e tratados conforme matriz de riscos.

Fontes, limites de aplicação e requisitos complementares: [Caderno de fundamentação e controles](27_FUNDAMENTACAO_E_CONTROLES_UHMR.md).
