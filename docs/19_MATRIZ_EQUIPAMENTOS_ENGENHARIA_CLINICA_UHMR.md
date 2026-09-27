# SES-MT - UHMR
## Matriz de Equipamentos e Engenharia Clínica

**Código:** UHMR-ENG-002  
**Versão:** 2.0 - estrutura de dimensionamento

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
