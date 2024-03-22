# Preguntas a resolver, caso Torres de Hanoi

## ¿Cuáles son los PEAS de este problema? (Performance, Environment, Actuators, Sensors)

### Performance
- **Rápido:** Capaz de encontrar una solución en el menor tiempo posible.
- **Eficiente:**: Usa el menor número de movimientos posibles para alcanzar la solución. La eficiencia puede medirse por cuán cercano está el agente a alcanzar este ideal, siendo este un mínimo teórico de movimientos necesarios para resolver el juego ($2^n - 1$, donde $n$ es el número de discos).
- **Preciso:** Mueve los discos de acuerdo a las reglas del juego. Moviendo un disco a la vez y sin colocar un disco más grande sobre uno más chico.
- **Completo:** Encuentra una solución si esta existe.
- **Mutable:** Puede resolver el problema con diferentes números de discos (contando con la restricción de la cantidad de discos que puede manejar la máquina de procesamiento).

### Environment
- **Varillas:** El espacio físico o virtual en el que se juega el juego. En este caso, las varillas de origen, auxiliar y destino.
- **Discos:** Los discos que se deben mover de una varilla a otra. Donde cada disco tiene un tamaño único, lo que afecta dónde puede ser colocado.

### Actuators
- **Movimiento de los discos:** La única acción concreta realizada durante el juego, mover un disco de una varilla a otra siguiendo las reglas del juego. Función de software de movimiento de un disco.

### Sensors
- **Posición de los discos en las varillas:** Información sobre la posición actual de los discos en las varillas. Esta información es necesaria para determinar cuál es el siguiente movimiento a realizar. Función de software de lectura de la posición de los discos.

## ¿Cuáles son las propiedades del entorno de trabajo?
Se trata de un entorno de trabajo totalmente observable, determinístico, secuencial y estático.
## En el contexto de este problema, establezca cuáles son los: estado, espacio de estados, árbol de búsqueda, nodo de búsqueda, objetivo, acción y frontera.
### Estado
Posición de los discos en las varillas.
### Espacio de estados
Todas las posibles posiciones de los discos en las varillas.
### Árbol de búsqueda

### Nodo de búsqueda
### Objetivo
Mover los 5 discos de la varilla de origen a la varilla de destino, cumpliendo las reglas del juego.
### Acción
Mover un disco de una varilla a otra.
### Frontera
## ¿Qué complejidad en tiempo y memoria tiene el algoritmo elegido?
-- Completar con los datos recopilados --
## A nivel implementación, ¿qué tiempo y memoria ocupa el algoritmo? 
-- Completar con los datos recopilados --
## Si la solución óptima es movimientos con k igual al número de discos. Qué tan lejos está la solución del algoritmo implementado de esta solución óptima (se recomienda correr al menos 10 veces y usar el promedio de trayecto usado).
-- Completar con los datos recopilados --
