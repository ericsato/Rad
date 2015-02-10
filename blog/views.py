from django.shortcuts import render
from suggestion.models import Suggestion

# Create your views here.

from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about/index.html')

def radsuggestion(request):
    suggestion = Suggestion.objects.order_by('?')[0]
    return render_to_response('radsuggestion/index.html', {'suggestion': suggestion})