# -*- coding: utf-8 -*-
#Autor: Francisco Giacomozzi
import os
import sys
from bs4 import BeautifulSoup as BS
import requests



def getSesiones(_id):
    sesiones = []
    Url_Sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=" + str(_id)
    r = requests.get(Url_Sesion)
    data = r.text
    soup = BS(data, 'xml')
    ses = soup.find_all("Sesion")
    for i in ses:
        _id = i.ID.text.encode('utf-8')
        Fecha = i.Fecha.text.encode('utf-8')
        tipo = i.Tipo.text.encode('utf-8')
        estado = i.Estado.text.encode('utf-8')
        sesiones.append(Fecha)
        sesiones.append(tipo)
        sesiones.append(estado)
    print(sesiones)
    return sesiones

getSesiones(10)
