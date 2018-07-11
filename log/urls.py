# log/urls.py
from django.conf.urls import url
from . import views
app_name = 'log'
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^consulterSynthese/$', views.consulterSynthese, name='consulterSynthese'),
    url(r'^demandeConge/$', views.demandeConge, name='demandeConge'),
    url(r'^demandeDocument/$', views.demandeDocument, name='demandeDocument'),
    url(r'^etatSortie/$', views.etatSortie, name='etatSortie'),
    url(r'^nonactivite/$', views.nonactivite, name='nonactivite'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^demandeenattenteconge/$', views.demandeenattenteconge, name='demandeenattenteconge'),
    url(r'^demandeenattente/valider/(?P<id_demande>[0-9]+)/$', views.validerdemande, name='validerdemande'),
    url(r'^demandeenattente/supprimer/(?P<id_demande>[0-9]+)/$', views.supprimerdemande, name='supprimerdemande'),
    url(r'^demandeenattentedocument/$', views.demandeenattentedocument, name='demandeenattentedocument'),
    url(r'^demandeenattentedocument/(?P<id_demande>[0-9]+)/$', views.documentenvoyer, name='documentenvoyer'),
    url(r'^collaborateur/$', views.collaborateur, name='collaborateur'),
    url(r'^collaborateur/(?P<id_collaborateur>[0-9]+)/$', views.collaborateur_infos, name='collaborateur_infos'),
    url(r'^listesouspole/(?P<var>[0-9]+)/$', views.listesouspole, name='listesouspole'),
    url(r'^documentconge/(?P<id_demande>[0-9]+)/$', views.documentconge, name='documentconge'), 
    url(r'^documenttravail/(?P<id_demande>[0-9]+)/$', views.documenttravail, name='documenttravail'),
    url(r'^documentsalaire/(?P<id_demande>[0-9]+)/$', views.documentsalaire, name='documentsalaire'),
    url(r'^documenttravailsalaire/(?P<id_demande>[0-9]+)/$', views.documenttravailsalaire, name='documenttravailsalaire'),
    url(r'^valideconge/(?P<id_demande>[0-9]+)/$', views.valideconge, name='valideconge'),
    url(r'^supprimerdocument/(?P<id_demande>[0-9]+)/$', views.supprimerdocument, name='supprimerdocument'),
    url(r'^confirmerdocument/(?P<id_demande>[0-9]+)/$', views.confirmerdocument, name='confirmerdocument'),
 ]
