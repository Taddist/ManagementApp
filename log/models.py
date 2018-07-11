from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class Souspole(models.Model):
        typesouspole=models.CharField(max_length=100,blank=True)
        def __str__(self):
                return self.typesouspole

class Pole(models.Model):
        typepole=models.CharField(max_length=100,blank=True)
        souspole=models.ForeignKey(Souspole,unique=False,on_delete=models.CASCADE,)
        def __str__(self):
                return '%s, %s' % (self.typepole, self.souspole)

class Contrat(models.Model):
        typecontrat=models.CharField(max_length=200)
        def __str__(self):
                return self.typecontrat

class Role(models.Model):
        role=models.CharField(max_length=200)
        def __str__(self):
                return self.role

class Situation(models.Model):
        situation=models.CharField(max_length=200)
        def __str__(self):
                return self.situation

class UserProfile(models.Model):
	user=models.ForeignKey(User,unique=True,on_delete=models.CASCADE,)
	matricule=models.CharField(max_length=20)
	cin=models.CharField(max_length=20)
	age=models.PositiveIntegerField()
	date_embauche=models.DateField()
	contrat=models.ForeignKey(Contrat,unique=False,on_delete=models.CASCADE,)
	role=models.ForeignKey(Role,unique=False,on_delete=models.CASCADE,)
	situation=models.ForeignKey(Situation,unique=False,on_delete=models.CASCADE,)
	enfant=models.IntegerField()
	pole=models.ForeignKey(Pole,unique=False,on_delete=models.CASCADE,)
	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)

class Conge(models.Model):
	user=models.ForeignKey(User,unique=False,on_delete=models.CASCADE,)
	nbrjour=models.PositiveIntegerField()
	valide=models.PositiveIntegerField(default=0)
	datedebutconge=models.DateField()
	datedemande=models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
                 return '%s %s' % (self.user.first_name, self.user.last_name)


class Raison(models.Model):
        id_raison=models.IntegerField(primary_key =True)
        raisons=models.CharField(max_length=50)
        def __str__(self):
                return self.raisons
                
class Synthese(models.Model):
        user=models.ForeignKey(User,unique=False,on_delete=models.CASCADE,)
        jour=models.DateField()
        entree=models.TimeField()
        pause=models.TimeField()
        sortie=models.TimeField()
        def __str__(self):
                return '%s %s' % (self.user.first_name, self.user.last_name)
        

class Typedocument(models.Model):
        id_type=models.IntegerField(primary_key =True)
        types=models.CharField(max_length=100)
        def __str__(self):
               return self.types

class Document(models.Model):
        user=models.ForeignKey(User,unique=False,on_delete=models.CASCADE,)
        datedemande=models.DateTimeField(auto_now_add=True, blank=True)
        valide=models.PositiveIntegerField(default=0)
        typedocument=models.ForeignKey(Typedocument,unique=False,on_delete=models.CASCADE,)
        def __str__(self):
               return '%s %s %s %s ' % (self.user.first_name, self.user.last_name,self.typedocument,self.datedemande )
     
class Nonactivite(models.Model):
        user=models.ForeignKey(User,unique=False,on_delete=models.CASCADE,)
        raison=models.ForeignKey(Raison ,unique=False,null=True,on_delete=models.CASCADE,)
        date_debut=models.DateField(null=True)
        nbr_jour=models.PositiveIntegerField(null=True)
        def __str__(self):
                return '%s %s' % (self.user.first_name, self.user.last_name)

class TrashConge(models.Model):
    user=models.ForeignKey(User,unique=False,on_delete=models.CASCADE,)
    nbrjour=models.PositiveIntegerField()
    datesupprime=models.DateTimeField(auto_now_add=True, blank=True)
    datedebutconge=models.DateTimeField()
    raison=models.TextField()

    def __str__(self):
                 return '%s %s' % (self.user.first_name, self.user.last_name)

class Salaire (models.Model):
    salaire=models.PositiveIntegerField()
    document=models.ForeignKey(Document,unique=True,on_delete=models.CASCADE,)
    def __str__(self):
            return '%s %s' % (self.document.datedemande, self.document.typedocument.types)

