from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from .forms import ConversationMessageForm
from .models import message
# Create your views here.

def index(request):
    return render(request, 'message/index.html', {
        'users':User.objects.all()
    })


def mess(request):
    conversations = message.objects.filter(members__in=[request.user.id])

    return render(request, 'message/message.html', {
        'conversations': conversations
    })


def new(request, user_pk):
    user = get_object_or_404(User, pk= user_pk)

    if user == request.user:
        return redirect('message:index')
    
    conversations = message.objects.filter(user=user).filter(user=user).filter(members__in=[request.user.id])

    if conversations:
         return redirect('message:detail',pk=conversations.first().id)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
           conversation = message.objects.create(user=user)
           conversation.members.add(request.user.id)
           conversation.members.add(user)
           conversation.save()

           conversation_message = form.save(commit=False)
           conversation_message.conversation = conversation
           conversation_message.created_by = request.user
           conversation_message.save()

           return redirect('message:detail',pk=conversations.last().id)
    else:
            form = ConversationMessageForm

    return render(request, 'message/new.html', {
    'form':form,
    'user':user
    })


def detail(request, pk):
     conversation =  message.objects.filter(members__in=[request.user.id]).get(pk=pk)

     if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('message:detail', pk=pk)
     else:
         form = ConversationMessageForm()

         return render(request, 'message/detail.html',{
             'conversation':conversation,
             'form':form
         })





def logout(request):
     auth.logout(request)
     return redirect('/')