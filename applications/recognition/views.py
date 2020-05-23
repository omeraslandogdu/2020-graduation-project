from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from applications.recognition.models.user import Attendance, User

from django.http import Http404
from django.shortcuts import render

@login_required
@csrf_exempt
def prediction(request):
    if request.method == 'POST':
        student_name = request.POST.dict()
        student_id = student_name['label']
        try:
            print(student_name)
        except:
            pass

        if request.POST.get('id_type') == 'origin':
            pass
        else:
            pass

    if request.user.admin:
        return render(request, 'facedetection.html')
    else:
        raise Http404


@login_required
@csrf_exempt
def yoklama_alma(request):
    if request.method == 'POST':
        data = request.POST.dict()
        student_id = data['personId']
        confidentce = data['personConf']

        user = User.objects.filter(id = student_id)
        try:
            attendance = Attendance(user=user, conf=confidentce)
            attendance.save()

        except Exception as e:
            pass
        """teacher_id =  data['teacherId']
        teacher_mail = data['teacherMail']"""

        try:
            print(type(student_id), type(confidentce))
        except:
            pass


    if request.user.admin:
        return render(request, 'index.html')
    else:
        raise Http404
