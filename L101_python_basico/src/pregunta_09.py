from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)

    counter = collections.defaultdict(int)

    for cell in df.iloc[:, 4]:

        pairs = str(cell).split(",")
        for pair in pairs:
            key, val = pair.split(":")
            counter[key] += 1

    resultado = {}
    for key in sorted(counter.keys()):
        resultado[key] = counter[key]

    return resultado
