# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Board
from .models import Topic
from .models import Post

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
# Register your models here.
