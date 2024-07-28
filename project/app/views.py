from django.shortcuts import render

# Create your views here.
def home(request):
    data={'name':'surya',
         'city':'bhopal',
        'quli':'MCA',
        'passout':  '2024'
        }
    
    return render(request,'home.html',data )