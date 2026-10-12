#!/usr/bin/env python3
"""Read a scikit-learn classification_report CSV and print its observed metrics.

Independent post-processing utility only; does not perform classification.
"""
import argparse
import csv
from pathlib import Path


def load_rows(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "precision" not in reader.fieldnames:
            raise ValueError("Input is not a classification-report CSV")
        return list(reader)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Saved report CSV from an existing evaluation")
    args = parser.parse_args()
    print("Class | Precision (%) | Recall (%) | F1 (%) | Support")
    print("--- | ---: | ---: | ---: | ---:")
    for row in load_rows(args.csv_path):
        label = row.get("", "")
        if label in {"accuracy", "macro avg", "weighted avg", "micro avg", "samples avg"}:
            continue
        precision, recall, f1 = (100 * float(row[k]) for k in ("precision", "recall", "f1-score"))
        print(f"{label} | {precision:.2f} | {recall:.2f} | {f1:.2f} | {int(float(row['support']))}")


if __name__ == "__main__":
    main()
