#!/usr/data_daysin/env python
# -*- coding: UTF-8 -*-
from datetime import *

data_previsao = '28-10-2014 08:30'
data_formatada = datetime.strptime(data_previsao, '%d-%m-%Y %H:%M')

tempo = 31
print (tempo)

horas = tempo % 8
print ("horas: " + str(horas))

dias = tempo / 8
print ("dias: " + str(dias))

data_days = data_formatada + timedelta(days = dias)
data_final = data_days + timedelta(hours = horas)

if data_final.hour >= 12:
	data_final = data_final + timedelta(hours = 1)

print (data_final.strftime('%d-%m-%Y %H:%M'))