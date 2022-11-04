import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} record(s) added')
        print(f'Last record id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('DB Connection Closed.')

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} record(s) added')
        print(f'Last record id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('DB Connection Closed.')

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")

    try:
        result = cursor.fetchall()    
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('DB Connection Closed.')
        
def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} record(s) updated')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('DB Connection Closed.')

def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    sql = "delete from products where id=%s"
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} record(s) deleted')
    except mysql.connector.Error as err:
        print('Error:', err)
    finally:
        connection.close()
        print('DB Connection Closed.')

deleteProduct(5)
getProducts()
