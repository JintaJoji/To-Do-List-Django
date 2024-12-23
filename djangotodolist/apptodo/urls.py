from .import views
from django.urls import path


urlpatterns = [
    path('',views.index,name="index"),
    path('listtodo',views.listtodo,name="listtodo"),
    path('list',views.list,name="list"),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
]