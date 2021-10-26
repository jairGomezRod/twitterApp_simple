from django.shortcuts import render
from django.urls import reverse

from .models import Tweet
# Create your views here.
def feed(request):


    tweets = Tweet.objects.filter(created_by_id__in=[1])
    
    return render(request, 'feed/feed.html', {'tweets':tweets})