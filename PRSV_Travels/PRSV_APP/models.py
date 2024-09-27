from django.db import models

# Create your models here.

class Places(models.Model):
    pin = models.IntegerField(primary_key = True) 
    place_name = models.CharField(max_length = 30) 
    state = models.CharField(max_length = 30)
    
    def __str__(self):
        return f"{self.place_name}"
        
    class Meta:
        db_table = 'Places'
        

class Hotels(models.Model):
    id_hotel = models.IntegerField(primary_key = True)
    pin = models.IntegerField()  
    name = models.CharField(max_length = 30) 
    place_name = models.CharField(max_length = 30) 
    state = models.CharField(max_length = 30)
    price = models.IntegerField() 
    
    fk_hot_pla = models.ForeignKey(Places, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = 'Hotels'
        
         
class Vehicles(models.Model):
    reg_no = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length = 30) 
    ac = models.BooleanField()
    
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = 'Vehicle'
              

class Drivers(models.Model):
    id = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length = 30)
    age = models.IntegerField()  
    yoe = models.IntegerField()
    price = models.IntegerField()  
    
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = 'Drivers'
        
        
class Guides(models.Model):
    id = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length = 30)
    age = models.IntegerField()  
    yoe = models.IntegerField()
    price = models.IntegerField()    
    
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = 'Guides'


class Ticket(models.Model):
    ticket_reg_no = models.CharField(max_length = 5, primary_key = True)
    from_place = models.CharField(max_length = 30)
    to_place = models.CharField(max_length = 30)
    distance = models.IntegerField()
    sdate =  models.DateField()
    edate =  models.DateField()
    
    hot_reg_no = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    veh_reg_no = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    dri_id = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    gui_id = models.ForeignKey(Guides, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.ticket_reg_no}"
        
    class Meta:
        db_table = 'Ticket'


class Customer(models.Model):
    ticket_reg_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)    
    fname = models.CharField(max_length = 25)
    lname = models.CharField(max_length = 25)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1)
    address = models.CharField(max_length = 30)
    
    def __str__(self):
        return f"{self.fname + ' ' + self.lname}"
        
    class Meta:
        db_table = 'Customer'
        

class Admin(models.Model):
    uid = models.IntegerField(primary_key = True)
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)
    
    def __str__(self):
        return f"{self.username}"
        
    class Meta:
        db_table = 'Admin'
    
