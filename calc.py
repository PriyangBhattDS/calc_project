def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mod(x,y):
    return x%y

def div(x,y):
    return x/y if y!=0 else "can't divide by zero"


def mul(x,y):
    return x*y

if __name__ == "__main__":
    print(add(10,20))
    print(sub(10,20))
    print(mod(10,20))
    print(mul(10,20))
    print(div(10,2))


