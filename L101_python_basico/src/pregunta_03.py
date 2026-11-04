from pathlib import Path
import pandas as pd

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)
    print(df)
    resultado = list(df.groupby(0)[1].sum().sort_index().items())
    return resultado


def main():
    pregunta_03()

if __name__ == "__main__":
    main()
