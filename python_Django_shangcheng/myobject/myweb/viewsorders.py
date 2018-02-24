from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from myweb.models import Types,Goods,Orders,Detail

import time




#===============公共信息加载函数====================
def loadinfo():
    context={}
    context['type0list'] = Types.objects.filter(pid=0)
    return context




#====================我的商城页面========================
def shopmember(request):
    context = {}
    return render(request,"myweb/shopmember.html",context)







# ====================购物车详情页=========================
def shopcart(request):
    context = loadinfo()
    if 'shoplist' not in request.session:
        request.session['shoplist']={}
    return render(request,"myweb/shopcart.html",context)


def shopcartadd(request,gid):
    #获取要添加的购物车信息
    goods = Goods.objects.get(id=gid)
    shop = goods.toDict();
    shop['m'] = int(request.POST['m'])

    
    #获取原购物车中的信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    #判断并放置到session中
    if gid in shoplist:
        shoplist[gid]['m'] += shop['m'] #若购物车中已包含要购买的商品，就将购买量加，
    else:
        shoplist[gid] = shop  # 若不存在则将当前商品直接放入购物车shoplist中

    #将购物车信息shoplist放入到session中
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))



def shopcartdel(request,gid):
    #获取购物车中的商品
    shoplist = request.session['shoplist']
    #删除对应的商品
    del shoplist[gid]
    #放回购物车到session中
    request.session['shoplist']=shoplist
    
    return redirect(reverse('shopcart'))



def shopcartclear(request):
    context = loadinfo()
    request.session['shoplist'] = {}
    return render(request,"myweb/shopcart.html",context)

def shopcartchange(request):
    context = loadinfo()
    shoplist = request.session['shoplist']
    #获取信息
    shopid = request.GET['gid']
    num = int(request.GET['num'])
    if num < 1:
        num = 1
    shoplist[shopid]['m'] = num  #更改商品数量
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shopcart.html",context)



#=============我的订单操作===========================
#我的订单
def order(request):
    context = loadinfo()
    #从session中获取登录者的id,并从订单表orders中获取当前用户的所有的订单
    orders = Orders.objects.filter(uid=request.session['vipuser']['id'])
    # print(orders)
    #遍历当前用户的所有的订单信息,并获取每个订单所对应的订单详情信息,并以detaillist属性放置
    for order in orders:
        dlist = Detail.objects.filter(orderid=order.id)  #获取当前订单中的详情
        # print(dlist)
        order.detaillist = dlist   #将订单详情以detaillist属性放置到订单对象中
        #遍历当前用户的所有的订单详情,并追加每个商品的图片信息
        for detail in dlist:
            goods = Goods.objects.get(id=detail.goodsid)
            detail.picname = goods.picname
        context['orders'] = orders  
    return render(request,'myweb/order.html',context)

#=====================订单详情页面==============================
#订单表单页
def ordersform(request):
    #获取药结账的商品id信息
    ids = request.GET.get('gids','')
    if ids == '':
        return HttpResponse("请选择要结账的商品")
    # print(999)
    gids = ids.split(',')
    #获取购物车中的商品信息
    shoplist = request.session['shoplist']
    #封装要结帐的商品信息,以及累计总额
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        total += shoplist[sid]['price']*shoplist[sid]['m']  #累计总金额
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    return render(request,"myweb/ordersform.html")


#订单确认页面
def ordersconfirm(request):
    return render(request,"myweb/ordersconfirm.html")



#执行订单添加
def ordersinsert(request):
    #封装订单信息,并执行添加
    orders = Orders()
    orders.uid = request.session['vipuser']['id']
    orders.linkman = request.POST['linkman']
    # orders.linkman = request.POST.get('linkman')

    print(orders.linkman)
    orders.address = request.POST['address']
    orders.code = request.POST['code']
    orders.phone = request.POST['phone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    #获取订单详情
    orderlist = request.session['orderlist']
    shoplist = request.session['shoplist']
    #便利购物信息,并添加订单详情信息
    for shop in orderlist.values():
        del shoplist[str(shop['id'])]
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()

    del request.session['orderlist']
    del request.session['total']
    request.session['shoplist'] = shoplist
    return HttpResponse("订单成功:订单id号: "+str(orders.id))


   


#订单信息
def ordersinfo(request):
    return render(request,"myweb/order.html")
