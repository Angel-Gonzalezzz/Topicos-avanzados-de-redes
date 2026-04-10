import numpy as np
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""""
Generación de datos
"""""

def generar_datos(n=200):
    np.random.seed(42)
    
    data = pd.DataFrame({
        "paquetes": np.random.randint(50, 500, n),
        "tamaño": np.random.randint(500, 10000, n),
        "duracion": np.random.uniform(0.1, 5, n),
        "latencia": np.random.uniform(1, 200, n),
        "ancho_banda": np.random.uniform(1, 100, n)
    })

    condiciones = [
        (data["tamaño"] > 8000) | (data["latencia"] > 150)
    ]

    data["tipo"] = np.select(condiciones, ["anómalo"], default="normal")
    return data

"""""
Entrenamiento
"""""

def entrenar_modelo(data):
    X = data[["paquetes","tamaño","duracion","latencia","ancho_banda"]]
    y = data["tipo"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    modelo = SVC()
    modelo.fit(X_train,y_train)

    pred = modelo.predict(X_test)

    print("\n=== Evaluación del modelo ===")
    print("Accuracy:", accuracy_score(y_test,pred))
    print("Matriz de confusión:\n", confusion_matrix(y_test,pred))
    print("\nReporte:\n", classification_report(y_test,pred))

    return modelo

"""""
Simulación 3D en tiempo real
"""""

def simulacion_3D(modelo, iteraciones=50):
    plt.ion()
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')

    x_bytes = []
    y_paquetes = []
    z_latencia = []
    colores = []

    for i in range(iteraciones):
        paquetes = random.randint(50,500)
        tamaño = random.randint(500,10000)
        duracion = random.uniform(0.1,5)
        latencia = random.uniform(1,200)
        ancho_banda = random.uniform(1,100)

        muestra = np.array([[paquetes,tamaño,duracion,latencia,ancho_banda]])
        pred = modelo.predict(muestra)[0]

        """""
        Guardar datos
        """""

        x_bytes.append(tamaño)
        y_paquetes.append(paquetes)
        z_latencia.append(latencia)

        """""
        Color según clasificación
        """""

        if pred == "anómalo":
            colores.append("red")
        else:
            colores.append("green")

        """""
        Limpiar gráfica
        """""

        ax.clear()

        ax.scatter(x_bytes, y_paquetes, z_latencia, c=colores, s=40)

        ax.set_title("Simulación de Tráfico")
        ax.set_xlabel("Bytes")
        ax.set_ylabel("Paquetes")
        ax.set_zlabel("Latencia")

        ax.grid(True, linestyle="--", alpha=0.5)

        plt.pause(0.5)

    plt.ioff()
    plt.show()

"""""
Interpretación
"""""

def interpretar_modelo():
    print("\n=== Interpretación ===")
    print("- El modelo SVM separa datos en un espacio multidimensional.")
    print("- Detecta patrones como alta latencia o gran tamaño de datos.")
    print("- El tráfico anómalo aparece en rojo en la gráfica 3D.")

"""""
MAIN
"""""

if __name__ == "__main__":
    data = generar_datos()
    print("Dataset:\n", data.head())

    modelo = entrenar_modelo(data)

    interpretar_modelo()

    simulacion_3D(modelo)