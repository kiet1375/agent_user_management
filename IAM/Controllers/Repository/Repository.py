#Below code was learnt on https://pynative.com/python-mysql-database-connection/
import psycopg2
from ...SecretsManager import Vernam_Cipher


            
def getHome(model):

    conn = {'dbname':'','user':'','password':'','host':''}

    connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection("f$f6rwgd;b/%;<"),
                                    user= Vernam_Cipher.decryptDbConnection("pvsn{|cdsvvw||"),
                                    password= Vernam_Cipher.decryptDbConnection("2#g5{4=?1`(vio:p?`cd'bpu%5+h$v5la4'4$'71g4fmw.ba>il:&e3ggbb? p"),
                                    host= Vernam_Cipher.decryptDbConnection('gt3(/6)3.7($%:9?njjrgup;&"zcuhkfd{c#qxl'))

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
                                    dbname= Vernam_Cipher.decryptDbConnection("f$f6rwgd;b/%;<"),
                                    user= Vernam_Cipher.decryptDbConnection("pvsn{|cdsvvw||"),
                                    password= Vernam_Cipher.decryptDbConnection("2#g5{4=?1`(vio:p?`cd'bpu%5+h$v5la4'4$'71g4fmw.ba>il:&e3ggbb? p"),
                                    host= Vernam_Cipher.decryptDbConnection('gt3(/6)3.7($%:9?njjrgup;&"zcuhkfd{c#qxl'))
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
