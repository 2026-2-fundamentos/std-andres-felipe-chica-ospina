import re

import pandas as pd


def pregunta_01():
    """
    El archivo `data/clusters_report.txt` es un reporte de clústeres de
    palabras clave pensado para ser leído por una persona, no por un programa:
    los encabezados ocupan varias líneas, las columnas están alineadas con
    espacios y la lista de palabras clave de un clúster continúa en las líneas
    siguientes.

    Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
    por clúster y las columnas:

    - `cluster`: número del clúster, como entero.
    - `cantidad_de_palabras_clave`: como entero.
    - `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
      texto `15,9 %` debe quedar como `15.9`.
    - `principales_palabras_clave`: todas las palabras clave del clúster en un
      solo texto, separadas por una coma y un único espacio.

    Retorne el DataFrame.

    Ejemplo del formato de la respuesta (se omite la última columna):

           cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
        0        1                         105                          15.9
        1        2                         102                          15.4
        ...
    """

    with open("data/clusters_report.txt", encoding="utf-8") as file:
        lines = file.readlines()[4:]  # se saltan los encabezados

    # Una línea nueva de clúster: número, cantidad, porcentaje con coma y "%"
    pattern = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d+,\d+)\s*%\s*(.*)$")

    clusters = []
    cantidades = []
    porcentajes = []
    palabras_clave = []

    for line in lines:
        match = pattern.match(line)

        if match:
            cluster, cantidad, porcentaje, texto = match.groups()
            clusters.append(int(cluster))
            cantidades.append(int(cantidad))
            porcentajes.append(float(porcentaje.replace(",", ".")))
            palabras_clave.append(texto.strip())
        elif line.strip() and palabras_clave:
            # línea de continuación: pertenece al último clúster leído
            palabras_clave[-1] += " " + line.strip()

    # Limpieza: espacios únicos, sin punto final, coma + un solo espacio
    palabras_clave = [
        re.sub(r"\s*,\s*", ", ", " ".join(texto.split())).rstrip(".")
        for texto in palabras_clave
    ]

    return pd.DataFrame(
        {
            "cluster": clusters,
            "cantidad_de_palabras_clave": cantidades,
            "porcentaje_de_palabras_clave": porcentajes,
            "principales_palabras_clave": palabras_clave,
        }
    )