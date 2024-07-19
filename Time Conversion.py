def time_conversion(s):
    return s[:-2] + ("00" if s[-2:] == "AM" and s[:2] == "12" else "12" if s[-2:] == "PM" and s[:2] == "12" else "12" if s[-2:] == "PM" else s[:2] if s[-2:] == "PM" else "00" if s[-2:] == "AM" else s[:2]) + s[2:-2]

if _name_ == "_main_":
    s = "07:45:54PM"
    print(time_conversion(s))
