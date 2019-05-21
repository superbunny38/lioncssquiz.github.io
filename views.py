from django.shortcuts import render, redirect
from .models import Message
def home(r):
    messages = Message.objects
    return render(r, 'home.html', {'messages':messages})

def submit(r):
    print('submit함수로 들어왔따!')
    message = Message()
    message.words = r.GET['words']
    message.date = r.GET['date']
    message.writer = r.GET['writer']
    message.save()
    print('모델이 저장되었다!')
    return redirect('/')