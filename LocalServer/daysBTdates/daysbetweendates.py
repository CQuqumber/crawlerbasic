
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 == year2:
        if month2 == month1:
            year = 0
            month = 0
            day = day2-day1

        else:
            if day2 == day1:
                year = 0
                month = month2 - month1
                day = 0
            elif day2 > day1:
                year = 0
                month = month2 - month1
                day = day2 - day1
            else:
                month = month2- month1 -1
                day = day2 -day1 + 30
    else:
        if month2 == month1:
            year = year2 - year1
            month = month2 - month1
            day = day2-day1
        elif month2 > month1:
            if day2 == day1:
                month = month2 - month1
                year = year2 - year1
                day = 0
            elif day2 > day1:
                day = day2 - day1
                month = month2 - month1
                year = year2 - year1
            else:
                year = year2 - year1
                month = month2- month1 -1
                day = day2 -day1 + 30
        elif month2 < month1: #y2>y1 m1>m2
            if day2 == day1:
                day = 0
                year = year2 - year1 -1
                month = month2 - month1 + 12
            if day2 > day1:
                day = day2 - day1
                year = year2 - year1 -1
                month = month2 - month1 + 12
            else:
                year = year2 - year1 -1
                month = month2- month1 -1 + 12
                day = day2 - day1 + 30

    return year*360 + month*30 + day

print daysBetweenDates(2012,9,30,2012,10,30)
print daysBetweenDates(2012,1,1,2013,1,1)
print daysBetweenDates(2012,9,1,2012,9,4)

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
