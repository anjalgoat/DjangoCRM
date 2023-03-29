
from django.urls import path, include
from .import views
from .views import RecordList, RecordDetail

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('delete_record/<int:pk>',views.delete_record, name='delete_record'),
    path('add_record/',views.add_record, name='add_record'),
    path('update_record/<int:pk>',views.update_record, name='update_record'),

    #-------------API Endpoint path ------------
    path('records_list/',RecordList.as_view(), name='record_list'),
    path('records_detail/<int:pk>',RecordDetail.as_view(), name='record_detail'),
]