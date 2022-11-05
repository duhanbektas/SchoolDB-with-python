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
        print('DB connection closed.')


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
        print('hata:', err)
    finally:
        connection.close()
        print('DB connection closed.')



list = []
while True:
    name = input('product name: ')
    price = float(input('product price: '))
    imageUrl = input('product image: ')
    description = input('product description: ')

    list.append((name, price, imageUrl, description))

    result = input('Continue? (y/n):')
    if result == 'n':
        print('Your entries are passing on to Database')
        print(list)
        insertProducts(list)
        break

# insertProduct(name, price, imageUrl, description)
