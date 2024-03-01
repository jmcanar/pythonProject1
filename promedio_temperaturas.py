temperaturas = [
    [   # cuenca
         [   # Semana 1
             {"dia": "Lunes", "temp": 28},
             {"dia": "Martes", "temp": 30},
             {"dia": "Miércoles", "temp": 35},
             {"dia": "Jueves", "temp": 27},
             {"dia": "Viernes", "temp": 25},
             {"dia": "Sábado", "temp": 26},
             {"dia": "Domingo", "temp": 20}
         ],
         [   # Semana 2
             {"dia": "Lunes", "temp": 26},
             {"dia": "Martes", "temp": 19},
             {"dia": "Miércoles", "temp": 23},
             {"dia": "Jueves", "temp": 22},
             {"dia": "Viernes", "temp": 25},
             {"dia": "Sábado", "temp": 23},
             {"dia": "Domingo", "temp": 24}
         ],
         [   # Semana 3
             {"dia": "Lunes", "temp": 26},
             {"dia": "Martes", "temp": 25},
             {"dia": "Miércoles", "temp": 23},
             {"dia": "Jueves", "temp": 20},
             {"dia": "Viernes", "temp": 18},
             {"dia": "Sábado", "temp": 21},
             {"dia": "Domingo", "temp": 22}
         ],
         [   #semana 4
             {"dia": "Lunes", "temp": 27},
             {"dia": "Martes", "temp": 27},
             {"dia": "Miércoles", "temp": 25},
             {"dia": "Jueves", "temp": 22},
             {"dia": "Viernes", "temp": 28},
             {"dia": "Sábado", "temp": 21},
             {"dia": "Domingo", "temp": 25}
         ],
    ],
    [  # azogues
         [  # Semana 1
             {"dia": "Lunes", "temp": 28},
             {"dia": "Martes", "temp": 20},
             {"dia": "Miércoles", "temp": 22},
             {"dia": "Jueves", "temp": 19},
             {"dia": "Viernes", "temp": 25},
             {"dia": "Sábado", "temp": 28},
             {"dia": "Domingo", "temp": 22}
         ],
         [  # Semana 2
             {"dia": "Lunes", "temp": 26},
             {"dia": "Martes", "temp": 29},
             {"dia": "Miércoles", "temp": 23},
             {"dia": "Jueves", "temp": 21},
             {"dia": "Viernes", "temp": 27},
             {"dia": "Sábado", "temp": 29},
             {"dia": "Domingo", "temp": 23}
         ],
         [  # Semana 3
             {"dia": "Lunes", "temp": 27},
             {"dia": "Martes", "temp": 21},
             {"dia": "Miércoles", "temp": 25},
             {"dia": "Jueves", "temp": 22},
             {"dia": "Viernes", "temp": 28},
             {"dia": "Sábado", "temp": 21},
             {"dia": "Domingo", "temp": 25}
         ],
         [  # semana 4
             {"dia": "Lunes", "temp": 27},
             {"dia": "Martes", "temp": 21},
             {"dia": "Miércoles", "temp": 25},
             {"dia": "Jueves", "temp": 22},
             {"dia": "Viernes", "temp": 28},
             {"dia": "Sábado", "temp": 21},
             {"dia": "Domingo", "temp": 25}
         ],
    ],
    [  #biblian
         [  # Semana 1
             {"dia": "Lunes", "temp": 28},
             {"dia": "Martes", "temp": 20},
             {"dia": "Miércoles", "temp": 22},
             {"dia": "Jueves", "temp": 29},
             {"dia": "Viernes", "temp": 25},
             {"dia": "Sábado", "temp": 28},
             {"dia": "Domingo", "temp": 22}
         ],
         [  # Semana 2
             {"dia": "Lunes", "temp": 26},
             {"dia": "Martes", "temp": 29},
             {"dia": "Miércoles", "temp": 23},
             {"dia": "Jueves", "temp": 21},
             {"dia": "Viernes", "temp": 27},
             {"dia": "Sábado", "temp": 29},
             {"dia": "Domingo", "temp": 23}
         ],
         [  # Semana 3
             {"dia": "Lunes", "temp": 27},
             {"dia": "Martes", "temp": 21},
             {"dia": "Miércoles", "temp": 25},
             {"dia": "Jueves", "temp": 22},
             {"dia": "Viernes", "temp": 28},
             {"dia": "Sábado", "temp": 21},
             {"dia": "Domingo", "temp": 25}
         ],
         [  # semana 4
             {"dia": "Lunes", "temp": 27},
             {"dia": "Martes", "temp": 21},
             {"dia": "Miércoles", "temp": 25},
             {"dia": "Jueves", "temp": 22},
             {"dia": "Viernes", "temp": 28},
             {"dia": "Sábado", "temp": 21},
             {"dia": "Domingo", "temp": 25}
         ]
    ]
]
suma_temperatura = int()
peomedio_semanal = int()
c = int()
x = int()
for ciudad in temperaturas:
    x = x + 1
    if x == 1:
        print("temperatura promedio de cuenca es: ")
    if x == 2:
        print("temperatura promedio de azogues es: ")
    if x == 3:
        print("temperatura promedio de biblian es: ")
    for semana  in ciudad:
        c = c + 1
        for dia in semana:
            suma_temperatura = suma_temperatura + dia["temp"]
        promedio_semanal = suma_temperatura / 7
        print(f"la semana {c}, tuvo un promedio  {promedio_semanal}, grados")
        suma_temperatura = 0
    c=0