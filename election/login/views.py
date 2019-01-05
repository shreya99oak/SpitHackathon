from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from login.models import Voters
# Create your views here.
def index(request):
	# return render(request , "./login/login_view.html")
	if request.method=='POST':
		first_name = request.POST['first_name']
		password = request.POST['password']
		user = authenticate(username=first_name,password=password)
		if user is not None:
				login(user)
				return render(request, )
		return HttpResponse(request,'fail')

	else:
		return render(request,'login_view.html')


	try:
		voter = Voters.objects.create(first_name , age)
		voter.save()
		response = { 'status':1 , 'message': "Request done"}
	except Exception as e:
		response = {'status':0 , 'message': "Request not done"}

	return HttpResponse(response , mimetype = 'application/json')	

def returnlogin(request):
	return HttpResponse("<H2> This is login </H2>")
