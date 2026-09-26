# Agentes UHMR SES-MT

Os agentes abaixo devem ser utilizados no fluxo do Cursor para revisar a UHMR por domínio. Nenhum agente substitui a decisão da autoridade competente ou a manifestação formal da área responsável.

## Ordem recomendada

1. Coordenador UHMR
2. Jurídico/Conformidade
3. Assistencial/Sanitário
4. Engenharia/Infraestrutura
5. Custos/Mercado
6. Fiscalização/Operação
7. Auditor Final

## Regra de saída

Cada agente deve retornar:

- achados;
- risco;
- evidência/fonte;
- documento afetado;
- alteração proposta;
- pendência;
- responsável sugerido;
- status: aprovado para próxima etapa / requer correção.

O Auditor Final bloqueia release quando houver inconsistência entre ETP, TR, edital, contrato, custos, riscos, SLA ou critérios de aceite.
