from generador_datos import Generador_datos
from paypal_driver import PaypalBot

#Datos de muestra, son opcionales y pueden ser eliminados del
#diccionario, por ejemplo si quitamos el numero de telefono o la pass, se 
#genera igual uno aleatorio por defecto
datos = {
		"BIN":			"42558104011xxxxx",
		"address":		"405x Havanna Street",
		"city":			"New York",
		"postalCode":	"10001",
		"phoneNumber":	"336364xxxx",
		"passw":		"netflixxxx",
		"state":		"NY",
		"paypal_loc":	"usa"
}


#Se generan los datos
datos = Generador_datos(datos).datos

#Se inicializa el bot
paypal_bot = PaypalBot()

#Se procede a la creacion
paypal_bot.crear_cuenta(datos)
