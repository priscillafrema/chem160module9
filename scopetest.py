def test():
    #global b
    #b=20
    #global a
    #a=10
    print("Inside test() a=%d"%(a))
    print("Inside test() b=%d"%(b))
a=1
print("Outside test() a=%d"%(a))
test()
print("Outside test() a=%d"%(a))
print("Outside test() b=%d"%(b))

#variable b is not visible outside of function but I believe variable a is visible inside the function at a=1.
#removing the # in front of global b statement does not make b visible outside as b is not actually defined.
#removing the # from a=10 does not change the outside function, it is still a=1 however, it does change the inside function from a=1 to a=10.
#removing the # from global a doesnt change the output.