import  csv
import functions as fc
import csvfunctions as fcsv
import dbfunctions as db
import csv
#import pandas as pd
def main():

    # mostra el menú i demanar  que es vol fer
    num = fc.menu()
    db.create_table()
    db.insert_data()
    #realitzar les acciones del menú.
    match (num):
        case 1:
            db.mostrar_reserves()
        case 2:
            db.guardar_csv()
        case 3:
            csv.mostrar_csv('files/fitxer.csv')
        case 4:
            fc.benefici()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
