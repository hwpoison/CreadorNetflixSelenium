#!/usr/bin/env Python 3.6
#Codigo by sRBill96 para netixzen.blogspot.com.ar
import sys
import math
import json
import random
import datetime

class Generar_tarjeta():
	def __init__(self,BIN, cantidad=1, solo_impresion=False):
		self.BIN = BIN.replace(" ","")
		if(len(self.BIN) > 16 or len(self.BIN) < 15):
			print("Por favor revisa la longitud del BIN.")
		else:
			print("Generando numero de tarjeta..")
			self.RANGO_GEN = 1000
			self.CANTIDAD_TARJETAS = cantidad
			self.lista_tarjetas = []
			self.dic_tarjetas = {}
			self.lista_tipos_de_tarjetas = self.lista_tipos_tarjetas()
			if self.CANTIDAD_TARJETAS >= 1:
				for i in range(0, self.CANTIDAD_TARJETAS):
					tarj_creada = self.crear_tarjeta()
					self.lista_tarjetas.append(tarj_creada["datos_completos"])
					self.dic_tarjetas[i] = {
							"numero":tarj_creada["numero_tarjeta"],
							"codigo_seg":tarj_creada["codigo_seg"],
							"tipo_tarjeta":tarj_creada["tipo_tarjeta"],
							"fecha":tarj_creada["venc"],
							"dato_completo":tarj_creada["datos_completos"]
					}
			else:
					self.crear_tarjeta()
			if solo_impresion:#solo impresion
				for n in self.lista_tarjetas:
					print(n)
	
	def lista_tipos_tarjetas(self):
		tipos_tarjetas_ = {"rnd":"Random Card Issuer",
			"rnd_v-mc":"Random Card Network (Visa / MasterCard only)",
			"3710 xxxx xxxx xxxx":"American Express Company, USA (Green)",
			"3712 xxxx xxxx xxxx":"American Express Company, USA (Green)",
			"3728 xxxx xxxx xxxx":"American Express Company, USA (Gold)",
			"3703 70xx xxxx xxxx":"American Express Company, USA (Platinum)",
			"3703 71xx xxxx xxxx":"American Express Company, USA (Platinum)",
			"3738 xxxx xxxx xxxx":"American Express Company, USA (Corporate Card)",
			"3702 46xx xxxx xxxx":"American Express - Industrial And Commercial Bank Of China, China",
			"3702 47xx xxxx xxxx":"American Express - Industrial And Commercial Bank Of China, China",
			"4003 91xx xxxx xxxx":"Visa - First United Bank, USA (Debit, Classic)",
			"4003 93xx xxxx xxxx":"Visa - Capital One Bank, USA (Classic)",
			"4223 99xx xxxx xxxx":"Visa - Chase Manhattan Bank USA, USA (Debit, Classic)",
			"4030 73xx xxxx xxxx":"Visa - Chase Manhattan Bank USA, USA (Platinum)",
			"4113 55xx xxxx xxxx":"Visa - Chase Manhattan Bank USA, USA (Platinum)",
			"4343 51xx xxxx xxxx":"Visa - HSBC Bank Nevada, USA (Classic)",
			"4343 85xx xxxx xxxx":"Visa - HSBC Bank Nevada, USA (Gold)",
			"4000 52xx xxxx xxxx":"Visa - The Connecticut Bank And Trust Company, USA (Debit, Classic)",
			"4265 10xx xxxx xxxx":"Visa - Barclays Bank Plc, UK (Classic)",
			"4265 03xx xxxx xxxx":"Visa - Barclays Bank Plc, UK (Gold)",
			"4265 04xx xxxx xxxx":"Visa - Barclays Bank Plc, UK (Platinum)",
			"4112 98xx xxxx xxxx":"Visa - Lloyds Tsb Bank Plc, UK (Classic)",
			"4479 65xx xxxx xxxx":"Visa - Citibank International Plc, UK (Business)",
			"4067 42xx xxxx xxxx":"Visa - Bank Of Valletta Plc, Malta (Debit, Classic)",
			"4233 85xx xxxx xxxx":"Visa - First International Bank Ltd., Malta (Gold)",
			"4188 75xx xxxx xxxx":"Visa - Bank Of Valletta Plc, Malta (Platinum)",
			"4137 73xx xxxx xxxx":"Visa - Topcard Service S.A., Switzerland (Classic)",
			"4133 91xx xxxx xxxx":"Visa - Ubs Ag (Union Bank Of Switzerland), Switzerland (Gold)",
			"4133 92xx xxxx xxxx":"Visa - Ubs Ag (Union Bank Of Switzerland), Switzerland (Business)",
			"4001 31xx xxxx xxxx":"Visa - Barclays Bank Plc, Portugal (Debit, Electron)",
			"4001 02xx xxxx xxxx":"Visa - Banco Do Brasil S.A., Brazil (Debit, Electron)",
			"4001 36xx xxxx xxxx":"Visa - Banco Do Brasil S.A., Brazil (Debit, Electron)",
			"4009 58xx xxxx xxxx":"Visa - Caixa Economica Federal, Brazil (Classic)",
			"4009 59xx xxxx xxxx":"Visa - Caixa Economica Federal, Brazil (Gold)",
			"4009 60xx xxxx xxxx":"Visa - Caixa Economica Federal, Brazil (Business)",
			"4002 13xx xxxx xxxx":"Visa - The Hongkong And Shanghai Banking Corporation Ltd., Brunei (Classic)",
			"4002 14xx xxxx xxxx":"Visa - The Hongkong And Shanghai Banking Corporation Ltd., Brunei (Gold)",
			"4002 59xx xxxx xxxx":"Visa - Banco Sudameris Argentina S.A., Argentina (Classic)",
			"4357 31xx xxxx xxxx":"Visa - HSBC Bank Argentina S.A., Argentina (Classic)",
			"4357 52xx xxxx xxxx":"Visa - Banco Velox S.A., Argentina (Classic)",
			"4357 53xx xxxx xxxx":"Visa - Banco Velox S.A., Argentina (Gold)",
			"4002 62xx xxxx xxxx":"Visa - Coop Bank Ab, Sweden (Classic)",
			"4003 31xx xxxx xxxx":"Visa - Sanpaolo Imi S.P.A., Italy (Debit, Electron)",
			"4003 15xx xxxx xxxx":"Visa - Banca Monte Dei Paschi Di Siena S.P.A., Italy (Electron)",
			"4003 29xx xxxx xxxx":"Visa - Banca Nazionale Del Lavoro, Italy (Classic)",
			"4003 59xx xxxx xxxx":"Visa - Taiwan Shin Kong Commercial Bank, Taiwan (Infinite)",
			"4003 61xx xxxx xxxx":"Visa - Chinatrust Commercial Bank, Taiwan (Infinite)",
			"4003 63xx xxxx xxxx":"Visa - Banco Nacional Ultramarino, S.A., Macau (Platinum)",
			"4017 80xx xxxx xxxx":"Visa - Banco Cooperativo Espanol S.A., Spain (Debit, Electron)",
			"4020 40xx xxxx xxxx":"Visa - Caja De Ahorros Y Pensiones De Barcelona (La Caixa), Spain (Debit, Electron)",
			"4035 69xx xxxx xxxx":"Visa - Banco Bilbao Vizcaya Argentaria S.A. (BBVA), Spain (Debit, Electron)",
			"4035 67xx xxxx xxxx":"Visa - Banco Bilbao Vizcaya Argentaria S.A. (BBVA), Spain (Classic)",
			"4035 68xx xxxx xxxx":"Visa - Banco Bilbao Vizcaya Argentaria S.A. (BBVA), Spain (Classic)",
			"4036 42xx xxxx xxxx":"Visa - Banco Bilbao Vizcaya Argentaria S.A. (BBVA), Spain (Platinum)",
			"4343 87xx xxxx xxxx":"Visa - Iberia Cards, Spain (Business)",
			"4539 71xx xxxx xxxx":"Visa - Citibank, Philippines (Classic)",
			"4539 72xx xxxx xxxx":"Visa - Citibank, Philippines (Gold)",
			"4036 49xx xxxx xxxx":"Visa - Deutscher Sparkassen- Und Giroverband, Germany (Debit, Classic)",
			"4036 50xx xxxx xxxx":"Visa - Deutscher Sparkassen- Und Giroverband, Germany (Debit, Gold)",
			"4035 79xx xxxx xxxx":"Visa - HSBC France, France (Debit, Classic)",
			"4561 22xx xxxx xxxx":"Visa - HSBC France, France (Gold)",
			"4150 56xx xxxx xxxx":"Visa - Societe Generale, France (Classic)",
			"4971 19xx xxxx xxxx":"Visa - BNP Paribas, France (Classic)",
			"4561 23xx xxxx xxxx":"Visa - BNP Paribas, France (Gold)",
			"4101 01xx xxxx xxxx":"Visa - Barclays Bank Egypt Sae, Egypt (Debit, Electron)",
			"4214 02xx xxxx xxxx":"Visa - Citizens Bank Of Canada, Canada (Debit, Classic)",
			"4257 02xx xxxx xxxx":"Visa - Banque Laurentienne Du Canada, Canada (Corporate)",
			"4257 03xx xxxx xxxx":"Visa - Absa Group Ltd., South Africa (Corporate)",
			"4101 00xx xxxx xxxx":"Visa - Wells Fargo Bank, USA (Classic)",
			"4113 40xx xxxx xxxx":"Visa - Wells Fargo Bank, USA (Debit, Classic)",
			"4023 80xx xxxx xxxx":"Visa - Barclays Bank Plc, Gibraltar (Debit, Electron)",
			"4050 68xx xxxx xxxx":"Visa - Barclays Bank Plc, Switzerland (Classic)",
			"4010 00xx xxxx xxxx":"Visa - Bayerische Landesbank Girozentrale, Germany (Gold)",
			"4018 49xx xxxx xxxx":"Visa - Commerzbank Ag, Germany (Debit, Classic)",
			"4667 04xx xxxx xxxx":"Visa - Icici Bank Ltd, India (Debit, Classic)",
			"4259 83xx xxxx xxxx":"Visa - Ixe Banco, S.A., Mexico (Debit, Classic)",
			"4259 84xx xxxx xxxx":"Visa - Ixe Banco, S.A., Mexico (Debit, Gold)",
			"4265 14xx xxxx xxxx":"Visa - HSBC Mexico S.A., Mexico (Electron)",
			"4265 13xx xxxx xxxx":"Visa - HSBC Mexico S.A., Mexico (Business)",
			"5404 36xx xxxx xxxx":"MasterCard - Lloyds Tsb Bank Plc., UK",
			"5404 37xx xxxx xxxx":"MasterCard - Lloyds Tsb Bank Plc., UK",
			"5177 43xx xxxx xxxx":"MasterCard - Credit Suisse, Switzerland",
			"5218 41xx xxxx xxxx":"MasterCard - Ubs Ag, Switzerland",
			"5288 77xx xxxx xxxx":"MasterCard - Banco Nacional De Mexico, S.A.",
			"5289 00xx xxxx xxxx":"MasterCard - Bank Of America, USA",
			"5314 50xx xxxx xxxx":"MasterCard - Bank Of America, USA",
			"5315 7xxx xxxx xxxx":"MasterCard - First Usa Bank, USA.",
			"5323 5xxx xxxx xxxx":"MasterCard - Chase Manhattan Bank USA, USA",
			"5369 90xx xxxx xxxx":"MasterCard - Chase Manhattan Bank USA, USA",
			"5405 10xx xxxx xxxx":"MasterCard - Wells Fargo Bank, USA",
			"5121 64xx xxxx xxxx":"MasterCard - HSBC Bank Canada, Canada",
			"5221 22xx xxxx xxxx":"MasterCard - Bank Of Montreal, Canada",
			"5122 17xx xxxx xxxx":"MasterCard - Commonwealth Bank Of Australia, Australia",
			"5324 20xx xxxx xxxx":"MasterCard - China Construction Bank, China",
			"5592 09xx xxxx xxxx":"MasterCard - Banco Nacional De Mexico, S.A., Mexico",
			"5137 4xxx xxxx xxxx":"MasterCard - Europay France Sas, France",
			"5520 71xx xxxx xxxx":"MasterCard - Banco Bilbao Vizcaya Argentaria S.A., Spain",
			"5522 00xx xxxx xxxx":"MasterCard - HSBC Bank Malta P.L.C., Malta",
			"5127 17xx xxxx xxxx":"MasterCard - National Bank Of Dubai Ltd., United Arab Emirates",
			"4xxx xxxx xxxx xxxx":"Visa",
			"5xxx xxxx xxxx xxxx":"MasterCard",
			"37xx xxxxxx xxxxx":"AmEx",
			"37x8 xxxxxx xxxxx":"AmEx Gold",
			"37x3 7xxxxx xxxxx":"AmEx Platinum",
			"3782 xxxxxx xxxxx":"AmEx - Small Corporate Card",
			"3787 xxxxxx xxxxx":"AmEx - Small Corporate Card",
			"30xxx xxxx xxxxx":"Diners Club",
			"31xxx xxxx xxxxx":"Diners Club",
			"35xxx xxxx xxxxx":"Diners Club",
			"36xxx xxxx xxxxx":"Diners Club",
			"38xxx xxxx xxxxx":"Carte Blanche",
			"35xx xxxx xxxx xxxx":"JCB (Japanese Credit Bureau)"
		}
		return tipos_tarjetas_ 
	
	def json(self):
		return json.dumps(self.dic_tarjetas)

	def crear_tarjeta(self):
		tarjeta = {}
		tarjeta["numero_tarjeta"] = self.crear_numero(self.BIN)
		tarjeta["codigo_seg"] 	  = self.generar_codigo_seguridad()
		tarjeta["tipo_tarjeta"]   = self.tipo_tarjeta(tarjeta["numero_tarjeta"])
		tarjeta["venc"]			  = self.generar_fecha_venc()
		
		self.string = ""
		self.string += tarjeta["numero_tarjeta"]
		self.string += " | " + tarjeta["codigo_seg"]
		self.string += " | " + tarjeta["venc"]["fecha_acortada"]
		self.string += " | " + tarjeta["tipo_tarjeta"]
		tarjeta["datos_completos"] = self.string
		return tarjeta
		
	def gen_aleatorio(self, BIN):
		numero = ""
		for i in BIN:
			numero+=str(random.randint(0,9)) if i.lower() == "x" else i
		return numero
		
	def checkear(self, cc): #Parametro ejemplo 4896889802135
		num = map(int, str(cc))
		return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

	def crear_numero(self, BIN):
		numero = self.gen_aleatorio(BIN)
		for i in range(1,self.RANGO_GEN):
			numero = self.gen_aleatorio(BIN)
			chk0 = self.checkear(numero)
			if(chk0 and numero):
				break
		return numero
		
	def generar_fecha_venc(self):
		fecha = {
			"anio":None,
			"mes":None,
			"fecha_completa":None,
			"fecha_acortada":None
		}
		def gen_anio():
			anio_actual = datetime.datetime.now().year
			return anio_actual  + random.randint(2,3)
		fecha["anio"] = str(gen_anio())
		def gen_mes():
			mes = random.randint(1,12)
			if(mes > 9):
				return str(mes)
			else:
				return "0"+str(mes)	
		
		fecha["mes"] = gen_mes()
		fecha["fecha_completa"] = fecha["mes"] + "/" + fecha["anio"]
		fecha["fecha_acortada"] = fecha["mes"] + "/" + fecha["anio"][2:]
		return fecha
		
	def generar_codigo_seguridad(self):
		return str(random.randint(101,998))
	
	def rellenar(self,numero):
		numero_f = numero
		for i in range(0,16-len(numero)):
			numero_f+="x"
		return numero_f
	
	def tipo_tarjeta(self, codigo):
		tipo = "desconodido"
		patron = self.rellenar(codigo[:6])
		for p_tarj in self.lista_tipos_de_tarjetas:
			for m in range(1,16):
				patron = self.rellenar(codigo[:m])
				if(patron in p_tarj.replace(" ","")):
					tipo = self.lista_tipos_de_tarjetas[p_tarj]
		return tipo
		
if __name__ == "__main__":
	argv = sys.argv
	if(len(argv) > 2):
		bin_generar = str(argv[1])
		num = Generar_tarjeta(bin_generar,int(argv[2]),True)
	else:
		print("USO:  BIN_BASE CANTIDAD")


# ~ bin_muestra = "493xxxxxxxxxxxxx"
#imprimir resultado en consola
# ~ num = Generar_tarjeta(bin_muestra,16,True)

# ~ print(num)
#omitir impresion
#num = Generar_tarjeta(bin_muestra,1)
#print()
#obtener diccionario
#diccionario = num.dic_tarjetas
#for e in diccionario:
#	print(e,diccionario[e])
#obtener un json para parsear
#json = num.json()

#obtener lista
#lista = num.lista_tarjetas






