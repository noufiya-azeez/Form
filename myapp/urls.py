from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.StudentDetails.as_view(), name="add-student"),
    path('list/', views.StudentListView.as_view(), name="list-student"),
    path('update/<id>/', views.StudentUpdateView.as_view(), name="update-student"),
]