#数列
def fu(y,t):
    f=[1,1]
    a=f[1]
    b=f[1]
    for i in range(y-2):
        a,b=b,b+t*a
        print (b)
     
      
fu(30,2)
