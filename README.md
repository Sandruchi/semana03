# Comparación entre Programación Tradicional y Orientada a Objetos (POO)

La **programación tradicional** y la **programación orientada a objetos (POO)** son enfoques diferentes para estructurar y organizar el código. Ambas tienen sus ventajas y desventajas según el tamaño, la complejidad y el propósito del proyecto. A continuación, se realiza una comparación basada en los ejemplos de los códigos proporcionados.

---

## 1. Estructura y Organización del Código

### **Programación Tradicional**
- El flujo del programa se organiza mediante **funciones independientes**.  
- En el ejemplo, las funciones `ingresar_temperaturas`, `calcular_promedio` y `main` manejan las tareas específicas del programa.  
- Esta estructura es clara y directa, especialmente para problemas pequeños, ya que permite identificar rápidamente qué hace cada parte del código.

### **POO**
- El código se organiza en **clases**, agrupando datos y comportamientos relacionados.  
- La clase `Clima` encapsula las temperaturas y los métodos relacionados (`ingresar_temperaturas` y `calcular_promedio`).  
- La clase `ProgramaClima` coordina la ejecución.  
- Este enfoque modular resulta más limpio y escalable, especialmente para proyectos grandes.

---

## 2. Encapsulamiento y Manejo de Datos

### **Programación Tradicional**
- Los datos, como las temperaturas, se gestionan mediante **estructuras simples** (en este caso, una lista).  
- Este enfoque es fácil de implementar, pero **carece de protección y encapsulamiento**, lo que puede dificultar la gestión de datos si el programa crece.

### **POO**
- La clase `Clima` encapsula las temperaturas como un **atributo**, lo que permite acceder y modificar los datos solo mediante métodos específicos.  
- Esto asegura una manipulación más controlada y ordenada de los datos, reduciendo errores y mejorando la coherencia del programa.

---

## 3. Extensibilidad y Reutilización del Código

### **Programación Tradicional**
- El diseño basado en funciones hace que sea **menos modular**.  
- Por ejemplo, agregar nuevas características (como registrar temperaturas adicionales o calcular la desviación estándar) implicaría **modificar directamente las funciones existentes**, lo que puede introducir errores.

### **POO**
- La **modularidad de las clases** facilita la extensión y reutilización.  
- Por ejemplo, se podría extender la clase `Clima` para incluir nuevos métodos, como calcular máximos, mínimos o estadísticas adicionales, **sin necesidad de modificar otras partes del programa**.

---

## 4. Complejidad y Escalabilidad

### **Programación Tradicional**
- Este enfoque es más **sencillo**, lo que lo hace ideal para problemas pequeños o cuando se requiere un desarrollo rápido.  
- Sin embargo, a medida que aumenta la complejidad del programa, puede volverse **desordenado y difícil de mantener**.

### **POO**
- Aunque más **compleja inicialmente**, la POO ofrece ventajas significativas en términos de **escalabilidad**.  
- La estructura orientada a objetos permite manejar programas más grandes de manera más organizada, reduciendo la complejidad de futuras modificaciones o ampliaciones.

---

## 5. Aplicación de Conceptos de POO

### **Programación Tradicional**
- No utiliza conceptos avanzados como **encapsulamiento**, **herencia** o **polimorfismo**.  
- Todo el enfoque se centra en funciones que operan sobre datos externos.

### **POO**
- En el ejemplo, se aplica el concepto de **encapsulamiento**, al agrupar datos (temperaturas) y métodos (cálculos y entradas) dentro de una clase.  
- Esto fomenta la coherencia y el diseño basado en responsabilidades.

---

## Ejemplo Práctico: Flujo del Programa

### **Programación Tradicional**
1. El programa comienza llamando a la función `main`, que gestiona el flujo completo:  
   - Solicita las temperaturas diarias con `ingresar_temperaturas`.  
   - Calcula el promedio semanal con `calcular_promedio`.  
   - Muestra el resultado al usuario.

### **POO**
1. El programa utiliza una instancia de la clase `ProgramaClima` para ejecutar el flujo:  
   - La clase `Clima` se encarga de gestionar los datos (temperaturas) y los cálculos (promedio).  
   - La clase `ProgramaClima` actúa como coordinadora, llamando a los métodos necesarios y mostrando el resultado.

---

## Conclusión

- La **programación tradicional** es una opción más simple y directa, ideal para programas pequeños y de baja complejidad.  
- La **POO** es más adecuada para proyectos grandes o en crecimiento, ya que permite organizar y encapsular datos y funcionalidades, facilitando la mantenibilidad y escalabilidad.  

El enfoque a elegir depende de las necesidades del proyecto:  
- Si se busca **rapidez y simplicidad**, la programación tradicional es suficiente.  
- En cambio, si se requiere un diseño **modular y extensible**, la POO es la mejor opción.
