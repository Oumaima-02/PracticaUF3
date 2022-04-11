import csv
import pandas as pd
DECO="................."
TITOL="|    RESERVES    |"

def mostrar_csv(csv):
#printar el titol.
    print(DECO)
    print(TITOL)
    print(DECO)

    df = pd.read_csv(csv)
    print(df)


