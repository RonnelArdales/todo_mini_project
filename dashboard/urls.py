from django.urls import include, path
from .views import addtask, home, taskupdate, taskview
from dashboard import views


urlpatterns = [
    path('', home, name="home" ),
    path('addtask/', addtask, name="addtask" ),
    path('taskdetail/<str:pk>/', taskview, name="taskview"),
    path('taskupdate/<int:pk>/', views.taskupdate, name="taskupdate"),
    path('<int:pk>/', views.taskdelete, name="taskdelete"),
]

