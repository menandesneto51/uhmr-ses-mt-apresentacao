# SES-MT - UHMR
## Matriz Mestre de Requisitos

**Código:** UHMR-GOV-005  
**Versão:** 2.0 - estrutura inicial

Esta matriz é a fonte de rastreabilidade da UHMR. ETP, TR, edital, contrato, fiscalização e caderno operacional devem referenciar os mesmos IDs.

| ID | Domínio | Requisito | Natureza | Fundamento | Aceite | SLA/KPI | Risco | Custo | Responsável | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| GOV-001 | governança | equipe de planejamento formalmente definida | obrigatório | Lei 14.133/2021 + Dec. MT 1.525/2022 | ato/processo | - | R01 | - | gestão | proposto |
| PLN-001 | planejamento | quantitativos com memória de cálculo | obrigatório | planejamento da contratação | memória aprovada | - | R02/R03 | todos | planejamento | proposto |
| MKT-001 | mercado | consulta ao mercado sem direcionamento | recomendado/necessário à robustez | ETP/levantamento de mercado | relatório RFI | - | R04/R06 | - | planejamento | proposto |
| OPS-001 | prontidão | inventário operacional atualizado | obrigatório contratual | TR | checklist | SLA01/SLA02 | R15/R23 | prontidão | logística | proposto |
| OPS-002 | mobilização | confirmação do acionamento registrada | obrigatório | TR | log | SLA03 | R08 | mobilização | contratada | proposto |
| ENG-001 | energia | contingência de energia compatível com cargas críticas | crítico | requisitos técnicos | teste de carga | SLA08 | R10 | infraestrutura | engenharia | proposto |
| ENG-002 | gases | redundância e monitoramento de gases medicinais | crítico | normas aplicáveis | comissionamento | SLA09 | R11 | infraestrutura | eng. clínica | proposto |
| SAN-001 | fluxos | fluxos assistenciais e de apoio compatíveis | crítico | RDC 50/2002 | inspeção/layout | - | R14 | infraestrutura | VISA/assistência | proposto |
| SAN-002 | funcionamento | boas práticas de funcionamento | crítico | RDC 63/2011 | checklist/documentação | - | R19/R20 | operação | assistência | proposto |
| SAN-003 | resíduos | PGRSS e fluxo de resíduos | obrigatório | RDC 222/2018 | PGRSS/registros | - | R24 | operação | gestão local | proposto |
| TEC-001 | equipamentos | rastreabilidade e manutenção | crítico | RDC 509/2021 | inventário/OS | SLA02/SLA11 | R15 | prontidão | eng. clínica | proposto |
| DAT-001 | dados | controle de acesso a dados de saúde | crítico | LGPD | auditoria/log | SLA14 | R21 | TI | TI | proposto |
| FIS-001 | medição | todo pagamento vinculado a evidência | obrigatório | Lei 14.133/2021/contrato | processo de medição | - | R22/R23 | todos | fiscalização | proposto |
| DES-001 | desmobilização | descontaminação, inventário e recomposição | crítico | plano operacional | termo | SLA16/SLA17 | R24 | desmobilização | contratada/fiscal | proposto |

## Regras

1. IDs não podem ser reutilizados.
2. Requisito removido permanece histórico como "retirado", com justificativa.
3. Requisito crítico sem aceite impede release.
4. Toda alteração em requisito deve indicar documentos derivados afetados.
5. Quantidade, prazo e valor só podem ser preenchidos como definitivos após validação.
