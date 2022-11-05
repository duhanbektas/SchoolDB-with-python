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
        print('DB Connection closed.')

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
        print('DB Connection closed.')

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password="password", database="node_app")
    cursor = connection.cursor()

    # cursor.execute('Select * From Products')
    cursor.execute('Select name,price From Products')

    # result = cursor.fetchall()    
    result = cursor.fetchone()
    
    print(f'name: {result[0]} price: {result[1]}')

    # for product in result:
    #     # print(f'name: {product[1]} price: {product[2]}')
    #     print(f'name: {product[0]} price: {product[1]}')

getProducts()
