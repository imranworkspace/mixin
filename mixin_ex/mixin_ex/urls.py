
from django.contrib import admin
from django.urls import path
from api.views import StudentList,StudentCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',StudentList.as_view()),
    path('create/',StudentCreate.as_view()),
]
