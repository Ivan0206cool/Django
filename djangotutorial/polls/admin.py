from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Location,Post

admin.site.register(Question)
admin.site.register(Location)
admin.site.register(Post)