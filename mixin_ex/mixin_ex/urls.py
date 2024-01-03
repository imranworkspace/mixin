
from django.contrib import admin
from django.urls import path
from api.views import StudentList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',StudentList.as_view()),
]
