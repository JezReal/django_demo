from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.index, name='StudentList'),
    path('<int:student_id>/', views.student_detail, name='StudentDetail'),
    path('<int:student_id>/edit', views.edit_student, name='EditStudent'),
    path('<int:student_id>/delete', views.delete_student, name='DeleteStudent'),
    path('student/new', views.add_student, name='AddStudent')
]
