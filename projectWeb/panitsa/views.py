# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .decorators import user_authenticated
from django.contrib.auth.forms import *
from django.contrib.auth.views import *
from django.http import Http404
from .models import *
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = UserRegisterForm()
    return render(request, 'panitsa/register.html', {'form': form})
   
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ตรวจสอบว่า username และ password ถูกต้องหรือไม่
        # นี่คือตัวอย่างเท่านั้น คุณต้องดูว่ามีวิธีการตรวจสอบในระบบของคุณ
        if username == 'user' and password == 'password':
            # ถ้าถูกต้อง, ทำการเก็บข้อมูลเช่น session หรือ cookie
            return redirect('home')  # ลิ้งไปที่หน้าหลักหลังจากล็อกอินสำเร็จ
 
    return render(request, 'panitsa/login_user.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')


def home(request):
    return render(request, 'panitsa/home.html')


def representative(request):
    representatives = Representative.objects.all().order_by('id')[:3]
    asom_representatives = Villagepublic.objects.all()[:10]
    print("Representatives:", representatives)
    print("Asom Representatives:", asom_representatives)
    return render(request, 'panitsa/representative.html', {'representatives': representatives, 'asom_representatives': asom_representatives})


def activity_news(request):
    activity_news = Activity_news.objects.all()

    return render(request, 'panitsa/activity_news.html',{'activity_news':activity_news})


def report_issue(request):
    return render(request, 'panitsa/report_issue.html')


def income_expenses(request):
    income_expenses = Income_expenses.objects.all()

    return render(request, 'panitsa/income_expenses.html',{'income_expenses':income_expenses})


def donation_reportform(request):
    return render(request, 'panitsa/donation_report.html')

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_edit_view') 
    else:
        form = AdminLoginForm()

    return render(request, 'admin/login.html', {'form': form})


def edit_view(request):
    representative = Representative.objects.first()  
    villagepublic = Villagepublic.objects.first()
    activity_news = Activity_news.objects.first()
    income_expenses = Income_expenses.objects.first()

    return render(request, 'admin/add_edit.html', {'representative': representative, 'villagepublic': villagepublic, 'activity_news': activity_news, 'income_expenses':income_expenses})
    

def add_representative(request):
    if request.method == 'POST':
        form = RepresentativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_edit')  
    else:
        form = RepresentativeForm()

    return render(request, 'admin/add_representative.html', {'form': form})

def add_activity_news(request):
    if request.method == 'POST':
        form = Activity_newsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_edit')
    else:
        form = Activity_newsForm()

    return render(request, 'admin/add_activity_news.html',  {'form': form})

def add_villagepublic(request):
    if request.method == 'POST':
        form = VillagepublicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_edit') 
    else:
        form = VillagepublicForm()

    return render(request, 'admin/add_villagepublic.html', {'form': form})


def add_income_expenses(request):
    if request.method == 'POST':
        form = Income_expensesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_edit')  
    else:
        form = Income_expensesForm()

    return render(request, 'admin/add_income_expenses.html',{'form': form})


def edit_representative(request, representative_id=None):
    representatives = Representative.objects.all()
    representative = get_object_or_404(Representative, id=representative_id)
    if request.method == 'POST':
        form = RepresentativeForm(request.POST, request.FILES, instance=representative)
        if form.is_valid():
            form.save()
            representative.delete()
            return redirect('admin_edit')
    else:
        form = RepresentativeForm(instance=representative)

    

    return render(request, 'admin/add_edit/edit_representative.html', {'representatives': representatives, 'form': form})


def edit_villagepublic(request, villagepublic_id=None):
    villagepublic = get_object_or_404(Villagepublic, id=villagepublic_id)

    if request.method == 'POST':
        form = VillagepublicForm(request.POST, request.FILES, instance=villagepublic)
        if form.is_valid():
            form.save()
            villagepublic.delete()
            return redirect('admin_edit')
    else:
        form = VillagepublicForm(instance=villagepublic)

    return render(request, 'admin/edit_villagepublic.html', {'villagepublic': villagepublic, 'form': form})


def edit_activity_news(request, activity_news_id=None):
    activity_news = get_object_or_404(Activity_news, id=activity_news_id)

    if request.method == 'POST':
        form = Activity_newsForm(request.POST, request.FILES, instance=activity_news)
        if form.is_valid():
            form.save()
            activity_news.delete()
            return redirect('admin_edit')  
    else:
        form = Activity_newsForm(instance=activity_news)

    return render(request, 'admin/edit_activity_news.html', {'activity_news': activity_news, 'form': form})

def edit_income_expenses(request, income_expenses_id=None):
    income_expenses_ = get_object_or_404(Income_expenses, id=income_expenses_id)
    
    if request.method == 'POST':
        form = Income_expensesForm(request.POST, request.FILES, instance=income_expenses_)
        if form.is_valid():
            form.save()
            income_expenses.delete()
            return redirect('admin_edit')
    else:
        form = Income_expensesForm(instance=income_expenses_)

    return render(request, 'admin/edit_income_expenses.html', {'income_expenses': income_expenses_,'form': form})

