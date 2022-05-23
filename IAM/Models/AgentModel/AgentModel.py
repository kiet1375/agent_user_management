from django import forms

class User_Agent():
    agent_id=""
    first_name=""
    last_name=""
    email=""

class Create_Agent(forms.Form):
    first_name= forms.CharField(max_length = 30)
    last_name= forms.CharField(max_length = 30)
    email= forms.CharField(max_length = 50)

class Complete_Update_Agent(forms.Form):
    agent_id= forms.CharField(max_length = 128)
    first_name= forms.CharField(max_length = 30)
    last_name= forms.CharField(max_length = 30)
    email= forms.CharField(max_length = 50)

class Update_Agent(forms.Form):
    agent_id= forms.CharField(max_length = 128)