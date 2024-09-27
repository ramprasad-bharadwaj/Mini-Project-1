from django.contrib import admin
from django.urls import path, include
from PRSV_APP import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    
    
    
    path("destinations", views.destinations, name="destinations"),
    path("showdestinations", views.showdestinations, name="destinations"),
    path("addplaces", views.addplaces, name="addplaces"), 
    path("addplacestodb", views.addplacestodb, name="addadmintodb"), 
    path("editplaces/<int:pin>", views.editplaces, name="editplaces"), 
    path("editplaces", views.editplaces, name="editplaces"), 
    path("editplaces/updateplaces", views.updateplaces, name="updateplaces"), 
    path("remplaces/<int:pin>", views.remplaces, name="remplaces"), 
    
    
    path("captains", views.captains, name="captains"),
    path("showcaptains", views.showcaptains, name="showcaptains"),
    path("addcaptains", views.addcaptains, name="addcaptains"), 
    path("addcaptainstodb", views.addcaptainstodb, name="addcaptainstodb"), 
    path("editcaptains/<int:id>", views.editcaptains, name="editcaptains"), 
    path("editcaptains", views.editcaptains, name="editcaptains"), 
    path("editcaptains/updatecaptains", views.updatecaptains, name="updatecaptains"), 
    path("remcaptains/<int:id>", views.remcaptains, name="remcaptains"), 
    
    
    path("guides", views.guides, name="guides"),
    path("showguides", views.showguides, name="showguides"),
    path("addguides", views.addguides, name="addguides"), 
    path("addguidestodb", views.addguidestodb, name="addguidestodb"), 
    path("editguides/<int:id>", views.editguides, name="editguides"), 
    path("editguides", views.editguides, name="editguides"), 
    path("editguides/updateguides", views.updateguides, name="updateguides"), 
    path("remguides/<int:id>", views.remguides, name="remguides"), 
    
    
    
    path("hotels", views.hotels, name="hotels"),
    path("showhotels", views.showhotels, name="showhotels"),
    path("addhotels", views.addhotels, name="addhotels"), 
    path("addhotelstodb", views.addhotelstodb, name="addhotelstodb"), 
    path("edithotels/<int:id_hotel>", views.edithotels, name="edithotels"), 
    path("edithotels", views.edithotels, name="edithotels"), 
    path("edithotels/updatehotels", views.updatehotels, name="updatehotels"), 
    path("remhotels/<int:id_hotel>", views.remhotels, name="remhotels"), 
    
    
    
    path("booking", views.booking, name="booking"),
    path("bookticket", views.bookticket, name="bookticket"),
    path("showbooking", views.showbooking, name="showbooking"),
    path("edittickets/updatehotels", views.updatehotels, name="updatehotels"), 
    path("remtickets/<int:ticket_reg_no>", views.remtickets, name="remhotels"), 
    

    path("showcustomers", views.showcustomers, name="showcustomers"),
    path("remcustomers/<int:id>", views.remcustomers, name="remcustomers"), 
    
    
    path("vehicles", views.vehicles, name="vehicles"),
    path("showvehicles", views.showvehicles, name="showvehicles"),
    path("addvehicles", views.addvehicles, name="addvehicles"), 
    path("addvehiclestodb", views.addvehiclestodb, name="addvehiclestodb"), 
    path("editvehicles/<int:reg_no>", views.editvehicles, name="editvehicles"), 
    path("editvehicles", views.editvehicles, name="editvehicles"), 
    path("editvehicles/updatevehicles", views.updatevehicles, name="updatevehicles"), 
    path("remvehicles/<int:reg_no>", views.remvehicles, name="remvehicles"), 
    
    
    path("admin_login", views.admin_login, name="admin_login"),
    path("admin", views.admin, name="admin"),   
    path("admin_page", views.admin_page, name="admin"),   
    path("showadmin", views.showadmin, name="showadmin"), 
    path("addadmin", views.addadmin, name="addadmin"), 
    path("addadmintodb", views.addadmintodb, name="addadmintodb"), 
    path("editadmin/<int:id>", views.editadmin, name="editadmin"), 
    path("editadmin", views.editadmin, name="editadmin"), 
    path("editadmin/updateadmin", views.updateadmin, name="editadmin"), 
    path("remadmin/<int:id>", views.remadmin, name="remadmin"), 
]