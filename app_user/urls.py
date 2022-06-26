from django.urls import path
from .views import AnotherLogin, AnotherLogout, register_view, ProfileDetailView, ProfileEditFromView, ProfilesListView, \
    RelativeFormView, StudentFormView, StudentEditFormView, RelativeEditFormView, SchoolList, main_page

urlpatterns = [
    path('login/', AnotherLogin.as_view(), name='login'),
    path('', main_page, name='main_page'),
    path('register/', register_view, name='register'),
    path('logout/', AnotherLogout.as_view(), name='logout'),
    path('profiles/', ProfilesListView.as_view(), name='profiles_list'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profiles_detail'),
    path('profile/<int:user_id>/edit', ProfileEditFromView.as_view(), name='edit_profile'),
    path('relative/create', RelativeFormView.as_view(), name='create_relative'),
    path('student/create', StudentFormView.as_view(), name='create_student'),
    path('student/<int:student_id>/edit', StudentEditFormView.as_view(), name='edit_student'),
    path('relative/<int:relative_id>/edit', RelativeEditFormView.as_view(), name='edit_student'),
    path('api/v1/photo/', SchoolList.as_view(), name='school-list'),
]
