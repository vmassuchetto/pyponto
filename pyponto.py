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
parser.add_option("-f", "--file", dest = "date_file",
    help = u"Arquivo com as datas.")
parser.add_option("-i", "--init", dest = "date_init",
    help = u"Data inicial no formato DD/MM/YYYY.")
parser.add_option("-e", "--end", dest = "date_end",
    help = u"Data final no formato DD/MM/YYYY.")
(options, args) = parser.parse_args()

try:
    date_file = options.date_file
    date_init = datetime.strptime(options.date_init, day_fmt)
    date_end = datetime.strptime(options.date_end, day_fmt)
except:
    parser.print_help()
    exit()

try:
    f = open(date_file, 'r')
except:
    parser.print_help()
    exit()

pattern = '(?P<date>[0-9/]+)\s+(?P<init>[0-9:]+)\s+(?P<end>[0-9:]+)'
pattern = re.compile(pattern)

total_days = 0

for line in f.readlines():

    try:
        m = pattern.match(line)
        date = datetime.strptime(m.group('date'), day_fmt)
        init = datetime.strptime(m.group('init'), time_fmt)
        end = datetime.strptime(m.group('end'), time_fmt)
    except:
        continue

    if date < date_init or date > date_end:
        continue

    extra = end - init - shift - interval
    if extra > timedelta(0):
        status = '+'
        total_extra += extra;
    else:
        status = '-'
        extra = shift - shift - extra
        total_extra -= extra;

    total_days += 1

    print '%s\t%s\t%s\t%s%s' % (
        date.strftime(day_fmt), init.strftime(time_fmt),
        end.strftime(time_fmt), status, extra)

if total_extra.total_seconds() > 0:
    status = '+'
else:
    status = '-'

print '\t%s\t\t\t%s%d:%d' % (
    total_days,
    status,
    abs(total_extra.total_seconds() / 3600),
    abs(total_extra.total_seconds() % 3600 / 60))
