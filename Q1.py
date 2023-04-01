x1 = 2
x2 = 3.2
x3 = 1.3



print( type(x1), type(x2), type(x3))

def my_func(x1,x2,x3):
    mone = 0.0   
    mechane = 0.0
    targil = 0.0
    
    if (type(x1) != float or  type(x2) != float or type(x3) != float):   
         print("Error: parameters should be float")
         return ("None")
      
      
    mone = (x1+ x2 +x3) * (x2+x3) * x3
    mechane = x1 +x2 +x3
    targil = mone / mechane
      
    if ( mechane == 0 ):
        print("Not a number – denominator equals zero")
      
    return (targil)
    
              
                
n = my_func(x1,x2,x3)

print(n)  
   
    
            
        




