from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo del formato de la respuesta:

        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)

    resultado = []

    for letter, codes, metrics in zip(df.iloc[:, 0], df.iloc[:, 3], df.iloc[:, 4]):

        n_codes = len(str(codes).split(","))
        n_metrics = len(str(metrics).split(","))
        resultado.append((str(letter), n_codes, n_metrics))

    return resultado
