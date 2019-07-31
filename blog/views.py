from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):

    objs = Post.objects.all()
    return render(  request,
                    template_name="post_list.html",
                    context={"posts":objs}
                )