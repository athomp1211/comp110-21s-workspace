"""A vaccination calculator."""

__author__ = "730318766"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses_adm: int = int(input("Doses administered: "))
doses_per: int = int(input("Doses per day: "))
target_per: int = int(input("Target percent vaccinated: "))

target_ppl: int = int(round((pop) * (target_per / 100)))
already_vacc: int = int(round(doses_adm / 2))
ppl_needed: int = int(target_ppl - already_vacc)
doses_needed: int = int(ppl_needed * 2)
days_til_per: int = int(round(doses_needed / doses_per))

today: datetime = datetime.today()
days_til: timedelta = timedelta(days_til_per)
target_date: datetime = today + days_til

print("We will reach " + str(target_per) + "% vaccination in " + str(days_til_per) + " days, which falls on " + target_date.strftime("%B %d, %Y") + ".")
