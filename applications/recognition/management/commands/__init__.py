from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404



@login_required
@csrf_exempt
def recognition_view(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')

    if request.user.admin and request.user.staff:
        return render(request, 'facedetection.html')
    else:
        raise Http404
