from django.db import models
# venv\Scripts\activate
# Create your models here.

DURATION_CHOICES = (
    ('6month','6 MONTHS'),
    ('12month', '12 MMONTHS'),
    ('18month','18 MONTHS'),
    ('24month','24 MONTHS'),
    ('36month','36 MONTHS'),
)
class bank(models.Model):
    toal_budget=models.DecimalField(max_digits=10, decimal_places=2)
    provide=models.DecimalField(max_digits=10, decimal_places=2)


class loanprovider(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile=models.IntegerField(max_length=11)
    email=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)
    provide_history=models.ForeignKey(bank, on_delete=models.CASCADE)
    def __str__(self):
        return self.id
    


class loan(models.Model):
    loan_amount=models.DecimalField(max_digits=10, decimal_places=2)
    duration=models.CharField(max_length=7, choices=DURATION_CHOICES, default='6month')
    interest_rate= models.DecimalField(max_digits=5, decimal_places=2)
    total_loan=models.DecimalField(max_digits=10,decimal_places=2)
    minimum_salary=models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def interest_price(self):
        if self.duration=='6month':
            return self.interest_rate==0.05
        elif self.duration=='12month':
            return self.interest_rate==0.1   
        elif self.duration=='18month':
            return self.interest_rate==0.15
        elif self.duration=='24month':
            return self.interest_rate==0.18
        elif self.duration=='36month':
            return self.interest_rate==0.2
    @property
    def total_price(self):
        self.total_loan=self.loan_amount +(self.loan_amount * self.interest_rate)        
        return self.total_loan



class loancustomer(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile=models.IntegerField(max_length=11)
    email=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    loandetail=models.ForeignKey(loan, on_delete=models.CASCADE)
    def __str__(self):
        return self.id
