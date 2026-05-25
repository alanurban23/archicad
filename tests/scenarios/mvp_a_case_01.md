# Scenario: MVP_A_CASE_01

Cel: przetestować przepływ PDF -> opis projektu -> raport zgodności WZ/MPZP.

## Wejścia (testowe)
- tests/fixtures/input/project_brief.case01.json
- tests/fixtures/input/site_constraints.case01.json
- tests/fixtures/input/source_documents_index.case01.json
- tests/fixtures/input/pdf_extraction.case01.json

## Generowanie wyjść
Uruchom:
- `python scripts/generate_case_outputs.py`

Wygenerowane pliki:
- tests/generated/project_description.case01.generated.json
- tests/generated/description_compliance_report.case01.generated.json
- tests/generated/qa_report.case01.generated.json

## Kryteria zaliczenia
1. Dane wejściowe są testowe (fixtures/input).
2. Dane wyjściowe są generowane przez skrypt (tests/generated).
3. Każdy parametr formalny ma status.
4. Raport wskazuje niezgodności oraz decyzje projektanta, jeśli wystąpią.
