# SES-MT - UHMR
## Memória de Cálculo e Dimensionamento N1-N4

**Código:** UHMR-DAT-001  
**Versão:** 2.0 - fonte metodológica  
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

A aba Custos permanece com valores zerados enquanto não houver RFI/pesquisa formal.

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
