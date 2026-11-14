from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"a": 122, "b": 49, "c": 91, ...}
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)

    sums = collections.defaultdict(int)

    for value, codes in zip(df.iloc[:, 1], df.iloc[:, 3]):

        letters = str(codes).split(",")
        for letter in letters:
            sums[letter] += int(value)

    resultado = {}
    for letter in sorted(sums.keys()):
        resultado[letter] = sums[letter]

    return resultado
