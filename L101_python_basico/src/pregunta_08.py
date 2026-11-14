from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)

    letters_dict = collections.defaultdict(set)

    for letter, value in zip(df.iloc[:, 0], df.iloc[:, 1]):

        letters_dict[int(value)].add(str(letter))

    resultado = []
    for value in sorted(letters_dict.keys()):
        resultado.append((value, sorted(letters_dict[value])))

    return resultado
