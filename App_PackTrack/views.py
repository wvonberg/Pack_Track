from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse as parse_date
from .models import *
from django.contrib import messages
from .Packcalculator import *
import bcrypt

# main page defs


def to_landing(request):
    return redirect('/landing')


def landing(request):
    return render(request, 'landing_page.html')


def log_page(request):
    return render(request, 'log_reg.html')


def reg_page(request):
    return render(request, 'reg_log.html')


def summary(request):
    if "user_id" not in request.session:
        return redirect('/')
    user_data=Body.objects.get(user=request.session['user_id'])
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'data': Body.objects.get(user=request.session['user_id']),
        'bmi': BMIcalc(user_data.current_weight,user_data.height),
        'bmr': BMRcalc(user_data.current_weight,user_data.height,request.session['user_age'],user_data.gender),
    }
    return render(request, "summary.html", context)


def profile(request):
    if "user_id" not in request.session:
        return redirect('/')
    user_data=Body.objects.get(user=request.session['user_id'])
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'data': Body.objects.get(user=request.session['user_id']),
        'bmi': BMIcalc(user_data.current_weight,user_data.height),
        'bmr': BMRcalc(user_data.current_weight,user_data.height,request.session['user_age'],user_data.gender),

    }
    return render(request, "profile.html", context)

# page redirects to prevent conifrm submission msg


def login(request):
    if request.method == "POST":
        return redirect("/log_page")
    return redirect("/")


def register(request):
    if request.method == "POST":
        return redirect("/reg_page")
    return redirect("/")

# user login and validation


def user_login(request):
    # logging in a user
    # queery for logged user
    logged_user = User.objects.filter(email=request.POST['email'])
    if logged_user:
        logged_user = logged_user[0]
        print(logged_user.first_name)
        # compare passwords
        if bcrypt.checkpw(request.POST['p_w'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_name'] = f"{logged_user.first_name} {logged_user.last_name}"
            dateA = parse_date(str(logged_user.birthday))
            dateB = date.today()
            difference_years = relativedelta(dateB, dateA).years
            request.session['user_age']=difference_years
            return redirect('/summary')
        errors = {}
        errors['inv_pwd'] = "Invalid password."
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/log_page')
    return redirect('/log_page')

# create user and validations


def create_user(request):
    # create user
    if request.method == 'POST':
        # validate data
        errors = User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/reg_page')
        # encrypting pw
        # store plaintext pw into var
        user_pw = request.POST['pw']
        # now hash it
        hash_pw = bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['f_n'],
            last_name=request.POST['l_n'],
            birthday=request.POST['b_d'],
            email=request.POST['email'],
            password=hash_pw
        )
        request.session['user_id'] = new_user.id
        request.session['user_name'] = f"{new_user.first_name}"
        dateA = parse_date(str(request.POST['b_d']))
        dateB = date.today()
        difference_years = relativedelta(dateB, dateA).years
        request.session['user_age']=difference_years
        body_data = Body.objects.create(
            user=User.objects.get(id=request.session['user_id']),
            current_weight=0,
            height=0,
            gender="X",
            activity_lvl=0,
            goal=0,
            carb_percent=45,
            fat_percent=25,
            protein_percent=30,
        )
        return redirect('/profile')
    return redirect('/reg_page')

# edit profile


def user_update(request):
    if request.method == "POST":
        edit_user = User.objects.get(id=request.session['user_id'])
        edit_pw = edit_user.password
        body_data = Body.objects.get(user=edit_user.id)
        errors = User.objects.edit_validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/profile')
        if edit_user.first_name != request.POST['f_n']:
            edit_user.first_name = request.POST['f_n']
            edit_user.save()
        if edit_user.last_name != request.POST['l_n']:
            edit_user.last_name = request.POST['l_n']
            edit_user.save()
        if edit_user.birthday != request.POST['b_d']:
            edit_user.birthday = request.POST['b_d']
            edit_user.save()
        if edit_user.email != request.POST['email']:
            edit_user.email = request.POST['email']
            edit_user.save()
        if bcrypt.checkpw(request.POST['old_pw'].encode(), edit_pw.encode()):
            user_pw = request.POST['pw']
            hash_pw = bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
            edit_user.password = hash_pw
            edit_user.save()
        if body_data.current_weight != request.POST['current_weight']:
            body_data.current_weight = request.POST['current_weight']
            body_data.save()
        if body_data.height != request.POST['height']:
            body_data.height = request.POST['height']
            body_data.save()
        if body_data.gender != request.POST['gender']:
            body_data.gender = request.POST['gender']
            body_data.save()
        if body_data.activity_lvl != request.POST['activity_lvl']:
            body_data.activity_lvl = request.POST['activity_lvl']
            body_data.save()
        if body_data.goal != request.POST['goal']:
            body_data.goal = request.POST['goal']
            body_data.save()
        if body_data.carb_percent != request.POST['carb_percent']:
            body_data.carb_percent = request.POST['carb_percent']
            body_data.save()
        if body_data.fat_percent != request.POST['fat_percent']:
            body_data.fat_percent = request.POST['fat_percent']
            body_data.save()
        if body_data.protein_percent != request.POST['protein_percent']:
            body_data.protein_percent = request.POST['protein_percent']
            body_data.save()
        return redirect("/profile")
    return redirect("/profile")

def logout(request):
    request.session.flush()
    return redirect("/")