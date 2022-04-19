from django.shortcuts import render
from ...Models.HomeModel import HomeModel, AboutModel
from ..Repository import Repository
from ...Secrets_Manager import Crypto_Bytes
from ...Secrets_Manager import Vernam_Cipher
import secrets


def home(request):
    model = HomeModel.Home()
    model = Repository.getHome(model)
    context = {'title': model.title,
               'description': model.description}
    return render(request,'home.html', context)


def about(request):
    model = AboutModel.About()
    model = Repository.getAbout(model)
    context = {'title': model.title,
               'description': model.description}
    return render(request,'about.html', context)