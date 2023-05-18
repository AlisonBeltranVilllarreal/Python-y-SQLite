import sqlite3

conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()

registros = [
    ('25/nov/2016', 'venta', 'AAPL', 10.5, 200),
    ('26/nov/2016', 'compra', 'GOOG', 20.75, 150),
    ('27/nov/2016', 'venta', 'MSFT', 30.25, 300),
    ('28/nov/2016', 'compra', 'AMZN', 18.9, 250),
    ('29/nov/2016', 'venta', 'TSLA', 40.0, 100)
]

c.executemany("INSERT INTO acciones VALUES (?, ?, ?, ?, ?)", registros)

conexion.commit()
conexion.close()
