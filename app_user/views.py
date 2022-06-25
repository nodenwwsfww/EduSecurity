from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.views import generic, View

from .forms import RelativeForm, StudentForm
from .models import School, Relative, Student


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profiles')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class AnotherLogin(LoginView):
    template_name = 'login.html'


class AnotherLogout(LogoutView):
    template_name = 'logout.html'


class ProfilesListView(generic.ListView):
    model = User
    template_name = 'profiles_list.html'
    context_object_name = 'profiles'
    queryset = User.objects.all()


class ProfileDetailView(generic.DetailView):
    model = User
    template_name = 'profile_detail.html'
    context_object_name = 'profile'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['schools'] = School.objects.all()
        context['relatives'] = Relative.objects.filter(main_parent=pk)
        context['students'] = Student.objects.filter(parent=pk)
        return context


class ProfileEditFromView(View):

    def get(self, request, profile_id):
        if request.user.is_authenticated:
            profile = User.objects.get(id=profile_id)
            profile_form = UserCreationForm(instance=profile)
            return render(request, 'edit_profile.html', context={'profile_form': profile_form,
                                                                 'profile_id': profile_id})
        else:
            raise PermissionError

    def post(self, request, profile_id):
        if request.user.is_authenticated:
            profile = User.objects.get(id=profile_id)
            profile_form = UserCreationForm(request.POST, request.FILES)

            if profile_form.is_valid():
                profile.save()
            return render(request, 'edit_profile.html', context={'profile_form': profile_form,
                                                                 'profile_id': profile_id})
        else:
            raise PermissionError


class StudentEditFormView(View):

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
