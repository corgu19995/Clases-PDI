# -*- coding: utf-8 -*-
import cv2
import numpy as np

def mouse(event, x, y, flags, param): #Posición del mouse
    if event==cv2.EVENT_MOUSEMOVE:
        print('RGB Pixel (', x ,', ', y ,'): ', imagen.item(y, x, 2), '/', imagen.item(y, x, 1), '/' , imagen.item(y, x, 0))

def separar(imagen):
    cv2.setMouseCallback('image',mouse)
    while(1):
        cv2.imshow('image',imagen)# Muestra laimagen
        cv2.namedWindow('b')#Creaunanueva ventana
        cv2.setMouseCallback('b',mouse)#Llama al método encargado de obtenener las coordenadas del mouse
        b = imagen.copy()#Se crea una copia de la imagen original
        b[:,:,1] = 0
        b[:,:,2] = 0    #Se hacen 0 los demás valores
        cv2.imshow('b',b)
        #Set blue and red Channel to 0
        cv2.namedWindow('g')
        cv2.setMouseCallback('g',mouse)
        g = imagen.copy()
        g[:,:,0] = 0
        g[:,:,2] = 0
        cv2.imshow('g',g)
        #Set green and ble Channel to 0
        cv2.namedWindow('r')
        cv2.setMouseCallback('r',mouse)
        r = imagen.copy()
        r[:,:,0] = 0
        r[:,:,1] = 0
        cv2.imshow('r',r)
        if cv2.waitKey(20) and 0xFF == ord('q'):#Espera hasta un tiempo  n para  cerrar ???
            break
    cv2.destroyAllWindows()#Secierran las ventanas

if __name__=='__main__':
  imagen = cv2.imread("rgb.png",1)#Se lee la imagen
  #Set green and red Channel to 0  
  separar(imagen)

