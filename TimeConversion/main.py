examples = ['12:01:00PM', '04:00:00AM', '06:00:00PM']

def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00'+s[2:-2]
        else:
            return s[:-2]
    else:
        hour = int(s[:2])
        if hour < 12:
            return str(hour+12) + s[2:-2]
        else:
            return s[:-2]
    return

for x in examples:
    print(timeConversion(x))