from django.shortcuts import render,redirect
from .models import Formulaire,Article
from .forms import FormulaireForm
from .programs import traitement
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
        form = FormulaireForm(request.POST)
        
        if form.is_valid():
            submitted_text = form.cleaned_data['content']
            result = traitement.process_data(submitted_text)
            request.session['processed_data'] = result  # Stockage du résultat dans la session
            form.save()
            return redirect('resultats')

    else:
        form = FormulaireForm()

    return render(request, 'blog/template_name.html', {'form': form, 'result': result})

def resultats(request):
    result = request.session.get('processed_data', '')  # Récupération des données; retourne une chaîne vide si non trouvée
    return render(request, 'blog/resultats.html', {'result': result})

