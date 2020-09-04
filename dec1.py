import time
def vaxtiHesabla(func):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        netice = func(*args, **kwargs)
        bitis = time.time()
        print(f"emeliyyat {bitis-baslangic} saniye cekdi")
        return netice
    return wrapper

@vaxtiHesabla
def kvadratiHesabla(list):
    netice = []
    for i in list:
        netice.append(i ** 2)
    return netice

@vaxtiHesabla
def kubuHesabla(list):
    netice = []
    for i in list:
        netice.append(i ** 2)
    return netice

@vaxtiHesabla
def toplamaniHesabla(*args):
    time.sleep(1)
    return sum(args)

print(kvadratiHesabla(range(100)))
print(kubuHesabla(range(100)))
print(toplamaniHesabla(5,10))