# Pipeline 02 — RINEX Parser Validation and Data Reconciliation

## 1. Purpose

This notebook validates and reconciles the manually developed
RINEX parser against the original raw RINEX observation file
and an independent GeoRinEx processing result.

The validation focuses on epoch structure, satellite records,
observation keys, observation values, and preservation of
missing values and observation attributes.

## 2. Dataset and Scope

- Station: BAKO
- Date: 27 October 2003
- DOY: 300
- RINEX version: 2.10
- Satellite system: GPS
- Observation types: L1, L2, C1, P2, P1, D1
- Nominal sampling interval: 30 seconds

The validation is limited to the evaluated BAKO DOY300 file.
It does not establish universal parser validity for all RINEX files.

## 3. Input Data

### Raw reference

`data/raw/DOY300/bako3000.03o`

### Manual parser outputs

`Output/Notebook_01/parsed_observations/parsed_observations_doy300.csv`

`Output/Notebook_01/parsed_observations/parsed_epochs_doy300.csv`

## 4. Validation Workflow

The notebook consists of the following stages:

1. Notebook initialization and dataset loading.
2. Input dataset and output integrity check.
3. Raw RINEX structural reassessment.
4. Epoch-level reconciliation.
5. Satellite-level reconciliation.
6. Observation-level reconciliation.
7. Independent GeoRinEx comparison.
8. Discrepancy identification and classification.
9. Validation assessment and acceptance criteria.
10. Final report and output documentation.
11. README finalization.

## 5. Validation Results

### 5.1 Epoch-level reconciliation

- Total epochs: 2,878
- Matched timestamps: 2,878
- Epoch flag mismatches: 0
- Satellite count mismatches: 0

### 5.2 Satellite-level reconciliation

- Epoch-satellite pairs: 24,254
- Matched pairs: 24,254
- Unmatched pairs: 0

### 5.3 Observation-level reconciliation

- Observation keys: 145,524
- Matched observation keys: 145,524
- Available observation values: 120,505
- Exact numerical matches: 120,505
- Missing observation values: 25,019
- Observation value mismatches: 0

LLI and SSI values and missing-value patterns were also
compared between the raw reference and manual parser output.

### 5.4 GeoRinEx comparison

All evaluated observation keys and available observation values
matched after positional epoch alignment.

A timestamp discrepancy was identified:

- 714 of 2,878 timestamps differ by -1 ms.
- All discrepant timestamps were verified against raw RINEX text.
- The cause remains unresolved.
- No timestamp correction was applied.

## 6. Discrepancy Classification

Nine findings were documented:

- NO DISCREPANCY: 8
- UNRESOLVED: 1

The unresolved finding concerns the GeoRinEx timestamp discrepancy.

## 7. Validation Assessment

The assessment produced:

- PASS: 9 criteria
- REVIEW: 2 criteria
- FAIL: 0 criteria

The REVIEW criteria concern:

1. GeoRinEx timestamp consistency.
2. Parser generalizability beyond BAKO DOY300.

## 8. Acceptance Statement

The manual RINEX parser is accepted for the tested BAKO DOY300
dataset within the evaluated RINEX structure and observation scope.

This acceptance is dataset-specific and does not constitute
universal validation for all RINEX files or untested structures.

The original raw RINEX timestamps remain the reference.

## 9. Output Directory

All Notebook 02 outputs are stored under:

`Output/Notebook_02/`

| Directory | Contents |
|---|---|
| input_integrity | Input dataset integrity evidence |
| raw_reference | Raw RINEX reference metadata |
| epoch_reconciliation | Epoch-level comparison results |
| satellite_reconciliation | Satellite-level comparison results |
| observation_reconciliation | Observation keys, values, LLI and SSI |
| georinex_comparison | Independent GeoRinEx comparison |
| discrepancy_analysis | Discrepancy register and classification |
| validation_assessment | Acceptance criteria assessment |
| final_report | Final report and output inventory |

## 10. Final Report

`Output/Notebook_02/final_report/final_rinex_parser_validation_report_doy300.md`

## 11. Limitations and Next Steps

- Validation currently covers one BAKO observation file.
- Satellite-list continuation handling has not been generalized.
- Nonzero epoch flag handling requires separate evaluation.
- GeoRinEx timestamp discrepancy remains unresolved.
- Cycle-slip correction, arc segmentation, STEC, and VTEC
  processing are outside the scope of this notebook.

Subsequent notebooks should address observation quality assessment,
cycle-slip investigation, satellite arc segmentation, and TEC processing.

---

Notebook 02 documentation reflects the validation work
and evidence generated for BAKO DOY300.