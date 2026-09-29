# SES-MT - UHMR
## Plano de Proteção de Dados e Segurança da Informação

**Código:** UHMR-LGPD-001
**Versão:** 2.1 - minuta para validação STI/encarregado/áreas competentes

## 1. Objetivo

Definir requisitos mínimos para tratamento seguro de dados pessoais e informações institucionais durante prontidão, mobilização, operação e desmobilização da UHMR.

## 2. Princípios

- finalidade;
- adequação;
- necessidade/minimização;
- segurança;
- prevenção;
- responsabilização;
- rastreabilidade;
- segregação de acesso;
- continuidade.

## 3. Dados esperados

Durante a operação podem existir dados pessoais e dados pessoais sensíveis, especialmente dados de saúde. O desenho da solução deve evitar coleta desnecessária e exposição em materiais públicos.

## 4. Requisitos mínimos

- autenticação individual;
- perfis por função;
- princípio do menor privilégio;
- logs;
- bloqueio de contas;
- gestão de dispositivos;
- criptografia quando aplicável;
- conexão segura;
- backup;
- contingência offline controlada;
- sincronização posterior;
- gestão de incidentes;
- descarte seguro;
- portabilidade e devolução de dados ao término;
- proibição de retenção indevida pela contratada.

## 5. Integrações

Toda integração com sistemas SES-MT deve ser previamente autorizada e documentada, com:

- finalidade;
- dados trafegados;
- responsável;
- protocolo;
- autenticação;
- logs;
- disponibilidade;
- contingência;
- retenção.

## 6. Contrato

O TR/contrato deve disciplinar, quando aplicável:

- papéis no tratamento;
- confidencialidade;
- acesso por subcontratados;
- incidentes;
- prazo de comunicação;
- auditoria;
- devolução/eliminação;
- cooperação com a SES-MT;
- continuidade;
- propriedade institucional dos dados.

## 7. Publicidade

Dados de pacientes, listas nominais, imagens identificáveis, credenciais, topologias sensíveis e informações protegidas não devem ser publicados no repositório ou GitHub Pages.

## 8. Incidente

Todo incidente deve possuir registro de:

- data/hora;
- sistema;
- dados potencialmente envolvidos;
- extensão;
- contenção;
- comunicação;
- análise;
- correção;
- lições aprendidas.

## 9. Validação

Este documento deve ser validado pela estrutura institucional responsável por segurança da informação e proteção de dados antes de integrar o TR definitivo.


## Revisão de prontidão e acionamento em 28 de setembro de 2026

Fornecimento isolado deverá usar apenas dados necessários à logística e rastreabilidade. Não exigir dados individuais de pacientes para simples entrega ao estabelecimento quando não necessários. Registros clínicos, quando existentes, permanecem sob regras próprias de acesso e finalidade.

Referência transversal: [Diretrizes de prontidão e acionamento](26_DIRETRIZES_PRONTIDAO_ACIONAMENTO_UHMR.md). Situação: minuta para validação institucional.


## Complementação técnica e normativa — revisão 2.1

### 10. Recebimento e responsabilidades

Distinguir aceite inicial e mensal da prontidão, liberação para funcionamento e recebimento de produtos. Fiscal técnico verifica execução; gestor coordena providências; área demandante fundamenta necessidade; assistência farmacêutica valida medicamentos; engenharia clínica valida equipamentos; autoridade sanitária atua em sua competência. As designações precisam ser formalizadas. Para módulo assistencial, anexar testes, registros profissionais, equipe, fluxos e licenças aplicáveis antes da abertura. Para fornecimento isolado, usar termo de recebimento por item e registrar recusas. Não considerar o silêncio da fiscalização como aceite.

Fontes, limites de aplicação e requisitos complementares: [Caderno de fundamentação e controles](27_FUNDAMENTACAO_E_CONTROLES_UHMR.md).
