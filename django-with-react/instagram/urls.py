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
    path('archives/<year:year>/',views.archives_year),
]