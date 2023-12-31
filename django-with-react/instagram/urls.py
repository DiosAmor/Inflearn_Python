from django.urls import path, re_path,  register_converter

from . import views
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')


app_name = 'instagram'  # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns=[
    path('',views.post_list),
    path('<int:pk>/',views.post_detail),
    # re_path
    # path('archives/<year:year>/',views.archives_year),
    
    path('archive/', views.post_archive,name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year,name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),
]