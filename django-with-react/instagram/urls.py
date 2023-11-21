from django.urls import path, re_path

from . import views

urlpatterns=[
    path('',views.post_list),
    path('<int:pk>/',views.post_detail),
    # re_path
    path('archives/<year:year>/',views.archives_year),
]