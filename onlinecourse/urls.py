from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
app_name = 'onlinecourse'

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path('<int:pk>/enroll/', views.enroll, name='enroll'),
    path('<int:pk>/course_details/', views.course_details, name='course_details'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path(
        '<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


