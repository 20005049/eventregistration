from django.shortcuts import render
from .models import participatents,participatentsAdmin
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    context = {}
    return render(request,'eventapp/home.html',context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = participatents()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.email = request.POST.get('phone','-')
        p1.email = request.POST.get('insitution','-')

        if  len(participatents.objects.all())>5:
            return render(request,'eventapp/failed.html',context)
        else:
            p1.save()
            return render(request,'eventapp/success.html',context)
    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['insitution'] = ''


    return render(request, 'eventapp/register.html', context)

def result(request):
    context = {}

    context['participatents'] = participatents.objects.all()

    return render(request, 'eventapp/result.html', context)





