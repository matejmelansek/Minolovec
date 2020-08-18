from model import *
import sys

POMOČ = ('\n'
'Minolovec je igra, kjer poskušamo počistiti minsko polje, tako da poiščemo\n'
'in odpremo vsa prazna mesta, mesta z minami pa pustimo na miru.\n'
'Igra se konča če počistimo minsko polje, ali če pomotoma odpremo mino.\n'
'Igro začnete tako, da vpišete želeno število vrstic, pritisnete presledek,\n'
'nato vpišete želeno število stolpcec in po presledku še število min.\n'
'Velikost mreže ne sme presegati 24x30, min pa ne sme biti več kot 668.')

def zacetek():
    return input('\n'
                 '===================================================\n'
                 'Dobrodošli v igri minolovca! Za pomoč pritisnite p.\n'
                 'Prosim vnesite želeno velikost mreže in število min:\n'
                 '===================================================\n'
    )

def izpis_igre(igra):
    mreza = '      '
    for stolpec in range(len(igra.postavitev_min[0])):
        if stolpec <= 7:
            mreza += str(stolpec + 1) + '  '
        else:
            mreza += str(stolpec + 1) + ' '
    mreza += '\n\n'
    for vrstica in range(len(igra.postavitev_min)):
        vrsta = ''
        for stolpec in range(len(igra.postavitev_min[0])):
            vrsta += str(izpis_celice(igra, vrstica, stolpec)) + '  '
        if vrstica <= 8:
            mreza += str(vrstica + 1) + '     ' + vrsta + '\n'
        else:
            mreza += str(vrstica + 1) + '    ' + vrsta + '\n'
    return mreza

def izpis_celice(igra, vrstica, stolpec):
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


def izpis_zmage():
    return '\n Čestitke, dobili ste igro!'  

def izpis_poraza():
    return '\n Žal ste to igro izgubili. \n ' 'Več sreče prihodnjič'

def izpis_napake():
    return '\n Nepravilen vnos. Za pomoč pritisni p.'

def pravilen_vnos(igra, vnos):
    vnos1 = vnos.split(' ')
    if len(vnos1) == 2:
        v = vnos1[0]
        s = vnos1[1]
        if v.isdigit() and s.isdigit():
            if 0 <= int(v) < len(igra.postavitev_min) + 1 and 0 <= int(s) < len(igra.postavitev_min[0]) + 1:
                return True
        else:
            return False
    elif len(vnos1) == 3:
        v = vnos1[0]
        s = vnos1[1]
        f = vnos1[2]
        if v.isdigit() and s.isdigit():
            if 0 <= int(v) < len(igra.postavitev_min) and 0 <= int(s) < len(igra.postavitev_min[0]):
                if f == 'f' or 'F':
                    return True
    return False

def zahtevaj_vnos(igra):
    vnos = input('Vnesi število vrstice in stolpca. Če želiš na celico postaviti zastavico, dodaj še črko f:')
    while pravilen_vnos(igra, vnos) == False:
        vnos = input('Nepravilen vnos. Najprej vnesi število vrstice in nato še število stolpca, loči ju s presledkom.\n'
        'Če želiš na celico postaviti zastavico dodaj še črko f:')
    vnos1 = vnos.split(' ')
    vrstica = vnos1[0]
    stolpec = vnos1[1]
    #celica = igra.postavitev_min[int(vrstica)][int(stolpec)]
    if len(vnos1) == 3:
        return [vrstica, stolpec, True]
    return [vrstica, stolpec, False]

def pozeni_vmesnik():
    velikost_mreze = zacetek()
    if velikost_mreze == 'p':
        print(POMOČ)
        pozeni_vmesnik()
    else:
        velikost_mreze1 = velikost_mreze.split(' ')
        if len(velikost_mreze1) != 3:
            print(izpis_napake())
            pozeni_vmesnik()
        else:
            v = velikost_mreze1[0]
            s = velikost_mreze1[1]
            m = velikost_mreze1[2]
            igra = nova_igra(v, s, m)
            while True:
                if  nova_igra(v, s, m) == 'N':
                    print(izpis_napake())
                    pozeni_vmesnik()
                else:
                    print(izpis_igre(igra))
                    poskus = zahtevaj_vnos(igra)
                    rezultat_ugiba = igra.ugibaj(poskus[0], poskus[1], poskus[2])
                    if rezultat_ugiba =='N':
                        print(izpis_napake())
                    if rezultat_ugiba == ZMAGA:
                        print(izpis_igre(igra))
                        print(izpis_zmage())
                        ponovni_zagon = input('Za ponovni zagon vpišite 1.\n')
                        if ponovni_zagon == '1':
                            pozeni_vmesnik()
                        else:
                            sys.exit()
                    if rezultat_ugiba == PORAZ:
                        print(izpis_igre(igra))
                        print(izpis_poraza())
                        ponovni_zagon = input('Za ponovni zagon vpišite 1. \n')
                        if ponovni_zagon == '1':
                            pozeni_vmesnik()
                        else:
                            sys.exit()

pozeni_vmesnik()