from django.shortcuts import render

# Create your views here.
def Filter(request):
    d={'date':'Im a Good Boy','a':6}
    return render(request,'filter.html',d)