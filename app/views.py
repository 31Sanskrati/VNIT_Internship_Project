from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        #personal information
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        aadhar_card_number = request.POST['aadhar_card_number']
        pan_card = request.POST['pan_card']

        #financial information
        annual_income = request.POST['annual_income']
        net_worth = request.POST['net_worth']
        liquid_net_worth = request.POST['liquid_net_worth']

        #DMAT account information
        dmat_account_number = request.POST['dmat_account_number']
        brokerage_firm = request.POST['brokerage_firm']
        account_credentials = request.POST['account_credentials']

        #consent info
        consent_personal_info = request.POST['consent_personal_info']
        consent_financial_info = request.POST['consent_financial_info']
        consent_dmat_account = request.POST['consent_dmat_account']
        consent_terms_conditions = request.POST['consent_terms_conditions']

    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def edit_account(request):
    return render(request, 'edit_account.html')

def view_account(request):
    return render(request, 'view_account.html')

def delete_account(request):
    return render(request, 'delete_account.html')

def recover_account(request):
    return render(request, 'recover_account.html')
