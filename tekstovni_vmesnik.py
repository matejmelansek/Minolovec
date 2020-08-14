import model

POMOČ = 'Minolovec je igra, kjer poskušamo počistiti minsko polje, tako da poiščemo\n'
' in odpremo vsa prazna mesta, mesta z minami pa pustimo na miru.\n'
' Igra se konča če počistimo minsko polje, ali če pomotoma odpremo mino.\n'
' Igro začnete tako, da vpišete želeno število vrstic, pritisnete presledek,\n'
'nato vpišete želeno število stolpcec in po presledku še število min.\n'
'Velikost mreže ne sme presegati 24x30, min pa ne sme biti več kot 668.'

def zacetek():
    return input('===================================================\n'
                 'Dobrodošli v igri minolovca! Za pomoč pritisnite p.\n'
                 'Prosim vnesite želeno velikost mreže in število min:\n'
                 '==================================================='
    )

def izpis_igre(igra):
    mreza = '   '
    for stolpec in range(len(igra.postavitev_min[0])):
        mreza += str(stolpec + 1) + '  ' 
    mreza += '\n\n'
    for vrstica in range(len(igra.postavitev_min)):
        vrsta = ''
        for stoplec in range(len(igra.postavitev_min[0])):
            vrsta += str(izpis_celice(igra, vrstica, stolpec)) + '  '
        mreza += str(vrstica) + '  ' + vrsta + '\n'
    return mreza

def izpis_celice(igra, vrstica, stoplec):
    celica = igra.postavitev_min[vrstica][stolpec]
    if celica.mina == True and celica.odprta == True:
        return 'M'
    elif celica.mina == False and celica.odprta == True:
        if igra.mine_v_okolici(vrstica, stolpec) == 0:
            return  ' '
        else:
            return str(igra.mine_v_okolici(vrstica, stolpec))
    elif celica.zastavica == True:
        return 'F'
    else:
        return 'X'


def izpis_zmage(igra):
    return '\n Čestitke, dobili ste igro!'  

def izpis_poraza(igra):
    return '\n Žal ste to igro izgubili. \n ' 'Več sreče prihodnjič'

def izpis_napake(igra):
    return 'Nepravilen vnos. Za pomoč pritisni p.'

def pravilen_vnos(igra, vnos):
    vnos1 = vnos.split('')
    if len(vnos1) == 2:
        v = vnos1[0]
        s = vnos1[1]
        if v.is_integer() and s.is_integer():
            if 0 <= v < len(igra.postavitev_min) and 0 <= s < len(igra.postavitev_min[0]):
                return True
        else:
            return False
    elif len(vnos1) == 3:
        v = vnos1[0]
        s = vnos1[1]
        f = vnos1[2]
        if v.is_integer() and s.is_integer():
            if 0 <= v < len(igra.postavitev_min) and 0 <= s < len(igra.postavitev_min[0]):
                if f == 'f' or 'F':
                    return True
    return False

def pravilna_velikost(sez):
    sez1 = sez.split('')
    if len(sez1) != 3:
        return False
    elif not (sez1[0].is_integer and sez1[1].is_integer and sez1[2].is_integer):
        return False
    elif 1 < sez1[0] <= 24 and  1 < sez1[1] <= 30 and 0 < sez[2] <= 668:
        return True 
    return False

def zahtevaj_vnos(igra):
    vnos = input('Vnesi število vrstice in stolpca. Če želiš na celico postaviti zastavico, dodaj še črko f:')
    while pravilen_vnos(igra, vnos) == False:
        vnos = input('Nepravilen vnos. Najprej vnesi število vrstice in nato še število stolpca, loči ju s presledkom.\n'
        'Če želiš na celico postaviti zastavico dodaj še črko f:')
    vnos1 = vnos.split('')
    vrstica = int(vnos1[0])
    stolpec = int(vnos1[1])
    zastavica = False
    celica = igra.postavitev_min[vrstica][stolpec]
    if len(vnos1) == 3:
        if celica.zastavica == True:
            zastavica = False
        else:
            zastavica = True
    return (vrstica, stolpec, zastavica)

def pozeni_vmesnik():
    velikost_mreze = zacetek()
    igra = model.nova_igra(velikost_mreze)
    while True:
        if velikost_mreze.pravilna_velikost() == False:
            print(izpis_napake(igra))
            pozeni_vmesnik()
        if velikost_mreze == 'p':
            print(POMOČ)
            pozeni_vmesnik()
        if model.nova_igra(velikost_mreze) == 'F':
            print(izpis_napake(igra))
            pozeni_vmesnik()
        else:
            print(izpis_igre(igra))
            poskus = zahtevaj_vnos(igra)
            rezultat_ugiba = igra.ugibaj(poskus)
            if igra.ugibaj(poskus) =='F':
                print(izpis_napake(igra))
            if rezultat_ugiba == model.ZMAGA:
                print(izpis_igre(igra))
                print(izpis_zmage(igra))
                ponovni_zagon = input('Za ponovni zagon vpišite 1.\n').strip()
                if ponovni_zagon == '1':
                    igra = model.nova_igra()
                else:
                    break
            if rezultat_ugiba == model.PORAZ:
                print(izpis_igre(igra))
                print(izpis_poraza(igra))
                ponovni_zagon = input('Za ponovni zagon vpišite 1.\n').strip()
                if ponovni_zagon == '1':
                    igra = model.nova_igra()
                else:
                    break

pozeni_vmesnik()  