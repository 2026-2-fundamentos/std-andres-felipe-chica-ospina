from pathlib import Path
import pandas as pd

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)
    conteo = list(df.iloc[:, 2].str[5:7].value_counts().sort_index().items())
    print(conteo)
    return conteo

def main():
    pregunta_04()

if __name__ == "__main__":
    main()
