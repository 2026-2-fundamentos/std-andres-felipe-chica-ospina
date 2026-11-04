from pathlib import Path
import pandas as pd

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)
    print(df)
    conteo = df.iloc[:, 0].value_counts().sort_index()
    resultado = list(conteo.items())
    return resultado

def main():
    pregunta_02()

if __name__ == "__main__":
    main()