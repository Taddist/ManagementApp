from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime
from datetime import timedelta
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from .models import UserProfile , Conge ,Raison ,Synthese ,Nonactivite,Typedocument,Document,Pole,Contrat,Role,Situation,Souspole,TrashConge ,Salaire
from .forms import SyntheseForm ,CongeForm , DocumentForm ,NonactiviteForm ,TrashCongeForm,SalaireForm
from django.shortcuts import redirect
from reportlab.pdfgen import canvas
from django.db.models import Sum , Count
from django.core.exceptions import ValidationError

@login_required(login_url="login/")
def home(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if request.method == "POST":
        form = SyntheseForm(request.POST)  
        if form.is_valid():
            synthese = form.save(commit=False)
            synthese.user_id = request.user.id 
            if testsynthesesynthese(request,synthese.jour)==0: 
                    if testsyntheseconge(request,synthese.jour)==0:
                        if synthese.jour>=pro.date_embauche  :
                            if (synthese.entree).hour>=8:
                                if (synthese.pause).hour>=12 and (synthese.pause).hour<14:
                                    if (synthese.sortie ).hour<=18:
                                        synthese.save()
                                        envoi=True
                                        form = SyntheseForm()
                                    else :
                                         erreurS=True
                                else :
                                    erreurP=True
                            else :
                                erreurE=True
                        else :
                            erreurD=True 
                    else :
                        erreurDRC=True
            else:
                erreurDRS=True                                                                       
    else:
        form = SyntheseForm()
    now=datetime.datetime.now()
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request,"home.html",locals())

def sommeconge(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==3:
        collaborateur=UserProfile.objects.filter(role_id__exact=1,pole_id__exact=pro.pole_id)
    if pro.role_id==2:
        collaborateur=UserProfile.objects.filter(role_id__exact=3)
    if pro.role_id==1:
        collaborateur=UserProfile.objects.filter(role_id__exact=2)
    if pro.role_id==4:
        collaborateur=UserProfile.objects.filter(role_id__exact=2)
    sommeconge=0
    for c in collaborateur:
            conge=Conge.objects.filter(valide=0,user_id=c.user_id).count()
            sommeconge=sommeconge+conge
    return sommeconge

def sommedocument(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==3:
        collaborateur=UserProfile.objects.filter(role_id__exact=1,pole_id__exact=pro.pole_id)
    if pro.role_id==2:
        collaborateur=UserProfile.objects.filter(role_id__exact=3)
    if pro.role_id==1:
        collaborateur=UserProfile.objects.filter(role_id__exact=2)
    if pro.role_id==4:
        collaborateur=UserProfile.objects.all()
    sommedocument=0
    for c in collaborateur:
            document=Document.objects.filter(valide=0,user_id=c.user_id).count()
            sommedocument=sommedocument+document
    return sommedocument

def testsynthesesynthese(request,dateaverifier):
    z=Synthese.objects.filter(user_id__exact=request.user.id)
    y=0
    for j in z :
        if j.jour==dateaverifier:
              y=1
    return y  

def testsyntheseconge(request,dateaverifier):
    z=Conge.objects.filter(user_id__exact=request.user.id,valide=1)
    y=0
    for j in z :
        for i in range (0,j.nbrjour):
            x=j.datedebutconge+timedelta(days=i)
            if x==dateaverifier:
                 y=1
    return y  
"""
def testsynthesenonactivite(request,dateaverifier):
    z=Nonactivite.objects.filter(user_id__exact=request.user.id)
    y=0
    for j in z :
        for i in range (0,j.nbr_jour):
            x=j.date_debut+timedelta(days=i)
            if x==dateaverifier:
                 y=1
    return y  
"""
def consulterSynthese(request):
    syn=Synthese.objects.filter(user_id__exact=request.user.id).order_by('jour').reverse()
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'consulterSynthese.html',locals())


def collaborateur(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    if pro.role_id==3 :
         collabo=UserProfile.objects.select_related('user').filter(pole_id__exact=pro.pole_id).exclude(user_id__exact=pro.user_id)
         return render(request, 'collaborateur_list.html',locals())
    elif pro.role_id==2:
         return render(request, 'superviseur_list.html',locals())
    else :
         return render(request, 'error.html',locals())

def collaborateur_infos(request,id_collaborateur):
     collabo=UserProfile.objects.select_related('user').get(user_id__exact=id_collaborateur)
     con=Contrat.objects.get(id__exact=collabo.contrat_id)
     situation=Situation.objects.get(id__exact=collabo.situation_id)
     cong=Conge.objects.filter(user_id__exact=collabo.user_id).order_by('datedemande').reverse()
     syn=Synthese.objects.filter(user_id__exact=collabo.user_id).order_by('jour').reverse()
     doc=Document.objects.filter(user_id__exact=collabo.user_id).order_by('datedemande').reverse()
     lastname=request.user.last_name
     firstname=request.user.first_name
     sc=sommeconge(request)
     sd=sommedocument(request)
     pro=UserProfile.objects.get(user_id__exact=request.user.id)
     if pro.role_id==1:
        option=False
     if pro.role_id==2:
        option=True
     if pro.role_id==3:
        option=True
     return render(request, 'collaborateur_infos.html',locals())

def list_collaborateur(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
        return render(request, 'error.html',locals())   
    if pro.role_id==3:
        option=True
        return render(request, 'error.html',locals())
    if pro.role_id==2 :
         collabo=UserProfile.objects.select_related('user').filter(pole_id__exact=pro.pole_id).exclude(user_id__exact=pro.user_id)
         option=True
         return render(request, 'collaborateur_list.html',locals())

def listesouspole(request,var):
    collabo=UserProfile.objects.select_related('user').filter(pole_id__exact=var,role_id__exact=1)
    responsable=UserProfile.objects.filter(pole_id__exact=var,role_id__exact=3)
    pole=Pole.objects.get(id__exact=var)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    return render(request, 'archie.html',locals())

def demandeConge(request):
    info=Conge.objects.filter(user_id__exact=request.user.id)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    somme=0
    for i in info : 
    	somme=somme+i.nbrjour
    if request.method == "POST":
        form = CongeForm(request.POST)
        if form.is_valid():
            conge = form.save(commit=False)
            conge.user_id = request.user.id
            if testsynthese(request,conge.datedebutconge,conge.nbrjour)==0:
                if testconge(request,conge.datedebutconge,conge.nbrjour)==0:
                    if testnonactivite(request,conge.datedebutconge,conge.nbrjour)==0:
                        if conge.nbrjour <= 21-somme : 
                            if pro.role_id==2:
                                conge.valide=1
                                nonactivite=Nonactivite(date_debut=conge.datedebutconge , nbr_jour=conge.nbrjour,raison_id=777,user_id=conge.user_id)
                                nonactivite.save()
                            conge.save()
                            envoi = True
                            form = CongeForm()
                        else :
                            nonenvoi=True
                    else:
                        erreurDRN=True
                else:
                    erreurDRC=True
            else:
                erreurDRS=True                    
    else:
        form = CongeForm()
    lastname=request.user.last_name
    firstname=request.user.first_name
    variable=21-somme
    sc=sommeconge(request)
    sd=sommedocument(request)
    
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'demandeConge.html',locals())

def testsynthese(request,dateavalide,nombre):
    z=Synthese.objects.filter(user_id__exact=request.user.id)
    y=0
    for j in z :
        for i in range (0,nombre):
            x=dateavalide+timedelta(days=i)
            if j.jour==x:
                    y=1
    return y 

def testconge(request,dateavalide,nombre):
    z=Conge.objects.filter(user_id__exact=request.user.id)
    y=0
    for j in z :
        for k in range (0,j.nbrjour):
            w=j.datedebutconge+timedelta(days=k)
            for i in range (0,nombre):
                x=dateavalide+timedelta(days=i)
                if w==x:
                    y=1
    return y

def testnonactivite(request,dateavalide,nombre):
    z=Nonactivite.objects.filter(user_id__exact=request.user.id)
    y=0
    for j in z :
        for k in range (0,j.nbr_jour):
            w=j.date_debut+timedelta(days=k)
            for i in range (0,nombre):
                x=dateavalide+timedelta(days=i)
                if w==x:
                    y=1
    return y

def demandeDocument(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.user_id = request.user.id
            if pro.role_id==2:
                document.valide=1
            document.save()
            envoi = True
            form = DocumentForm()
    else:
        form = DocumentForm()
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'demandeDocument.html',locals())

def etatSortie(request):
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    conge=Nonactivite.objects.select_related('user').filter(user_id__exact=request.user.id)
    document=Document.objects.select_related('typedocument').filter(user_id__exact=request.user.id,valide=1)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'etatSortie.html',locals())

def nonactivite(request):
    if request.method == "POST":
        form = NonactiviteForm(request.POST)
        if form.is_valid():
            nonactivite = form.save(commit=False)
            nonactivite.user_id = request.user.id
            if testsynthese(request,nonactivite.date_debut,nonactivite.nbr_jour)==0:
                    if testnonactivite(request,nonactivite.date_debut,nonactivite.nbr_jour)==0:
                        if nonactivite.raison_id !=777 :
                            nonactivite.save()
                            envoi = True
                            form = NonactiviteForm()
                        else :
                            erreurnonvalide=True
                    else:
                        erreurDRN=True  
            else:
                erreurDRS=True 
    else:
        form = NonactiviteForm()
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'nonactivite.html',locals())


def profile(request):
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    con=Contrat.objects.get(id__exact=pro.contrat_id)
    po=Pole.objects.get(id__exact=pro.pole_id)
    ro=Role.objects.get(id__exact=pro.role_id)
    sit=Situation.objects.get(id__exact=pro.situation_id)
    lastname=request.user.last_name
    firstname=request.user.first_name
    if ro.id==1:
        sc=0
        sd=0
        envoi=True
        option=False
        return render(request, 'profile.html',locals())

    if ro.id==2:
        sc=sommeconge(request)
        sd=sommedocument(request)
        envoi=False
        option=True
        return render(request, 'profile.html',locals())
    if ro.id==3:
        sc=sommeconge(request)
        sd=sommedocument(request)
        envoi=True
        option=True
        return render(request, 'profile.html',locals())
    if pro.role_id==4:
        optiond=True
        envoi=True
        sd=sommedocument(request)
        return render(request, 'profile.html',locals())
    
        

def demandeenattenteconge(request):
    lastname=request.user.last_name
    firstname=request.user.first_name
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    conge=Conge.objects.filter(valide=0).order_by('datedemande').reverse()
    sc=sommeconge(request)
    sd=sommedocument(request)
    if pro.role_id==3 :
         collaborateur=UserProfile.objects.select_related('user').filter(pole_id__exact=pro.pole_id).exclude(user_id__exact=pro.user_id)
         option=True 
         return render(request, 'demandeenattenteconge.html',locals())
    elif pro.role_id==2:
         collaborateur=UserProfile.objects.select_related('user').filter(role_id__exact=3)
         option=True
         return render(request, 'demandeenattenteconge.html',locals())

    else :
         option=False
         return render(request, 'error.html',locals())
 
def validerdemande(request,id_demande):
    conge=Conge.objects.get(id__exact=id_demande)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    id_demande=id_demande
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    return render(request, 'demandevalide.html',locals())

def supprimerdemande(request,id_demande):
    conge=Conge.objects.get(id__exact=id_demande)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    if request.method == "POST":
        form = TrashCongeForm(request.POST)
        if form.is_valid():
            trashconge = form.save(commit=False)
            trashconge.user_id = conge.user.id
            trashconge.datedebutconge=conge.datedebutconge
            trashconge.nbrjour=conge.nbrjour
            trashconge.save()
            conge.delete()
            envoi = True
            form = TrashCongeForm()
            return redirect('/demandeenattenteconge/')  
        else:
            erreur=True                                      
    else:
        form = TrashCongeForm()
    
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    return render(request, 'demandesupprime.html',locals())

def demandeenattentedocument(request):
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==4 :
         collaborateur=UserProfile.objects.select_related('user').all().exclude(user_id__exact=pro.user_id)
         document=Document.objects.select_related('user' ).select_related('typedocument' ).filter(valide=0).order_by('datedemande').reverse().exclude(user_id__exact=pro.user_id)
         optiond=True
         return render(request, 'demandeenattentedocument.html',locals())
    
    else :
         option=False
         return render(request, 'error.html',locals())



def documentenvoyer(request,id_demande):
    document=Document.objects.get(id__exact=id_demande)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'demandevalider.html',locals())


def supprimerdocument(request,id_demande):
    document=Document.objects.get(id__exact=id_demande)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    document.delete()
    envoi = True
    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'supprimerdocument.html',locals())
            
def confirmerdocument(request,id_demande):  
    document=Document.objects.get(id__exact=id_demande)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    if document.typedocument_id==222:
            document.valide=1
            document.save()
            return redirect('/demandeenattentedocument/')
    else :
        if request.method == "POST":
            form = SalaireForm(request.POST)
            if form.is_valid():
                salaire = form.save(commit=False)
                salaire.document_id = id_demande
                salaire.save()
                document.valide=1
                document.save()
                envoi = True
                form = SalaireForm()
                return redirect('/demandeenattentedocument/')
            else:
                erreur=True                                      
        else:
            form = SalaireForm()

    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'confirmerdocument.html',locals())



def documentconge(request,id_demande):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="demande_conge.pdf"'
    salarie=request.user.first_name +' '+ request.user.last_name
    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==2:
             e=pro
             option=True
             employeur=e.user.last_name+' '+e.user.first_name
             
    if pro.role_id==3:
             e=UserProfile.objects.select_related('user' ).get(role_id__exact=2)
             option=True
             employeur=e.user.last_name+' '+e.user.first_name
            
    if pro.role_id==1:
             e=UserProfile.objects.select_related('user' ).get(role_id__exact=3 , pole_id__exact=pro.pole_id)
             option=False
             employeur=e.user.last_name+' '+e.user.first_name
             
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    c=Nonactivite.objects.get(id=id_demande)
    nbrjour=c.nbr_jour
    datedebut=c.date_debut
    datefin=datedebut+timedelta(days=nbrjour-1)
    datejour=datetime.date.today()
    p.setFont('Helvetica',15,leading=None)
    p.drawString(20,750,salarie)
    p.drawString(450,720,employeur)
    p.drawString(250,700,"à Rabat Le ")
    p.drawString(335,700,"%s" %datejour)
    p.setFont('Helvetica',16,leading=None)
    p.drawString(20, 650, "Concerne : Demande en vue de bénéficier de mon congé légal de récréation.")
    p.setFont('Helvetica',11,leading=None)
    p.drawString(20, 600, "Madame / Monsieur,")
    p.drawString(20, 570, "Par la présente, je vous prie de bien vouloir m'accorder")
    p.drawCentredString(295,570,"%s" %nbrjour)
    p.drawString(305,570, "jours de congé pour la période du")
    p.drawString(475, 570,"%s" %datedebut)
    p.drawString(535, 570, "au")
    p.drawString(20, 540, "%s" %datefin)
    p.drawString(20,510,"La présente demande est basée sur l'article L.233-10 du Code du travail." )  
    p.drawString(20,480,"Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
from reportlab.pdfgen import canvas
def documenttravail(request,id_demande):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="demande.pdf"'
    salarie=request.user.first_name +' '+ request.user.last_name
    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==2:
             option=True        
    if pro.role_id==3:
             option=True        
    if pro.role_id==1:
             option=False
    e=UserProfile.objects.select_related('user' ).get(role_id__exact=4)
    employeur=e.user.last_name+' '+e.user.first_name
    
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    
    d=Document.objects.get(id=id_demande)
    p.setFont('Helvetica', 20)
    p.drawString(180,750,"ATTESTATION DE TRAVAIL")
    p.setFont('Helvetica', 12)
    p.drawString(80, 700, "Je/Nous soussigné (es)")
    p.drawString(210, 700, employeur)
    p.drawString(270, 700, "trésorier générale de la Fondation Hassan II pour   ")
    p.drawString(50, 670, "les Marocains Résidants à l'Etranger , atteste/attestons par la présente que")
    p.drawString(455, 670, salarie)
    p.drawString(50, 640, "titulaire de la CIN N°")
    p.drawString(160, 640, e.cin)
    p.drawString(215, 640, ", est salarié au sein de la société du")
    p.drawString(410, 640,"%s" %e.date_embauche)
    p.drawString(475, 640, "à ce jour.")
    p.drawString(80, 590, "Cette attestation est délivrée à l’intéressé (e) pour servir et valoir ce que de droit.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def documentsalaire(request,id_demande):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="demande.pdf"'
    salarie=request.user.first_name +' '+ request.user.last_name
    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==2:
             option=True        
    if pro.role_id==3:
             option=True        
    if pro.role_id==1:
             option=False
    e=UserProfile.objects.select_related('user' ).get(role_id__exact=4)
    employeur=e.user.last_name+' '+e.user.first_name
    
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    d=Salaire.objects.get(document_id=id_demande)
    p.setFont('Helvetica', 18)
    p.drawString(180,750,"ATTESTATION DE SALAIRE ")
    p.setFont('Helvetica', 12)
    p.drawString(50, 700, "Madame, Monsieur,  ")
    p.drawString(50, 670, "Par la présente, j'atteste que Monsieur / Madame ")
    p.drawString(317, 670, salarie)
    p.drawString(390, 670, "occupe au sein de la Fondation")
    p.drawString(50, 640, "Hassan II pour les Marocains Résidants à l'Etranger")
    p.drawString(330, 640, "un poste depuis le")
    p.drawString(430, 640,"%s" %e.date_embauche)
    p.drawString(500, 640,"et reçoit ")
    p.drawString(50,610,"un salaire brut annuel de ")
    p.drawString(185,610,"%s" %d.salaire)
    p.drawString(215,610,"DHS.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def documenttravailsalaire(request,id_demande):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="demande.pdf"'
    salarie=request.user.first_name +' '+ request.user.last_name
    pro=UserProfile.objects.select_related('user' ).get(user_id__exact=request.user.id)
    if pro.role_id==2:
             option=True        
    if pro.role_id==3:
             option=True        
    if pro.role_id==1:
             option=False
    e=UserProfile.objects.select_related('user' ).get(role_id__exact=4)
    employeur=e.user.last_name+' '+e.user.first_name
    
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    x=UserProfile.objects.select_related('contrat' ).get(user_id__exact=request.user.id)
    d=Salaire.objects.get(document_id=id_demande)
    p.setFont('Helvetica', 18)
    p.drawString(20,750,"ATTESTATION DE SALAIRE ET ENGAGEMENT DE L’EMPLOYEUR")
    p.setFont('Helvetica', 12)
    p.drawString(50, 700, "Madame, Monsieur,  ")
    p.drawString(50, 650, "Par la présente, j'atteste que Monsieur / Madame ")
    p.drawString(317, 650, salarie)
    p.drawString(390, 650, "occupe au sein de la Fondation")
    p.drawString(50, 630, "Hassan II pour les Marocains Résidants à l'Etranger")
    p.drawString(330, 630, "un poste depuis le")
    p.drawString(430, 630,"%s" %e.date_embauche)
    p.drawString(450,630," .")
    p.drawString(50, 590,"A ce titre, M. / Mme")
    p.drawString(160, 590, salarie)
    p.drawString(232,590,"bénéficie d'un contrat ")
    p.drawString(358,590,x.contrat.typecontrat)
    p.drawString(480,590,"et reçoit un ")
    p.drawString(50,570,"salaire brut annuel de")
    p.drawString(175,570,"%s" %d.salaire)
    p.drawString(215,570,"DHS.")
    p.drawString(50,520,"Cette attestation est rédigée pour valoir ce que de droit.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def valideconge(request,id_demande):
    conge=Conge.objects.get(id__exact=id_demande)
    lastname=request.user.last_name
    firstname=request.user.first_name
    sc=sommeconge(request)
    sd=sommedocument(request)
    p = Nonactivite.objects.create(date_debut=conge.datedebutconge, nbr_jour=conge.nbrjour, raison_id=777,user_id= conge.user_id)
    p.save()
    conge.delete()
    return redirect('/demandeenattenteconge/')
    pro=UserProfile.objects.get(user_id__exact=request.user.id)
    if pro.role_id==1:
        option=False
    if pro.role_id==2:
        option=True
    if pro.role_id==3:
        option=True
    if pro.role_id==4:
        optiond=True
    return render(request, 'valideconge.html',locals())


    
#p.drawCentredString(500,750,"%s" %variable1)

#"today" : datetime.date.today() la date 

#"lastname=Conge.objects.get(id__exact=5)
#lastname=Conge.objects.get(id__exact=request.user.id)
#sommeconge=Conge.objects.filter(valide=0).count()
#sommedocument=Document.objects.filter(valide=0).count()  

#    datefin=datedebut+timedelta(days=nbrjour-1)
