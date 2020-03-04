import re


def filter_year(s):
    s=str(s)
    rel = re.match(r'(.*)-(.*)-(.* )', s).group(1)
    return rel


def filter_month(s):
    s = str(s)
    rel = re.match(r'(.*)-(.*)-(.* )', s).group(2)
    return rel


def filter_day(s):
    s = str(s)
    rel = re.match(r'(.*)-(.*)-(.* )', s).group(3)
    return rel

