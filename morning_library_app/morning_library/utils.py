import datetime


def length_to_formatted_length(length):
    if length is not None:
        length_formatted = str(datetime.timedelta(seconds=float(length)))
        if length_formatted[0] == "0" and length_formatted[1] == ":":
            length_formatted = length_formatted[2:]
        return length_formatted.split(".")[0]
    else:
        return None
