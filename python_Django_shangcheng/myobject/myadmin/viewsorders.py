from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types,Goods,Orders,Detail
from PIL import Image
import time,json,os







#==========订单状态======================
def amendedicts(request,oid):
    ob=Orders.objects.get(id=oid)
    print(ob.status)
    print('================')
    context={'status':ob}
    return render(request,'myadmin/orders/amend.html',context)

#执行订单编辑
def amendinserts(request,oid):
    ob=Orders.objects.get(id=oid)
    ob.status=request.POST['status']
    ob.save()
    context={'info':'状态修改成功!'}
    return render(request,'myadmin/info.html',context)