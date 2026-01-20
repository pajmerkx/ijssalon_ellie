def algemene_functies_1(waarde):
    uitkomst = 0
    uitkomst = waarde * waarde
    return uitkomst        

def algemene_functies_2(a,b):
    mijn_lijst2 = []
    mijn_lijst2.append(a+b)
    mijn_lijst2.append(a-b)
    mijn_lijst2.append(a*b)
    mijn_lijst2.append(a/b)
    return mijn_lijst2

mijn_lijst_1 = [2,4,10,12]

for arg in mijn_lijst_1:
    print (algemene_functies_1(arg))

print (algemene_functies_2(12,3))
print (algemene_functies_2(12,2))
print (algemene_functies_2(10,5))
print (algemene_functies_2(100,20))

        
