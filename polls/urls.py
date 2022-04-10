from django.urls import path

from . import views

# app_name use for unique namespace
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # First, the polls are read, 
    # then the string matching <int:question_id> is read as the question_id.
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/resutlts/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]