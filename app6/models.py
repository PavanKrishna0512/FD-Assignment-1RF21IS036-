from django.db import models

class Customer(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    Aadhaar = models.CharField(max_length=12)
    Pincode = models.CharField(max_length=6)
    CustId = models.CharField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.CustId:
            last_customer = Customer.objects.order_by('-id').first()
            if last_customer:
                last_id = int(last_customer.CustId.split('_')[1])
                self.CustId = f'CID_{last_id + 1}'
            else:
                self.CustId = 'CID_5001'
        super().save(*args, **kwargs)

def __str__(self):
        return self.name1