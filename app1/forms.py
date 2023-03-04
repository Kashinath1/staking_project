from django import forms
from .models import Stake

class StakeForm(forms.ModelForm):
    class Meta:
        model = Stake
        fields = ['investor_agent', 'stake_user_name', 'email', 'phone_number', 'amount', 'start_date', 'end_date', 'status', 'staking_rate']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
