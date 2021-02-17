"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730318766"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    x: int = days_to_target(population, doses, doses_per_day, target)
    y: str = future_date(target_date)
    print("We will reach " + str(target) + "% vaccination in " + str(x) + " days, which falls on " + str(y) + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Returns an int number of days until reaching the target percent vaccinated."""
    target_ppl: int = int(round((population) * (target / 100)))
    already_vacc: int = int(round(doses / 2))
    ppl_needed: int = int(target_ppl - already_vacc)
    doses_needed: int = int(ppl_needed * 2)
    days_til_per: int = int(round(doses_needed / doses_per_day))
    return days_til_per


def future_date(target_date: int) -> str
    """Returns a str representation of the date that's int number of days from now."""
    today: datetime = datetime.today()
    days_til: timedelta = timedelta(days_til_per)
    target_date: datetime = today + days_til
    return target_date.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
