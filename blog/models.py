from django.db import models
from django.conf import settings
from django.utils import timezone

# create
# user = User.objects.get(username = "<username>")
# new_post = Post(author=user)
# new_post.update_title("<title>")
# new_post.update_text("<text>")
# new_post.create_now()

# get 
# Post.objects.filter(author__username="<username>")

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def update_title(self,value):
        self.title = value
    def update_text(self,value):
        self.text = value
    def create_now(self):
        self.created_date = timezone.now()
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return str({"author":self.author,"title":self.title})