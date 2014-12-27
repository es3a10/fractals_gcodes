from itertools import chain
from math import sin,cos,radians

def mover(angulo,distancia):
	nx = round(cos(radians(angulo)),9)*distancia
	ny = round(sin(radians(angulo)),9)*distancia
	return (nx,ny)

def hacer_linea(i,j,fname,giros,grado_inicial):
	# i iteracion, j longitud, fname fichero gcode, giros lista de giros, grado_inicial
	for g in giros:
		if i == 1:
			posicion = mover(grado_inicial+g,j/(len(giros)-1))
			gcodes = "G1 X{0} Y{1} \n".format(posicion[0],posicion[1])
			print gcodes
			#print j
			#print " "
			f = open(fname,'a')
			f.write(gcodes)
		else:
			hacer_linea(i-1,j/(len(giros)-1),fname,giros,grado_inicial+g)
		
	
def prod(i,j):
	print(i*j)
	return i*j
	
def koch_ant(i,j,fname):
	resultado = i*j
	s = "G1 X{0} \n".format(resultado)
	print(s)
	f = open(fname,'a')
	f.write(s)
	f.close
	return resultado