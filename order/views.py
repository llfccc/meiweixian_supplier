#coding=utf-8
from django.shortcuts import render
from .models import U8S,Invoices
import json, datetime,time,sys,os  #,logging
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.db.models import Q,Count
from .forms import DeliveryForm,QueryForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
# from echarts import Echart, Legend, Bar, Axis
from django.http import Http404
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models import Q


# Create your views here.

#修改要处理的公司
@login_required
def processOrder(request):
    company_name=request.user.profile.company_name
    process_company=request.user.profile.process_company
    if not process_company:
        process_company=u"美味鲜"
    query=U8S.objects.filter(supplier=company_name).filter(current_company=process_company).select_related()
    data=query.filter(arrival_date__isnull=True).order_by("id")
    count = data.count()
    count2 = query.filter(received__isnull=True).count()       
    return render(request,'processOrder.html',locals())

#接收供应商更新的订单信息
@login_required
def updateOrder(request): 
    if request.method == 'POST':        
        received_data = json.loads(request.body)     

    for k, v in received_data.items():
        if v['received']==True:
            print(v["deliver_date"])
            try:
                deliver_date=v["deliver_date"].split(" ")[0]
                deliver_date=datetime.datetime.strptime(deliver_date, "%Y-%m-%d")
                U8S.objects.filter(id=k).update(deliver_date=deliver_date)
            except:
                pass
            try:
                arrival_date=v["arrival_date"].split(" ")[0]
                arrival_date=datetime.datetime.strptime(arrival_date, "%Y-%m-%d")
                U8S.objects.filter(id=k).update(arrival_date=arrival_date)
            except:                
                pass
            try:
                U8S.objects.filter(id=k).update(remarks=v["remarks"])
                U8S.objects.filter(id=k).update(received=v["received"])
            except:
                pass
    return str("success")


def viewFinishedOrder(request):
    company_name=request.user.profile.company_name
    process_company=request.user.profile.process_company
    if not process_company:
        process_company=u"美味鲜"
    if request.method == 'POST':
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        try:
            start_date=start_date.split(" ")[0]
            start_date=datetime.datetime.strptime(start_date, "%Y-%m-%d")
        except:
            pass
        try:
            end_date=end_date.split(" ")[0]
            end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d")
        except:                
            pass
        if not start_date:
            start_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if not end_date:
            end_date=datetime.date.today() + datetime.timedelta(days=1)
        data = U8S.objects.filter(supplier=company_name).filter(current_company=process_company).filter(add_date__gte=start_date).filter(add_date__lte=end_date).filter(arrival_date__isnull=False).order_by("id")

    return render(request,'viewFinishedOrder.html',locals())    


@login_required
def processInvoice(request):
    company_name=request.user.profile.company_name
    process_company=request.user.profile.process_company
    data=Invoices.objects.filter(supplier=company_name).filter(current_company=process_company).filter(settledate__isnull=True).order_by("storage_code")

    count=len(data)
    return render(request,'processInvoice.html',locals())    


#接收供应商更新的订单信息
@login_required
def updateInvoice(request): 
    if request.method == 'POST':        
        received_data = json.loads(request.body)

    nowTime =datetime.datetime.now()
    for k, v in received_data.items():
        if v['settlement']==True:            
            try:                
                Invoices.objects.filter(id=k).update(settledate=nowTime)
            except:
                pass
    return str("success")


 
@login_required
def finishedInvoice(request): 
    company_name=request.user.profile.company_name
    process_company=request.user.profile.process_company

    if request.method == 'POST':
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        try:
            start_date=start_date.split(" ")[0]
            start_date=datetime.datetime.strptime(start_date, "%Y-%m-%d")
        except:
            pass
        try:
            end_date=end_date.split(" ")[0]
            end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d")
        except:                
            pass
        if not start_date:
            start_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if not end_date:
            end_date=datetime.date.today() + datetime.timedelta(days=1)
        
        data=Invoices.objects.filter(supplier=company_name).filter(add_date__gte=start_date).filter(add_date__lte=end_date).filter(current_company=process_company).filter(settledate__isnull=False).order_by("storage_code")      
        
    return render(request,'finishedInvoice.html',locals())



def queryDelivery(request):

    if request.method == 'POST':
        form = QueryForm(request.POST) # 获取Post表单数据
        if form.is_valid(): # 验证表单
            cleanFormData=form.cleaned_data
            try:
                inputList = cleanFormData['name'].strip().split() 
            except:
                inputText=0
            #如果2个字段那么就是xxx
            if len(inputList)==1:
                inputText=inputList[0]            
                try:
                    up_code=int(inputText)
                except:
                    up_code=0                
                data=U8S.objects.filter(Q(up_code=up_code) | Q(stock_code=inputText)| Q(material_name=inputText)| Q(model=inputText)).order_by("-id")

            if len(inputList)==2:
                try:
                    material_name=inputList[0]
                    model=inputList[1]
                    data=U8S.objects.filter(Q(material_name=material_namet) &  Q(model=model)).order_by("-id")
                except:
                    data=None
            return render(request,'queryDelivery.html',locals())  
    else:
        form = QueryForm()
    return render(request,'queryDelivery.html',locals())  



@login_required
def queryOrder(request):
    company_name=request.user.profile.company_name
    process_company=request.user.profile.process_company
    if not process_company:
        process_company=u"美味鲜"    
    if request.method == 'POST':
        form = QueryForm(request.POST) # 获取Post表单数据
        if form.is_valid(): # 验证表单
            cleanFormData=form.cleaned_data
            materialName = cleanFormData['name'].strip().split()
            
            data=U8S.objects.filter(supplier=company_name).filter(order_code=materialName[0]).filter(current_company=process_company).order_by("id")
        
            return render(request,'queryOrder.html',locals())  
    else:
        form = QueryForm()
        return render(request,'queryOrder.html',locals())  


#接收订单excel
def receiveExcelOrder(request):
    received_data = json.loads(request.body)  

    if not received_data:
        raise Http404
    data = json.loads(received_data)
    list_to_insert = list()

    for x in data:   
        list_to_insert.append(U8S(add_date=x[0],supplier=x[1], up_code=x[2],order_code=x[3],stock_code=x[4],material_name=x[5],brand=x[6],serial_number=x[7],model=x[8],unit=x[9],number=x[10],price=x[11],comment1=x[12],timestamp=x[13],current_company=x[14]))
    U8S.objects.bulk_create(list_to_insert)
    return HttpResponse()

#接收发票
def receiveExcelInvoice(request):
    received_data = json.loads(request.body)  

    if not received_data:
        raise Http404   
    data = json.loads(received_data)
    list_to_insert = list()   

    for x in data:
        tmp=Invoices(supplier=x[0],add_date=x[1],order_code=x[2],storage_code=x[3],stock_code=x[4],material_name=x[5],model=x[6],unit=x[7],number=x[8],notaxprice=x[9],notaxmoney=x[10],price=x[11],stagequotation=x[12],current_company=x[13],timestamp=x[14])           
        list_to_insert.append(tmp)    
    Invoices.objects.bulk_create(list_to_insert)
    return HttpResponse()

@login_required
def queryAll(request):  
    #在公司为admin的情况下才查询，并按照指定日期字段内查询
    company_name=request.user.profile.company_name
    process_company=u"厨邦"
    if  (company_name == 'admin'):
        
        if not process_company:
            process_company=u"美味鲜"
        if request.method == 'POST':
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            try:
                start_date=start_date.split(" ")[0]
                start_date=datetime.datetime.strptime(start_date, "%Y-%m-%d")
            except:
                pass
            try:
                end_date=end_date.split(" ")[0]
                end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d")
            except:                
                pass
            if not start_date:
                start_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            if not end_date:
                end_date=datetime.date.today() + datetime.timedelta(days=1)

            data = U8S.objects.filter(add_date__gte=start_date).filter(add_date__lte=end_date).filter(current_company=process_company).order_by("id")
        return render(request,'query_all.html',locals())   
    else:
        raise Http404

@login_required
def queryAll2(request):  
    #在公司为admin的情况下才查询，并按照指定日期字段内查询
    company_name=request.user.profile.company_name
    process_company=u"美味鲜"
    if  (company_name == 'admin'):
   
        if not process_company:
            process_company=u"美味鲜"
        if request.method == 'POST':
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            try:
                start_date=start_date.split(" ")[0]
                start_date=datetime.datetime.strptime(start_date, "%Y-%m-%d")
            except:
                pass
            try:
                end_date=end_date.split(" ")[0]
                end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d")
            except:                
                pass
            if not start_date:
                start_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            if not end_date:
                end_date=datetime.date.today() + datetime.timedelta(days=1)

            data = U8S.objects.filter(add_date__gte=start_date).filter(add_date__lte=end_date).filter(current_company=process_company).order_by("id")
        return render(request,'query_all.html',locals())   
    else:
        raise Http404


# def log_test(request):
#     logger = logging.getLogger("django") # 为loggers中定义的名称
#     logger.error("level error test")
#     logger.info("level info test")
    
