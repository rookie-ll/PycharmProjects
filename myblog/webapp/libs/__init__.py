from .myfilter import filter_day, filter_month, filter_year
from .mystrings import read_str

def app_filter(app):
    app.add_template_filter(filter_day, "day")
    app.add_template_filter(filter_month, "month")
    app.add_template_filter(filter_year, "year")
