import functions as f
MSG_NIF="Introdueix el NIF: "
MSG_HORA="Hora:"
MSG_MOTIU="Motiu:"
DADES="DADES: "
MSG1="1.Mostrar les reserves del dia actual"
MSG2="2.Exportar les dades de la taula de reserves en fitxer csv"
MSG3="3.Mostrar totes les dades del fitxer csv de reserves en format taula"
MSG4="4.Mostrar el beneficis esperats del dia"
MSG5="Indica que vols fer: "

#printar el menu i demana al usuari que vol fer.
def menu():
    print(MSG1)
    print(MSG2)
    print(MSG3)
    print(MSG4)
    num=int(input(MSG5))
    return num

def date():
    print("Data ==> ")
    any=int(input("any: "))
    mes=int(input("Mes:"))
    while mes<1 or mes>12:
        print("T'has equivocat al introduir el mes. Torna a itroduir-lo.")
        mes = int(input("Mes:"))
    dia=int(input("dia : "))
    if mes==2:
        while dia<1 or dia>28:
            print("Dia incorrecte. Torna a introduir-lo.")
            dia = int(input("dia : "))
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        while dia<1 or dia>31:
            print("No es correcte, torna a introduir-lo.")
            dia = int(input("dia : "))
    else:
        while dia<1 or dia>30:
            print("No es correcte, torna a introduir-lo.")
            dia = int(input("dia : "))
    return dia, mes,any

