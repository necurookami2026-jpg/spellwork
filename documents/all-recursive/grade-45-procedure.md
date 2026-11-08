# All Recursive · Grade 45 program procedure

Use [the example](../../programs/grade-45/example.json) as the input format.

| Field | Meaning |
| --- | --- |
| `unit` | Non-empty label for the fictional unit |
| `influx` | Non-negative whole number of units |
| `entry` | ID of the first record |
| `records` | Object mapping record IDs to their seal, request, and outbound links |
| `sealed` | Boolean eligibility flag for the record |
| `request` | Non-negative whole number requested by the record |
| `links` | Ordered list of distinct record IDs in the scenario |

[Validate](../../programs/grade-45/validate.py) checks the input and reports the record count. [Flood](../../programs/grade-45/flood.py) validates first and prints the simulated ledger. Both commands take one local JSON file. Invalid input produces a message on standard error and a nonzero exit status.

The example routes 45 fictional units. It allocates 18 to `systemat` and 12 to `quilt`, stops at `held`, and leaves 15 undistributed.
