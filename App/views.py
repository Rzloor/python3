#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from App.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import hashlib
# @csrf_protect
#表单

class UserForm(forms.Form):
    username = forms.CharField(required=True, max_length=30)
    password = forms.CharField(required=True, max_length=32)
@csrf_exempt


#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password_encrypt(password))
            return HttpResponse('注册成功')
    else:
        return render(req, 'regist.html', {'error': '注册失败'})

#登陆
@csrf_exempt
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/App/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/App/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response
##md5 加密
def password_encrypt(pwd):
        md5 = hashlib.md5()
        md5.update(pwd.encode())
        result = md5.hexdigest()
        return result