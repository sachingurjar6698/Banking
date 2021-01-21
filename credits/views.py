from django.shortcuts import render,redirect
from .models import User
from .models import Record
from django.http import Http404
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def transfer(request):
    users = User.objects.all()
    return render(request, 'transfer.html', {'users':users})


def money(request,user_id):
    try:
        users = User.objects.all()
        customer = User.objects.get(id=user_id)
    except:
        raise Http404("Employee Not Found")
    return render(request, 'money.html', {'customer':customer, 'users':users})


def transaction(request, user_id):
    recipient = request.POST.get("recipient")
    amount = request.POST.get("amount")  
    sender = User.objects.get(id = user_id)
    sender_name = sender.name
    receiver = User.objects.get(name = recipient)

    
    UpdatedReceiverCredit = receiver.current_credits + int(amount)
    UpdatedSenderCredit = sender.current_credits - int(amount)
 

    if sender.current_credits >= int(amount):
        transaction_status = True
        
        UpdateSender = User.objects.get(name = sender.name)
        UpdateSender.current_credits = UpdatedSenderCredit
        UpdateSender.save()

        UpdateReceiver = User.objects.get(name = receiver.name)
        UpdateReceiver.current_credits = UpdatedReceiverCredit
        UpdateReceiver.save()

    else:
        transaction_status = False

    p = Record(Name_Of_Sender=sender_name,Name_Of_Receiver=recipient,Transfer_Amount=amount,Sender_Updated_Balance=UpdatedSenderCredit,Receiver_Updated_Balance=UpdatedReceiverCredit)
    p.save()
    users = User.objects.all()
    data = {'users': users, 
            'transaction_status': transaction_status,
            'recipient': recipient,
            'sender_name': sender_name,
            'amount': amount,
        }
    return render(request,'transaction.html', data)
    


def all_transaction(request):
    user = Record.objects.all().order_by()
    paginator = Paginator(user,8)
    page = request.GET.get('pg')
    user = paginator.get_page(page)
    data = {'user': user}
    return render(request, 'all_transaction.html', data)