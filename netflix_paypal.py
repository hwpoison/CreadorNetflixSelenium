#!/usr/bin/env Python 3.6
#Codigo by sRBill96 para netixzen.blogspot.com.ar
import os
from modulos.seleniumFork import SFork
from modulos.generador_datos import Generador_datos
from modulos.generador_tarjetas import Generar_tarjeta

class NetflixBot():
	def __init__(self):
		self.elementos_netflix = {
			#Nombres de elementos y alternativos (debido a la dinamica de la pagina en cada carga)
			"email":["email"],
			"password":["password"],
			"continue":["btn-submit","continue","btn continue btn-blue btn-large","btn","btn-blue"],
			"tarjeta":["container","paymentExpandoHd"],
			#tarjetadatos
			"firstName":["firstName"],
			"lastName":["lastName"],
			"expiration":["creditExpirationMonth","id_creditExpirationMonth"],
			"creditCardNumber":["creditCardNumber"],
			"creditZipcode":["creditZipcode"],
			"creditCardSecurityCode":["creditCardSecurityCode"],
			#PAYPAL
			"paypalCrearBoton":["signupBtn", "createAccount"],
			"paypalTarjeta":["cardNumber", "cc"],
			"paypalVencimiento":["expiry_value"],
			"paypalCodigoSeg":["cvv"],
			"paypalNombre":["firstName"],
			"paypalApellido":["lastName"],
			"paypalTelefono":["telephone"],
			"paypalDomicilio":["billingLine1"],
			"paypalCiudad":["billingCity"],
			"paypalPostal":["billingPostalCode"],
			"paypalEmail":["email"],
			"paypalPass":["password"],
			"paypalCPass":["confirmPassword"],
			
			}
		#Url comunes de la pagina y registro
		self.url_paypal = {
			"usa":{
				"home":"https://www.paypal.com/myaccount/home",
				"registro":"https://www.paypal.com/us/signup/account?Z3JncnB0=",
				"formulario_registro":"https://www.paypal.com/signup/create",
				"aniadir_tarjeta":"https://www.paypal.com/signup/addCard",
				"promocion":"https://www.paypal.com/signup/promoteCredit",
				"success":"https://www.paypal.com/signup/success"
			},
			"ca":{
				"home":"https://www.paypal.com/myaccount/home",
				"registro":"https://www.paypal.com/ca/signup/account?Z3JncnB0=",
				"formulario_registro":"https://www.paypal.com/signup/create?Z3JncnB0=",
				"aniadir_tarjeta":"https://www.paypal.com/signup/addCard",
				"promocion":"https://www.paypal.com/signup/promoteCredit",
				"success":"https://www.paypal.com/signup/success"
			}
		}
		self.datosUsuario = {}
	def crear_cuenta(self, datos):	
		nv = SFork()
		nv.IniciarDriver()
		nv.elementos = self.elementos_netflix
		
		self.datosUsuario = Generador_datos(datos).datos
		
		
		netflix = {
			"loginNetflix":"https://www.netflix.com/ar/login",
			"suscribirse":"https://www.netflix.com/signup?action=startAction",
			"regPaypal":"https://www.paypal.com/ca/signup/account",
			"tarjeta":"https://www.netflix.com/signup/creditoption",
		}
		
		nv.Ir(netflix["suscribirse"])
	
		
		
		loginNetflix = {	"email":self.datosUsuario["email"],
							"password":self.datosUsuario["passw"]
		}
		
		loginPaypal  = {
							"email":self.datosUsuario["email"],
							"password":self.datosUsuario["passw"]
		}
		
		registroRapidoPaypal = {
							"paypalTarjeta":self.datosUsuario["tarjeta"]["numero"],
							"paypalVencimiento":self.datosUsuario["tarjeta"]["fecha"]["fecha_acortada"],
							"paypalCodigoSeg":self.datosUsuario["tarjeta"]["codigo_seg"],
							"paypalNombre":self.datosUsuario["firtsName"],
							"paypalApellido":self.datosUsuario["lastName"],
							"paypalTelefono":self.datosUsuario["phoneNumber"],
							"paypalDomicilio":self.datosUsuario["address"],
							"paypalCiudad":self.datosUsuario["city"],
							"paypalPostal":self.datosUsuario["postalCode"],
							"paypalEmail":self.datosUsuario["email"],
							"paypalPass":self.datosUsuario["passw"],
							"paypalCPass":self.datosUsuario["passw"]
		}
		
		#Pagina de creacion cuenta netflix 
		print("Clickeando boton 1")
		nv.ClickearObjeto(".submitBtnContainer", "https://www.netflix.com/signup?action=startAction")
		nv.ClickearObjeto(".submitBtnContainer", "https://www.netflix.com/signup/planform")
		nv.ClickearObjeto(".submitBtnContainer", "https://www.netflix.com/signup/registration")
		nv.completarFormulario(loginNetflix)
		nv.ClickearObjeto(".submitBtnContainer", "https://www.netflix.com/signup/regform")
		
		while(True):
			metodo = input("1)registroPaypalRapido 2)binDirecto:")
			if(metodo == "1"):
				nv.ClickearObjeto("#paypalDisplayStringId","https://www.netflix.com/signup/payment")
				#Login en pagina de Paypal
				print("Entrando a pagina de login de Paypal")
				#nv.completarFormulario(loginPaypal)
				nv.Clickear(nv.Buscar("paypalCrearBoton"))
				nv.Esperar(5)
				input(">PRESIONAR TECLA PARA CONTINUAR CON EL RELLENO DE FORMULARIO EN PAYPAL")
				nv.completarFormulario(registroRapidoPaypal)
			elif(metodo == "2"):
				self.datosUsuario = Generador_datos(datos).datos
				binDirecto = {
								"firstName":self.datosUsuario["firtsName"],
								"lastName":self.datosUsuario["lastName"],
								"creditCardNumber":self.datosUsuario["tarjeta"]["numero"],
								"creditExpirationMonth":self.datosUsuario["tarjeta"]["fecha"]["fecha_acortada"],
								"creditCardSecurityCode":self.datosUsuario["tarjeta"]["codigo_seg"]	,
								"creditZipcode":self.datosUsuario["postalCode"],
				}
				nv.Ir(netflix["tarjeta"])
				nv.completarFormulario(binDirecto)
				nv.Enter()
			else:
				print("No se selecciono ninguna opcion")
		
		
		
		#Consola de depuracion
		while(1):
			comand = input("#$")
			try:
				eval(comand)
			except:
				print("Error al ejecutar comando")
		nv.Enter()
		
		
		#numeroNuevo = Generar_tarjeta(datos["BIN"],6,True).dic_tarjetas[0]["numero"]
		#print(numeroNuevo)
		
		input(">")
	
			
#Plantilla de datos para generar			
datos = {
		"BIN":			"405037110401x1x1",
		"address":		"Street aveneu xxxx",
		"city":			"New york ",
		"postalCode":	"10001",
		"phoneNumber":	"615xxxxxxx",
		"passw":		"netflicxxxx",
		"state":		"NY",
		"paypal_loc":	"us"
}

#Inicio de creacion
botCrear = NetflixBot().crear_cuenta(datos)



