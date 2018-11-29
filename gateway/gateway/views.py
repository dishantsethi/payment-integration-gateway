from django.shortcuts import render

def pay_button(request):  
    return render(request , pay.html)


# Note: Please read this before integrate.
# The response_data contain following details. 
# {'MERCHANT_KEY': '3o6jgxhp',
#  'action': 'https://sandboxsecure.payu.in/_payment',
#  'hash_string': '3o6jgxhp|123456789122212|100.0|TEST PRODUCT|Renjith|renjithsraj@live.com|||||||||||67bAgZX1B3',
#  'hashh': 'b2cf76954c390a4aa318fb1b3c918a3a9304fb18c7f7d3314ce5539dca6ee42187493a0f8b87f07aa2e5bab2ffd6a161b62c66d0897b58efc94e0ae32bfed21a',
#  'posted': {'amount': '100.0',
#   'email': 'renjithsraj@live.com',
#   'firstname': 'Renjith',
#   'furl': '/',
#   'key': '3o6jgxhp',
#   'phone': '9746272610',
#   'productinfo': 'TEST PRODUCT',
#   'surl': '/',
#   'txnid': '123456789122212'},
#  'service_provider': 'payu_paisa',
#  'txnid': '123456789122212'}    
