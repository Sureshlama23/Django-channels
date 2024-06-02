from django.shortcuts import render
from .models import Group,Chat
# Create your views here.
def home(request,group_name):
    groupName = Group.objects.filter(name=group_name).first()
    chats = []
    if groupName:
        chats = Chat.objects.filter(group=groupName)
    else:
        group = Group(name=group_name)
        group.save()
    return render(request,'index.html',{'groupName':group_name,'chats':chats})