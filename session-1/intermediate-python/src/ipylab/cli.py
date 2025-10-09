# cli.py
import typer
import logging
from pathlib import Path
import numpy as np
import time

from .io import load_signal_csv, save_features_csv
from .features import feature_vector
from .vectorize import python_rms, numpy_rms

app = typer.Typer(help="Intermediate Python Lab CLI")

# -------------------------------
# 1️⃣ Generate synthetic data
# -------------------------------
@app.command()
def generate_data(
    out: Path = typer.Option(Path("data/signal.csv"), help="Output CSV path"),
    n: int = 4000,
    noise: float = 0.15
):
    """
    Generate synthetic 1D signal (sine + square mixture) with optional noise and save to CSV.
    """
    t = np.linspace(0, 2 * np.pi, n)
    sine = np.sin(5 * t)
    square = np.sign(np.sin(2 * t))
    signal = sine + square + np.random.normal(0, noise, n)

    out.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(out, signal, delimiter=",")
    typer.echo(f"Synthetic signal saved to {out}")


# -------------------------------
# 2️⃣ Run feature extraction pipeline
# -------------------------------
@app.command()
def run_pipeline(
    inp: Path = Path("data/signal.csv"),
    out: Path = Path("data/features.csv"),
    chunk: int = 256
):
    """
    Stream input CSV in chunks, compute features per chunk, and save to CSV.
    """
    data = load_signal_csv(inp)
    n = len(data)
    features = []

    for start in range(0, n, chunk):
        chunk_data = np.array(data[start:start + chunk])
        feat = feature_vector(chunk_data)
        features.append(feat)

    save_features_csv(out, features)
    typer.echo(f"Features saved to {out}")


# -------------------------------
# 3️⃣ Profile Python vs NumPy RMS
# -------------------------------
@app.command()
def profile():
    """
    Profile pure-Python vs NumPy RMS computation on 1e6 random floats.
    """
    arr = np.random.randn(int(1e6))
    lst = arr.tolist()

    # Python RMS
    start = time.perf_counter()
    python_rms(lst)
    py_time = (time.perf_counter() - start) * 1000

    # NumPy RMS
    start = time.perf_counter()
    numpy_rms(arr)
    np_time = (time.perf_counter() - start) * 1000

    typer.echo(f"Python RMS: {py_time:.2f} ms")
    typer.echo(f"NumPy RMS: {np_time:.2f} ms")


# -------------------------------
# CLI entry
# -------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
