# `invest_dates`

Pick several dates in the coming N months on which to buy investment assets.

## Usage

To print the dates, as well as "Create Event" Google Calendar links, type:

```
$ python invest_dates.py 17
```

where `17` stands in for the number of months you're currently planning for.

To also generate a handy HTML file (so the "Create Event" calendar links are
clickable), try:

```
$ python invest_dates.py 17 invest_date_links.html
```

## Motivation

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
add "MAKE INVESTMENT" as an all-day event.  They're spaced one per calendar
month, mostly just cuz that's when I have accrued enough savings that it's worth
the effort of going throuhg the buy process.
