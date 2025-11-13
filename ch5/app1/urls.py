
from django.urls import path
from app1.views import learn_app1

urlpatterns = [
    path("app1/",learn_app1,{"key":"value"},name='learn_app1')
]
