from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def prediction(request):
    if request.method == 'POST':
        #photo = request.FILES.get('photo')
        pass
    
    if request.user.admin and request.user.staff:
        return render(request, 'facedetection.html')
    else:
        raise Http404