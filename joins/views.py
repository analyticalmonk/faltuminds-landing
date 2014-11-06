from django.shortcuts import render

from .forms import EmailForm, joinForm
from .models import join

def home(request):
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = join.objects.get_or_create(email = email)
	form = joinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)

		email = form.cleaned_data['email']
		new_join_old, created = join.objects.get_or_create(email = email)
		print new_join_old.timestamp

	context = {"form":form}
	template = "home.html"
	return render(request, template, context)