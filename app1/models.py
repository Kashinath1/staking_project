from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from decimal import Decimal
from django.template.loader import render_to_string

# Create your models here.
class Stake(models.Model):
    investor_agent = models.ForeignKey(User, on_delete=models.CASCADE)
    stake_user_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('closed', 'Closed')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    staking_rate = models.IntegerField()


    def staking_duration(self):
        duration = self.end_date - self.start_date
        years = duration.days / 365.25
        return round(years,2)
     


    def total_profit(self):
        duration = Decimal(self.staking_duration())
        rate = Decimal(str(self.staking_rate))
        profit = self.amount * duration * rate /Decimal ('100')
        return round(profit, 2)
    


    
    def daily_profit_rate(self):
        staking_period = Decimal(str(self.staking_duration()))
        daily_profit_rate = Decimal(str(self.staking_rate)) / (Decimal('365.25') / Decimal(str(staking_period)))
        return round(daily_profit_rate, 5)
    


    # email service for staking 
    
    def send_email_notification(self):
        subject = f"Staking Notification for {self.stake_user_name}"
        message = f"Hello {self.stake_user_name},\n\n"\
                  f"You have staked {self.amount} for a duration of {self.staking_duration()} years.\n"\
                  f"Your daily profit rate is {self.daily_profit_rate()} and your total profit is {self.total_profit()}.\n\n"\
                  "Thank you for using our platform.\n\n"\
                  "Best regards,\n"\
                  "The Investment Team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email], fail_silently=False)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_email_notification()

    


# class Wallet(models.Model):
#     stake = models.ForeignKey(Stake, on_delete=models.CASCADE)
#     daily_profit = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



    









   


    



    


