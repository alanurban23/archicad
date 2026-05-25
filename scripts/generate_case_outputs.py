#!/usr/bin/env python3
import json
from pathlib import Path

STATUS_OK = "potwierdzone"
STATUS_RISK = "ryzyko"


def load_json(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def save_json(p, data):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')


def generate(case_id: str = "case01"):
    base_in = Path(f"tests/fixtures/input")
    brief = load_json(base_in / f"project_brief.{case_id}.json")
    constraints = load_json(base_in / f"site_constraints.{case_id}.json")
    extraction = load_json(base_in / f"pdf_extraction.{case_id}.json")

    pid = brief["project_id"]
    ext = extraction["extracted"]
    plan = constraints["planning"]

    roof_ok = ext.get("roof_shape") == plan["roof"]["value"]
    pbc_ok = ext.get("biologically_active_area_pct", 0) >= plan["biologically_active_area_min_pct"]["value"]
    parking_ok = ext.get("parking_spaces", 0) >= plan["parking_spaces_min"]["value"]
    height_ok = ext.get("height_m", 999) <= plan["height_limit_m"]["value"]

    description = {
        "project_id": pid,
        "description_version": "generated_v1",
        "sections": {
            "general": f"Budynek mieszkalny jednorodzinny, PU {ext.get('usable_area_m2')} m2.",
            "functional": f"Wejście: {ext.get('entry_orientation')}, strefa dzienna: {ext.get('day_zone_orientation')}.",
            "formal": "Opis wygenerowany automatycznie z danych testowych i porównania z MPZP/WZ."
        },
        "status_tags": {
            "building_function": STATUS_OK,
            "roof_shape": STATUS_OK if roof_ok else STATUS_RISK,
            "usable_area": STATUS_OK,
            "biologically_active_area": STATUS_OK if pbc_ok else STATUS_RISK,
            "parking_spaces": STATUS_OK if parking_ok else STATUS_RISK,
            "height": STATUS_OK if height_ok else STATUS_RISK,
        }
    }

    checks = [
        {"name": "przeznaczenie", "result": "zgodne", "status": STATUS_OK},
        {"name": "dach", "result": "zgodne" if roof_ok else "niezgodne", "status": STATUS_OK if roof_ok else STATUS_RISK,
         "expected": plan["roof"]["value"], "actual": ext.get("roof_shape")},
        {"name": "pbc", "result": "zgodne" if pbc_ok else "niezgodne", "status": STATUS_OK if pbc_ok else STATUS_RISK,
         "expected_min": plan["biologically_active_area_min_pct"]["value"], "actual": ext.get("biologically_active_area_pct")},
        {"name": "miejsca_parkingowe", "result": "zgodne" if parking_ok else "niezgodne", "status": STATUS_OK if parking_ok else STATUS_RISK},
        {"name": "wysokosc", "result": "zgodne" if height_ok else "niezgodne", "status": STATUS_OK if height_ok else STATUS_RISK}
    ]

    mismatches = []
    decisions = []
    if not roof_ok:
        mismatches.append("Niezgodny typ dachu względem MPZP/WZ.")
        decisions.append("Skorygować geometrię dachu do wymagań planu.")
    if not pbc_ok:
        mismatches.append("Niespełnione minimalne PBC.")
        decisions.append("Skorygować PZT dla osiągnięcia wymaganego PBC.")

    compliance = {
        "project_id": pid,
        "overall_status": STATUS_RISK if mismatches else STATUS_OK,
        "checks": checks,
        "mismatches": mismatches,
        "designer_decisions_required": decisions,
    }

    qa = {
        "project_id": pid,
        "scenario": f"MVP_A_{case_id.upper()}",
        "checks_summary": {
            "total": len(checks),
            "passed": sum(1 for c in checks if c["result"] == "zgodne"),
            "warnings": 0,
            "failed": sum(1 for c in checks if c["result"] != "zgodne"),
        },
        "errors": mismatches,
        "risks": ["Ryzyka formalne wymagają decyzji projektanta."] if mismatches else [],
        "missing_data": [],
        "designer_decisions_required": decisions,
    }

    out = Path("tests/generated")
    save_json(out / f"project_description.{case_id}.generated.json", description)
    save_json(out / f"description_compliance_report.{case_id}.generated.json", compliance)
    save_json(out / f"qa_report.{case_id}.generated.json", qa)


if __name__ == "__main__":
    generate("case01")
