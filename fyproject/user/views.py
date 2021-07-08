from nltk.util import pr
from company.views import questions, status
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from company.models import InterviewQuestion, Jobs, QuestionBank, Interview
from django.contrib import messages


from django.http.response import StreamingHttpResponse
from user.camera import VideoCamera
from user.camera import *
import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import webbrowser
import sys


import numpy as np
from django.conf import settings
import os
from user.model1 import FacialExpressionModel
import cv2
from .utils.model import *
from .utils.helpers import *
import os
from textblob import TextBlob

audiojs = False

current_path = os.path.abspath(os.path.dirname(__file__))
facec = cv2.CascadeClassifier(
    "opencv_haarcascade_data/haarcascade_frontalface_default.xml"
)
model = FacialExpressionModel(
    "opencv_haarcascade_data/model.json", "opencv_haarcascade_data/model_weights.h5"
)
font = cv2.FONT_HERSHEY_SIMPLEX

pred1 = []


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)

        for (x, y, w, h) in faces:
            fc = gray_fr[y : y + h, x : x + w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            if pred == "Happy":
                pred1.append("Happy")
            elif pred == "Sad":
                pred1.append("Sad")
            elif pred == "Neutral":
                pred1.append("Neutral")
            elif pred == "Surprise":
                pred1.append("Surprise")
            elif pred == "Angry":
                pred1.append("Angry")
            elif pred == "Disgust":
                pred1.append("Disgust")
            elif pred == "Fear":
                pred1.append("Fear")
            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
        _, jpeg = cv2.imencode(".jpg", fr)
        return jpeg.tobytes()


def webcam(request):
    global capturing
    global captured_video
    capturing = True
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    captured_video = cv2.VideoWriter("video.avi", fourcc, 20.0, (width, height))
    while capturing:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        captured_video.write(img_final)
    #   if keyboard.is_pressed('q'):
    #           capturing = False
    #           return render(request, 'grader/index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


def video_feed(request):

    return StreamingHttpResponse(
        gen(VideoCamera()), 
        content_type="multipart/x-mixed-replace; boundary=frame"
    )


# Create your views here.a
def uhome(request):

    return render(request, "user/home.html")


def ujob(request):
    user = User.objects.get(username=request.user.username)

    alljobs = Jobs.objects.all()
    allinterview = Interview.objects.filter(user=user)
    context = {"alljobs": alljobs,"allinterview": allinterview}
    return render(request, "user/job.html", context)


def profile(request):
    user = User.objects.get(username=request.user.username)

    context = {"user": user}
    return render(request, "user/profile.html", context)


def interview(request):
    user = User.objects.get(username=request.user.username)
    allinterview = Interview.objects.filter(user=user)
    jsId = []
    for interview in allinterview:
        id = str(interview.id)
        jsId.append(id)

    print(jsId)
    context = {"allinterview": allinterview ,"interviewid":jsId}

    return render(request, "user/interview.html", context)


def takeinterview(request, id, qid):
    
    data = ""
    sent = ""
    if request.method == "POST":
        VideoCamera().__del__
        
        question_id = request.POST["questionid"]
        qid = int(request.POST["qid"])
        qanswer = request.POST["answer"]

        if request.method == "POST" and "next" in request.POST:
           
            qid = qid + 1
            edu = TextBlob(qanswer)
            x = edu.sentiment.polarity
            if x < 0:
                qsent = "negative"
            elif x > 0 and x <= 1:
                qsent = "positive"
            elif x == 0:
                qsent = "neutral"

            if len(qanswer) > 2:
                interview = Interview.objects.get(id=id)
                job = interview.job.id
                question = InterviewQuestion.objects.get(id=question_id)
                # Question = question[qid]

                ques = question.question_answer
                # num_features = 300
                # model = word2vec.KeyedVectors.load_word2vec_format(os.path.join(current_path, "deep_learning_files/word2vec.bin"), binary=True)
                clean_test_essays = []
                question1 = []

                clean_test_essays.append(
                    essay_to_wordlist(qanswer, remove_stopwords=True)
                )
                question1.append(essay_to_wordlist(ques, remove_stopwords=True))
                aa = np.intersect1d(clean_test_essays, question1)
                b = len(aa)

                happy = pred1.count("Happy")
                sad = pred1.count("Sad")
                neutral = pred1.count("Neutral")
                surprise = pred1.count("Surprise")
                fear = pred1.count("Fear")
                disgust = pred1.count("Disgust")
                angry = pred1.count("Angry")

                uquestion = InterviewQuestion.objects.get(id=question_id)
                uquestion.candidate_answer = qanswer
                uquestion.score = b
                uquestion.sent = qsent
                uquestion.Happy = happy
                uquestion.Neutral = neutral
                uquestion.Sad = sad
                uquestion.Fear = fear
                uquestion.Angry = angry
                uquestion.Surprise = surprise
                uquestion.Disgust = disgust
                uquestion.status = True

                uquestion.save()

                pred1.clear()

        if request.method == "POST" and "submit" in request.POST:
            qid=0
            
            edu = TextBlob(qanswer)
            x = edu.sentiment.polarity
            if x < 0:
                qsent = "negative"
            elif x > 0 and x <= 1:
                qsent = "positive"
            elif x == 0:
                qsent = "neutral"

            if len(qanswer) > 2:
                interview = Interview.objects.get(id=id)
                job = interview.job.id
                question = InterviewQuestion.objects.get(id=question_id)
                # Question = question[qid]

                ques = question.question_answer
                # num_features = 300
                # model = word2vec.KeyedVectors.load_word2vec_format(os.path.join(current_path, "deep_learning_files/word2vec.bin"), binary=True)
                clean_test_essays = []
                question1 = []

                clean_test_essays.append(
                    essay_to_wordlist(qanswer, remove_stopwords=True)
                )
                question1.append(essay_to_wordlist(ques, remove_stopwords=True))
                aa = np.intersect1d(clean_test_essays, question1)
                b = len(aa)

                happy = pred1.count("Happy")
                sad = pred1.count("Sad")
                neutral = pred1.count("Neutral")
                surprise = pred1.count("Surprise")
                fear = pred1.count("Fear")
                disgust = pred1.count("Disgust")
                angry = pred1.count("Angry")

                uquestion = InterviewQuestion.objects.get(id=question_id)
                uquestion.candidate_answer = qanswer
                uquestion.score = b
                uquestion.sent = qsent
                uquestion.Happy = happy
                uquestion.Neutral = neutral
                uquestion.Sad = sad
                uquestion.Fear = fear
                uquestion.Angry = angry
                uquestion.Surprise = surprise
                uquestion.Disgust = disgust
                uquestion.status = True

                uquestion.save()

        if request.method == "POST" and "giveanser" in request.POST:
            import speech_recognition as sr

            r = sr.Recognizer()
            # mic = sr.Microphone(device_index=1)
            mic = sr.Microphone()
            with mic as source:
                print("Talk")
                # r.adjust_for_ambient_noise(source)
                audio_text = r.record(source=mic, duration=5)
                # audio_text = r.listen(source)
                # with sr.Microphone() as source:
                #     print("Talk")
                #     audio_text = r.listen(source)
                print("Time over, thanks")
                # with open('speach.wav', 'wb') as f:
                #     f.write(audio_text.get_wav_data())
            try:
                output = " " + r.recognize_google(audio_text)
            except sr.UnknownValueError:
                output = ""
            except sr.RequestError as e:
                output = "Could not request results; {0}".format(e)
            data = output

        else:
            data = ""

    print(qid)
    user = User.objects.get(username=request.user.username)
    interview = Interview.objects.get(id=id)
    job = interview.job.id
    question = InterviewQuestion.objects.filter(job_id=job)

    total_question = question.count()
    last = False

    if qid + 1 == total_question:
        last = True

    firstQuestion = question[qid]

    context = {"firstQuestion": firstQuestion, "last": last, "data": data, "sent": sent,"qid":qid , "audiojs":audiojs}
    return render(request, "user/takeinterview.html", context)


def interviewschdule(request, id):
    if request.method == "POST":

        date = request.POST["date"]
        time = request.POST["time"]

        user = User.objects.get(username=request.user.username)
        ujob = Jobs.objects.get(id=id)
        interview = Interview(
            user=user,
            job=ujob,
            company_user_id=ujob.user.id,
            applidejob_id=ujob.id,
            date=date,
            time=time,
            schduele_time="2021-05-06 22:01",
        )
        interview.save()
        questions = QuestionBank.objects.filter(job=ujob)

        for index, question in enumerate(questions):
            interviewquestion = InterviewQuestion(
                question_id=question.id,
                job_id=id,
                job_title=ujob.job_title,
                user=user,
                Interview=interview,
                question=question.question,
                question_answer=question.answer,
            )
            interviewquestion.save()

        # messages.success(request, "Your Application is applide successfully.")
        return redirect("/user/interview/")
        # return render(request, 'company/jobs.html')

    # alljobs = Jobs.objects.all()
    # context = {'alljobs':alljobs}
    user = User.objects.get(username=request.user.username)
    ujob = Jobs.objects.get(id=id)
    print(user)
    context = {"job": ujob}
    return render(request, "user/secduleinterview.html", context)


def countdown(request,id):
    allinterview = Interview.objects.filter(id = id)
    context = {"allinterview": allinterview}
    return render(request, "user/countdown.html", context) 
