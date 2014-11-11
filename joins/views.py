from django.shortcuts import render, HttpResponseRedirect

from .forms import EmailForm, joinForm
from .models import join

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

import uuid

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = join.objects.get(ref_id=ref_id)
		get_ref_id()	
	except:
		return ref_id

def share(request, ref_id):
	#print ref_id
	try:
		join_obj = join.objects.get(ref_id=ref_id)
		friends_referred = join.objects.filter(friend=obj)
		count = join_obj.referral.all().count()
		ref_url = "http://fmlanding.herokuapp.com/?ref=%s" %(join_obj.ref_id
		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request, template, context)
	except:
		raise HTTP404
	

def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = join.objects.get(id = join_id)
	except:
		obj = None

	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = join.objects.get_or_create(email = email)
	form = joinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)

		email = form.cleaned_data['email']
		new_join_old, created = join.objects.get_or_create(email = email)
		if created:
			new_join_old.ref_id = get_ref_id()
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip = get_ip(request)
			new_join_old.save()
		print join.objects.filter(friend=obj).count()

		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		# new_join.ip = get_ip(request)
		# new_join.save()
		# print new_join_old.timestamp

	context = {"form":form}
	template = "home.html"
	return render(request, template, context)