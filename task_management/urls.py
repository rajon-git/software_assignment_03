
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name="homepage"),
    path('category/', include("category.urls")),
    path('task/', include("tasks.urls")),
]
