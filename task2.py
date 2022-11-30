a = ( input("entar your phone number: "))
b = int ( input("How many numbers of your phone number should be hidden except 09--?: "))
if len(a) == 11 and 4 <= b <= 7 :
    print( a.replace(a[4:4+b] , b*"*"))
else:
    print("error!")  