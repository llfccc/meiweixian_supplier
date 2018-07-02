# coding=utf-8
import time   #,logging
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import Http404

from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, ChangepwdForm
from .models import Profile

# logger = logging.getLogger(__name__)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form, }))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:
                # print("dfdf")
                # logger.debug('The password is wrong')
                return render_to_response('login.html', RequestContext(request, {'form': form, 'password_is_wrong': True}))
        else:
            return render(request,'login.html', locals())


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")

# 不知道干嘛什么用的，先注释掉了


def login_validate(request, username, password):
    rtvalue = False
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return True
    return rtvalue

@csrf_exempt
@login_required
def register(request):
    error = []
    #在公司为admin的情况下才查询，并按照指定日期字段内查询
    company_name=request.user.profile.company_name
    if  (company_name == 'admin'):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                supplier_company_name = data['company_name']
                # group_name = data['group_name']
                password = data['password']
                password2 = data['password2']
                if not User.objects.all().filter(username=username):
                    if form.pwd_validate(password, password2):
                        user = User.objects.create_user(username,'', password)
                        profile=Profile(company_name=supplier_company_name,user_id=user.id)
                        profile.save()
                        user.save()
                        # login_validate(request, username, password)
                        return render_to_response('welcome.html', {'user': username})
                    else:
                        error.append('Please input the same password')
                else:
                    error.append(
                        'The username has existed,please change your username')
        else:
            form = RegisterForm()
        return render_to_response('register.html', {'form': form, 'error': error})
    else:
        raise Http404


@login_required
def changeProcessCompany(request):
    id=request.user.id

    # profile.company_name
    process_company=request.user.profile.process_company
    if not process_company:
        process_company=u"美味鲜"
    if process_company==u"美味鲜":
        change_company=u"厨邦"
    if process_company==u"厨邦":
        change_company=u"美味鲜"
  

    Profile.objects.filter(id=id).update(process_company=change_company)    
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(request.session['login_from'])


@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render(request,'changepwd.html',locals())
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('index.html', RequestContext(request, {'changepwd_success': True}))
            else:
                return render_to_response('changepwd.html', RequestContext(request, {'form': form, 'oldpassword_is_wrong': True}))
        else:
            return render_to_response('changepwd.html', RequestContext(request, {'form': form, }))
