# SES-MT - UHMR
## Matriz de Equipamentos e Engenharia Clínica

**Código:** UHMR-ENG-002
**Versão:** 2.1 - estrutura de dimensionamento

## Campos obrigatórios

| Campo | Descrição |
|---|---|
| ID | identificador |
| módulo | local/função |
| equipamento | categoria funcional |
| quantidade N1 | a validar |
| quantidade N2 | a validar |
| quantidade N3 | a validar |
| quantidade N4 | a validar |
| criticidade | C1-C4 |
| registro | requisito regulatório |
| energia | consumo/interface |
| gases | interface |
| rede | conectividade |
| manutenção | periodicidade |
| calibração | quando aplicável |
| backup | contingência |
| SLA reposição | prazo |
| consumíveis | itens associados |
| aceite | teste |
| responsável | área |

## Categorias iniciais

### Estabilização e críticos

- monitor multiparamétrico;
- ventilador pulmonar;
- desfibrilador/cardioversor;
- bombas de infusão;
- aspirador;
- equipamentos de via aérea;
- equipamentos de emergência.

### Observação/internação

- monitorização conforme perfil;
- bombas;
- oxigenoterapia;
- camas/macas;
- dispositivos de suporte.

### Cirurgia/RPA

- mesa cirúrgica;
- foco;
- aparelho de anestesia;
- monitor;
- bisturi;
- aspirador;
- bombas;
- aquecimento;
- equipamentos de RPA.

### Diagnóstico

- ultrassom;
- radiografia móvel/digital, se aprovada;
- point-of-care;
- equipamentos laboratoriais definidos.

### Farmácia/cadeia fria

- refrigeração monitorada;
- controle de temperatura;
- armazenamento seguro.

### CME/processamento

- equipamentos definidos após decisão de modelo próprio ou terceirizado.

## Regras

1. especificar desempenho, não marca;
2. cada item crítico deve possuir contingência;
3. compatibilidade elétrica e de gases deve ser verificada;
4. consumíveis proprietários devem ser explicitados e analisados quanto a dependência;
5. manutenção e calibração devem compor o custo;
6. quantitativos finais devem derivar do dimensionamento clínico.


## Revisão de prontidão e acionamento em 28 de setembro de 2026

Para cada ativo registrar identificação, fabricante, risco, periodicidade preventiva, última/próxima manutenção, calibração aplicável, teste, responsável, evidência e cobertura durante indisponibilidade. A empresa custeia manutenção, peças e substituição, com custos inclusos e sem parcela adicional ordinária.

Referência transversal: [Diretrizes de prontidão e acionamento](26_DIRETRIZES_PRONTIDAO_ACIONAMENTO_UHMR.md). Situação: minuta para validação institucional.


## Complementação técnica e normativa — revisão 2.1

### 4. Prontidão verificável e manutenção

O aceite inicial do N0 exige inventário identificável, localização dos bens, estado de conservação, testes funcionais, plano de manutenção, capacidade de mobilização e responsáveis. Mensalmente, a empresa entregará posição do inventário, intervenções previstas e realizadas, falhas, substituições, reservas e evidência da capacidade garantida. A empresa executa e custeia manutenção preventiva e corretiva ordinária, calibração aplicável, peças e testes, inclusive sem missões, em preços já contratados. Definir contratualmente capacidade reservada, exclusividade ou compartilhamento admitido e resposta a missões simultâneas; não remunerar como exclusiva uma capacidade comprometida com terceiros. A RDC nº 509/2021 sustenta plano, registros e rastreabilidade; terceirizar a gestão não elimina a responsabilidade sanitária do estabelecimento.

Fontes, limites de aplicação e requisitos complementares: [Caderno de fundamentação e controles](27_FUNDAMENTACAO_E_CONTROLES_UHMR.md).
