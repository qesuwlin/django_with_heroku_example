from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic

#class IndexView(generic.ListView):
#   template_name ='index.html'
def index(request):
   return render_to_response('mysite/index.html')
