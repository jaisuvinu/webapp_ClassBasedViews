
from django.contrib import admin
from django.urls import path
from myapp1.views import View1, View2, ShowAllPatients

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('view1/',View1.as_view()),
    path('view2/',View2.as_view()),
    path('all/',ShowAllPatients.as_view())
]
