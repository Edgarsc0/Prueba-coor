'''
import matplotlib.pyplot as m
import MySQLdb as sql
miConexion = sql.connect( host='localhost', user= 'root', passwd='n0m3l0', db='simap')
cur = miConexion.cursor()
cur.execute( "SELECT cor_lat,cor_lon,cor_alt FROM coordenadas" )
longitud=[]
latitud=[]
altitud=[]
for cor_lat,cor_lon,cor_alt in cur.fetchall() :
    longitud.append(cor_lon)
    latitud.append(cor_lat)
    altitud.append(cor_alt)
print(longitud)
print(latitud)
m.plot(longitud,latitud,"o")
m.show()
miConexion.close()
'''

import matplotlib.pyplot as m
import MySQLdb as sql
consultar_usu=sql.connect(host='localhost',user= 'root', passwd='Hal02012()', db='simap')
cur=consultar_usu.cursor()
print("INTRODUZCA SU USUARIO")
usuario=input()
print("INTRODUZCA SU PASSWORD")
psw=input()
cur.execute("select * from usuario")
usu=[]
usu_psw=[]
for u,p in cur.fetchall():
    usu.append(u)
    usu_psw.append(p)
if usuario in usu and psw in usu_psw:
    consultar_usu.close()
    print("logeo exitante")
    consultar_ruta=sql.connect( host='localhost', user= 'root', passwd='Hal02012()', db='simap')
    cur = consultar_ruta.cursor()
    cur.execute( "select cor_lat,cor_lon,cor_alt from coordenadas where id_ruta=1" )
    longitud=[]
    latitud=[]
    altitud=[]
    for cor_lat,cor_lon,cor_alt in cur.fetchall() :
        longitud.append(cor_lon)
        latitud.append(cor_lat)
        altitud.append(cor_alt)
    print(longitud)
    print(latitud)
    m.plot(longitud,latitud,"o")
    m.show()
    consultar_ruta.close()
else:
    print("algo fallo")
