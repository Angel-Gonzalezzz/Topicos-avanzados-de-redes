"""""
PRACTICA 4

Simple con IA para detectar
"""""

import os
import numpy as np
import sklearn.tree as DecisionTreeClassifier

#Simulacion de datos

"""""
Caractersiticas: [Tiempo_respuesta_ms]
"""""

x = np.array([[10], [20], [30], [200], [300], [400]])
y = np.array([1, 1, 1, 0, 0, 0])

"""""
Modelo de la Ia
"""""

modelo = DecisionTreeClassifier()
modelo.fit(x,y)

"""""
Escaneo de Red
"""""
red = "192.168.1."

for i in range (1, 20):
    ip = red + str(1)

    """""
    Ping Window
    """""
    respuesta = os.popen(f"ping -n -w 100 {ip}").read()

    if "tiempo=" in respuesta:

        try:
            tiempo = int(respuesta.split("tiempo=" [1].split ("ms")[0]))

        except:
            tiempo = 300

    else:
        tiempo = 400


    """""
    Prediccion con IA
    """""

    prediccion = modelo.predict([[tiempo]])[0]

    if prediccion == 1:
        print(f"Dispositivo Activa IA: {ip} - {tiempo} ms")

    else:
        print(f"Dispositivo inactivo (IA): {ip}")     