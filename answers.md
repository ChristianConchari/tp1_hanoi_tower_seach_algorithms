# Preguntas a resolver, caso Torres de Hanoi

## 1. ¿Cuáles son los PEAS de este problema? (Performance, Environment, Actuators, Sensors)

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

## 2. ¿Cuáles son las propiedades del entorno de trabajo?
Se trata de un entorno con las siguientes propiedades:
- **Completamente observable:** Se puede ver la posición de los discos en las varillas en todo momento.
- **Agente único:** Solo hay un agente que toma decisiones durante el transcurso del juego.
- **Determinístico:** Las reglas del juego son claras y no hay elementos aleatorios que afecten el resultado.
- **Secuencial:** El juego se desarrolla en una serie de pasos secuenciales, donde cada movimiento afecta el estado del juego.
- **Estático:** El entorno no cambia por sí mismo, solo cambia cuando el agente realiza una acción (mover un disco).
- **Discreto:** Las acciones y estados del juego son discretos, no continuos.
- **Conocido:** El agente tiene completo conocimiento del entorno y las reglas del juego desde el principio.

## 3. En el contexto de este problema, establezca cuáles son los: estado, espacio de estados, árbol de búsqueda, nodo de búsqueda, objetivo, acción y frontera.

### Estado
La disposición específica de los discos en las varillas en un momento dado.

### Espacio de estados
Todas las posibles posiciones de los discos en las varillas. Se trata de un espacio de estados finito, ya que el número de discos y varillas es limitado.

### Árbol de búsqueda
Una representación de todas las posibles secuencias de movimientos desde el estado inicial hasta el estado objetivo. 

### Nodo de búsqueda
Un nodo en el árbol de búsqueda que representa un estado específico dentro del árbol de búsqueda. Cada nodo tiene un estado, un nodo padre, ceros o más nodos hijos.

### Objetivo
El estado objetivo es cuando todos los discos están en la varilla de destino, en orden de tamaño decreciente.

### Acción
Mover un disco de una varilla a otra. Solamente válida si se cumplen las reglas del juego.

### Frontera
Conjunto de todos los nodos que han sido generados, pero no han sido explorados aún. La frontera separa los nodos explorados de los nodos sin explorar, y el algoritmo de búsqueda decide que nodo explorar a continuación. Por ejemplo, en una búsqueda en profundidad, la frontera es una pila de nodos, donde el último nodo en ser agregado es el siguiente en ser explorado.

## 4. Implemente algún método de búsqueda.
Se eligió implementar el algoritmo de búsqueda por profundidad primero (DFS). La implementación esta en el archivo `depth_first_search.py`.	

## 5. ¿Qué complejidad en tiempo y memoria tiene el algoritmo elegido?

El algoritmo elegido es búsqueda por profundidad primero (DFS). La complejidad en tiempo y memoria de este algoritmo es la siguiente:

- **Complejidad en tiempo:** La complejidad en timepo de la búsqueda por profundidad primero esta limitada por el tamaño del espacio de estados. En ese caso, la complejidad es $O(b^m)$, donde $m$ es la profundidad máxima de cualquier nodo, puede ser mucho más grande que el tamaño del espacio de estados, y $b$ es el factor de ramificación, es decir, el número máximo de hijos que puede tener un nodo. 

- **Complejidad en memoria:** La complejidad en memoria de la búsqueda por profundidad primero es $O(bm)$, donde $m$ es la profundidad máxima de cualquier nodo, y $b$ es el factor de ramificación.

## 6. A nivel implementación, ¿qué tiempo y memoria ocupa el algoritmo? 

Se midió a nivel de implementación el tiempo y memoria que ocupa el algoritmo de búsqueda por profundidad primero (DFS) corriendo $n=100$ pruebas para el caso de cinco discos.

- **Tiempo:** El tiempo promedio de ejecución del algoritmo fue de 0.0356 segundos con una desviación estándar de 0.0029 segundos.

- **Memoria:** La memoria promedio utilizada por el algoritmo fue de 0.20 MB con una desviación estándar de 0.0009 MB.


## 7. Si la solución óptima es $2^k - 1$ movimientos con $k$ igual al número de discos. Qué tan lejos está la solución del algoritmo implementado de esta solución óptima (se recomienda correr al menos 10 veces y usar el promedio de trayecto usado).

Para el caso de cinco discos, la solución óptima es $2^5 - 1 = 31$ movimientos. Se corrieron $n=100$ pruebas y se obtuvo un promedio de 121 movimientos. Por lo tanto, la solución encontrada por el algoritmo implementado está a 90 movimientos de la solución óptima.
