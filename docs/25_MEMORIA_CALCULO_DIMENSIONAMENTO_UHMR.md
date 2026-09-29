# SES-MT - UHMR
## Memória de Cálculo e Dimensionamento N1-N4

**Código:** UHMR-DAT-001
**Versão:** 2.1 - fonte metodológica
**Status:** modelo preliminar para validação multidisciplinar
**Artefato associado:** `UHMR_SES_MT_MEMORIA_CALCULO_E_CUSTOS_v2.xlsx`

## 1. Objetivo

Estabelecer a metodologia de dimensionamento da UHMR, relacionando capacidade assistencial, recursos humanos, equipamentos, infraestrutura, consumos, logística e custos.

Os valores atualmente utilizados são parâmetros de trabalho. Nenhum valor preliminar deve ser convertido em requisito definitivo de edital ou contrato sem validação formal.

## 2. Estrutura do modelo

A planilha contém as seguintes abas:

1. **Parametros** - premissas editáveis;
2. **Niveis** - capacidades N0-N4;
3. **RH** - postos e FTE;
4. **Equipamentos** - quantitativos por nível;
5. **Infraestrutura** - água e potência preliminar;
6. **Custos** - inputs de pesquisa de mercado;
7. **Cenarios** - simulação de custo anual;
8. **Dashboard** - resumo executivo.

## 3. Modelo dos níveis

### N0 - Prontidão

Sem leitos ativados. Representa a capacidade contratual mantida disponível e verificável.

### N1 - Resposta rápida

Faixa preliminar preservada da versão anterior:

- 6 a 12 posições/leitos de observação;
- referência de trabalho: 10;
- 2 a 4 posições críticas;
- referência de trabalho: 3.

### N2 - Assistência ampliada

- 12 a 20 leitos;
- referência de trabalho: 16;
- 4 posições críticas.

### N3 - Hospital modular

- 20 a 30 leitos;
- referência de trabalho: 24;
- 4 posições críticas;
- possibilidade de centro cirúrgico e demais módulos definidos no ETP/TR.

### N4 - Hospital expandido

- 40 a 100 leitos;
- referência exclusivamente para simulação: 60;
- quantitativos críticos e módulos adicionais sujeitos à memória de cálculo específica.

## 4. Dimensionamento de RH

O modelo inicial utiliza:

**FTE estimado = postos simultâneos x fator de cobertura**

O fator de cobertura é um parâmetro editável da planilha.

Ele deve ser substituído/validado a partir de:

- jornada aplicável;
- número de turnos;
- folgas;
- férias;
- absenteísmo;
- necessidade de cobertura 24/7;
- legislação profissional;
- perfil clínico;
- tempo de missão.

A matriz não deve ser utilizada como dimensionamento normativo sem validação das áreas assistenciais e de gestão de pessoas.

## 5. Equipamentos

A quantidade de equipamentos deve ser função de:

- leitos;
- posições críticas;
- módulos;
- perfil de pacientes;
- redundância;
- tempo máximo de reposição;
- necessidade de backup.

Equipamentos críticos devem possuir contingência definida.

## 6. Água

Modelo preliminar:

**População operacional equivalente = leitos + FTE estimado**

**Água base = população operacional equivalente x consumo unitário diário**

**Água com reserva = água base x fator de reserva**

O consumo unitário e o fator de reserva permanecem placeholders técnicos até validação pela engenharia/WASH e áreas assistenciais.

A memória final deverá separar, quando necessário:

- consumo humano;
- higiene;
- limpeza;
- cozinha;
- processamento;
- equipamentos;
- reserva de incêndio;
- usos técnicos.

## 7. Energia

O modelo preliminar soma as potências nominais dos equipamentos cadastrados por nível.

A engenharia deverá evoluir para:

**Demanda de projeto = soma das cargas x fator de simultaneidade x margem de reserva**

e incluir:

- climatização;
- iluminação;
- TI;
- bombas;
- gases;
- equipamentos de apoio;
- cargas de partida;
- expansão;
- UPS;
- geração de contingência.

O valor calculado na planilha nesta fase é somente um indicador parcial de carga de equipamentos e não substitui projeto elétrico.

## 8. Gases medicinais

A versão seguinte da memória deverá incorporar:

- número de pontos;
- perfil de uso;
- vazão por ponto;
- fator de simultaneidade;
- consumo horário;
- autonomia;
- reserva;
- fonte principal;
- contingência.

O dimensionamento deverá ser validado pela engenharia clínica/engenharia e assistência.

## 9. Modelo econômico

O custo total é decomposto em:

**Custo total = prontidão + mobilização + implantação + operação + expansão + desmobilização + demais componentes autorizados**

Preços ausentes permanecem pendentes. Zero somente representa preço efetivamente definido como zero ou item não acionado. A aba Acionamento permite composição independente por item; os cenários antigos são apenas referenciais.

### Componentes mínimos

- prontidão mensal;
- mobilização;
- implantação;
- diária N1;
- diária N2;
- diária N3;
- diária N4;
- módulos opcionais;
- equipes;
- consumíveis;
- exercícios;
- desmobilização;
- recomposição.

## 10. Cenários

O modelo compara:

- zero ativação;
- baixa utilização;
- utilização moderada;
- hospital modular;
- evento prolongado;
- expansão crítica.

A configuração final dos cenários deverá ser baseada em histórico estadual e cenários prospectivos.

## 11. Dados necessários para evolução

### Assistência e rede

- CNES;
- capacidade instalada;
- ocupação;
- SIH;
- SISREG;
- IndicaSUS;
- transferências;
- filas;
- histórico de interrupções.

### Emergências

- eventos climáticos;
- desastres;
- incêndios;
- epidemias;
- múltiplas vítimas;
- isolamento territorial.

### Logística

- distâncias;
- tempos;
- rotas;
- bases potenciais;
- disponibilidade de transporte;
- sazonalidade de acesso.

### Mercado

- prontidão;
- mobilização;
- operação;
- expansão;
- desmobilização;
- equipamentos;
- equipes;
- consumíveis.

## 12. Gates de validação

### Gate 1 - Assistencial

Validar:

- leitos;
- críticos;
- cirurgia;
- isolamento;
- perfil de RH;
- equipamentos.

### Gate 2 - Engenharia

Validar:

- área;
- energia;
- gases;
- água;
- saneamento;
- climatização;
- incêndio;
- comunicação.

### Gate 3 - Mercado

Validar:

- disponibilidade;
- prazos;
- custos;
- modularidade;
- capacidade de fornecedores.

### Gate 4 - Econômico

Comparar alternativas e cenários.

### Gate 5 - Jurídico/administrativo

Verificar compatibilidade dos resultados com ETP, TR, edital e contrato.

## 13. Integração documental

Os resultados aprovados desta memória devem atualizar simultaneamente:

- UHMR-ETP-001;
- UHMR-TR-001;
- UHMR-EDT-001;
- UHMR-CTR-001;
- UHMR-ENG-001;
- UHMR-ENG-002;
- UHMR-OPS-002;
- UHMR-FIN-001;
- UHMR-SLA-001;
- matriz mestre de requisitos.

## 14. Regra Cursor

O Cursor deve tratar valores classificados como hipótese, placeholder, simulação ou pendente de RFI como **não aprovados**.

Qualquer tentativa de propagá-los para edital/contrato deve gerar alerta e exigir evidência de validação.


## Revisão de prontidão e acionamento em 28 de setembro de 2026

Acrescentar às planilhas a configuração efetiva por itens, meses N0 e parcelas variáveis independentes. Usar quantidade zero para item não acionado; preço ausente deve permanecer pendente. Não inferir infraestrutura, RH ou custos de missão a partir de um nível fixo. Cenários referenciais permanecem para comparação, separados da composição personalizada.

Referência transversal: [Diretrizes de prontidão e acionamento](26_DIRETRIZES_PRONTIDAO_ACIONAMENTO_UHMR.md). Situação: minuta para validação institucional.


## Complementação técnica e normativa — revisão 2.1

### 2. Necessidade, alternativas e dimensionamento

O ETP deverá comparar capacidade própria, locação com suporte, serviço integrado e aproveitamento de contratos ou capacidade existente, documentando investimento, custo anual, tempo de resposta, logística e risco de indisponibilidade. Para cada cenário, registrar fonte e data dos dados, população exposta, demanda provável e máxima plausível, capacidade operacional residual da rede, lacuna, duração e incerteza. Dimensionar a configuração para a lacuna demonstrada, sem usar capacidade cadastrada como sinônimo de capacidade disponível. Os números de leitos nas versões anteriores são referências de planejamento e não autorizam quantitativos ou preços.

### 7. Formação de preços, medição e vedação à duplicidade

A pesquisa de mercado deverá solicitar composição homogênea para N0, dez leitos, laboratório, medicamentos e missão combinada, incluindo distâncias e durações comparáveis. Separar reserva de estoque, aquisição, consumo e reposição; esclarecer titularidade e destino dos saldos. O mapa de custos indicará o que cada preço inclui. Na medição mensal, conciliar OA, boletim de execução, inventário, aceite, nota fiscal e histórico de pagamentos. Suporte compartilhado e manutenção ordinária não geram cobrança duplicada. Para insumos pagos por unidade entregue e aceita, não cobrar novamente reposição da mesma entrega. A continuidade do N0 durante a missão depende das obrigações que permanecem e da segregação de custos.

Fontes, limites de aplicação e requisitos complementares: [Caderno de fundamentação e controles](27_FUNDAMENTACAO_E_CONTROLES_UHMR.md).
