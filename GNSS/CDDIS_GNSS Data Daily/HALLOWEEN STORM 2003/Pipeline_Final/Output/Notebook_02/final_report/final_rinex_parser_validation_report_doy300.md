# RINEX Parser Validation and Data Reconciliation Report

## 1. Dataset and Validation Scope

This report documents the validation of the manually developed
RINEX parser using the BAKO DOY300 observation dataset.

- Station: BAKO
- Date: 27 October 2003
- Day of Year: 300
- RINEX version: 2.10
- Satellite system: GPS
- Observation types: L1, L2, C1, P2, P1, D1
- Sampling interval: 30 seconds (based on temporal assessment)

The validation compares the manual parser output against the original
raw RINEX file and an independent GeoRinEx processing result.

## 2. Input Data Integrity

The raw RINEX file and parsed datasets were checked for availability,
file integrity, and expected data schemas.

The input datasets were successfully loaded for validation.
Missing observation values were preserved as missing values and
were not replaced with zero.

## 3. Raw RINEX Structural Assessment

The raw RINEX file contains:

- 51,404 physical lines.
- 18 header lines.
- 2,878 epoch records.
- 28 unique GPS satellite identifiers.
- 24,254 epoch-satellite occurrences.
- Six observation types.

The header declares the observation types L1, L2, C1, P2, P1, and D1.
The temporal assessment identified a nominal sampling interval
of 30 seconds.

## 4. Epoch-Level Reconciliation

- Raw epoch records: 2878
- Matched epoch records: 2878
- Matching epoch flags: 2878
- Matching declared satellite counts: 2878

The raw RINEX and manual parser epoch records show exact agreement
for the evaluated timestamps and epoch-level attributes.

## 5. Satellite-Level Reconciliation

- Raw epoch-satellite pairs: 24254
- Matched pairs: 24254

All evaluated epoch-satellite pairs were matched between the raw
RINEX reference and the manual parser output.

## 6. Observation-Level Reconciliation

### 6.1 Observation Keys

- Total observation keys: 145524
- Matched observation keys: 145524

No unmatched observation keys were identified.

### 6.2 Observation Values

- Available observation values: 120505
- Exact numerical matches: 120505
- Missing raw values: 25019
- Missing parsed values: 25019

All available observation values matched exactly between the raw
RINEX reference and the manual parser output.

### 6.3 LLI and SSI Preservation

- Missing LLI values in raw data: 25019
- Missing SSI values in raw data: 97407

The comparison confirmed consistent preservation of LLI and SSI
values and their missing-value patterns between the raw reference
and parsed output.

## 7. Independent GeoRinEx Comparison

The manual parser output was independently compared with GeoRinEx.

- Total observation records evaluated: 145524
- Matched observation keys: 145524
- Both datasets missing: 25019
- Both datasets available: 120505
- Exact available-value matches: 120505
- Observation value mismatches: 0

All evaluated observation keys and available observation values
matched after positional epoch alignment.

### Timestamp Coordinate Discrepancy

A separate timestamp comparison identified 714 of 2,878 epochs
with a difference of -1 ms in the GeoRinEx output relative to
the raw RINEX timestamps.

All discrepant timestamps were verified against the original
raw RINEX text. The cause of this difference remains unresolved.

No timestamp correction or modification was applied.

## 8. Discrepancy Analysis

The discrepancy register contains 9 findings:

- NO DISCREPANCY: 8
- UNRESOLVED: 1
- RESOLVED: 0

The unresolved finding concerns the 1 ms GeoRinEx timestamp
difference. Other evaluated reconciliation parameters showed
no identified discrepancy.

## 9. Validation Assessment

The validation criteria assessment produced:

- PASS: 9
- REVIEW: 2
- FAIL: 0

The two REVIEW criteria concern:

1. The unresolved GeoRinEx timestamp coordinate discrepancy.
2. Parser generalizability beyond the tested BAKO DOY300 dataset.

No validation criterion was classified as FAIL.

## 10. Final Conclusion

The manually developed RINEX parser successfully reproduced
the evaluated epoch structure, satellite records, observation
keys, observation values, and missing-value patterns of the
original BAKO DOY300 RINEX file.

The parser is accepted for the tested BAKO DOY300 dataset within
the evaluated RINEX structure and observation scope.

This acceptance is dataset-specific. It does not establish
universal validity for all RINEX files or guarantee compatibility
with untested RINEX structures.

The original raw RINEX timestamps remain the reference.
The unresolved GeoRinEx timestamp discrepancy is documented
without applying an artificial timestamp correction.

## 11. Recommendations for Subsequent Processing

1. Preserve the original raw RINEX data as the reference dataset.
2. Retain the documented parser limitations during subsequent use.
3. Validate additional observation files before extending the
   parser acceptance to other dates or datasets.
4. Continue with dedicated observation quality assessment,
   cycle-slip investigation, and satellite arc analysis in
   their respective processing stages.

---

Report generated from Notebook 02 validation outputs.