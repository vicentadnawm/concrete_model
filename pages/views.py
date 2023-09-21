from django.shortcuts import render
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle
# Create your views here.
def home(request):
    path="pages/concrete_model.pk"
    params=['Cement', 'Blast Furnace Slag', 'Fly Ash', 'Water', 'Superplasticizer',
       'Coarse Aggregate', 'Fine Aggregate', 'Age']
    if(request.method=="POST"):
        forest=pickle.load(open(path,"rb"))
        data=request.POST
        
        predictor=set_parameters(data)
        results=forest.predict([predictor[0]])
       
        new=round(results[0],2)
        context={"data":new,"default":predictor[1]}
        return render(request,"index.html",context)
    new=None
    context={"data":new,"params":params,"default":None}
    return render(request,"index.html",context)

def set_parameters(data):
    params=['cement', 'blast_furnace_slag', 'fly_ash', 'water', 'superplasticizer',
        'coarse_aggregate', 'fine_aggregate', 'age']
    total_params=params
    
    data_set=[]
    data_set2={}
    for param in total_params:
        val=data.get(param,0)
        val=eval(val)
        if(val==''):
            val=0
        data_set2[param]=val
        data_set.append(val)
    
    return [data_set,data_set2]