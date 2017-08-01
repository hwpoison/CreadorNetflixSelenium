#!/usr/bin/env Python 3.6
#Codigo by sRBill96 para netixzen.blogspot.com.ar
import os
import json
import random
import sqlite3
from generador_tarjetas import Generar_tarjeta

class Generador_datos():
	def __init__(self,DATOS):
		self.datos = {
				"BIN":			"xxxxxxxxxxxxxx",
				"firtsName":	None,
				"lastName":		None,
				"address":		None,
				"city":			None,
				"postalCode":	None,
				"phoneNumber":	None,
				"email":		None,
				"passw":		None,
				"state":		None,
				"tarjeta":		None,
				"ocupacion":	None,
				"paypal_loc":	None
		}
		for d in DATOS:
			if(d in self.datos):
				self.datos[d] = DATOS[d]
		self.generar_datos()
	
	def remplazar_x(self, dic):
		nueva = ""
		for i in dic:
			if(i == "x"):
				nueva += str(random.randint(0,9))
			else:
				nueva +=i
		return nueva
	
	def generar_datos(self):
		p = self.persona_azar()
		#Generar primer nombre
		if self.datos["firtsName"] == None:
			self.datos["firtsName"] = p[1]
			
		#Generar segundo nombre
		if self.datos["lastName"]  == None:
			self.datos["lastName"]  = p[2]
		
		#Generar direccion calle
		if self.datos["address"]  == None:
			self.datos["address"]  = p[3]
		else:
			self.datos["address"] = self.remplazar_x(self.datos["address"])
		#Generar ciudad				
		if self.datos["city"] == None:
			self.datos["city"] =	 p[6]
		#Generar codigo postal
		if self.datos["postalCode"] == None:
			self.datos["postalCode"] = p[8]
		#Generar numero telefono
		if self.datos["phoneNumber"] == None:
			self.datos["phoneNumber"] = p[5]
		else:
			self.datos["phoneNumber"] = self.remplazar_x(self.datos["phoneNumber"])
		#Generar email
		if self.datos["email"] == None:
			arroba = p[9].index("@")
			self.datos["email"] = p[9][:arroba] + str(random.randint(0,1990)) +  "@gmail.com"
		#Generar contraseña
		if self.datos["passw"] == None:
			self.datos["passw"] = "holasoyun"+str(random.randint(100,300))
		else:
			self.datos["passw"] = self.remplazar_x(self.datos["passw"])
		#Generar estado
		if self.datos["state"] == None:
			self.datos["state"] = "NY"
		#Generar datos tarjeta
		self.datos["tarjeta"] = Generar_tarjeta(self.datos["BIN"],1).dic_tarjetas[0]
		
		print("Datos generado:")
		for i in self.datos:
			print(i,":",self.datos[i])
		print("===============")
		
	def sql_a_sqlite(self, sql, sqlite):
		"""Para convertir un sql de fakenamegenerator
		del siguiente orden
		CREATE TABLE fakenames (
			  number INTEGER PRIMARY KEY AUTOINCREMENT,
			  givenname varchar(20) NOT NULL,
			  surname varchar(23) NOT NULL,
			  streetaddress varchar(100) NOT NULL,
			  telephonecountrycode integer NOT NULL,
			  telephonenumber varchar(25) NOT NULL,
			  city varchar(100) NOT NULL,
			  gender varchar(6) NOT NULL,
			  zipcode varchar(15) NOT NULL,
			  emailaddress varchar(100) NOT NULL,
			  birthday varchar(10) NOT NULL
		);
		"""
		print("Convirtiendo..")
		db = sqlite3.connect(sqlite)
		cursor = db.cursor()
		try:
			sql = str(open(sql,"r").read())[3:]
		except:
			print("Error con el fichero sql..")
		cursor.executescript(sql)
		db.commit()
		print("Listo..")
		
	def persona_azar(self):
		db = sqlite3.connect("datos_gente.db")
		cur = db.cursor()
		numero_azar = random.randint(1,32979)
		encontrado = False
		while(encontrado == False):
			for e in cur.execute("SELECT * FROM fakenames where number='%s'"%(numero_azar)):
				if(e):
					encontrado = True
			numero_azar+=1
		return e

