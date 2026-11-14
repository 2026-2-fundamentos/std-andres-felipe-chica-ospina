from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)

    letters_dict = collections.defaultdict(list)

    for letter, value in zip(df.iloc[:, 0], df.iloc[:, 1]):

        letters_dict[int(value)].append(str(letter))

    resultado = []
    for value in sorted(letters_dict.keys()):
        resultado.append((value, letters_dict[value]))

    return resultado

def main():
    print(pregunta_07())

if __name__ == "__main__":
    main()
