import random

ZMAGA = "W"
PORAZ = "L"
ZACETEK = "S"
NAPAKA = "N"


class Celica:

    def __init__(self, vrstica, stolpec, mina, odprta=False, zastavica=False):
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.mina = mina
        self.odprta = odprta
        self.zastavica = zastavica
        return

    def odpri(self):
        self.odprta = True
        return
    
    def postavi_zastavico(self):
        self.zastavica = not self.zastavica
        return

    def postavi_mino(self):
        self.mina = True
        return



class Mreza:

    def __init__(self, postavitev_min):
        self.postavitev_min = postavitev_min
        return

    def mine_v_okolici(self, vrstica, stolpec):
        mine_v_okolici = 0
        for v, s in self.sosednje_celice(vrstica, stolpec):
            celica = self.postavitev_min[v][s]
            if celica.mina == True:
                mine_v_okolici += 1
        return mine_v_okolici

    def sosednje_celice(self, v, s):
        sez1 = [[v + 1, s - 1], [v + 1, s], [v + 1, s + 1], [v, s - 1], [v, s + 1], [v - 1, s - 1], [v - 1, s], [v - 1, s + 1]]
        sez2 = []
        for celica in sez1:
            i = celica[0]
            j = celica[1]
            if self.je_na_mrezi(i, j):
                sez2.append(celica)
        return sez2
    
    def je_na_mrezi(self, vrstica, stolpec):
        vrstice = len(self.postavitev_min)
        stolpci = len(self.postavitev_min[0])
        if vrstica >= 0  and vrstica < vrstice:
            if stolpec >= 0 and stolpec < stolpci:
                return True
        return False

    def postavi_zastavico(self, vrsta, stolpec):
        celica = self.postavitev_min[vrsta][stolpec]
        if celica.odprta == False:
            celica.postavi_zastavico()

    def odpri(self, vrstica, stolpec):
        celica = self.postavitev_min[vrstica][stolpec]
        if celica.zastavica == True:
            return
        if celica.odprta == False:
            celica.odpri()
            if self.mine_v_okolici(vrstica, stolpec) == 0:
                for i, j in self.sosednje_celice(vrstica, stolpec):
                    self.odpri(i, j)

    def poraz(self):
        for vrstica in self.postavitev_min:
            for celica in vrstica:
                if celica.odprta == True and celica.mina == True:
                    return True
        return False

    def zmaga(self):
        for vrstica in self.postavitev_min:
            for celica in vrstica:
                if celica.odprta == False and celica.mina == False:
                    return False
        return True


def ustvari_mrezo(st_vrstic, st_stolpcev, st_min):
    mreza = []
    for i in range(st_vrstic):
        vrstica = []
        for j in range(st_stolpcev):
            vrstica.append(Celica(i, j, False))
        mreza.append(vrstica)

    celice_brez_mine = []
    for i in range(st_vrstic):
        for j in range(st_stolpcev):
            celice_brez_mine.append([i, j])

    for m in range(st_min):
        dodaj_mino = random.choice(celice_brez_mine)
        celice_brez_mine.remove(dodaj_mino)
        i = dodaj_mino[0]
        j = dodaj_mino[1]
        mreza[i][j].postavi_mino()
    return mreza

def nova_igra(st_vrstic, st_stolpcev, st_min):
    if not st_vrstic.isdigit():
        return NAPAKA
    if not st_stolpcev.isdigit():
        return NAPAKA
    if not st_min.isdigit():
        return NAPAKA

    velikost_mreze = int(st_vrstic) * int(st_stolpcev)
    mine = int(st_min)
    if mine > velikost_mreze:
        return NAPAKA
    else:    
        nova_mreza = ustvari_mrezo(st_vrstic, st_stolpcev, st_min)
        return Mreza(nova_mreza)



class Minolovec:
    
    def __init__(self):
        self.igre = {}
    
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i

    def nova_igra(self, st_vrstic, st_stolpcev, st_min):
        nov_id = self.prost_id_igre()
        mreza = ustvari_mrezo(st_vrstic, st_stolpcev, st_min)
        igra = Mreza(mreza)
        self.igre[nov_id] = [igra, st_vrstic, st_stolpcev, st_min, ZACETEK]
        return nov_id