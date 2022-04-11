import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import functions as f
connection_args = {
    'host': 'mysql-oumaima.alwaysdata.net',
    'user': 'oumaima',
    'password': 'oumamvm15'
}

#funcio per crear la taula.
def create_table():
    # afegim al dictionary a quina bbdd volem accedir
    connection_args.update({'database': 'oumaima_db'})
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        #sentencia per crear la taula
        table = (
            "CREATE TABLE IF NOT EXISTS `oumaima_db`.`reserves` ("
            "`nif` VARCHAR(9) NOT NULL,"
            "`data` DATE NULL,"
            "`hora` TIME NULL,"
            "`motiu` VARCHAR(45) NULL,"
            "`datares` BIGINT(6) NULL,"
            "PRIMARY KEY (`nif`)"")ENGINE=InnoDB ")
        crs = cnx.cursor()
        crs.execute(table)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()



#Inserir les dades que hi ha a la taula.

def insert_data():
    try:
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("INSERT INTO reserves "
               "(NIF, Data, Hora, Motiu) "
               "VALUES (%s, %s, %s, %s, %s)")
        nif = input(MSG_NIF)
        dia, mes, any = f.date()
        hora = (input(MSG_HORA))
        motiu = input(MSG_MOTIU)
        data=('null', nif,(f'{dia}/{mes}/{any}'), hora, motiu)
        # creem el cursor, executem la sentència (passant la tupla també) i fem commit
        crs = cnx.cursor()
        crs.execute(sql, data)
        cnx.commit()
        # mostra per pantalla quants registres s'han inserit
        print(crs.rowcount, "registres inserits.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()






def mostrar_reserves():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("SELECT * FROM reserves")
        # creem el cursor, executem la sentència i fem fetchall (per obtenir tots els registres)
        crs = cnx.cursor()
        crs.execute(sql)
        result = crs.fetchall()
        # mostra tots els resultats
        for x in result:
            print(x)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()


#Exportar les dades a un fitxer csv.

def guardar_csv():
    try:

        cnx = mysql.connector.connect(**connection_args)
        # exportar sql a un fitxercsv

        sql = pd.read_sql ("SELECT * FROM reserves", cnx)
        sql.to_csv(r'files/fitxer.csv', index=False)
        crs = cnx.cursor()
        crs.execute(sql)
        result = crs.fetchall()
        # mostra tots els resultats
        for x in result:
            print(x)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()
