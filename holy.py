#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import os.path as path
import nltk
from nltk.corpus import stopwords
from unidecode import unidecode
import re
#from pymongo import *

connect = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual")
#connect = urllib2.urlopen('http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas')

info= connect.read()
soupAc = BeautifulSoup(info,'xml')
idAc = soupAc.find_all('ID')
idNum = []
for i in idAc:
     idNum=(str((i.get_text())))        #Id legislatura actual

print idNum
idSesiones = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+idNum)
soupSec = BeautifulSoup(idSesiones,'xml')
idSec = soupSec.find_all('ID')     
idNumSec = []
for i in idSec:
     idNumSec.append(str((i.get_text())))    #Id sesiones 
print idNumSec
basura = '<?xml version="1.0" encoding="utf-8"?>'
idProyLey = []
for i in idNumSec:
     idBoletin = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+i)
     var= idBoletin.read()
     if (var != basura):
          soupBol = BeautifulSoup(var,'xml')
          text = soupBol.get_text(strip=True)
          text= unidecode(text)         #boletin en ascii sin tags
          for proy in soupBol.find_all('PROYECTO_LEY'):
               idProyLey.append(str((proy.get('BOLETIN'))))
idProyLey2= []
for i in idProyLey:
     i = i.replace('y',',')
     i = i.replace('Y',',')
     i = i.replace('.','') 
     cadena = i.replace(" ","")
     element = cadena.split(',')
     for j in element:
          if j!="":
               idProyLey2.append(str(j))
          else:
               pass
print idProyLey2

idVotacion = []
for i in idProyLey2:
     proyecto = urllib2.urlopen("http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarProyectoLey?prmNumeroBoletin="+i)
     soupProy = BeautifulSoup(proyecto,'xml')
     for vol in soupProy.select('VotacionProyectoLey > Id'):
          idVotacion.append(str((vol.get_text())))

print idVotacion

for i in idVotacion:
     votos = urllib2.urlopen("http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle?prmVotacionId="+i)
     info = votos.read()
     print info
##          tokens = [t for t in text.split()]
##          clean_tokens = tokens[:] 
##          sr = stopwords.words('spanish')
##          for token in tokens:
##              if token in stopwords.words('spanish'):
##                  clean_tokens.remove(token)
##          freq = nltk.FreqDist(clean_tokens)
##          for key,val in freq.items():
##               key= key.encode('utf-8')
##               #print (str(key) + ':' + str(val))
##          print i
    # break
##print "listo"

               






