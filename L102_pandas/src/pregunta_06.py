from pathlib import Path
import pandas as pd

PROJECT_FILE = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_FILE / "data"
def pregunta_06():
    """
    Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
    conviértalos a mayúsculas y retórnelos como una lista ordenada
    alfabéticamente.

    Ejemplo del formato de la respuesta:

        ["A", "B", "C", "D", "E", "F", "G"]
    """

    df = pd.read_csv(DATA_DIR / "tbl1.tsv", sep="\t")

    return sorted(df["c4"].str.upper().unique().tolist())
