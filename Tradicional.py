# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Suponiendo que se ingresan 7 días (una semana)
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la temperatura.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Función principal que coordina el flujo
def main():
    print("Cálculo del promedio semanal del clima")
    temperaturas = ingresar_temperaturas()  # Pedir temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcular promedio
    print(f"El promedio de las temperaturas de la semana es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
