from pathlib import Path
import pandas as pd
import collections

PROJECT_FILE = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_FILE / "data" / "data.csv.gz"

def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None)
    
    metrics_dict = collections.defaultdict(list)
    
    for cell in df.iloc[:, 4]:

        pairs = str(cell).split(",")
        for pair in pairs:
            key, val = pair.split(":")
            metrics_dict[key].append(int(val))
            
    resultado = []
    for key in sorted(metrics_dict.keys()):
        min_val = min(metrics_dict[key])
        max_val = max(metrics_dict[key])
        resultado.append((key, min_val, max_val))
        
    return resultado

def main():
    print(pregunta_06())

if __name__ == "__main__":
    main()
