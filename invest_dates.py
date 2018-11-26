"""Pick several dates in the coming N months on which to make investments.

Usage (to pick dates in the coming 17 months):

  $ python invest_dates.py 17

Usage, which also generates a handy HTML file of add-to-calendar links:

  $ python invest_dates.py 17 invest_date_links.html

It's important to take your cash savings and move them into returns-generating
investments.  But it's also important to make sure those investments are
diversified.  And not just in terms of *what* you pick as an investment (stock,
vs. bond, vs., I dunno, a REIT or something), but also diversified in terms of
*when* you purchase assets.

"Timing the market" is a hard thing to do, and there's a whole industry of
bandits waiting to take your money if you screw it up.  So here's a utility that
will just pick some dates randomly.  Hopefully that'll smooth out your exposure
any particular market conditions at the time of purchase.  E.g., if you just have
a standing calendar event to always buy on the first of the month, but so does
every other lazy lay investor, you'll always be buying at slightly inflated
prices!! Let me repeat that: **SLIGHTLY INFLATED!!!!!**

Give it a parameter for how many months into the future you'd like to plan for,
and it will return one random date from each of the coming months.  That date
will always be a weekday, Monday through Friday.  That should make it more
likely that you can place your order on the particular day, though maybe you'll
have to wait in case of it being a bank holiday.  That's a source of bias buuut
whatevs, I'm not exactly running Jane Street here.

This will print the set of selected weekdays, and a Google Calendar link to
add "MAKE INVESTMENT" as an all-day event.

Anyway, don't leave nickels on the table, use this thing to diversify your
investing along the time axis.
"""

import random
import sys

from datetime import date, timedelta


def IncrementMonth(d):
    "Returns the first date of the next month following `d`."
    curr_month = d.month
    while d.month == curr_month:
        d += timedelta(days=1)
    return d


def PickLuckyDate(year, month):
    while True:
        lucky_day = random.randint(1, 31)
        try:
            lucky_date = date(year=year, month=month, day=lucky_day)
        except:
            continue
        if lucky_date.weekday() not in (5, 6):
            return lucky_date


def GetGoogleCalendarLink(d):
    "Return a link to add an all-day event for date `d`."
    d_str = d.strftime("%Y%m%d")
    dp1 = d + timedelta(days=1)
    dp1_str = dp1.strftime("%Y%m%d")
    return ("http://www.google.com/calendar/event?"
            "action=TEMPLATE"
            "&text=Invest+Savings"
            "&dates=%s/%s"
            "&details=Purchase+investments"
            "&trp=false"
            "&sprop="
            "&sprop=name:") % (d_str, dp1_str)


def GetHTML(dates_and_links):
    header = """
    <html>
        <head>
            <title>Dates to make investments</title>
        </head>
        <body>
            <h1>Dates to make investments</h1>
            <ul>
    """
    footer ="""
            </ul>
        </body>
    </html>
    """
    html = header
    for d, link in dates_and_links:
        d_str = d.strftime("%Y-%m-%d")
        html += ("""
            <li><a href="%s">%s</a></li>
        """ % (link, d_str))
    html += footer
    return html


def main(num_months, html_outfile=None):
    # Encodes the current month we're going to sample from.
    # Start with the next calendar month.
    dates_and_links = []
    month_ptr = IncrementMonth(date.today())
    for _ in range(num_months):
        # The date we'll pick for this month:
        lucky_date = PickLuckyDate(year=month_ptr.year, month=month_ptr.month)
        print lucky_date
        link_str = GetGoogleCalendarLink(lucky_date)
        print link_str
        print ""
        month_ptr = IncrementMonth(month_ptr)
        dates_and_links.append((lucky_date, link_str))
    if html_outfile is not None:
        with open(html_outfile, "w") as outfile:
            outfile.write(GetHTML(dates_and_links))


if __name__ == "__main__":
    try:
        num_months = int(sys.argv[1])
    except:
        # Ugh, I'm too lazy to specify expected exceptions
        num_months = 12
    try:
        html_out = sys.argv[2]
    except:
        html_out = None
    main(num_months, html_out)
