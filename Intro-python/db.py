import mysql.connector
mydb = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'Agranxa8',
    database = 'prueba',
    )


cursor = mydb.cursor()


#Listar Datos

cursor.execute('select * from Usuario ')
resultado = cursor.fetchall()
print(resultado)


mydb.commit()


"""
#actualizar datos
sql = 'update Usuario set email = %s where edad = %s'
values = ('micorrero@correo.com',45)
cursor.execute (sql, values)

mydb.commit()


#print(cursor,rowcount)
#print(cursor,rowcount)
#print(resultado)

_________________________________________________________________________________
#Ver definiciones de tablas
#cursor.execute('show create table usuario')
__________________________________________________________________________________
#insertar datos
sql = 'insert into Usuario(email, username, edad) values(%s, %s,%s)'
values = ('micorreo@correo.com', 'nombreusuario',45)
#cursor.execute(sql, values)
#mydb.commit()
resultado = cursor.fetchall()
#print (cursor.rowcount)
___________________________________________________________________________________
#Eliminar datos
sql = 'delete from Usuario where id = %s'
values = (11, )
cursor.execute(sql, values)
mydb.commit()
______________________________________________________________________________________

__________________________________________________________________________________________



#actualizar datos
sql = 'update Usario set email = %s where id = %s'
values = ('micorrero@correo.com',4)
cursor.execute (sql, values)

midb.commit()


#print(cursor,rowcount)
"""