from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

REQUIRED_META = ["**Código:**", "**Versão:**"]
FORBIDDEN = [
    "raw.githubusercontent.com/menandesneto51/ciatox-mt-apresentacao",
]
PLACEHOLDER_MARKERS = ["A preencher", "a definir", "definir", "validar"]

errors = []
warnings = []

for path in sorted(DOCS.glob("*.md")):
    text = path.read_text(encoding="utf-8")

    for marker in REQUIRED_META:
        if marker not in text:
            errors.append(f"{path}: ausência de metadado obrigatório {marker}")

    for bad in FORBIDDEN:
        if bad in text:
            errors.append(f"{path}: referência externa proibida: {bad}")

    if "http://" in text:
        warnings.append(f"{path}: contém URL HTTP não segura")

    # Detecta menções a requisitos críticos sem sinais mínimos de aceite.
    if re.search(r"\bcrític[oa]\b", text, re.I):
        if not re.search(r"aceite|evidência|teste|comission", text, re.I):
            warnings.append(f"{path}: menciona criticidade sem critério de evidência/aceite")

    # Evita tratar placeholders como versão final sem alerta.
    if any(x.lower() in text.lower() for x in PLACEHOLDER_MARKERS):
        if "minuta" not in text.lower() and "estrutura" not in text.lower():
            warnings.append(f"{path}: contém campos pendentes sem indicar claramente minuta/estrutura")

# Verificações estruturais obrigatórias da v2.
required_files = [
    "00_GOVERNANCA_DOCUMENTAL_UHMR_SES_MT.md",
    "01_BASE_LEGAL_E_NORMATIVA_UHMR_SES_MT.md",
    "02_DFD_UHMR_SES_MT_v2.md",
    "03_MATRIZ_RISCOS_UHMR_v2.md",
    "07_MATRIZ_SLA_KPI_ACEITE_UHMR.md",
    "11_MATRIZ_MESTRE_REQUISITOS_UHMR.md",
    "14_ETP_UHMR_SES_MT_v2_FONTE.md",
    "15_TERMO_DE_REFERENCIA_UHMR_v2_FONTE.md",
    "16_MINUTA_EDITAL_UHMR_v2_FONTE.md",
    "17_MINUTA_CONTRATUAL_UHMR_v2_FONTE.md",
    "25_MEMORIA_CALCULO_DIMENSIONAMENTO_UHMR.md",
]

for name in required_files:
    if not (DOCS / name).exists():
        errors.append(f"arquivo obrigatório ausente: docs/{name}")

# Verifica referências mínimas entre documentos derivados.
cross_checks = {
    "15_TERMO_DE_REFERENCIA_UHMR_v2_FONTE.md": ["UHMR-ETP-001", "UHMR-RSK-001", "UHMR-SLA-001"],
    "16_MINUTA_EDITAL_UHMR_v2_FONTE.md": ["TR", "matriz de riscos", "SLA"],
    "17_MINUTA_CONTRATUAL_UHMR_v2_FONTE.md": ["TR", "SLA", "matriz de riscos"],
}

for name, tokens in cross_checks.items():
    path = DOCS / name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8").lower()
    for token in tokens:
        if token.lower() not in text:
            errors.append(f"{path}: referência cruzada esperada ausente: {token}")

print("=== UHMR Documentation Validator ===")
for item in warnings:
    print(f"WARNING: {item}")
for item in errors:
    print(f"ERROR: {item}")

print(f"Resumo: {len(errors)} erro(s), {len(warnings)} aviso(s)")
sys.exit(1 if errors else 0)
