import json
import re

from django.http import JsonResponse, HttpResponse

from django.core import serializers

from .models import Tweet

def api_add_tweet(request):
    
    data = json.loads(request.body)
    contentTweet = data['contentTweet']
    userTweet = data['userTweet']

    tweet = Tweet.objects.create(contentTweet=contentTweet, userTweet=userTweet, created_by=request.user)

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)

    for result in results:
        result = result[1]

        print(result)

    return JsonResponse({'success': True})

