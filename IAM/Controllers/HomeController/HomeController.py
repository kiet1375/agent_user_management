import requests
from django.shortcuts import render
from ...Models.HomeModel import HomeModel, AboutModel
from ..Repository import Repository
from ...Controllers.AgentController import AgentController




def home(request):
    model = HomeModel.Home()
    model = Repository.getHome(model)
    state = 'Log_off'
    agents = AgentController.getAgents()
    context = {'state': state,
               'title': model.title,
               'description': model.description,
               'agents': agents}
    return render(request,'home.html', context)


def about(request):
    model = AboutModel.About()
    model = Repository.getAbout(model)
    context = {'title': model.title,
               'description': model.description}
    return render(request,'about.html', context)