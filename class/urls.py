from django.urls import path
from. import views
from .views import JobCreate,Joblist
from .views import JobDetailView,JobUpdate,JobDelete
urlpatterns=[
    path('jobcreate',JobCreate.as_view()),
    path('joblist',Joblist.as_view()),
    path('<pk>/',JobDetailView.as_view()),
    path('<pk>/jupdate',JobUpdate.as_view()),
    path('<pk>/jdelete',JobDelete.as_view()),
]