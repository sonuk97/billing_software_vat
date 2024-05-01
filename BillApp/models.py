from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    cmp_id = models.AutoField(('CID'),primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    phone_number = models.BigIntegerField(null= True, blank= True)
    gst_number = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=150,null=True,blank=True)
    country = models.CharField(max_length=150,null=True,blank=True)
    logo = models.ImageField(upload_to='logo/',null=True)

class ClientTrials(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    company =  models.ForeignKey(Company,on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null = True, blank=True)
    end_date = models.DateField(null = True, blank=True)
    trial_status = models.BooleanField(null = True, default = True)
    purchase_start_date = models.DateField(null = True)
    purchase_end_date = models.DateField(null = True)
    payment_term = models.CharField(max_length=50,null=True)
    purchase_status = models.CharField(max_length = 15,null = True, default = 'false')
    subscribe_status = models.CharField(max_length = 50, null = True, default = 'null')

class PaymentTerms(models.Model):
    duration = models.IntegerField(null=True, default=0)
    term = models.CharField(max_length=20, null=True, default='Days')
    days = models.IntegerField(null=True, default = 0)

class Items(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    hsn = models.IntegerField()
    unit = models.CharField(max_length=100)
    tax = models.CharField(max_length=50)
    sale_price = models.FloatField(null=True, blank= True)
    purchase_price = models.FloatField(null=True, blank= True)
    stock = models.IntegerField()
    date = models.DateField(auto_now_add=True, auto_now=False, null=True, blank= True)

class Item_units(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

class Item_transactions(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    date = models.DateField(blank=True, null= True)
    quantity = models.IntegerField()
    bill_number = models.CharField(max_length=50, null=True , blank=True)

class Purchases(models.Model):
    bill_no = models.AutoField(('bill_no'),primary_key=True)
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True, blank=True)
    party_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    gstin = models.CharField(max_length=15)
    subtotal = models.FloatField(null=True, blank= True)
    tax = models.FloatField(null=True, blank= True)
    adjustment = models.FloatField(null=True, blank= True)
    total_amount = models.FloatField(null=True, blank= True)
    # deleted_bill_no = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='deleted_bills')

class DeletedPurchases(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=50)


class Purchase_items(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    pid = models.ForeignKey(Purchases, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    hsn = models.CharField(max_length=15)
    quantity = models.IntegerField()
    rate = models.FloatField()
    tax = models.CharField(max_length=10)
    total = models.FloatField()

class Sales(models.Model):
    bill_no = models.AutoField(('bill_no'),primary_key=True)
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True, blank=True)
    party_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    gstin = models.CharField(max_length=15)
    subtotal = models.FloatField(null=True, blank= True)
    tax = models.FloatField(null=True, blank= True)
    adjustment = models.FloatField(null=True, blank= True)
    total_amount = models.FloatField(null=True, blank= True)

class Sales_items(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    sid = models.ForeignKey(Sales, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200)
    hsn = models.CharField(max_length=15)
    quantity = models.IntegerField()
    rate = models.FloatField()
    tax = models.CharField(max_length=10)
    total = models.FloatField()

class DeletedSales(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=50)