from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Friend

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'friends'

    def get_queryset(self):
        return Friend.objects.all()

def addfriend(request):
    friend = Friend(name=request.POST['name'], email=request.POST['email'])
    friend.save()
    return HttpResponseRedirect(reverse('main:index'))

def friend_update(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    friend.name = request.POST['name']
    friend.email = request.POST['email']
    friend.save()
    return HttpResponseRedirect(reverse('main:index'))

def remove_friend(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    friend.delete()
    return HttpResponseRedirect(reverse('main:index'))

class FriendDetailView(generic.DetailView):
    model = Friend
    template_name = 'main/friend_detail.html'