import urllib2
from bs4 import BeautifulSoup
import os.path as path

if path.exists('sesion.json'):
     infile = open("sesion.json","r")
     contents = infile.read()
     soup = BeautifulSoup(contents,'xml')
     titles = soup.find_all('BOLETINXML')
     for title in titles:
          print "SESION NUMERO: ", title.SESION['NUMERO']
else:
     opcion=input("ingrese 1 para obtener datos de legislatura actual y 2 para obtener informacion completa  ")

     try:  
          
          if opcion==1:
               connect = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual")
               info= connect.read()
               soupAc = BeautifulSoup(info,'xml')
               idAc = soupAc.find_all('ID')
               idNum = []
               for i in idAc:
                    idNum=(str((i.get_text())))

               print idNum
               idSesiones = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+idNum)
               soupSec = BeautifulSoup(idSesiones,'xml')
               idSec = soupSec.find_all('ID')     #id legislatura
               idNumSec = []
               for i in idSec:
                    idNumSec.append(str((i.get_text())))
               print idNumSec
               basura = '<?xml version="1.0" encoding="utf-8"?>'
               delete_list = ["<br>", "</br>"]
               for i in idNumSec:
                    print "hola: ",i
                    idBoletin = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+i)
                    var= idBoletin.read()
                    if (var != basura):
                         sesion = open('sesion.json','w')
                         sesion.write(var)
                         sesion.close
                         print var
               

          if opcion==2:
               connect = urllib2.urlopen('http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas')
               connect2 =  connect.read()

               soup = BeautifulSoup(connect2,'xml')
               ids = soup.find_all('ID')     #id legislatura
               id1= []                       
               for i in ids:
                    id1.append(str((i.get_text())))
               id1l= []
               for i in id1:
                    legislaturasid = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+i)
                    soup = BeautifulSoup(legislaturasid,'xml')
                    idss = soup.find_all('ID')     #id legislatura
                    for j in idss:
                         id1l.append(str((j.get_text())))
               basura = '<?xml version="1.0" encoding="utf-8"?>'
               for i in id1l:
                    sesionesid = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+i)
                    var= sesionesid.read()
                    if (var != basura):
                         sesion = open('sesion.json','w')
                         sesion.write(var)
                         sesion.close
                         print var
          if opcion!=1 or opcion!=2:
               print "opcion invalida"

     except:
          print "opcion invalida"



