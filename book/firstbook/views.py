import os
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.models import User

from userprofile.models import UserRole
from .models import Apply

from .models import application
from django.http import HttpResponse
from .models import FilesAdmin
def index(request):
    return render(request,'firstbook/index.html')
def mayor(request):
    return render(request,'firstbook/mayor.html')





def registration(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        first_name = method_dict.get('first_name')
        usertype = method_dict.get('usertype')
        last_name = method_dict.get('last_name')
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken!')
                else:
                    user = User.objects.create_user(username=username,
                                             password=password,
                                             first_name=first_name,
                                             last_name=last_name,
                                             email=email
                                             )
                    UserRole.objects.create(user=user, role=usertype)
                    messages.success(request, 'You are successfully registered!')
                    return HttpResponseRedirect(reverse('registration'))
        else:
            messages.error(request, 'Password does not match!')

        return HttpResponseRedirect(reverse('registration'))

    #	return redirect('user-register') # not standard


    return render(request,'firstbook/registration.html')
def application(request):
    if request.method=="POST":
        name1=request.POST['name']
        phone = request.POST['phone']
        postcode=request.POST['postcode']
        type=request.POST['type']
        price=request.POST['price']
        payment=request.POST['payment']
        app=application(name=name1,phone=phone,postcode=postcode,type=type,price=price,payment=payment)
        app.save()
    return render(request,'firstbook/application.html')
def login(request):

    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in!')
            # return HttpResponseRedirect(reverse('index'))
            if request.user.userrole.role == 'mayor':
                return render(request,'firstbook/button.html')
            elif request.user.userrole.role == 'councilor':
                return render(request,'firstbook/index.html')
            elif request.user.userrole.role == 'public':
                return render(request,'firstbook/application.html')
        else:
            messages.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(reverse('login'))

    return render(request,'firstbook/login.html')
def new(request):
    if request.method=="POST":
        throwby1 = request.POST['throwby']
        name = request.POST['name']
        email= request.POST['email']
        phone1 = request.POST['phone']
        Application_Type= request.POST['ovi']
        address = request.POST['address']
        WardNO= request.POST['WardNO']
        Messerment=request.POST['comment']


        payment=request.POST['payment']
        cheek=Apply(throwby=throwby1,a_name=name,a_email=email,a_phone=phone1,a_type=Application_Type,a_adress=address,a_ward=WardNO,a_messur=Messerment,a_pyment=payment)
        cheek.save()
        send_mail(
            'Insert your application ',
            'Thank you for contacting us. We Will contact you soon. DJRE Team.',
            settings.EMAIL_HOST_USER,
            [request.user.email, settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('index'))
    else:
        return  render(request,'firstbook/new.html')



"""def viewlist(request):
    return render(request,'firstbook/view.html')"""
def home(request):
	context={'file':FilesAdmin.objects.all()}
	return render(request,'firstbook/view.html',context)


def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminupload")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

	raise Http404
