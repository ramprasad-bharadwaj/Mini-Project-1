from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import *
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.


#---------------------------------------------------------------------------#


def index(request):
    return render(request, 'index.html')


#---------------------------------------------------------------------------#

def destinations(request):
    places = Places.objects.all()
    return render(request, 'destinations.html',{'places':places})

def showdestinations(request):
    places = Places.objects.all()
    return render(request, 'showdestinations.html',{'places':places})

def addplaces(request):
    return render(request, 'addplaces.html')

def addplacestodb(request):
    pin = request.POST.get('pin')
    place_name = request.POST['place_name']
    state = request.POST['state']
    user_save = Places(pin = pin, place_name = place_name, state = state)
    user_save.save()
    places = Places.objects.all()
    return render(request, 'showdestinations.html',{'places':places})

def editplaces(request, pin):
    places = Places.objects.get(pin=pin)
    return render(request, 'editplaces.html',{'places':places})

def updateplaces(request):  
    pin = request.POST['pin'] 
    place_name = request.POST['place_name']
    state = request.POST['state']
    user_save = Places(pin = pin, place_name = place_name, state = state)
    user_save.save()
    return redirect('/showdestinations')


def remplaces(request, pin):
    place = Places.objects.get(pin=pin)
    place.delete()
    return redirect('/showdestinations')
    




#---------------------------------------------------------------------------#

def captains(request):
    captains = Drivers.objects.all()
    return render(request, 'captains.html', {'captains':captains})

def showcaptains(request):
    captains = Drivers.objects.all()
    return render(request, 'showcaptains.html',{'captains':captains})

def addcaptains(request):
    return render(request, 'addcaptains.html')

def addcaptainstodb(request):
    id = request.POST.get('id')
    name = request.POST['name']
    age = request.POST['age']
    yoe = request.POST['yoe']
    price = request.POST['price']
    user_save = Drivers(id = id, name = name, age = age, yoe= yoe, price = price)
    user_save.save()
    captains = Drivers.objects.all()
    return render(request, 'showcaptains.html',{'captains':captains})

def editcaptains(request, id):
    captains = Drivers.objects.get(id=id)
    return render(request, 'editcaptains.html',{'captains':captains})

def updatecaptains(request):  
    id = request.POST.get('id')
    name = request.POST['name']
    age = request.POST['age']
    yoe = request.POST['yoe']
    price = request.POST['price']
    user_save = Drivers(id = id, name = name, age = age, yoe= yoe, price = price)
    user_save.save()
    return redirect('/showcaptains')


def remcaptains(request, id):
    captains = Drivers.objects.get(id=id)
    captains.delete()
    return redirect('/showcaptains')
    



#---------------------------------------------------------------------------#

def guides(request):
    guides = Guides.objects.all()
    return render(request, 'guides.html', {'guides':guides})

def showguides(request):
    guides = Guides.objects.all()
    return render(request, 'showguides.html',{'guides':guides})

def addguides(request):
    return render(request, 'addguides.html')

def addguidestodb(request):
    id = request.POST.get('id')
    name = request.POST['name']
    age = request.POST['age']
    yoe = request.POST['yoe']
    price = request.POST['price']
    user_save = Guides(id = id, name = name, age = age, yoe= yoe, price = price)
    user_save.save()
    guides = Guides.objects.all()
    return render(request, 'showguides.html',{'guides':guides})

def editguides(request, id):
    guides = Guides.objects.get(id=id)
    return render(request, 'editguides.html',{'guides':guides})

def updateguides(request):  
    id = request.POST.get('id')
    name = request.POST['name']
    age = request.POST['age']
    yoe = request.POST['yoe']
    price = request.POST['price']
    user_save = Guides(id = id, name = name, age = age, yoe= yoe, price = price)
    user_save.save()
    return redirect('/showguides')


def remguides(request, id):
    guides = Guides.objects.get(id=id)
    guides.delete()
    return redirect('/showguides')



#---------------------------------------------------------------------------#

def hotels(request):
    hotels = Hotels.objects.all()
    return render(request, 'hotels.html',{'hotels':hotels})

def showhotels(request):
    hotels = Hotels.objects.all()
    return render(request, 'showhotels.html',{'hotels':hotels})

def addhotels(request):
    places = Places.objects.all()
    return render(request, 'addhotels.html',{ 'places':places})

def addhotelstodb(request):
    id_hotel = request.POST.get('id_hotel')
    name = request.POST['name']
    price = request.POST['price']
    pin = request.POST['pin']
    place = Places.objects.get(pin = pin)
    place_name = place.place_name
    state = place.state
    fk_hot_pla = place.pin
    user_save = Hotels(id_hotel = id_hotel, pin = pin, name = name, place_name = place_name, state = state, price = price, fk_hot_pla_id = fk_hot_pla )   
    user_save.save()
    hotels = Hotels.objects.all()
    return render(request, 'showhotels.html',{'hotels':hotels})

def edithotels(request, id_hotel):
    hotels = Hotels.objects.get(id_hotel=id_hotel)
    places = Places.objects.all()
    return render(request, 'edithotels.html',{'hotels':hotels,'places':places})

def updatehotels(request):  
    id_hotel = request.POST.get('id_hotel')
    name = request.POST['name']
    price = request.POST['price']
    pin = request.POST['pin']
    place = Places.objects.get(pin = pin)
    place_name = place.place_name
    state = place.state
    fk_hot_pla = place.pin
    user_save = Hotels(id_hotel = id_hotel, pin = pin, name = name, place_name = place_name, state = state, price = price, fk_hot_pla_id = fk_hot_pla )   
    user_save.save()
    return redirect('/showhotels')


def remhotels(request, id_hotel):
    hotels = Hotels.objects.get(id_hotel=id_hotel)
    hotels.delete()
    return redirect('/showhotels')




#---------------------------------------------------------------------------#

def booking(request):
    import random
    if(Ticket.objects.all()):
        t = Ticket.objects.all().last()
        ticket_reg_no = int(t.ticket_reg_no) + 1
    else:
        ticket_reg_no = 1 
    captains = Drivers.objects.all()
    hotels = Hotels.objects.all()
    guides = Guides.objects.all()
    places = Places.objects.all()
    vehicles = Vehicles.objects.all()
    
    return render(request, 'booking.html',{'ticket_reg_no':ticket_reg_no,'hotels':hotels,'guides':guides,'captains':captains,'places':places,'vehicles':vehicles})

def bookticket(request):
    #tickets
    import random
    if(Ticket.objects.all()):
        t = Ticket.objects.all().last()
        ticket_reg_no = int(t.ticket_reg_no) + 1
    else:
        ticket_reg_no = 1 
    
    
    from_place = request.POST['from_place']
    to_place = request.POST['to_place']
    distance = random.randint(200,700)
    sdate = request.POST['sdate']
    edate = request.POST['edate']
    veh = Vehicles.objects.get(reg_no = request.POST['vehicle']) 
    dri = Drivers.objects.get(id = request.POST['captain'])
    gui = Guides.objects.get(id = request.POST['guide'])
    hot = Hotels.objects.get(id_hotel = request.POST['hotel'])
    veh_reg_no_id =  veh.reg_no
    dri_id_id = dri.id
    gui_id_id =  gui.id
    hot_reg_no_id = hot.id_hotel
    
    user_save = Ticket(ticket_reg_no = ticket_reg_no, from_place = from_place, to_place = to_place, distance = distance, sdate = sdate, edate = edate, veh_reg_no_id = veh_reg_no_id, dri_id_id = dri_id_id, gui_id_id = gui_id_id, hot_reg_no_id = hot_reg_no_id)   
    user_save.save()
    
    # import time
    # time.sleep(1)
    
    #=customers
    
    if(Customer.objects.all()):
        c = Customer.objects.all().last()
        id = int(c.id) + 1
    else:
        id = 1
        
    # t = Ticket.objects.all().last()
    # ticket_reg_no = t.ticket_reg_no
    ticket_reg_no = Ticket.objects.get(ticket_reg_no = request.POST['ticket_reg_no'])
    fname = request.POST['fname']
    lname = request.POST['lname']
    age = request.POST['age']
    gender = request.POST['gender']
    address = request.POST['address']
    user_save1 = Customer(id = id, ticket_reg_no = ticket_reg_no, fname = fname, lname = lname, age = age, gender = gender, address = address)   
    user_save1.save()
    
    customers = Customer.objects.all().filter(id = id)  
    tickets = Ticket.objects.all().filter(ticket_reg_no = ticket_reg_no)
    
    return render(request, 'bookingsuccess.html',{'customers':customers, 'tickets':tickets})


def showbooking(request):
    tickets = Ticket.objects.all()
    return render(request, 'showbooking.html',{'tickets':tickets})

def remtickets(request, ticket_reg_no):
    ticket = Ticket.objects.get(ticket_reg_no = ticket_reg_no)
    ticket.delete()
    return redirect('/showbooking')
    

#---------------------------------------------------------------------------#

def showcustomers(request):
    customers = Customer.objects.all()
    return render(request, 'showcustomers.html',{'customers':customers})


def remcustomers(request, id):
    customer = Customer.objects.get(id = id)
    customer.delete()
    return redirect('/showcustomers')
    

#---------------------------------------------------------------------------#

def vehicles(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'vehicles.html',{'vehicles':vehicles})

def showvehicles(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'showvehicles.html',{'vehicles':vehicles})

def addvehicles(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'addvehicles.html',{'vehicles':vehicles})

def addvehiclestodb(request):
    reg_no = request.POST.get('reg_no')
    name = request.POST['name']
    ac = request.POST['ac']
    user_save = Vehicles(reg_no = reg_no, name = name, ac = ac)   
    user_save.save()
    vehicles = Vehicles.objects.all()
    return render(request, 'showvehicles.html',{'vehicles':vehicles})

def editvehicles(request, reg_no):
    vehicles = Vehicles.objects.get(reg_no=reg_no)
    return render(request, 'editvehicles.html',{'vehicles':vehicles})

def updatevehicles(request):  
    reg_no = request.POST.get('reg_no')
    name = request.POST['name']
    ac = request.POST['ac']
    user_save = Vehicles(reg_no = reg_no, name = name, ac = ac)   
    user_save.save()
    return redirect('/showvehicles')


def remvehicles(request, reg_no):
    vehicles = Vehicles.objects.get(reg_no=reg_no)
    vehicles.delete()
    return redirect('/showvehicles')




#---------------------------------------------------------------------------#

def admin_login(request):
    return render(request, 'admin_login.html')

def admin(request):
    uname = request.POST['adminusername']
    pword = request.POST['adminpassword']        
    isadmins = Admin.objects.all().filter(username = uname, password = pword)
    if(isadmins):
        return render(request, 'admin.html')
    else:
        return HttpResponse("<center><h1>Unauthorized access denied</h1><p>Incorrect username and password</p></center>")

def admin_page(request):
    return render(request, 'admin.html')
    
def showadmin(request):
    admins = Admin.objects.all()
    return render(request, 'showadmin.html',{'admins':admins})
    
def addadmin(request):
    return render(request, 'addadmin.html')

def addadmintodb(request):
    uid = request.POST.get('uid', False)
    username = request.POST['username']
    password = request.POST['password']
    user_save = Admin(uid = uid, username = username, password = password)
    user_save.save()
    admins = Admin.objects.all()
    return render(request, 'showadmin.html',{'admins':admins})
    # HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def editadmin(request, id):
    admins = Admin.objects.get(uid=id)
    return render(request, 'editadmin.html',{'admins':admins})

def updateadmin(request):  
    uid = request.POST['uid'] 
    username = request.POST['username']
    password = request.POST['password']
    user_save = Admin(uid = uid, username = username, password = password)
    user_save.save()
    return redirect('/showadmin')


def remadmin(request, id):
    admininfo = Admin.objects.get(uid=id)
    admininfo.delete()
    return redirect('/showadmin')
    
    

    
    
    
    
    '''
    # admins = Admin.objects.all()
    # string =  render(request,'')
    # HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # return render(request,'showadmin.html',{'admins':admins})
    # return addadmin
    
    
    
    # path = os.path.join(BASE_DIR, "admin.html")
    # return render(request, 'admin.html',{'admins':admins})
    # next = request.POST.get('next', '/')
    # return HttpResponseRedirect(next)
    # return redirect()
    # med = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    def admin(request):
    try:
        uname = request.POST['adminusername']
        pword = request.POST['adminpassword']
        
        # username = Admin.objects.get(username = uname)
        # password = Admin.objects.get(password = pword)
        
        isadmins = Admin.objects.all().filter(username = uname, password = pword)
        
        if(isadmins):
            return render(request, 'admin.html')
        
    except Admin.DoesNotExist:
        return HttpResponse("<center><h1>Unauthorized access denied</h1></center>")
    
    '''