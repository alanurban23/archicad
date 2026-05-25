# Archicad Autonomous Design Agent – MVP 80%

This repository contains a practical MVP implementation plan for a multi-agent system that prepares a conceptual 100 m² single-family house package for Archicad workflows in Poland.

## Scope
- Plan 1 target (1–2 weeks): one coherent concept variant `DOM_100_MVP_A`.
- Deliverables: brief, legal/planning assumptions with statuses, site plan assumptions (PZT), conceptual layout, modeling plan for Archicad/Tapir, and QA report.

## Folder structure
- `agents/` – agent specifications and QA checklists.
- `skills/` – procedural skill cards for each specialist agent.
- `data/` – shared JSON interfaces between agents.
- `variants/` – design variants (A/B/C), MVP starts with A.
- `outputs/` – generated reports, project description, print-ready files and handoff package.
- `docs/` – architecture and execution notes.

## Standard status taxonomy
Every legal and data-sensitive assumption must use one of:
- `potwierdzone`
- `robocze`
- `do_weryfikacji`
- `ryzyko`
- `blokada`

## MVP acceptance (high level)
1. Functional area sum in range 95–105 m².
2. MPZP/WZ assumptions explicitly tagged with status (no false certainty).
3. PZT includes: house, access, parking, terrace, retention, waste, utilities.
4. Basic BIM structure prepared for Archicad handoff.
5. QA report includes errors, risks, missing data, and designer decisions.


## New MVP capability requested by designers
- Convert project PDF content into a structured project description.
- Produce print-ready output (PDF pipeline via HTML/MD).
- Auto-check description consistency against WZ/MPZP and report mismatches.
