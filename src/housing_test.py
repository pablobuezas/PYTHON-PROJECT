from housing import *

def test_lee_ficheros(fichero):
    print("test_lee_ficheros", +"="*25)
    LISTA_TUPLAS = (lee_fichero(fichero))
    print("Leídos", len(LISTA_TUPLAS), "registros.")
    print("Los primeros tres registros son", LISTA_TUPLAS[:3])
    print("Los últimos tres registros son:", LISTA_TUPLAS[-3:])
    