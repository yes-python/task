a = ( input ( "entar your phone number: ") )

if len(a)==11 :
    print( a.replace( a[4:7] , 3 * "*" ))

else :
    print("error!")


