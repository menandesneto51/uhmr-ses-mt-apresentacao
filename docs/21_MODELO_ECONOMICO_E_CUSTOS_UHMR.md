# SES-MT - UHMR
## Modelo Econômico e Estrutura de Custos

**Código:** UHMR-FIN-001
**Versão:** 2.1 - estrutura para pesquisa de preços

## 1. Objetivo

Permitir comparação entre alternativas e propostas sem misturar custo de prontidão com custo de ativação.

## 2. Componentes

### A. Prontidão

- armazenagem;
- inspeções;
- manutenção;
- calibração;
- seguros;
- estoque mínimo;
- equipe mínima;
- gestão;
- testes;
- disponibilidade logística.

### B. Mobilização

- preparação;
- carga;
- transporte;
- pedágios;
- escolta quando aplicável;
- deslocamento de equipe;
- descarga.

### C. Implantação

- montagem;
- infraestrutura;
- conexões;
- testes;
- comissionamento.

### D. Operação

- diária por módulo acionado;
- infraestrutura;
- manutenção;
- suporte;
- utilidades sob responsabilidade da contratada;
- pessoal contratado;
- reposição.

### E. Expansão

- módulos adicionais;
- transporte;
- montagem;
- operação adicional.

### F. Desmobilização

- encerramento;
- desmontagem;
- limpeza/descontaminação;
- transporte;
- recomposição.

## 3. Cenários de comparação

A pesquisa deve calcular custo anual/contratual em cenários:

- sem ativação;
- baixa ativação;
- ativação moderada;
- evento prolongado;
- expansão N4;
- múltiplas ativações.

## 4. Fórmula conceitual

**Custo total = prontidão + somatório(mobilizações + implantação + operação por configuração + adicionais + desmobilização) + custos previstos não recorrentes.**

## 5. Memória de cálculo

Cada item deverá conter:

- unidade;
- quantidade;
- preço unitário;
- fonte;
- data-base;
- premissa;
- frequência;
- duração;
- tributos;
- inclusão/exclusão de mão de obra;
- inclusão/exclusão de consumíveis.

## 6. Regras de comparabilidade

- normalizar unidade;
- separar impostos quando necessário à análise;
- identificar frete;
- evitar preços globais sem composição quando a segregação for essencial à medição;
- sinalizar outliers;
- documentar descarte de fonte;
- manter evidência da pesquisa.

## 7. TCO

Avaliar custo de ciclo de vida para alternativas de aquisição e contratação, incluindo:

- obsolescência;
- armazenamento;
- manutenção;
- reposição;
- pessoal;
- tecnologia;
- descarte;
- atualização;
- ociosidade.

## 8. Indicadores econômicos internos

- custo anual de prontidão;
- custo por ativação;
- custo por dia operacional;
- custo incremental por leito/dia;
- custo de expansão;
- custo de indisponibilidade evitada, quando estimável;
- proporção prontidão/uso.

## 9. Gate

Nenhum valor deve migrar para edital/TR sem fonte, metodologia e data-base.


## Revisão de prontidão e acionamento em 28 de setembro de 2026

O custo sem missão inclui N0. O custo variável é o somatório de quantidades e períodos de itens acionados multiplicados por preços unitários, sem manutenção ordinária adicional. Medicamentos isolados geram fornecimento e logística efetivos, sem diária, montagem ou desmobilização hospitalar não executadas. A mensalidade durante missão exige delimitar obrigações mantidas e excluir sobreposição.

Referência transversal: [Diretrizes de prontidão e acionamento](26_DIRETRIZES_PRONTIDAO_ACIONAMENTO_UHMR.md). Situação: minuta para validação institucional.


## Complementação técnica e normativa — revisão 2.1

### 7. Formação de preços, medição e vedação à duplicidade

A pesquisa de mercado deverá solicitar composição homogênea para N0, dez leitos, laboratório, medicamentos e missão combinada, incluindo distâncias e durações comparáveis. Separar reserva de estoque, aquisição, consumo e reposição; esclarecer titularidade e destino dos saldos. O mapa de custos indicará o que cada preço inclui. Na medição mensal, conciliar OA, boletim de execução, inventário, aceite, nota fiscal e histórico de pagamentos. Suporte compartilhado e manutenção ordinária não geram cobrança duplicada. Para insumos pagos por unidade entregue e aceita, não cobrar novamente reposição da mesma entrega. A continuidade do N0 durante a missão depende das obrigações que permanecem e da segregação de custos.

### 8. Indicadores e tratamento da indisponibilidade

Proposta de indicadores: disponibilidade por componente = horas de capacidade disponível e comprovada / horas de capacidade contratada; manutenção preventiva no prazo = intervenções concluídas no prazo / intervenções devidas; entrega conforme = unidades aceitas / unidades entregues. Denominador zero será registrado como não aplicável. Registrar também tempo da OA ao recebimento, tempo até liberação e falhas críticas. Metas, janelas de apuração, tolerâncias, substituição e regra proporcional de medição devem ser validadas antes do edital. Não fixar percentuais de glosa arbitrários nem confundir redução por serviço não prestado com sanção administrativa. Impedimentos atribuíveis à SES ou a terceiros serão registrados e tratados conforme matriz de riscos.

Fontes, limites de aplicação e requisitos complementares: [Caderno de fundamentação e controles](27_FUNDAMENTACAO_E_CONTROLES_UHMR.md).

## Revisão 2.2 — benchmark e estrutura de preços

Adotar [UHMR-ECO-002](29_MATRIZ_RESPONSABILIDADES_E_CUSTOS_MODULARES_UHMR.md) como estrutura mínima para RFI e pesquisa de preços. A Consulta Pública FN-SUS nº 04/2026 serve como benchmark técnico contemporâneo, mas o Relatório Final registrou ausência de contribuições significativas quanto à precificação. Logo, não há valor federal atual suficiente para ser transplantado à UHMR.

Preços históricos de aquisições federais, se utilizados, deverão aparecer apenas como referência secundária, com data, objeto, atualização monetária, diferenças de escopo e alerta expresso de não equivalência.

O orçamento estimado será formado por fontes próprias compatíveis com o art. 23 da Lei nº 14.133/2021 e regulamento estadual, normalizadas pelo mesmo catálogo, duração, distância, capacidade e matriz de responsabilidades.
