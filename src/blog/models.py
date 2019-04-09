from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)

    ### one User can delete (many) post. User is a foreignkey of Post Model
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # ....for commandline and views.py....
    # >>user = User.objects.first()
    # >>user.post_set //it gives u all the set of post <.ModelName>+<_>+<set>
    # >>user.post_set.all() //gives u all the set of post
    
    # >>user.post_set.create(title = "Blog 2", content = "two")
    # [And there is no need save() and set 'author' . because author gets from user]


    # special type of function...
    def __str__(self):
        return self.title