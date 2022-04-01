from unittest import result
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def lotto(request):
    import random
    lotto_number = []
    while True :
        num = random.randrange(1,46)
        if lotto_number.count(num) == 0 :
            lotto_number.append(num)
        if len(lotto_number) == 6 :
            break
    lotto_number.sort()
    for i in range (len(lotto_number)):
        print ("{}".format(lotto_number[i]),end='')

    return render(request, 'lotto.html',{'lotto_number': lotto_number})