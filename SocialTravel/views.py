from django.shortcuts import render
from SocialTravel.models import Post

# Create your views here.

def index(request):
    return render(request, "SocialTravel/index.html")

#def mostrar_otro_template(request):
 #   posts = Post.objects.all()
  #  return render(request, "SocialTravel/otro-template.html", {"posts": posts})


def mostrar_otro_template(request):

    posts = Post.objects.all()


    return render(request, "SocialTravel/otro-template.html", {"posts": posts})


