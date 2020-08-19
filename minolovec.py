import bottle
import model

SKRIVNOST = 'nekaj_skrivnega'
minolovec = model.Minolovec()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    tezavnost = bottle.request.forms.getunicode('tezavnost')
    if tezavnost == 'Začetnik':
        st_vrstic = 9
        st_stolpcev = 9
        st_min = 10
    elif tezavnost == 'Poznavalec':
        st_vrstic = 16
        st_stolpcev = 16
        st_min = 40
    elif tezavnost == 'Profesionalec':    
        st_vrstic = 16
        st_stolpcev = 30
        st_min = 99
    elif tezavnost == 'Po meri':
        st_vrstic = int(bottle.request.forms.getunicode('polj_tez_vrstice'))
        st_stolpcev = int(bottle.request.forms.getunicode('polj_tez_stolpci'))
        st_min = int(bottle.request.forms.getunicode('polj_tez_mine'))
    id_igre = minolovec.nova_igra(st_vrstic, st_stolpcev, st_min)
    bottle.response.set_cookie('id_igre', id_igre, secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    [igra, st_vrstic, st_stolpcev, st_min, stanje] = minolovec.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje, id_igre=id_igre, st_vrstic=st_vrstic, st_stolpcev=st_stolpcev, st_min=st_min)

@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    celica1 = bottle.request.forms.getunicode('celica1')
    celica2 = celica1.split(' ')
    vrstica = int(celica2[0]) + 1
    stolpec = int(celica2[1]) + 1
    minolovec = minolovec.ugibaj(id_igre, vrstica, stolpec, False)
    bottle.redirect('/igra/')

@bottle.post('/igra_zastavice/')
def postavljaj_zastavice():
    bottle.request.forms.getunicode('postavljaj_zastavice')
    bottle.redirect('/igra_zastavice/')

@bottle.get('/igra_zastavice/')
def igra_zastavice():
    id_igre = int(bottle.request.get_cookie('id_igre', secret=SKRIVNOST))
    [igra, st_vrstic, st_stolpcev, st_min, stanje] = minolovec.igre[id_igre]
    return bottle.template('igra_zastavice.tpl', igra=igra, stanje=stanje, id_igre=id_igre, st_vrstic=st_vrstic, st_stolpcev=st_stolpcev, st_min=st_min)

@bottle.post('/igra_zastavice/')
def postavi_zastavico():
    id_igre = int(bottle.request.get_cookie('id_igre', secret=SKRIVNOST))
    celica = bottle.request.getunicode('celica').split(' ')
    vrstica = int(celica[0]) + 1
    stolpec = int(celica[1]) + 1
    minolovec = minolovec.ugibaj(id_igre, vrstica, stolpec, True)
    bottle.redirect('/igra_zastavice/')

@bottle.post('/igra/')
def nazaj_na_odpiranje():
    bottle.request.forms.getunicode('odkrivaj_celice')
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(reloader=True, debug=True)