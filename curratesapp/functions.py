from .models import CurRates
from datetime import date
import requests


def get_curr_rate():
    today = date.today()
    q = CurRates.objects.filter(day=today)
    if q.exists():
        return q.get().rate
    rate_usd = CurRates()
    rate_usd.day = today
    try:
        rate_usd.rate = requests.get('http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2'). \
            json()['Cur_OfficialRate']
        rate_usd.save()
        return rate_usd.rate
    except requests.ConnectionError:
        print('Can\'t get usd rate')
