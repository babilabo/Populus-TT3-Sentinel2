# Three-season Populus euphratica mapping — limited research materials

Supporting materials for the manuscript **“Three-Season Spectral–Phenological Modeling for Source-Domain Classification and Cross-Region Candidate Mapping of Populus euphratica Using Sentinel-2 Imagery”** (Forests manuscript `forests-4583393`).

## What is included

- `configs/public_experiment_manifest.json`: feature names, season windows, class labels, architecture-level hyperparameters, and fixed spatial-block evaluation metadata.
- `results/tt3_spatial_seed42_classification_report.csv`: **observed class-wise classification metrics** for one Original TT3 run (seed 42) on the 14,007-sample spatial-block test set. This is **not** the historical random-pixel-split Figure 6 result and **not** a three-seed class-wise mean.
- `tools/summarize_class_report.py`: a small, standalone utility for reading an existing classification report CSV and formatting class-wise metrics. Python standard library only.
- `docs/method_scope.md`: important distinctions among source-domain results, target-region candidate mapping and probability interpretation.

## What is not included

The **original model source implementation, full training and inference pipelines, scene-processing scripts, sample extraction, trained weights, sample coordinates, reference polygons, and geospatial rasters** are **not** included in this limited release. Accordingly, **this repository is not an end-to-end reproducibility package**, and the included utility **cannot train the model or generate a Kuqa map**. The public architecture metadata do not, by themselves, constitute an implementation.

## Checking the published per-class results

```bash
python tools/summarize_class_report.py results/tt3_spatial_seed42_classification_report.csv
```

The input CSV originates from the saved class report of the E1-A source-domain spatial-block run, not from calculated estimates or digitization of a figure.

## Availability

Sentinel-2 imagery is accessible from its official public data providers. Access to additional research materials may be considered upon reasonable request to the corresponding author, subject to applicable permissions and data-sharing constraints. **Availability upon request does not guarantee release of all code or data.**

## Rights and use

No open-source software license is granted for the material in this repository. **All rights reserved, except rights otherwise mandated by law or the hosting platform.** A public repository is publicly viewable: it is **not** a technical safeguard against copying. Do not upload private notebooks, checkpoints or reference data to this repository.

## Publication status

This package was assembled for pre-submission review. It should not be described in the manuscript as a publicly accessible repository until the repository has actually been created, published, and checked.
