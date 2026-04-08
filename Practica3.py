import numpy as np
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


plt.style.use("dark_background")


"""
dataset
"""
def generar_datos(n=2000):
    np.random.seed(42)

    data = pd.DataFrame({
        "paquetes": np.random.randint(100,5000,n),
        "bytes": np.random.randint(1000,60000,n),
        "duracion": np.random.uniform(0.1,15,n),
        "protocolo": np.random.choice([0,1], n),
        "latencia": np.random.randint(1,200,n),
        "puerto": np.random.randint(20,9000,n),
        "perdida": np.random.uniform(0,10,n),
        "jitter": np.random.uniform(0,50,n)
    })

    condiciones = [
        (data["bytes"]>45000) & (data["jitter"]>30),
        (data["paquetes"]>3000) & (data["latencia"]>100),
    ]

    opciones = ["ataques", "video"]

    data["tipo"] = np.select(condiciones, opciones, default="normal")

    return data


"""
entrenamiento
"""
def entrenar_modelo(data):
    X = data[["paquetes","bytes","duracion","protocolo","latencia","puerto","perdida","jitter"]]
    y = data["tipo"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    modelo = SVC()
    modelo.fit(X_train,y_train)

    pred = modelo.predict(X_test)

    print("\n=== Evaluación del modelo ===")
    print("Accuracy:", accuracy_score(y_test,pred))
    print(classification_report(y_test,pred))

    return modelo


"""
simulacion
"""
def simulacion(modelo, iteraciones=10):
    for i in range(iteraciones):
        paquetes = random.randint(100,5000)
        bytes = random.randint(1000,60000)
        duracion = random.uniform(0.1,15)
        protocolo = random.choice([0,1])
        latencia = random.randint(1,200)
        puerto = random.randint(20,9000)
        perdida = random.uniform(0,10)
        jitter = random.uniform(0,50)

        muestra = np.array([[paquetes,bytes,duracion,protocolo,latencia,puerto,perdida,jitter]])
        pred = modelo.predict(muestra)[0]

        print(f"\n Iteración {i+1}")
        print(f" Clasificación: {pred}")
        print("="*40)

        time.sleep(1)


"""
grafica
"""
def grafica(data):
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(
        data["bytes"],
        data["paquetes"],
        data["latencia"],
        c="orange",
        s=20,
        alpha=0.7,
        edgecolors="white"
    )

    ax.set_title("Visualización de Tráfico de Red", fontsize=14, color="yellow")
    ax.set_xlabel("Bytes", fontsize=10, color="white")
    ax.set_ylabel("Paquetes", fontsize=10, color="white")
    ax.set_zlabel("Latencia", fontsize=10, color="white")

    ax.set_facecolor("#1B1919")
    ax.grid(True, linestyle="--", alpha=0.3)

    plt.show()


"""
main
"""
if __name__ == "__main__":
    data = generar_datos()

    print("\n Dataset generado:")
    print(data.head())

    modelo = entrenar_modelo(data)

    grafica(data)

    simulacion(modelo)