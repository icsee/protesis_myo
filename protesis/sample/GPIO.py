import RPi.GPIO as GPIO # Libreria para controlar el GPIO
import time # Libreria para funciones relacionadas con el tiempo

GPIO.setmode(GPIO.BCM)# usar pines de la placa y no del procesador
GPIO.setwarnings(False)#imperdir que salgan warings
varflex=0
flex=2
ext=3
giro_iz=17
giro_de=27
abrir=22
cerrar=10
finflex=9
finext=11
fingiro_iz=5
fingiro_de=6
finabrir=13
fincerrar=19

GPIO.setup(flex,GPIO.OUT)
GPIO.setup(ext,GPIO.OUT)
GPIO.setup(giro_iz,GPIO.OUT)
GPIO.setup(giro_de,GPIO.OUT)
GPIO.setup(abrir,GPIO.OUT)
GPIO.setup(cerrar,GPIO.OUT)
GPIO.setup(finflex,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(finext,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(fingiro_iz,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(fingiro_de,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(finabrir,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(fincerrar,GPIO.IN,GPIO.PUD_UP)

GPIO.output(flex,0)
GPIO.output(ext,0)
GPIO.output(giro_iz,1)
GPIO.output(giro_de,0)
GPIO.output(abrir,0)
GPIO.output(cerrar,0)

if varflex==0:
    GPIO.output(cerrar,1)
    varflex=1;
    print(varflex)
else:
    print("no ingreso")
