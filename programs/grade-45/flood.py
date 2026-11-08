"""Simulate the fictional Temaline Valid Quilt influx and print its ledger."""

from collections import deque

from validate import run_cli


def simulate(scenario):
    records = scenario["records"]
    remaining = scenario["influx"]
    queue = deque([scenario["entry"]])
    seen = set(queue)
    reached = []
    held = []
    allocations = {}

    while queue:
        name = queue.popleft()
        record = records[name]
        if not record["sealed"]:
            held.append(name)
            continue

        reached.append(name)
        amount = min(record["request"], remaining)
        if amount:
            allocations[name] = amount
            remaining -= amount

        for link in record["links"]:
            if link not in seen:
                seen.add(link)
                queue.append(link)

    return {
        "unit": scenario["unit"],
        "influx": scenario["influx"],
        "reached": reached,
        "held": held,
        "allocations": allocations,
        "undistributed": remaining,
    }


if __name__ == "__main__":
    run_cli(__doc__, simulate)
