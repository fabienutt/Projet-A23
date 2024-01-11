from datetime import datetime
from django.http import FileResponse, HttpResponse
from django.shortcuts import render,redirect
from .models import Formulaire,Article,Shape
from .forms import *
from .programs import modelsgenerations, traitement
import pandas as pd
import json
import subprocess
import os
import mimetypes

def blog_index(request):
    articles = Article.objects.all()
    data = {'articles': articles}
    return render(request, 'blog/blog_index.html', data)

def article(request, name):
    try:
        article = Article.objects.get(title=name)
        data = {'article': article }
    except:
        data = {'message': 'l\'article demandé n\'existe pas'}
    return render(request, 'blog/article.html', data)


def new_view(request):
    result=""
    if request.method == 'POST':
        form=FormulaireForm(request.POST)
        if form.is_valid():
            
            submitted_text = form.cleaned_data['content']
            #result = traitement.process_data(submitted_text)
            request.session['processed_data'] = result  # Stockage du résultat dans la session
            form.save()
            return redirect('resultats')

    else:
        form = FormulaireForm()

    return render(request, 'blog/template_name.html', {'form': form, 'result': result})

def resultats(request):
    result = request.session.get('processed_data', '')  # Récupération des données; retourne une chaîne vide si non trouvée
    return render(request, 'blog/resultats.html', {'result': result})


def my_view(request):
    
    inspection_form = InspectionForm()
    transport_form = TransportForm()
    manipulation_form = ManipulationForm()
    terr_form = TerrestreForm()
    air_form = AirForm()
    aqua_form = AquaForm()
    choice_form = ChoiceForm()
    context = {
        'inspection_form': inspection_form,
        'transport_form': transport_form,
        'manipulation_form': manipulation_form,
        'terrestre_form': terr_form,
        'air_form': air_form,
        'aqua_form': aqua_form,
        'choice_form': choice_form,
    }
    if request.method == 'POST':
        inspection_form = InspectionForm(request.POST or None)
        transport_form = TransportForm(request.POST or None)
        manipulation_form = ManipulationForm(request.POST or None)
        terr_form = TerrestreForm(request.POST or None)
        air_form = AirForm(request.POST or None)
        aqua_form = AquaForm(request.POST or None)
        choice_form = ChoiceForm(request.POST or None)
        
        inspection_data = get_form_data_or_default(inspection_form, {'content': ''})
        transport_data = get_form_data_or_default(transport_form, {})
        manipulation_data = get_form_data_or_default(manipulation_form, {'content2': ''})
        terr_data = get_form_data_or_default(terr_form, {})
        air_data = get_form_data_or_default(air_form, {})
        aqua_data = get_form_data_or_default(aqua_form, {})
        choice_data = get_form_data_or_default(choice_form, {'intsaisie': 0, 'floatsaisie': 0.0})
    
        data = {
            'inspection_form': inspection_data,
            'transport_form': transport_data,
            'manipulation_form': manipulation_data,
            'terrestre_form': terr_data,
            'air_form': air_data,
            'aqua_form': aqua_data,
            'choice_form': choice_data,
        }
        print(data)
        ###### GENERATION DES PIECES
        prompt=prompt2=""
        dim=data["choice_form"]["floatsaisie"]
        if data['transport_form']["type_vehicule"]=="Aquatique" :
            prompt=data['aqua_form']['votre_champ_radio']+" Aquatic with a size of : "+str(data["choice_form"]["floatsaisie"]) + " cm "
            prompt2= f"aquatic robot chassis {10*dim}"
            
            path1=modelsgenerations.generation(getdate(),prompt)
            #path2=modelsgenerations.generation(getdate(),prompt2)
        elif data['transport_form']["type_vehicule"]=="Terrestre":
            prompt=data['terrestre_form']['votre_champ_radio']+" terrestrial with a size of: "+str(data["choice_form"]["floatsaisie"]) + " cm "
            prompt2= f"ground robot chassis {10*dim}"
            
            path1=modelsgenerations.generation(getdate(),prompt)
           # path2=modelsgenerations.generation(getdate(),prompt2)
        elif data['transport_form']["type_vehicule"]=="Aérien":
            prompt=data['air_form']['votre_champ_radio']+" Aerial with a size of : "+str(data["choice_form"]["floatsaisie"]) + " cm "
            prompt2= f"aerial robot chassis {10*dim}"
            
            path1=modelsgenerations.generation(getdate(),prompt)
           # path2=modelsgenerations.generation(getdate(),prompt2)

        print(data)
        #######
        data['path1']=path1
        #data['path2']=path2

        with open('blog/programs/data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        request.session['data'] = str(data)
        request.session['path1'] = str(data['path1'])
        #request.session['path2'] = str(data['path2'])
        print(str(data['transport_form']))
        return redirect('confirmation') 
    else:
        
        return render(request, 'blog/template.html', context)

def confirmation(request):
    result = request.session.get('data', '')
    final=traitement.process_data(result)
    final=str(final).replace(',',' ')
    final=final.replace('(','')
    final=final.replace(')','')
    final=final.replace("'","")
    return render(request, 'blog/confirmation.html',{'result':final})



def download_page(request):
    result = request.session.get('path1', '')
    file_path = result
    file_name = os.path.basename(file_path)
    return render(request, 'blog/3D.html',{'file':file_name})

def download_file(request):
    result = request.session.get('path1', '') #path2 a mettre quans resolu
    print(result)
    file_path = result
    file_name = os.path.basename(file_path)
    fl = open(file_path, 'r')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response
def download_file1(request):
    result = request.session.get('path1', '')
    print(result)
    file_path = result
    file_name = os.path.basename(file_path)
    fl = open(file_path, 'r')
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response

def get_form_data_or_default(form, default_values):
    
    if form.is_valid():

        return form.cleaned_data
    else:
        return default_values
    

def getdate():
    # Récupération de la date et de l'heure actuelles
    now = datetime.now()
    # Conversion en string avec le format souhaité
    formatted_date = now.strftime('%Y%m%d%H%M%S')
    return formatted_date