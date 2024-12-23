class Clima:
    def __init__(self):
        # Atributo para almacenar las temperaturas de los 7 días
        self.temperaturas = []

    # Método para ingresar las temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):  # Suponiendo que se ingresan 7 días (una semana)
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para la temperatura.")

    # Método para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Clase para coordinar la ejecución
class ProgramaClima:
    def __init__(self):
        self.clima = Clima()  # Instancia la clase Clima

    # Método para ejecutar el flujo del programa
    def ejecutar(self):
        print("Cálculo del promedio semanal del clima")
        self.clima.ingresar_temperaturas()  # Ingresar temperaturas
        promedio = self.clima.calcular_promedio()  # Calcular promedio
        print(f"El promedio de las temperaturas de la semana es: {promedio:.2f}°C")

# Crear una instancia de ProgramaClima y ejecutarla
if __name__ == "__main__":
    programa = ProgramaClima()
    programa.ejecutar()
