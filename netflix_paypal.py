#!/usr/bin/env Python 3.6
#Codigo by sRBill96 para netixzen.blogspot.com.ar
import os
from seleniumFork import SFork
from generador_datos import Generador_datos
from generador_tarjetas import Generar_tarjeta

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

	def crear_cuenta(self):	
		nv = SFork()
		nv.IniciarDriver()
		nv.elementos = self.elementos_netflix
		DU = Generador_datos(datos).datos
		paginas = {
			"loginNetflix":"https://www.netflix.com/ar/login",
			"suscribirse":"https://www.netflix.com/signup?action=startAction",
			"regPaypal":"https://www.paypal.com/ca/signup/account",
		}
		
		nv.Ir(paginas["suscribirse"])

		
		loginNetflix = {	"email":DU["email"],
							"password":DU["passw"]
		}
		
		loginPaypal  = {
							"email":DU["email"],
							"password":DU["passw"]
		}
		
		registroRapidoPaypal = {
							"paypalTarjeta":DU["tarjeta"]["numero"],
							"paypalVencimiento":DU["tarjeta"]["fecha"]["fecha_acortada"],
							"paypalCodigoSeg":DU["tarjeta"]["codigo_seg"],
							"paypalNombre":DU["firtsName"],
							"paypalApellido":DU["lastName"],
							"paypalTelefono":DU["phoneNumber"],
							"paypalDomicilio":DU["address"],
							"paypalCiudad":DU["city"],
							"paypalPostal":DU["postalCode"],
							"paypalEmail":DU["email"],
							"paypalPass":DU["passw"],
							"paypalCPass":DU["passw"]
		}
		
		
		
		#Pagina de creacion cuenta netflix 
		print("Clickeando boton 1")
		print(nv.driver.current_url)
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
				DU = Generador_datos(datos).datos
				binDirecto = {
								"firstName":DU["firtsName"],
								"lastName":DU["lastName"],
								"creditCardNumber":DU["tarjeta"]["numero"],
								"creditExpirationMonth":DU["tarjeta"]["fecha"]["fecha_acortada"],
								"creditCardSecurityCode":DU["tarjeta"]["codigo_seg"]	,
								"creditZipcode":DU["postalCode"],
				}
				nv.ClickearObjeto("#creditOrDebitCardDisplayStringId","https://www.netflix.com/signup/payment")
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
	
			
			
datos = {
		"BIN":			"425032xx89x1xxx3",
		"address":		"Street aveneu xxxx",
		"city":			"New york ",
		"postalCode":	"10001",
		"phoneNumber":	"615xxxxxxx",
		"passw":		"netflicxxxx",
		"state":		"NY",
		"paypal_loc":	"us"
}


a = NetflixBot().crear_cuenta()
