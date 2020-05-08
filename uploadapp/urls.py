from django.urls import path
from .views import *

# call the api function
urlpatterns = [
    path('', FileUploadView.as_view())
]