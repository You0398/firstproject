from django.shortcuts import render
from .models import Article, Entree, Sortie


def etat(request):
    solde = []
    for p in Article.objects.raw('SELECT * FROM stock_article'):
        article = p.nom
        article_id = p.id
        e = Entree.objects.raw(
            'SELECT article_id as id,   sum(quantite) as quantite FROM stock_entree where article_id = '+str(article_id))
        s = Sortie.objects.raw(
            'SELECT article_id as id,sum(quantite) as quantite FROM stock_sortie where article_id = '+str(article_id))

        qe = 0 if e[0].quantite is None else e[0].quantite
        qs = 0 if s[0].quantite is None else s[0].quantite

        solde.append({'id': article_id, 'article': article, 'entree': qe,
                      'sortie': qs, 'solde': qe-qs})
    return render(request=request, template_name='index.html', context={'data': solde})

