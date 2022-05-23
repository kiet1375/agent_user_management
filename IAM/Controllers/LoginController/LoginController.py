from django.views.decorators.csrf import csrf_protect 
import psycopg2
from django.shortcuts import render, redirect, HttpResponsePermanentRedirect, HttpResponse
from ...Models.LoginModel import LoginModel
from ...SecretsManager import Vernam_Cipher



class loginModel():
   user_id = ""
   password = ""
   email =""
   role_id = ""
   is_dorment = ""

class secretModel():
   secret_id = ""
   secret = ""
   creation_date = ""

@csrf_protect 
def login(request):
   if request.session.has_key('user_id'):
     return redirect('https://agentusermanagement.herokuapp.com/home')
   else:
      return render(request,'login.html')
      


def getCredentials(email):
   connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection("f$f6rwgd;b/%;<"),
                                    user= Vernam_Cipher.decryptDbConnection("pvsn{|cdsvvw||"),
                                    password= Vernam_Cipher.decryptDbConnection("2#g5{4=?1`(vio:p?`cd'bpu%5+h$v5la4'4$'71g4fmw.ba>il:&e3ggbb? p"),
                                    host= Vernam_Cipher.decryptDbConnection('gt3(/6)3.7($%:9?njjrgup;&"zcuhkfd{c#qxl'))
   model = loginModel()
   try:
        sql_select_Query = "SELECT * FROM users;"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
         model.user_id = row[0]
         model.password = row[1]
         model.email = row[2]
         model.role_id= row[3]
         model.is_dorment = row[4]
   except e:
      print("Failed to create table in MySQL: {}".format(e))
   finally:
      if connection is not None:
            connection.close()
            cursor.close()

   return model


def getSecret(userId):
   connection = psycopg2.connect(
                                    dbname= Vernam_Cipher.decryptDbConnection("f$f6rwgd;b/%;<"),
                                    user= Vernam_Cipher.decryptDbConnection("pvsn{|cdsvvw||"),
                                    password= Vernam_Cipher.decryptDbConnection("2#g5{4=?1`(vio:p?`cd'bpu%5+h$v5la4'4$'71g4fmw.ba>il:&e3ggbb? p"),
                                    host= Vernam_Cipher.decryptDbConnection('gt3(/6)3.7($%:9?njjrgup;&"zcuhkfd{c#qxl'))
   model = secretModel()
   try:
        sql_select_Query = "SELECT * FROM secrets;"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
         model.secret_id = row[0]
         model.secret = row[1]
         model.creation_date = row[2]
   except e:
      print("Failed to create table in MySQL: {}".format(e))
   finally:
      if connection is not None:
            connection.close()
            cursor.close()

   return model


def loginPost(request):
   email = ""
   password = ""
   userModel =""
   secretModel=""
   
   if request.method == "POST":

      LoginForm = LoginModel.LoginForm(request.POST)
      
      if LoginForm.is_valid():
         email = LoginForm.cleaned_data['email']
         password = LoginForm.cleaned_data['password']
         userModel = getCredentials(email)
         secretModel = getSecret(userModel.user_id)
         array = secretModel.secret.split('#')
         T3 = list(map(int, array[:-1]))
         de = Vernam_Cipher.encryptOrDecrypt(T3, userModel.password)
         sa = ""
         
         for i in de:
            sa += str(chr(i))
         
         if sa == password:
            request.session['user_id'] = userModel.user_id
            request.session['state'] = 'Logg_off'
            return redirect("https://agentusermanagement.herokuapp.com/home")
         else:
            return HttpResponsePermanentRedirect("https://agentusermanagement.herokuapp.com?error")


def logout(request):
   try:
      del request.session['user_id']
      del request.session['state']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")