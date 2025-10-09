from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    """
    Load a single-column CSV of floats into a list.
    TODO:
      - Validate that path exists and is a file; else raise FileNotFoundError
      - Read rows; parse as float; collect into list
      - Use try/except to catch ValueError and log it (then re-raise)
    """
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    values: list[float] = []
    try:
        with path.open(newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:  # skip empty rows
                    continue
                try:
                    values.append(float(row[0]))
                except ValueError as e:
                    logging.exception(f"Invalid float value in {path}: {row}")
                    raise
    except Exception as e:
        logging.exception(f"Error reading CSV file {path}: {e}")
        raise

    return values


def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    TODO:
      - Ensure parent dir exists (mkdir parents=True, exist_ok=True)
      - Write header and rows via csv.writer
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["rms", "zero_crossings", "peak_to_peak", "mad"])
        for row in rows:
            writer.writerow(row)
