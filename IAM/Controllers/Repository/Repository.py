#Below code was learnt on https://pynative.com/python-mysql-database-connection/


import psycopg2

            
def getHome(model):

    connection = psycopg2.connect(
                                    dbname='d5v1s0dmp6evba',
                                    user='swiocjfrjrjerz',
                                    password='3d5f3d65e6eedfb5149006884c8813311dcedccbfa301c122b71318c8eb0ae72',
                                    host='ec2-44-194-4-127.compute-1.amazonaws.com')
    try:

        sql_select_Query = "select * from home"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            model.title = row[1]
            model.description = row[2]
    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    
    return model

def getAbout(model):
    connection = psycopg2.connect(
                                    dbname='d5v1s0dmp6evba',
                                    user='swiocjfrjrjerz',
                                    password='3d5f3d65e6eedfb5149006884c8813311dcedccbfa301c122b71318c8eb0ae72',
                                    host='ec2-44-194-4-127.compute-1.amazonaws.com')
    try:
        sql_select_Query = "select * from about"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            model.title = row[1]
            model.description = row[2]
    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    
    return model
