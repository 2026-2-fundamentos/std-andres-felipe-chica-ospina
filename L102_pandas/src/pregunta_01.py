from pathlib import Path
import pandas as pd

PROJECT_FILE = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_FILE / "data"

def pregunta_01():
    """
    ¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        40
    """

    df = pd.read_csv(DATA_DIR / "tbl0.tsv", sep="\t")

    return int(len(df))
