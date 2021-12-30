from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Course, Videos, Author, Reach
from json import dumps
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

# @login_required(login_url='login')
def courses(request):
    template_name = 'courses/courses.html'

    courses = Course.objects.all()
    return render(request, template_name, {'courses': courses})


# @login_required(login_url='login')
def teach(request):
    template_name = 'courses/teach.html'

    form_link = Reach.objects.last()
    return render(request, template_name, {'form_link': form_link})


# @login_required(login_url='login')
def ac(request, slug):
    template_name = 'courses/about-course.html'
    course_detail = Course.objects.get(slug=slug)
    course__author = Author.objects.get(id=course_detail.id)
    return render(request, template_name, {'cd':course_detail, 'ca': course__author})

# @login_required(login_url='login')
def cm(request, id):
    template_name = 'courses/course-main.html'
    # course_videos = serializers.serialize("json", Videos.objects.filter(course=id), fields = ("video_title","video",'pk'))
    latest_three_courses = Course.objects.all().order_by('-id')[:3:-1]
 
    course_videos = list(Videos.objects.filter(course=id))

    videos = (Videos.objects.filter(course=id))

    print('videos')
    print(videos)

    # videos_json = json.dumps(list(videos), cls=DjangoJSONEncoder)

    course_detail = Course.objects.get(id=id)
    return render(request, template_name, {'cv': videos, 'course_detail': course_detail, 'ltc' : latest_three_courses})


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