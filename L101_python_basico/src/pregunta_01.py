from pathlib import Path
import pandas as pd

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """
    PROJECT_FOLDER = Path(__file__).resolve().parents[1]
    INPUT_FILE = PROJECT_FOLDER / "data" / "data.csv.gz"
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)
    suma = df.iloc[:, 1].sum()
    return suma

def main():
    print(pregunta_01())

if __name__ == "__main__":
    main()