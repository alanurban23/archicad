# Agents Catalog (MVP)

1. Agent Briefu
2. Agent Prawno-Planistyczny
3. Agent Zagospodarowania Terenu
4. Agent Architektoniczny
5. Agent Konstrukcyjny
6. Agent Instalacyjny
7. Agent Energetyczny
8. Agent Wykonawczy
9. Agent BIM/Archicad
10. Agent QA
11. Agent Opisu Projektu (PDF -> opis + zgodność WZ/MPZP)

Each agent uses a dedicated skill card in `skills/` and produces structured outputs into JSON contracts in `data/`.

## Priorytet biznesowy od projektanta
Agent 11 realizuje kluczowy przypadek użycia:
- czyta informacje z projektu (w szczególności PDF),
- przygotowuje gotowy opis projektu budowlanego zgodny ze strukturą rozporządzenia,
- generuje wersję do wydruku (PDF),
- sprawdza zgodność opisu z decyzją WZ lub MPZP i raportuje rozbieżności.
