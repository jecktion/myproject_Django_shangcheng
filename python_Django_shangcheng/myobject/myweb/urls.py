"""myobject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views,viewsorders,viewsusers

urlpatterns = [
     

    
    #商城前台首页
    url(r'^shopindex$', views.shopindex,name='shopindex'), #  商城首页
    url(r'^shoplist$', views.shoplist,name='shoplist'), #  商城列表页
    url(r'^shopdetail/(?P<gid>[0-9]+)$', views.shopdetail,name='shopdetail'), #  商城详情页


    
    
    # 前台会员登录路由
    url(r'^login$', viewsusers.login, name="login"),  #  登陆页
    url(r'^dologin$', viewsusers.dologin, name="dologin"),
    url(r'^logout$', viewsusers.logout, name="logout"),
    url(r'^verify$', viewsusers.verify, name="verify"), #验证码

    
    # 前台会员注册路由
    url(r'^register$', viewsusers.register,name='register'), #  注册页
    url(r'^registeradd$', viewsusers.registeradd,name='registeradd'), #  注册页
    url(r'^registerinsert$', viewsusers.registerinsert,name='registerinsert'), #注册执行
    

    #购物车路由
    url(r'^shopcart$', viewsorders.shopcart,name='shopcart'), #  购物车页
    url(r'^shopcartadd/(?P<gid>[0-9]+)$', viewsorders.shopcartadd,name='shopcartadd'), #  添加购物车
    url(r'^shopcartdel/(?P<gid>[0-9]+)$', viewsorders.shopcartdel,name='shopcartdel'), #  删除购物车中一件
    url(r'^shopcartclear$', viewsorders.shopcartclear,name='shopcartclear'), #  清空购物车
    url(r'^shopcartchange$', viewsorders.shopcartchange,name='shopcartchange'), #  更改购物车商品数量
    

    #订单详情页
    url(r'^order$',viewsorders.order,name='order'),
    url(r'^ordersform$', viewsorders.ordersform,name='ordersform'), #浏览订单
    url(r'^ordersconfirm$', viewsorders.ordersconfirm,name='ordersconfirm'), #订单确认
    url(r'^ordersinsert$', viewsorders.ordersinsert,name='ordersinsert'), #执行订单添加
    url(r'^ordersinfo$', viewsorders.ordersinfo,name='ordersinfo'), #订单信息
    



    #我的商城页个人中心
    url(r'^shopmember$', viewsorders.shopmember,name='shopmember')



]
