#! /usr/bin/python
#! encoding: UTF-8
a= float(raw_input("Valor de a: "))
b= float(raw_input("Valor de b: "))

if a!=0:
  x = -b/a
  print "Solucion: ",x
elif (a==0) and (b!=0):
  print "La ecuacion no tiene solución."
elif (a==0) and (b==0):
  print "La ecuacion tiene soluciones infinitas"