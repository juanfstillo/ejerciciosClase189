#!/usr/bin/env python
# coding: utf-8

# 1 - Diseña un programa en Python que permita al usuario ingresar una lista de 10 números enteros. Luego, el programa debe calcular lo siguiente:
# 
# a. La cantidad de valores ingresados que son números negativos.
# b. La cantidad de valores ingresados que son números positivos.
# c. La cantidad de números ingresados que son múltiplos de 15.
# d. La suma de todos los números ingresados que son pares.
# 
# Puedes usar este enfoque para desarrollar tu programa en Python:

# In[11]:


#1
negativo = 0
positivo = 0
multiplo_de_15 = 0
suma_par = 0
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    if numero != 0:
        if numero < 0:
            negativo = negativo +1
        elif numero > 0:
            positivo +=1

        if numero %15 == 0:
            multiplo_de_15+=1

        if numero %2 == 0:
            suma_par +=1
        
print("los negativos son: ",negativo)
print("los positivos son: ",positivo)
print("los multiplos de 15 son: ",multiplo_de_15)
print("los pares son: ",suma_par)


# 2- Guardar en un archivo txt. todas la notas de los alumnos de Economía.

# In[13]:


#2
notas = {
    'Alumno 1':10,
    'Alumno 2': 9,
    'Alumno 3':4,
    'Alumno 4': 1,
    'Alumno 5' :10
}
print(notas)

nombre_archivo = 'notas.txt'

with open(nombre_archivo,'w') as archivo:
    for alumno, nota in notas.items():
        archivo.write(f'{alumno} : {nota}\n')
        


# In[7]:


from IPython.display import Image
Image(filename='./desktop/massa.png')


# 3 -Usted trabaja en el supermercado Día y su jefe desea obtener una muestra de aquellas personas que son beneficiadas por la nueva medida del ministro de economía.
# 1-Realizar una función que quite el IVA a un precio dado y otra que aplique un descuento.
# Finalmente, realizar una tercera que reciba un diccionario con precios y porcentajes de un carrito de compras. Dicha función debe utilizar las funciones pasadas para aplicar IVA y descuento a los productos del carrito y devolver el precio final. 

# In[20]:


#quita de iva

def quitar_iva(precio, tasa_iva=0.21):
    precio_sin_iva = precio / (1+ tasa_iva)
    return precio_sin_iva

# funcion que aplique descuento
def aplicar_descuento (precio,descuento):
    precio_con_descuento = precio - (precio * descuento)
    return precio_con_descuento

# funcion precio final
def calcular_precio_final(carrito, tasa_iva= 0.21):
    precio_total = 0
    
    for producto, precio in carrito.items():
        precio_sin_iva = quitar_iva(precio,tasa_iva)
        
        if(producto in descuentos):
            precio_con_descuento = aplicar_descuento(precio_sin_iva, descuentos[producto])
        else:
            precio_con_descuento = precio_sin_iva
            
        precio_total += precio_con_descuento
        
    return precio_total

carrito_de_compras = {
    'patys':10,
    'yogurth':200,
    'pan' :10,
    'azucar':90
}

descuentos = {
    'pan':0.1,
    'azucar':0.05
}

#calcular el precio final
precio_final = calcular_precio_final(carrito_de_compras)

print(f'El precio final del carrito de compras es: ${precio_final:.2f}')


# 4 -  Imaginate que trabajas como analista político en una campaña electoral y estás a cargo de analizar las encuestas de intención de voto de un candidato en particular durante los últimos 7 días. Hay acceso a datos de encuestas realizadas diariamente donde los encuestados indican si votarán "Sí" o "No" al candidato.
# 
# El objetivo es realizar un análisis de la tendencia de voto del candidato en la última semana y calcular:
# 
# a. El promedio de apoyo diario al candidato en porcentaje.
# b. El día con el mayor apoyo al candidato.
# c. El día con el menor apoyo al candidato.
# d. La cantidad de días en los que el candidato tuvo más del 50% de apoyo.
# 
# El lunes obtuvo el 60 % de apoyo, martes 55 %, miercoles 63%, jueves 68%, viernes 50%, sabado 58% y viernes 70%
# 

# 5- Guardar en un archivo txt. las edades de los políticos con más votos en la elección pasada.

# In[8]:


from IPython.display import Image
Image(filename='./desktop/cavallo.png')


# 6-Realizar una función que aplique el nuevo IVA a un precio dado y otra que aplique un descuento.
# Finalmente, realizar una tercera que reciba un diccionario con precios y porcentajes de un carrito de compras y una de las funciones anteriores. Dicha función debe utilizar alguna de las funciones pasadas para aplicar IVA o descuento a los productos del carrito y devolver el precio final.

# In[ ]:




