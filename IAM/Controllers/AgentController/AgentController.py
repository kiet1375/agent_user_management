import psycopg2
from ...Models.AgentModel import AgentModel
from ...SecretsManager import Vernam_Cipher



def getAgents():
    
    models = []

    
    connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection("f$f6rwgd;b/%;<"),
                                    user= Vernam_Cipher.decryptDbConnection("pvsn{|cdsvvw||"),
                                    password= Vernam_Cipher.decryptDbConnection("2#g5{4=?1`(vio:p?`cd'bpu%5+h$v5la4'4$'71g4fmw.ba>il:&e3ggbb? p"),
                                    host= Vernam_Cipher.decryptDbConnection('gt3(/6)3.7($%:9?njjrgup;&"zcuhkfd{c#qxl'))

    try:

        sql_select_Query = "select * from user_agents"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            model = AgentModel.User_Agent()
            model.agent_id = row[0]
            model.first_name = row[1]
            model.last_name= row[2]
            models.append(model)

    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    
    return models