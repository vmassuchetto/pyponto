This script will calculate the working hours in a date range from a date file.

Parameters
----------

    -h, --help            show this help message and exit
    -f DATE_FILE, --file=DATE_FILE
                          Date file.
    --start=DATE_START    Start date in format DD/MM/YYYY.
    --end=DATE_END        End date in format DD/MM/YYYY.
    --shift=SHIFT         Shift duration by day in hours.
    --interval=INTERVAL   Total intervals duration by day in hours.

Usage
-----

    ./pyponto.py \
        --file ~/doc/ponto.txt \
        --shift 8 \
        --interval 1 \
        --start 18/07/2012 \
        --end 31/07/2012

File Format
-----------

    31/07/2012 08:05
    30/07/2012 07:42 17:21
    29/07/2012
    28/07/2012
    27/07/2012 07:54 17:15 # Comment
    26/07/2012 09:00 18:00
    25/07/2012 07:50 18:40 # Comment
    24/07/2012 07:47 17:16
    23/07/2012 07:51 17:23
    22/07/2012
    21/07/2012
    20/07/2012 07:51 17:51
    19/07/2012 08:01 17:26
    18/07/2012 07:53 17:13

Output For The Above
--------------------

    30/07/2012 07:42 17:21 +0:39:00
    27/07/2012 07:54 17:15 +0:21:00
    26/07/2012 09:00 18:00 -0:00:00
    25/07/2012 07:50 18:40 +1:50:00
    24/07/2012 07:47 17:16 +0:29:00
    23/07/2012 07:51 17:23 +0:32:00
    20/07/2012 07:51 17:51 +1:00:00
    19/07/2012 08:01 17:26 +0:25:00
    18/07/2012 07:53 17:13 +0:20:00
             9             +5:36
