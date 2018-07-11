#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import UserProfile , Conge ,Raison ,Synthese ,Nonactivite,Typedocument,Document,Pole,Contrat,Role,Situation,TrashConge,Salaire
from django.core.exceptions import ValidationError
# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
class SyntheseForm(forms.ModelForm):

    class Meta:
        model= Synthese
        fields=('jour','entree','pause','sortie',)
        labels = {
            'jour': ("Date du jour **"),
            'entree': ("Heure d'entrée"),
            'pause':("Pause déjeuner"),
            'sortie':("Heure de sortie"),
                 }
  


class CongeForm(forms.ModelForm):

    class Meta :
        model= Conge
        fields=('nbrjour','datedebutconge')
        labels = {
            'nbrjour': ("Nombre de jour*"),
            'datedebutconge': ("Date debut du congé"),
                 }
  

    
        

class DocumentForm(forms.ModelForm):

     class Meta:
         model= Document
         fields=('typedocument',)
         labels={
            'typedocument':("Type de document demandé "),
                }



class NonactiviteForm(forms.ModelForm):

     class Meta:
         model= Nonactivite
         fields=('raison','date_debut','nbr_jour',)
         labels={
            'raison':("Motif d'absence "),
            'date_debut':("Date debut d'absence "),
            'nbr_jour':("nombre de jour d'absence"),
                }

class TrashCongeForm(forms.ModelForm):

     class Meta:
         model= TrashConge
         fields=('raison',)
         labels={
            'raison':(""),
                }

class SalaireForm(forms.ModelForm):
    class Meta:
         model=Salaire
         fields=('salaire',)
         labels={
            'salaire':("salaire"),
         }
