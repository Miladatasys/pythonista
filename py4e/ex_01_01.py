score = input("Enter score: ")

fs = float(score)
if fs >= 0.0 and fs <= 1.0:
    if fs >= 0.9:
            print("A")
    elif fs >= 0.8:
            print("B")
    elif fs >= 0.7:
            print("C")
    elif fs >= 0.6:
            print("D")
    elif fs < 0.6:
       print("F")
    else:
        print("Error: the score is out of range")
    quit()