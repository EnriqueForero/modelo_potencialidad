import pandas as pd
import numpy as np
import re
import os
path = os.getcwd()


# BASE PRODUCTOS POTENCIALES
base2 = pd.read_csv("{}/files3/Base prod potenciales.txt".format(path),
                    sep="|", encoding="utf-8", dtype={"Pais": str, "Posición": str, 'Descripcion': str})


# Types
dtype2 = {
    "Exportaciones Colombianas en 2020 (miles USD)": int,
    "Valor Importaciones 2020 (miles USD)": int,
    "Exportaciones promedio 2016-2020 (miles USD)": int,
    "Importaciones promedio 2016-2020 (miles USD)": int,
    "Diferencia Promedio exportaciones 2016-2020 (miles USD)": int,
    "Diferencia Promedio importaciones 2016-2020 (miles USD)": int}

base2 = base2.astype(dtype2)


filt = base2[["Cadena", "Subsector"]].groupby(
    ["Cadena", "Subsector"]).sum().reset_index("Cadena")

final_dict = {}

for cadena in filt["Cadena"].unique():
    final_dict[cadena] = filt[filt["Cadena"] == cadena].index.to_list()


print(final_dict)
