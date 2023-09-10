A continuación se presentan los comandos para ejecutar cada uno de los servicios. Todos se deben ejecutar en al raíz del proyecto.

Para ejecutar el monitor:
`python monitor/app.py `

Para ejecutar el task de monitor:
`celery -A monitor.tasks.monitor_task worker`

Para ejecutar el task de cada microservicio:

`celery -A <microservicio>.tasks.<microservicio>_task worker`