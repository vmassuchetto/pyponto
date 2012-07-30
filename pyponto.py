#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from datetime import datetime
from datetime import timedelta
from optparse import OptionParser

day_fmt = '%d/%m/%Y'
time_fmt = '%H:%M'

interval = timedelta(hours = 1)
shift = timedelta(hours = 8)
total_extra = timedelta()

parser = OptionParser()
parser.add_option("-i", "--inicial", dest = "data_inicial",
    help = u"Data inicial no formato DD/MM/YYYY.")
parser.add_option("-f", "--final", dest = "data_final",
    help = u"Data final no formato DD/MM/YYYY.")
(options, args) = parser.parse_args()

try:
    data_inicial = datetime.strptime(options.data_inicial, day_fmt)
    data_final = datetime.strptime(options.data_final, day_fmt)
except:
    parser.print_help()
    exit()

pattern = '(?P<data>[0-9/]+)\s+(?P<entrada>[0-9:]+)\s+(?P<saida>[0-9:]+)'
pattern = re.compile(pattern)

total_days = 0

f = open('/home/vinicius/doc/ponto.txt', 'r')
for line in f.readlines():

    try:
        m = pattern.match(line)
        data = datetime.strptime(m.group('data'), day_fmt)
        entrada = datetime.strptime(m.group('entrada'), time_fmt)
        saida = datetime.strptime(m.group('saida'), time_fmt)
    except:
        continue

    if data < data_inicial or data > data_final:
        continue

    extra = saida - entrada - shift - interval
    if extra > timedelta(0):
        status = '+'
        total_extra += extra;
    else:
        status = '-'
        extra = shift - shift - extra
        total_extra -= extra;

    total_days += 1

    print '%s\t%s\t%s\t%s%s' % (
        data.strftime(day_fmt), entrada.strftime(time_fmt),
        saida.strftime(time_fmt), status, extra)

if total_extra.total_seconds() > 0:
    status = '+'
else:
    status = '-'

print '\t%s\t\t\t%s%d:%d' % (
    total_days,
    status,
    abs(total_extra.total_seconds() / 3600),
    abs(total_extra.total_seconds() % 3600 / 60))
