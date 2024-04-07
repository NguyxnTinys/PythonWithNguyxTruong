weight = float(input("Weight: "))
rep = str(input("(K)g or (L)bs: "))
rep = rep.lower()
if rep == 'l':
    res = weight * 0.45
    print("Weight in Kg: ", res)
else: 
    res = weight / 0.45
    print("Weight in Lbs: ", res)