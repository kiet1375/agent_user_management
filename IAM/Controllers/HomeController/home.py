from django.shortcuts import render
from ...Models.HomeModel import HomeModel, AboutModel
from ..Repository import Repository
from ...SecretsManager import Crypto_Bytes, Vernam_Cipher



def home(request):
    key = Crypto_Bytes.generateSecret()
    text = "test that is not encypted."
    en = Vernam_Cipher.encryptOrDecrypt(key,text)
    ent=""
    for i in en:
        ent+= str(chr(i))
    de = Vernam_Cipher.encryptOrDecrypt(key, ent)
    fi = ""
    for i in de:
        fi+= str(chr(i))
    model = HomeModel.Home()
    model = Repository.getHome(model)
    context = {'title': ent,
               'description': fi}
    return render(request,'home.html', context)


def about(request):
    model = AboutModel.About()
    model = Repository.getAbout(model)
    context = {'title': model.title,
               'description': model.description}
    return render(request,'about.html', context)