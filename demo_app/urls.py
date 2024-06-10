from django.urls import path
# from api.views import *
from demo_app.views import Login, Logout, Signup, TestView, TeamLeadSignup,InternSignup,StaffSignup,FrontOfficeSignup

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('team/lead/signup/', TeamLeadSignup.as_view(), name='signup'),
    path('intern/signup/', InternSignup.as_view(), name='signup'),
    path('staff/signup/', StaffSignup.as_view(), name='signup'),
    path('frontoffice/signup/', FrontOfficeSignup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('test/view/', TestView.as_view(), name='test_view'),
    path('logout/', Logout.as_view(), name='logout')
    
]



