from itertools import chain
from math import sin,cos,radians,sqrt
import modulo_koch

centro = (95,95)
longitud = 140.0
iteracion = 4
giros = (0,60,-60,0)

grado_inicial = 0
angulo_linea = -120

gcodes = """
G91
G1 Z2
G28
G1 Z2
"""
print gcodes
fname = 'koch.gcode'
f = open(fname,'w')
f.write(gcodes)
f.close()

for i in range(iteracion):
	f = open(fname,'a')
	posicion = modulo_koch.mover(150,longitud/(sqrt(3)*(iteracion-i)))
	gcodes = """
	G90
	G1 X{0} Y{1}
	G1 Z0
	G91
	""".format(centro[0]+posicion[0],centro[1]+posicion[1])
	print gcodes
	f.write(gcodes)
	f.close()


	angulo = 0
	while angulo > -360 :
		modulo_koch.hacer_linea(i+1,longitud/(iteracion-i),fname,giros,angulo)
		angulo = angulo + angulo_linea
	

	gcodes = "G1 Z2 \n"
	print gcodes
	fname = 'koch.gcode'
	f = open(fname,'a')
	f.write(gcodes)
	f.close()

