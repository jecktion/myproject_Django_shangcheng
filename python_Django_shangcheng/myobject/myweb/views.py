from django.shortcuts import render
from django.http import HttpResponse
from myweb.models import Users

from myweb.models import Types,Goods	


#公共信息加载函数
def loadinfo():
    context={}
    context['type0list'] = Types.objects.filter(pid=0)
    return context

# 商城首页
def shopindex(request):
    context = loadinfo()
    list = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        list = list.filter()
    context['goodslist'] = list
    return render(request,"myweb/shopindex.html",context)

# 商城商品列表页
def shoplist(request):
    context = loadinfo()
    list = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        list = list.filter()
    context['goodslist'] = list
    return render(request,"myweb/shoplist.html",context)

# 商城商品详情页
def shopdetail(request,gid):
    context = loadinfo()
    ob = Goods.objects.get(id=gid)
    #累加点击量
    ob.clicknum += 1
    ob.save()
    
    context['goods'] = ob
    return render(request,"myweb/shopdetail.html",context)






