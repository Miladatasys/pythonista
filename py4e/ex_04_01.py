def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        regular = 40
        overtime = (h - 40) * r * 1.5
        return regular + overtime
hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)