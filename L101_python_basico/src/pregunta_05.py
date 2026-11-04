from pathlib import Path
import pandas as pd

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)
    value = df.groupby(0)[1].agg(["max", "min"]).sort_index()
    print(value)
    resultado = [
        (letra, row['max'], row['min']) 
        for letra, row in value.iterrows()
    ]
    print(resultado)
    return resultado

def main():
    pregunta_05()

if __name__ == "__main__":
    main()