from django.contrib import admin
from django.contrib.auth.models import User
from .models import Stake


# Register your models here.
class StakemodelAdmin(admin.ModelAdmin):
    
    list_display=('id','investor_agent',
                  'stake_user_name','email',
                  'amount','status',
                  'staking_duration',
                  'staking_rate',
                  'total_profit',
                  'daily_profit_rate',)
    search_fields = ['id','email','investor','send_daily_interest_emails',]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.total_profit:
            obj.daily_profit_rate()
    
    
admin.site.register(Stake, StakemodelAdmin)

  













