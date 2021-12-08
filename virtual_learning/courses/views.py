from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# @login_required(login_url='login')
def courses(request):
    template_name = 'courses/courses.html'
    return render(request, template_name)


# @login_required(login_url='login')
def teach(request):
    template_name = 'courses/teach.html'
    return render(request, template_name)


# @login_required(login_url='login')
def ac(request):
    template_name = 'courses/about-course.html'
    return render(request, template_name)

# @login_required(login_url='login')
def cm(request):
    template_name = 'courses/course-main.html'
    return render(request, template_name)


# @login_required(login_url='login')
# def grades_subjects(request, grade_id):
#     template_name = 'curriculum/grade-subject.html'
#     grade= Grade.objects.get(id=grade_id)
#     subjects= Subject.objects.filter(grade=grade_id)
#     image_video = ImageVideo.objects.filter(grade=grade_id)
#     comments = GradeComment.objects.filter(grade=grade, parent=None)
#     replies = GradeComment.objects.filter(grade=grade).exclude(parent=None)
#     rDict = {}
#     for reply in replies:
#         if reply.parent.id not in rDict.keys():
#             rDict[reply.parent.id] = [reply]
#         else:
#             rDict[reply.parent.id].append(reply)
#     return render(request, template_name, {'context': subjects, 'grade':grade, 'comments': comments, 'replyDict': rDict, 'image_video': image_video})