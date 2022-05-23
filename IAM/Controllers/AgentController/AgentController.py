import hashlib, os, time, datetime,psycopg2
from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from ...Models.AgentModel import AgentModel
from ...SecretsManager import Vernam_Cipher
from ...Models.DbConnection import DbConnection


def getAgents():
    
    dbConnection = DbConnection.DbConnection()
    models = []
    connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection(dbConnection.dbname),
                                    user= Vernam_Cipher.decryptDbConnection(dbConnection.user),
                                    password= Vernam_Cipher.decryptDbConnection(dbConnection.password),
                                    host= Vernam_Cipher.decryptDbConnection(dbConnection.host))

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
            model.email= row[4]
            models.append(model)

    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    
    return models


def getAgent(id):

    dbConnection = DbConnection.DbConnection()
    model = AgentModel.User_Agent()
    connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection(dbConnection.dbname),
                                    user= Vernam_Cipher.decryptDbConnection(dbConnection.user),
                                    password= Vernam_Cipher.decryptDbConnection(dbConnection.password),
                                    host= Vernam_Cipher.decryptDbConnection(dbConnection.host))

    try:

        sql_select_query = """select * from user_agents where agent_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        for row in records:
            model = AgentModel.User_Agent()
            model.agent_id = row[0]
            model.first_name = row[1]
            model.last_name= row[2]
            model.email= row[4]

    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    
    return model

def completeCreateAgent(agentid, firstname, lastname, email):

    dbConnection = DbConnection.DbConnection()
    connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection(dbConnection.dbname),
                                    user= Vernam_Cipher.decryptDbConnection(dbConnection.user),
                                    password= Vernam_Cipher.decryptDbConnection(dbConnection.password),
                                    host= Vernam_Cipher.decryptDbConnection(dbConnection.host))
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    
    try:


        sql_select_query = """INSERT INTO user_agents VALUES (%s,%s,%s,%s,%s)"""
        cursor = connection.cursor()
        cursor.execute(sql_select_query, (agentid, firstname, lastname, timestamp,email))
        # Commit the changes to the database
        connection.commit()
        connection.close()
        cursor.close()

    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    return "sucess"

def completeUpdate(userid, firstname,lastname):

    dbConnection = DbConnection.DbConnection()
    model = AgentModel.User_Agent()
    connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection(dbConnection.dbname),
                                    user= Vernam_Cipher.decryptDbConnection(dbConnection.user),
                                    password= Vernam_Cipher.decryptDbConnection(dbConnection.password),
                                    host= Vernam_Cipher.decryptDbConnection(dbConnection.host))

    try:


        sql_select_query = """UPDATE user_agents SET first_name=%s, last_name=%s WHERE agent_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql_select_query, (firstname, lastname, userid))
        # Commit the changes to the database
        connection.commit()
        connection.close()
        cursor.close()
        return "seccess"

    except e:
        print("Failed to create table in MySQL: {}".format(e))
    finally:
        if connection is not None:
            connection.close()
            cursor.close()
    return "failure"



def update(request):

    agentModel = AgentModel.Update_Agent(request.POST)

    if agentModel.is_valid():
        userid = agentModel.cleaned_data['agent_id']
        model = getAgent(userid)    
        context = {'state':"Logoff",
                   'title':"Update",
                   'agent_id': model.agent_id,
                   'first_name': model.first_name,
                   'last_name': model.last_name,
                   'email':model.email}
        return render(request,'update.html', context)
    

def completeAgentUpdate(request):
    
    agentid = request.POST['agent_id']
    firstname = request.POST['first_name']
    lastname= request.POST['last_name']

    completeUpdate(agentid, firstname, lastname)

    return HttpResponsePermanentRedirect("https://agentusermanagement.herokuapp.com/home")

def createUserAgent(request):
    if request.session.get('user_id') == None:
        return redirect('http:127.0.0.1:8080')
    else:
        context = {'state': "logoff",
                   'title': "Create"}
        return render(request,'create.html', context)

def createAgent(request):
    if request.session.get('user_id') == None:
        return redirect('http:127.0.0.1:8080')
    else:
        agentModel = AgentModel.Create_Agent(request.POST)

        if agentModel.is_valid():
            agentid = Vernam_Cipher.generateAgentId()
            firstname = agentModel.cleaned_data['first_name']
            lastname = agentModel.cleaned_data['last_name']
            email = agentModel.cleaned_data['email']
            response = completeCreateAgent(agentid,firstname,lastname,email)
            if(response == 'success'):
               return HttpResponsePermanentRedirect("https://agentusermanagement.herokuapp.com/home?sucess") 
            else:
                return HttpResponsePermanentRedirect("https://agentusermanagement.herokuapp.com/home?failure")
        



