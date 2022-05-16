from fnmatch import translate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Message, Room
from chat import trans
# Create your views here.
def home(request):
  return render(request,'home.html')

def room(request,room):
  username = request.GET.get('username')
  language = request.GET.get('language')
  room_details = Room.objects.get(room_name=room)
  return render(request,'room.html',{
    'username':username,
    'room':room,
    'room_details':room_details,
    'language':language
  })

def checkview(request):
  room = request.POST.get('room_name')
  username = request.POST.get('username')
  language = request.POST.get('language')
  if Room.objects.filter(room_name=room).exists():
    return redirect('/'+room+'/?username='+username+'&language='+language)
  else:
    new_room = Room.objects.create(room_name=room)
    new_room.save()
    return redirect('/'+room+'/?username='+username+'&language='+language)

def send(request):
  room = request.POST['room_name']
  user_name = request.POST['username']
  message = request.POST['message']
  new_msg = Message.objects.create(user_id=user_name,room_name=room,msg=message)
  new_msg.save()
  return HttpResponse("Message Saved Successfully")

def getMessage(request,room,language):
  room_details = Room.objects.get(room_name=room)
  message = Message.objects.filter(room_name = room)[:5]
  msg = list(message.values())
  for text in msg:
    text['msg'] = trans.translate_text(text['msg'],language)
    # print(text['msg'])
  return JsonResponse({'messages':msg})