from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
import numpy as np
import cloudinary.uploader
from statistics import mean
import cloudinary
from django.conf import settings

def result(url):
    b = pd.read_csv(url)
    c = pd.DataFrame(b)
    a = c['High'].values.tolist()
    d = c['Low'].values.tolist()
    e = []
    for i in range(1, len(a)):
        e.append(a[i]-d[i])
    test2 = a[1:]
    test3 = c['Close'].values.tolist()
    f = []
    for i in range(0, len(test2)):
        f.append(abs(test2[i]-test3[i]))
    g = []
    test4 = d[1:]
    for i in range(0, len(test4)):
        g.append(abs(test4[i]-test3[i]))
    tr = []
    for i in range(len(e)):
        tr.append(max(e[i], f[i], g[i]))
    tr = [None] + tr
    c['TR'] = tr
    # +DM1
    high = a[1:]
    low = d[1:]
    dm1 = []
    for i in range(0, len(high)):
        if (high[i]-high[i-1]) > (low[i-1]-low[i]):
             dm1.append(max(high[i]-high[i-1], 0))
        else:
             dm1.append(0)
    dm1 = [None]+dm1
    c['+DM 1'] = dm1
    # -DM1
    nedm1 = []
    beg = 0
    first = a
    last = d
    for i in range(1, len(low)):
        if (low[i-1]-low[i]) > (high[i]-high[i-1]):
             nedm1.append(max(low[i-1]-low[i], 0))
        else:
             nedm1.append(0)
    if (last[0]-last[1]) > (first[1]-first[0]):
         beg = max(last[0]-last[1], 0)
    nedm1 = [None, beg] + nedm1
    c['-DM 1'] = nedm1
    # TR14
    tr14 = []
    start = sum(tr[1:15])
    tr14 = [None for x in range(14)]+[start]
    for i in range(15, len(tr)):
         tr14.append(tr14[i-1]-(tr14[i-1]/14)+tr[i])
    c['TR14'] = tr14
    # +DM14
    dm14 = []
    start = sum(dm1[1:15])
    dm14 = [None for x in range(14)]+[start]
    for i in range(15, len(dm1)):
         dm14.append((dm14[i-1]-(dm14[i-1]/14)+dm1[i]))
    c['+DM14'] = dm14
    # -DM14
    nedm14 = []
    start = sum(nedm1[1:15])
    nedm14 = [None for x in range(14)]+[start]
    for i in range(15, len(nedm1)):
         nedm14.append((nedm14[i-1]-(nedm14[i-1]/14)+nedm1[i]))
    c['-DM14'] = nedm14
    # +DI14
    di14 = []
    di14 = [None for x in range(14)]
    for i in range(14, len(dm14)):
         di14.append(100*dm14[i]/tr14[i])
    c['+DI14'] = di14
    # -DI14
    nedi14 = []
    nedi14 = [None for x in range(14)]
    for i in range(14, len(nedm14)):
         nedi14.append(100*nedm14[i]/tr14[i])
    c['-DI14'] = nedi14
    # +DI 14 DIFF
    di14diff = []
    di14diff = [None for x in range(14)]
    for i in range(14, len(di14)):
         di14diff.append(abs(nedi14[i]-di14[i]))
    c['DI 14 Diff'] = di14diff
    # -DI 14 SUM
    di14sum = []
    di14sum = [None for x in range(14)]
    for i in range(14, len(di14)):
         di14sum.append(nedi14[i]+di14[i])
    c['DI 14 Sum'] = di14sum
    # DX
    dx = []
    dx = [None for x in range(14)]
    for i in range(14, len(di14diff)):
         dx.append(100*di14diff[i]/di14sum[i])
    c['DX'] = dx
    # ADX
    adx = []
    adx_start = mean(dx[14:28])
    adx = [None for x in range(27)]+[adx_start]
    for i in range(28, len(dx)):
         adx.append((adx[i-1]*13+dx[i])/14)
    c['ADX'] = adx
#     c.fillna(0, inplace=True)
    c.to_csv('result.csv')
    fb = open('result.csv', 'rb')
    res = cloudinary.uploader.upload(fb, upload_preset='react-tracks',
                                     resource_type="raw", cloud_name='saiashish', api_secret=settings.API_SECRET, api_key=settings.API_KEY)
    return res['secure_url']



@api_view(['GET','POST'])
def csv(request):
    if request.method == 'GET':
            return JsonResponse({"msg":"hi"})
    
    if request.method == 'POST':
            res=result(request.data['url'])
            return JsonResponse({"result":res})





