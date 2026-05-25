# Skill: Agent Opisu Projektu (PDF -> opis + zgodność)

## Cel
Na bazie dokumentacji projektowej (szczególnie PDF) utworzyć gotowy opis do projektu budowlanego oraz raport zgodności z WZ/MPZP.

## Wejścia
- `data/source_documents_index.json` (lista dokumentów i ich typów)
- `data/project_brief.json`
- `data/site_constraints.json`
- ekstrakcja danych z PDF (tekst/tabele/parametry)

## Działania
1. Wyciągnij parametry i informacje opisowe z projektu PDF.
2. Ułóż rozdziały opisu zgodnie z wymaganym układem formalnym (sekcje techniczne/funkcjonalne).
3. Oznacz każde twierdzenie statusem pewności: `potwierdzone`, `robocze`, `do_weryfikacji`, `ryzyko`, `blokada`.
4. Zweryfikuj zgodność treści z WZ/MPZP (przeznaczenie, dach, PBC, miejsca parkingowe, wysokość i inne limity).
5. Zapisz wynik do:
   - `outputs/project_description.md`
   - `outputs/project_description_print.html` (źródło do PDF)
   - `outputs/compliance_report.md`
   - `data/description_compliance_report.json`

## QA (must-have)
- brak "fałszywej pewności" (każdy kluczowy parametr ma status),
- każda niezgodność z WZ/MPZP ma wpływ i rekomendację korekty,
- gotowy opis nadaje się do eksportu do PDF i wydruku.
