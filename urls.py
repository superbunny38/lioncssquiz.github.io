
from django.contrib import admin
from django.urls import path

import boards.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', boards.views.home, name="board"),
    path('submit/', boards.views.submit, name="submit"),
]
