def profile(request):
	if request.method=="POST":
		form=ProfileForm(request.POST)
		if form.is_valid():
			profile=form.save(commit=False)
			profile.user_id=request.user.id
			if profile.moyenne_bac>9:
				if (profile.date_naissance).year>1995 and (profile.date_naissance).year<2000:
					if (profile.tel).startswith('06'):
							profile.save()
							envoi=True
							form=ProfileForm()
					else: 
						erreurT=True
				else:
					erreurDN=True
			else:
				erreurMB=True
	else:
		form=ProfileForm()
	lastname=request.user.last_name
	firstname=request.user.first_name
	return render (request,"profile.html",locals())

