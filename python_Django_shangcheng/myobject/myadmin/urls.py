
from django.conf.urls import url
from . import views,viewsgoods,viewsorders

urlpatterns = [
    
    # 后台首页
    url(r'^$', views.index, name="myadmin_index"),


    # 后台用户管理
    url(r'^users/(?P<pIndex>[0-9]*)$', views.usersindex, name="myadmin_usersindex"),# 浏览会员
    url(r'^usersadd$', views.usersadd, name="myadmin_usersadd"),# 会员信息添加表单
    url(r'^usersinsert$', views.usersinsert, name="myadmin_usersinsert"),#执行会员信息添加
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel, name="myadmin_usersdel"),# 执行会员信息删除
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit, name="myadmin_usersedit"),# 打开会员信息编辑表单
    url(r'^usersupdate/(?P<uid>[0-9]+)$', views.usersupdate, name="myadmin_usersupdate"),# 执行会员信息编辑
    

    # 后台管理员路由
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),
    url(r'^verify$', views.verify, name="myadmin_verify"), #验证码


    # 后台商品类别信息管理
    url(r'^type/(?P<pIndex>[0-9]*)$', viewsgoods.typeindex, name="myadmin_typeindex"),
    url(r'^typeadd/(?P<tid>[0-9]+)$', viewsgoods.typeadd, name="myadmin_typeadd"),
    url(r'^typeinsert$', viewsgoods.typeinsert, name="myadmin_typeinsert"),
    url(r'^typedel/(?P<tid>[0-9]+)$', viewsgoods.typedel, name="myadmin_typedel"),
    url(r'^typeedit/(?P<tid>[0-9]+)$', viewsgoods.typeedit, name="myadmin_typeedit"),
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.typeupdate, name="myadmin_typeupdate"),


    # 后台商品信息管理
    url(r'^goods/(?P<pIndex>[0-9]*)$', viewsgoods.goodsindex, name="myadmin_goodsindex"),
    url(r'^goodsadd$', viewsgoods.goodsadd, name="myadmin_goodsadd"),
    url(r'^goodsinsert$', viewsgoods.goodsinsert, name="myadmin_goodsinsert"),
    url(r'^goodsdel/(?P<gid>[0-9]+)$', viewsgoods.goodsdel, name="myadmin_goodsdel"),
    url(r'^goodsedit/(?P<gid>[0-9]+)$', viewsgoods.goodsedit, name="myadmin_goodsedit"),
    url(r'^goodsupdate/(?P<gid>[0-9]+)$', viewsgoods.goodsupdate, name="myadmin_goodsupdate"),


    #后台订单管理
    url(r'^orders$',viewsgoods.ordersindex,name="myadmin_ordersindex"),
    url(r'^ordersedit/(?P<gid>[0-9]*)$',viewsgoods.ordersedit,name="myadmin_ordersedit"),
    # url(r'^ordersinsert/(?P<gid>[0-9]$',viewsgoods.ordersinsert,name="myadmin_ordersinsert"),

    #后台订单状态修改
    url(r'^amendedicts/(?P<oid>[0-9]*)$',viewsorders.amendedicts,name="myadmin_amendedicts"),#订单状态修改
    url(r'^amendinserts/(?P<oid>[0-9]*)$',viewsorders.amendinserts,name="myadmin_amendinserts"),#订单状态修改执行
    
    
    
]
