from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)

    sums = collections.defaultdict(int)

    for letter, metrics in zip(df.iloc[:, 0], df.iloc[:, 4]):

        pairs = str(metrics).split(",")
        for pair in pairs:
            key, val = pair.split(":")
            sums[str(letter)] += int(val)

    resultado = {}
    for letter in sorted(sums.keys()):
        resultado[letter] = sums[letter]

    return resultado
