
text1 = "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak"
text2 = ", van "
text3 = " euro voor " 
text4 = " euro."
virtinkomsten = [220, 430, 125, 160, 205, 90, 345]
invoer_lijst_2 = [10,5,3,2,1,2,9]
virtbtw = 0.09

def algemene_functies_2(a,b):
    mijn_lijst2 = []
    mijn_lijst2.append(a+b)
    mijn_lijst2.append(a-b)
    mijn_lijst2.append(a*b)
    mijn_lijst2.append(a/b)
    return mijn_lijst2

def aanbieding_1(smaak, prijs, korting):
    if (smaak == "aardbei"):
        aanbieding_product = smaak
        van_prijs = prijs
        voor_prijs = prijs - (prijs*korting)
        totaal = f"{text1} {aanbieding_product} {text2} {van_prijs} {text3} {voor_prijs} {text4}"
        return totaal
    else:
        print("Geen waarde ingevoerd")

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for inkperdag in inkomsten:
        totaal = totaal + inkperdag
        bedrag = totaal * btw
    week_totaal = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return week_totaal  

def laag_en_hoog(mijn_lijst):
    
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    mijnlijst=[hoog, laag]
    return mijnlijst

def gemiddelde(mijn_lijst):
    resultaat=""
    bedrag=0
    bedrag= sum(mijn_lijst)/len(mijn_lijst)
    bedrag="{:.2f}".format(round(bedrag,2))
    resultaat = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return resultaat

def meervoudig(invoer_lijst):
    uitvoer_lijst=[]
    uitvoer_lijst = laag_en_hoog(invoer_lijst)
    return uitvoer_lijst

def combinatie(invoer_lijst_2):
    mijn_combinatie=[]
    shortlist = 0
    korte_lijst=[]
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    a,b = korte_lijst
    mijn_combinatie = algemene_functies_2(a,b)
    return mijn_combinatie

print (aanbieding_1("aardbei",4,0.1))
print (inkomsten_totaal(virtinkomsten,virtbtw))
print (laag_en_hoog(virtinkomsten))
print (gemiddelde(virtinkomsten))
print (meervoudig(invoer_lijst_2))
print (combinatie(invoer_lijst_2))
