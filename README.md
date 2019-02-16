# Creador de cuentas Netflix 
Es un automatizador para crear cuentas de netflix a traves de los metodos de pagos como paypal o bin directo.
Incluye:
-Generador de datos personales aleatorios.
-Numeros de tarjeta de creditos a base de un BIN opcional.
-Un pequeño fork de Selenium para controlar aspectos especificos de una pagina, en este caso netflix y paypal, hasta la fecha de creacion del codigo.

En si no hay que hacer mas que ejecutar el script principal con los datos configurados y ejecutarlo, tiene para soportar la intervencion manual, pero no total automatica debido a ciertas restricciones cohesionadas con la variabilidad de las interfaces, tiempos de cargas y otros detalles, lo cual hará inutilizable en un futuro o quien sabe si ahora mismo la utilidad de esta pieza.


Lo adapte para que funcione en Windows o GNU/Linux.

Requiere:
  pip3 install selenium
  Los drivers estan en la carpeta "drivers", pero si necesitan alguno acorde a su arquitectura descargue de aca y re-emplacen
  https://sites.google.com/a/chromium.org/chromedriver/downloads
