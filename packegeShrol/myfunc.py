def printHello():
    print("Hello, my friend!")


def suma(a:int,b:int)->None:
    """
    @a parametr
    @b parametr
    output suma @a+@b 
    """
    print(f"{a}+{b}={a+b}")

def returnSuma(a:int,b:int)->int:
    """
    @a parametr
    @b parametr
    output suma @a+@b 
    """
    return a+b

if __name__=="__main__":
    printHello()