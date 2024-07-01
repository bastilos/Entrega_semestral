
from django.urls import path
from .views import (
    index,index_ropa_api,usuario,usuarios,ingresar,menu_superior,miscompras,nosotros,registro,
    vistaadmin,vistausuario,carrito,boleta,bodega,admin_ventas,admin_add_prod,ficha
)

urlpatterns = [
    path("",index,name="index"),
    path("index_ropa_api",index_ropa_api,name="index_ropa_api"),
    path("ingresar",ingresar,name="ingresar"),
    path("menu_superior",menu_superior,name="menu_superior"),
    path("miscompras",miscompras,name="miscompras"),
    path("usuario",usuario,name="usuario"),
    path("usuarios",usuarios,name="usuarios"),
    path("nosotros",nosotros,name="nosotros"),
    path("registro",registro,name="registro"),
    path("vistaadmin",vistaadmin,name="vistaadmin"),
    path("vistausuario",vistausuario,name="vistausuario"),
    path("carrito",carrito,name="carrito"),
    path("ficha",ficha,name="ficha"),
    path("boleta",boleta,name="boleta"),
    path("bodega",bodega,name="bodega"),
    path("admin_ventas",admin_ventas,name="admin_ventas"),
    path("admin_add_prod",admin_add_prod,name="admin_add_prod")
]
