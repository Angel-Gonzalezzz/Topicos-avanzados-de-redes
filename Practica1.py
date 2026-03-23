import numpy as np
import pandas as pd
import matplotlib.pyplot as pit
import random
import time

"""
configuracion

"""
Num_paquetes = 100
Tamaño_paquete = 1024 #bytes
Velocidad_red = 100000 #bytes por segundo

"""
Listas para almacenar datos
"""

latencias = []
paquetes_envidas = []
paquetes_recibidos = []
perdidos = []

print("Simulando trafico de datos ....n")

for i in range (Num_paquetes):
   tiempo_envio = time.time()

   """
   Simular lactencia (entre 10ns y 100ns)
   """

   latencia = random.uniform(0.01, 0.1)
   time.sleep(latencia)

   """
   Simular pérdidad de paquetes (10%)
   """

   if random.random () < 0.1:
      perdidos += 1
      continue

   tiempo_recepcion = time.time()
   latencia.append(tiempo_recepcion - tiempo_envio)
   paquetas_envidas.append(Tamano_paquete)
   paquetas_recibidos.append(Tamano_paquete)

"""
Metricas
"""

total_enviados = len(paquetas_envidas)
total_recibidos = len(paquetas_recibidos)
tasa_perdida = perdidos / Num_paquetes

latencia_promedio = np.mean(latencias)

throughput = (sum(paquetas_recibidos) / sum (latencia)) if latencias else 0

