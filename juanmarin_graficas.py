import matplotlib.pyplot as plt
import numpy as np

#carga los datos
datos_python = np.genfromtxt(times_python.csv)
datos_cpp = np.genfromtxt(times_cpp)
#hace la grafica
plt.plot(datos_python[0], datos_python[1], label= "datos python")
plt.plot(datos_cpp[0],datos_cpp[1], label = "datos c++")
plt.legend(loc=0)
plt.xlabel("N")
plt.ylabel("Tiempo")
plt.savefig("cpp_vs_python.png")

