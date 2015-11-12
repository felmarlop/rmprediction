'''
Created on 29 de oct. de 2015

@author: PC1
'''
from bigml.api import BigML
import json
api = BigML('felmarlop', '0b4b8f7e1c73500796bc00b974518b571abf752f')

def list_teams(dataset):
    salida =[]
    lists = dataset['object']['fields']['000006']['summary']['categories']
    for l in lists:
        if l[0] != "Real Madrid":
            salida.append(tuple((l[0], l[0])))
    return sorted(salida)

def list_referees(dataset):
    salida =[]
    lists = dataset['object']['fields']['000001']['summary']['categories']
    for l in lists:
        salida.append(tuple((l[0], l[0])))
    return sorted(salida)

def prediction(rm, other, day, referee, model):
    if rm == "Home":
        local = "Real Madrid"
        visitante = other
    else:
        local = other
        visitante = "Real Madrid"
    predic = api.create_prediction(model, {'Eq. Local': local, 'Eq. Visitante': visitante, 'Fecha.day-of-week': day,'Arbitro': referee}, {'name': local+" "+visitante})
    predicJSON = json.dumps(predic, default=lambda o: o.__dict__)
    valoresPredic = json.loads(predicJSON)
    obj = valoresPredic['object']['objective_field']
    res = str(valoresPredic['object']['prediction'][obj])
    per = str(round(valoresPredic['object']['confidence']*100, 2))
    
    return [res, per]
    
    