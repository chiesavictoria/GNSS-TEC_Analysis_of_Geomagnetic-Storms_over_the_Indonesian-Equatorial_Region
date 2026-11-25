# GNSS-TEC Processing Pipeline v0.1

## 1. Research Overview

**Research Title:**

Multi Parameter Observations of Solar Storm Impacts on the Indonesian Equator Ionosphere

**Dataset:** GPS RINEX 2.10 observation data from BAKO station.

**Research Event:** Halloween Storm 2003, covering 27 October–3 November 2003 (DOY 300–307).

**Research Objective:** To investigate the response of equatorial ionospheric TEC to geomagnetic storm activity.

## 2. Pipeline Objectives

This pipeline is designed to process GNSS observation data systematically and reproducibly.

The planned processing stages are:

1. Dataset Inventory and Integrity Audit.
2. RINEX Data Ingestion and Parser Development.
3. RINEX Parser Validation and Data Reconciliation.
4. GNSS Observation Quality Assessment.
5. Cycle Slip Detection and Anomaly Investigation.
6. Satellite Arc Segmentation and Continuity Analysis.
7. Relative STEC Processing and Validation.
8. Calibrated STEC Processing and Bias Correction.
9. VTEC Conversion and Delta TEC Analysis.
10. Geomagnetic Storm Response Analysis.
11. Comparative Analysis of Geomagnetic Storm Events.

Each stage must be evaluated before its output is used by the next stage.

## 3. Project Directory Structure

Pipeline_Final/
- data/
  - raw/
    - DOY300/
    - DOY301/
    - DOY302/
    - DOY303/
    - DOY304/
    - DOY305/
    - DOY306/
    - DOY307/
  - external/
- documentations/
  - README_Pipeline_v0.1.md
- notebooks/
  - 00_Dataset_Inventory_and_Integrity_Audit.ipynb
  - 01_RINEX_Data_Ingestion_and_Parser_Development.ipynb
  - 02_RINEX_Parser_Validation_and_Data_Reconciliation.ipynb
- Output/
- config.py
- processing_functions.py
- rinex_parser.py

Existing Python modules are retained but have not yet been approved for reuse in the new pipeline.

## 4. Dataset Inventory and Initial Audit

Eight local RINEX files were identified in the raw data directory.

The initial audit examined:

- File and folder identity.
- Observation date recorded in the RINEX header.
- First and last observation epochs.
- Nominal temporal sampling interval.
- Daily 30-second grid coverage.
- Missing epochs at the beginning, middle, and end of the day.
- Unmapped and duplicate grid epochs.

### 4.1 Initial Audit Results

| DOY | Observation Date | Observed Epochs | Coverage (%) | Initial Status |
|---|---|---:|---:|---|
| 300 | 2003-10-27 | 2878 | 99.930556 | ELIGIBLE_FOR_NEXT_STAGE |
| 301 | 2003-10-28 | 2878 | 99.930556 | ELIGIBLE_FOR_NEXT_STAGE |
| 302 | 2003-10-29 | 2878 | 99.930556 | ELIGIBLE_FOR_NEXT_STAGE |
| 303 | 2003-10-30 | 2878 | 99.930556 | ELIGIBLE_FOR_NEXT_STAGE |
| 304 | 2003-10-31 | 2867 | 99.548611 | REVIEW_BOUNDARY_COVERAGE |
| 305 | 2003-11-08 | 2878 | 99.930556 | HOLD_IDENTITY_MISMATCH |
| 306 | 2003-11-02 | 2878 | 99.930556 | ELIGIBLE_FOR_NEXT_STAGE |
| 307 | 2003-11-03 | 2878 | 99.930556 | ELIGIBLE_FOR_NEXT_STAGE |

### 4.2 Important Findings

**DOY300–303 and DOY306–307**

Each file contains 2,878 observed epochs against 2,880 expected daily epochs. One epoch is missing at the beginning and one at the end of the daily grid. No internal missing grid slots were identified.

**DOY304**

The file contains 2,867 observed epochs. Twelve grid slots are missing at the beginning and one at the end of the day. No internal missing grid slots were identified. This file is retained for further review.

**DOY305**

The file is stored in the DOY305 directory, but its RINEX header indicates an observation date of 8 November 2003 rather than 1 November 2003.

The source of this discrepancy has not yet been established. The file is retained in the raw directory but placed on hold.

## 5. Audit Outputs

The initial audit generates the following files in Output/:

- dataset_inventory.csv
- dataset_header_identity_audit.csv
- dataset_temporal_audit.csv
- dataset_grid_coverage_audit.csv
- dataset_initial_eligibility.csv
- dataset_final_audit_report.csv
- dataset_final_audit_report.txt

## 6. Current Pipeline Status

### Notebook 00 — Dataset Inventory and Integrity Audit

**Status:** Initial audit completed.

The notebook documents the available raw files, header identity, temporal coverage, and initial eligibility classification.

ELIGIBLE_FOR_NEXT_STAGE does not mean that all GNSS observations have passed quality control. Observation-level validation remains necessary.

### Notebook 01 — RINEX Data Ingestion and Parser Development

**Status:** Planned / not yet validated.

Objectives:

- Read RINEX 2.10 header metadata.
- Identify observation types and their ordering.
- Develop a manual parser.
- Handle epoch records, satellite lists, and observation records.
- Support continuation records and event flags.
- Generate a structured observation table.

### Notebook 02 — RINEX Parser Validation and Data Reconciliation

**Status:** Planned / not yet validated.

Objectives:

- Compare manual parser output with raw RINEX records.
- Compare parsed observations with GeoRinex output.
- Reconcile timestamps, satellite identifiers, and observation values.
- Investigate discrepancies.
- Establish parser pass/fail criteria.

The manual parser will only become the official data source after validation requirements have been satisfied.

## 7. Planned Processing Stages

| Notebook | Processing Stage |
|---|---|
| 03 | GNSS Observation Quality Assessment |
| 04 | Cycle Slip Detection and Anomaly Investigation |
| 05 | Satellite Arc Segmentation and Continuity Analysis |
| 06 | Relative STEC Processing and Validation |
| 07 | Calibrated STEC Processing and Bias Correction |
| 08 | VTEC Conversion and Delta TEC Analysis |
| 09 | Geomagnetic Storm Response Analysis |
| 10 | Comparative Analysis of Geomagnetic Storm Events |

These stages are a preliminary roadmap and may be revised after technical evaluation and supervisor discussion.

## 8. Methodological Notes and Limitations

- The RINEX observation time system must be identified and converted explicitly before comparison with UTC-based geomagnetic indices.
- Successful temporal grid mapping does not establish observation-level quality.
- Parser validation must account for RINEX record structure, including continuation records and event flags.
- Relative STEC is not equivalent to calibrated absolute STEC.
- VTEC processing requires appropriate satellite geometry and a mapping function.
- Navigation or precise orbit data availability must be verified before VTEC processing.
- DOY305 must not be treated as 1 November 2003 data until its identity discrepancy is resolved.
- Data eligibility and processing decisions must be documented to preserve reproducibility.

## 9. Version Information

**Pipeline Version:** v0.1

**Current Focus:** Notebook 00–02.

**Development Principle:** Build, test, validate, and document each processing stage before proceeding to the next stage.
