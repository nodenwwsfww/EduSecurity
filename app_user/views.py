from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.views import generic, View
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .forms import RelativeForm, StudentForm, RegisterForm
from .models import School, Relative, Student, Profile
from .serializers import SchoolSerializer


def register_view(request):
    """Регистрация и авторизация"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            # last_name = form.cleaned_data.get('last_name')
            # first_name = form.cleaned_data.get('first_name')
            # patronymic = form.cleaned_data.get('patronymic')
            phone_number = form.cleaned_data.get('phone_number')
            email = form.cleaned_data.get('email')
            # relative_type = form.cleaned_data.get('relative_type')
            Profile.objects.create(
                user=user,
                city=city,
                # last_name=last_name,
                # first_name=first_name,
                # patronymic=patronymic,
                phone_number=phone_number,
                email=email,
                # relative_type=relative_type
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(f'/profile/{request.user.id}')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class AnotherLogin(LoginView):
    """Функция логина"""
    template_name = 'login.html'


class AnotherLogout(LogoutView):
    """Функция разлогина"""
    template_name = 'logout.html'


def main_page(request):
    """Страница-прослойка для редиректа в settings.py"""
    user_id = request.user.idg # todo fix
    if request.user.is_authenticated:
        return redirect(f'/profile/{user_id}')
    else:
        return redirect(f'../login')


class ProfilesListView(generic.ListView):
    """Функция для отображения списка пользователей"""
    model = Profile
    template_name = 'profiles_list.html'
    context_object_name = 'profiles'
    queryset = Profile.objects.all()


class ProfileDetailView(generic.DetailView):
    """Функция для отображения детальной информации по пользователям"""
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        """Передача дополнительных моделей в шаблон через контекст"""
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['schools'] = School.objects.all()
        context['relatives'] = Relative.objects.filter(main_parent=pk)
        context['students'] = Student.objects.filter(parent=pk)
        return context


class ProfileEditFromView(View):
    """Функция описывающая логику редактирования профиля"""
    def get(self, request, user_id):
        if request.user.is_authenticated:
            user = User.objects.get(id=user_id)
            profile = Profile.objects.get(id=user_id)
            user_form = UserCreationForm(instance=user)
            profile_form = RegisterForm(instance=profile)
            return render(request, 'edit_profile.html', context={'user_form': user_form, 'user_id': user_id,
                                                                 'profile_form': profile_form})
        else:
            raise PermissionError

    def post(self, request, user_id):
        if request.user.is_authenticated:
            user = User.objects.get(id=user_id)
            profile = Profile.objects.get(id=user_id)
            user_form = UserCreationForm(instance=user)
            profile_form = RegisterForm(instance=profile)
            return render(request, 'edit_profile.html', context={'user_form': user_form, 'user_id': user_id,
                                                                 'profile_form': profile_form})
        else:
            raise PermissionError


class StudentEditFormView(View):
    """Функция описывающая логику редактирования профиля ученика"""
    def get(self, request, student_id):
        if request.user.is_authenticated:
            student = Student.objects.get(id=student_id)
            student_form = StudentForm(instance=student)
            return render(request, 'edit_student.html', context={'student_form': student_form,
                                                                 'student_id': student_id})
        else:
            raise PermissionError

    def post(self, request, student_id):
        if request.user.is_authenticated:
            student = Student.objects.get(id=student_id)
            student_form = StudentForm(request.POST)
            if student_form.is_valid():
                student.save()
            return render(request, 'edit_student.html', context={'student_form': student_form,
                                                                 'student_id': student_id})
        else:
            raise PermissionError


class RelativeEditFormView(View):
    """Функция описывающая логику редактирования профиля довереных лиц"""
    def get(self, request, relative_id):
        if request.user.is_authenticated:
            relative = Relative.objects.get(id=relative_id)
            relative_form = RelativeForm(instance=relative)
            return render(request, 'edit_relative.html', context={'relative_form': relative_form,
                                                                  'relative_id': relative_id})
        else:
            raise PermissionError

    def post(self, request, relative_id):
        if request.user.is_authenticated:
            relative = Relative.objects.get(id=relative_id)
            relative_form = RelativeForm(request.POST)
            if relative_form.is_valid():
                relative.save()
            return render(request, 'edit_relative.html', context={'relative_form': relative_form,
                                                                  'relative_id': relative_id})
        else:
            raise PermissionError


class RelativeFormView(View):
    """Функция для создания профиля довереного лица"""
    def get(self, request):
        if request.user.is_authenticated:
            relative_form = RelativeForm()
            return render(request, 'create_relative.html', context={'relative_form': relative_form})
        else:
            raise PermissionError

    def post(self, request):
        if request.user.is_authenticated:
            context = {}
            if request.method == 'POST':
                relative_form = RelativeForm(request.POST)
                if relative_form.is_valid():
                    relative_form.save()
                    return redirect('../profiles')
            else:
                relative_form = RelativeForm()
            context['relative_form'] = relative_form
            return render(request, 'create_relative.html', context={'relative_form': relative_form})
        else:
            raise PermissionError


class StudentFormView(View):
    """Функция для создания профиля ученика"""
    def get(self, request):
        if request.user.is_authenticated:
            student_form = StudentForm()
            return render(request, 'create_student.html', context={'student_form': student_form})
        else:
            raise PermissionError

    def post(self, request):
        if request.user.is_authenticated:
            context = {}
            if request.method == 'POST':
                student_form = StudentForm(request.POST)
                if student_form.is_valid():
                    student_form.save()
                    return redirect('../profiles')
            else:
                student_form = RelativeForm()
            context['student_form'] = student_form
            return render(request, 'create_student.html', context={'student_form': student_form})
        else:
            raise PermissionError


class SchoolList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Функция даля отображения данных по школе в документации модуля swagger и работы с API"""
    serializer_class = SchoolSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = School.objects.filter(user=user)
        school = self.request.query_params.get('school')
        if school:
            queryset.filter(name=school)
        return queryset

    def get(self, request):
        """Определение метода GET"""
        return self.list(request)

    def post(self, request):
        """Определение метода POST"""
        return self.create(request)
