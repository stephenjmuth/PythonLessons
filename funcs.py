def print_func(func_var1):
    print(func_var1)

def func1(func_var1):
    print(f"\t\tCall func1 - print func_var1: {func_var1}")
    func_var2=func_var1*2
    print(f"\t\tCreate func_var2(*2) and print: {func_var2}")
    return func_var2
def func12(func_var11,func_var12):
    print(func_var11,func_var12)
    func_var22=func_var11*2
    func_var23=func_var12*2
    return func_var22,func_var23
