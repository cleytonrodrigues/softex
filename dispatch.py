from multipledispatch import dispatch

#@dispatch(float,float,float)
#@dispatch(str,str,str)
def summation(float_1,float_2,float_3):
    total = float_1+float_2+float_3
    print(total);
  
def difference(int_1,int_2,int_3):
    diff  = int_1 - int_2 - int_3
    print(diff);

summation(6.9,3.14,7.12) 
summation('oi,', ' tudo', ' bem?')

difference(6.9,3.14,7.12) 
