def indo_date_to_iso(date_string):
    indo_date_splitted = date_string.split("-")
    indo_date_reversed = list(reversed(indo_date_splitted))
    iso_date = "-".join(indo_date_reversed)
    return iso_date
