"""Validate a fictional Temaline Valid Quilt influx scenario."""

import argparse
import json
from pathlib import Path


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key!r}")
        result[key] = value
    return result


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def whole_units(value):
    return type(value) is int and value >= 0


def load_scenario(path):
    scenario = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(scenario, dict):
        raise ValueError("Scenario must be a JSON object.")
    if not nonblank(scenario.get("unit")):
        raise ValueError("unit must be a non-empty string.")
    if not whole_units(scenario.get("influx")):
        raise ValueError("influx must be a non-negative integer.")
    records = scenario.get("records")
    if not isinstance(records, dict) or not records:
        raise ValueError("records must be a non-empty object.")
    entry = scenario.get("entry")
    if not nonblank(entry) or entry not in records:
        raise ValueError("entry must identify a record in the scenario.")

    for name, record in records.items():
        if not nonblank(name) or not isinstance(record, dict):
            raise ValueError(f"Invalid record: {name!r}.")
        if type(record.get("sealed")) is not bool:
            raise ValueError(f"{name!r}: sealed must be a boolean.")
        if not whole_units(record.get("request")):
            raise ValueError(f"{name!r}: request must be a non-negative integer.")
        links = record.get("links")
        if not isinstance(links, list) or any(not nonblank(link) or link not in records for link in links):
            raise ValueError(f"{name!r}: links must be an array of existing record IDs.")
        if len(links) != len(set(links)):
            raise ValueError(f"{name!r}: links must be distinct.")
    return scenario


def run_cli(description, process):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("scenario", type=Path, help="Local JSON scenario")
    args = parser.parse_args()
    try:
        scenario = load_scenario(args.scenario)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(process(scenario), indent=2))


if __name__ == "__main__":
    run_cli(__doc__, lambda scenario: {"valid": True, "records": len(scenario["records"])})
