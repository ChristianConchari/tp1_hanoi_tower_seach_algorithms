# Hanoi Tower Search Algorithms

Este repositorio contiene la implementación del problema de la Torre de Hanoi usando algoritmos de búsqueda. El código en el directorio hanoi_tower fue extraído del repositorio [intro_ia](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/tree/main/clase2/hanoi_tower). Parte del material del curso de Introducción a la Inteligencia Artificial (CEIA - FIUBA).

## Contenidos

- [Introducción](#introducción)
- [Preparación](#preparación)
- [Ejecución](#ejecución)

## Introducción

Las respuestas a las preguntas a resolver se encuentran en el archivo [answers.md](answers.md). El código de la implementación de la búsqueda por profundidad primero se encuentra en el archivo [depth_first_search.py](depth_first_search.py). También se incluyen los archivos json `initial_state.json` y `sequence.json` para la simulación.

La implementación experimental para encontrar el tiempo, la memoria y el número de movimientos para resolver el problema de la Torre de Hanoi se encuentra en el notebook `hanoi_search_notebook.ipynb`. 

## Preparación

Para usar el notebook `hanoi_search_notebook.ipynb` y la simulación es necesario instalar las siguientes librerías:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el notebook `hanoi_search_notebook.ipynb`, se puede usar Jupyter Notebook o Jupyter Lab. También debe considerarse tener el ambiente virtual activado, si se va a usar.

Al final del notebook se copian los json para la simulación en el directorio `hanoi_tower/simulator`. Entonces, para correr la simulación, se debe navegar al directorio `hanoi_tower/simulator` y ejecutar el siguiente comando:

```bash
python simulation_hanoi.py
``` 

