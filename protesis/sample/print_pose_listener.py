import sys
import RPi.GPIO as GPIO # Libreria para controlar el GPIO
import time # Libreria para funciones relacionadas con el tiempo
GPIO.setmode(GPIO.BCM)# usar pines de la placa y no del procesador
GPIO.setwarnings(False)#imperdir que salgan warings
sys.path.append('../lib/')
flex=2
ext=3
giro_iz=17
giro_de=27
abrir=22
cerrar=10
fincerrar=9
finabrir=11
fingiro_iz=5
fingiro_de=6
finext=13
finflex=19
red=16
blue=20
green=21
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
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
GPIO.output(giro_iz,0)
GPIO.output(giro_de,0)
GPIO.output(abrir,0)
GPIO.output(cerrar,0)
GPIO.output(blue,0)
GPIO.output(green,0)
GPIO.output(red,0)
varflex=1
tiempo=5
from device_listener import DeviceListener
from pose_type import PoseType

class PrintPoseListener(DeviceListener):
	def on_pose(self, pose):
	  pose_type = PoseType(pose)
	  print(pose_type.name)
	  global varflex
          if pose_type.name=="WAVE_OUT":
           if GPIO.input(fingiro_iz)==True:
              GPIO.output(giro_iz,1);
              GPIO.output(giro_de,0)
              GPIO.output(cerrar,0)
              GPIO.output(abrir,0)
              GPIO.output(flex,0)
              GPIO.output(ext,0)
              GPIO.output(blue,0)
              GPIO.output(green,1)
              GPIO.output(red,1)
           if GPIO.input(fingiro_iz)==False:
              GPIO.output(giro_iz,0);     
              GPIO.output(blue,0)
              GPIO.output(green,0)
              GPIO.output(red,1)     
          elif pose_type.name=="WAVE_IN":
           GPIO.output(giro_iz,0)
           if GPIO.input(fingiro_de)==True:
              GPIO.output(giro_de,1);
              GPIO.output(cerrar,0)
              GPIO.output(abrir,0)
              GPIO.output(flex,0)
              GPIO.output(ext,0)
              GPIO.output(blue,1)
              GPIO.output(green,0)
              GPIO.output(red,1)
           if GPIO.input(fingiro_de)==False:
              GPIO.output(giro_de,0);     
              GPIO.output(blue,0)
              GPIO.output(green,0)
              GPIO.output(red,1)
          elif pose_type.name=="FIST":
           GPIO.output(giro_iz,0)
           GPIO.output(giro_de,0)
           if GPIO.input(fincerrar)==True:
              GPIO.output(cerrar,1);
              GPIO.output(abrir,0)
              GPIO.output(flex,0)
              GPIO.output(ext,0)
              GPIO.output(blue,1)
              GPIO.output(green,1)
              GPIO.output(red,0)
           if GPIO.input(fincerrar)==False:
              GPIO.output(cerrar,0);     
              GPIO.output(blue,0)
              GPIO.output(green,0)
              GPIO.output(red,1)
          elif pose_type.name=="FINGERS_SPREAD":
           GPIO.output(giro_iz,0)
           GPIO.output(giro_de,0)
           GPIO.output(cerrar,0)
           if GPIO.input(finabrir)==True:
              GPIO.output(abrir,1);
              GPIO.output(flex,0)
              GPIO.output(ext,0)
              GPIO.output(blue,1)
              GPIO.output(green,0)
              GPIO.output(red,0)
           if GPIO.input(finabrir)==False:
              GPIO.output(abrir,0);     
              GPIO.output(blue,0)
              GPIO.output(green,0)
              GPIO.output(red,1)
          elif pose_type.name=="DOUBLE_TAP":
           GPIO.output(giro_iz,0)
           GPIO.output(giro_de,0)
           GPIO.output(cerrar,0)
           GPIO.output(abrir,0)
           if varflex==0:
              GPIO.output(flex,1)
              GPIO.output(ext,0)
              GPIO.output(blue,0)
              GPIO.output(green,1)
              GPIO.output(red,0)
              if GPIO.input(finflex)==False:
                 
                 varflex=1;
           else:
              GPIO.output(flex,0)
              GPIO.output(ext,1)
              GPIO.output(blue,0)
              GPIO.output(green,1)
              GPIO.output(red,0)
              if GPIO.input(finext)==False:
                 
                 varflex=0;
          elif pose_type.name=="REST":
           GPIO.output(giro_iz,0)
           GPIO.output(giro_de,0)
           GPIO.output(cerrar,0)
           GPIO.output(abrir,0)
           GPIO.output(flex,0)
           GPIO.output(ext,0)
           GPIO.output(blue,1)
           GPIO.output(green,1)
           GPIO.output(red,1)
