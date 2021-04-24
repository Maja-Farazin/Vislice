import Model

PONOVNI_ZAGON = "p"
IZHOD = "i"

def izpis_igre(igra):
    tekst = f"""###################################\n
    {igra.pravilni_del_gesla()}\n
    Število poskusov: {stopnje[Model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()]}\n
    Nepravilne črke: {igra.nepravilni_ugibi()}\n
###################################\n
    """
    return tekst

def izpis_zmage(igra):
    tekst = f"""###################################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
###################################\n
    """
    return tekst

def izpis_poraza(igra):
    tekst = f"""###################################\n
    {stopnje[0]}
    Porabili ste vse poskuse.\n
    Pravilno geslo je bilo: {igra.geslo}\n
###################################\n
    """
    return tekst

def zahtevaj_vnos():
    return input("Vnesite črko:")

def zahtevaj_moznost():
    return input("Vnesite možnost:")

def ponudi_moznost():
    tekst = F""" Vpišite črko za izbor naslednjih možnosti:\n
    {PONOVNI_ZAGON} : ponovni zagon igre\n
    {IZHOD} : izhod\n
    """
    return tekst

def izberi_moznost():
    print(ponudi_moznost())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = Model.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD

def pozeni_vmesnik():
    igra = Model.nova_igra()
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == Model.ZMAGA:
            print(izpis_zmage(igra))
            igra = izberi_moznost()
            if igra == IZHOD:
                break
        elif odziv == Model.PORAZ:
            print(izpis_poraza(igra))
            igra = izberi_moznost()
            if igra == IZHOD:
                break
        else:
            print(izpis_igre(igra))

stopnje = [
"""
       _____
       |   |
       |   o
       |  /|\\
       |  / \\
      _|______
""",
"""
       _____
       |   |
       |   o
       |  /|\\
       |  / 
      _|______
""",
"""
       _____
       |   |
       |   o
       |  /|\\
       |  
      _|______
""",
"""
       _____
       |   |
       |   o
       |  /|
       |  
      _|______
""",
"""
       _____
       |   |
       |   o
       |   |
       |  
      _|______
""",
"""
       _____
       |   |
       |   o
       |  
       |  
      _|______
""",
"""
       _____
       |   |
       |   o
       |  
       |  
      _|______
""",
"""
       _____
       |   |
       |   
       |  
       |  
      _|______
""",
"""
       _____
       |   
       |   
       |  
       |  
      _|______
""",
"""
    
       |   
       |   
       |  
       |  
      _|______
""",
"""
       
          
          
        
         
      _______
""",
"""
       
          
         
         
         
      
"""

]

pozeni_vmesnik()