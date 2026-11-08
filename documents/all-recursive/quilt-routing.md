# All Recursive · Valid Quilt routing and ledger

1. Start from the entry record named in the scenario.
2. Visit sealed records in breadth-first order. Each record lists its outbound links in traversal order. Unsealed records stop their branch. A record is considered once even when the graph contains cycles or converging branches.
3. Allocate up to each visited record's request from the remaining influx. A record with a zero request can still relay the flood. Unreachable records receive zero units.
4. Report allocations, reached records, unsealed records encountered, and the undistributed remainder. The sum of allocations and the remainder always equals the starting influx.

A seal is a boolean provided by the scenario author and represents eligibility within this fictional simulation. The program prints the resulting ledger as JSON. Each run starts from its input scenario.
