#!/usr/bin/env python
from datetime import datetime
import os
import shutil
import subprocess
import click

# Using UTC so the date is right just before the day unlocks
TODAY = datetime.utcnow()
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(ROOT_PATH, "template.py")


def validate_year(ctx, param, year):
    if year < 2015 or year > TODAY.year:
        raise click.BadParameter(f"year should be in range [2015, {TODAY.year}]")
    return year


def validate_day(ctx, param, day):
    if day < 1 or day > 25:
        raise click.BadParameter("day should be in range [1, 25]")
    return day


@click.command()
@click.option("--year", "-y", prompt="Year", default=TODAY.year, callback=validate_year)
@click.option("--day", "-d", prompt="Day", default=TODAY.day, callback=validate_day)
@click.option("--open", is_flag=True, default=False)
def main(year, day, open):
    year_path = os.path.join(ROOT_PATH, "solutions", f"y{year}")
    day_path = os.path.join(year_path, f"d{day:02d}.py")
    if not os.path.exists(year_path):
        os.mkdir(year_path)
        click.echo(f"Created folder for year {year}")

    if not os.path.exists(day_path):
        shutil.copyfile(TEMPLATE_PATH, day_path)
        click.echo(f"Created script for y{year}/d{day:02d}.py")
    else:
        click.echo(f"y{year}/d{day:02d}.py already exists")

    if open:
        subprocess.run(f"code {day_path}", shell=True, check=True)


if __name__ == "__main__":
    main()
