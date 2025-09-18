def sprinkles(func):
    def wrapper():
        print("sprinkles")
        func()
    return wrapper

def cubes(func):
    def wrapper():
        print("cubes")
        func()
    return wrapper


@sprinkles
@cubes
def ice_cream():
    print("icecream")


ice_cream()