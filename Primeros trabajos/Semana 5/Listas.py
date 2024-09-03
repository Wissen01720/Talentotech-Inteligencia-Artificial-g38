# Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad). Crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden.
import queue as q

tareas = [6, 'Distribución', 2, 'Diseño', 1, 'Concepción', 7, 'Mantenimiento', 4, 'Producción', 3, 'Planificación', 5, 'Pruebas']

prioridades = q.PriorityQueue()

for i in range(0, len(tareas), 2):
    prioridades.put((tareas[i], tareas[i + 1]))

while not prioridades.empty():
    tarea = prioridades.get()
    print(tarea[1])