def decoratorFunc(originalFunc):
    def wrapperFunc(*args, **kwargs):
            print("Wrapper Emeliyyatlari")
            print(f"Original function {originalFunc.__name__} ")
            def canNotRun():
                print("Bu funkisiyanin islemeyine icaze yoxdur", originalFunc.__name__)

            if not canRun:
                return canNotRun()
            return originalFunc(*args, **kwargs)
    return wrapperFunc

@decoratorFunc
def myFunc():
    print("bezi isler yerine yetirirem")

@decoratorFunc
def displayInfo(name, age):
    age= int(age)
    print(f"Menim adim {name} ve yasin {age}")

canRun = False
myFunc()
canRun = True
displayInfo("Jale", "19")