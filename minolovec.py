import bottle
import model

SKRIVNOST = 'nekaj_skrivnega'
minolovec = model.Minolovec()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    for tezavnost in bottle.request.forms.getall['tezavnost']:
        if tezavnost == 'Začetnik':
            st_vrstic = 9
            st_stolpcev = 9
            st_min = 10
        if tezavnost == 'Poznavalec':
            st_vrstic = 16
            st_stolpcev = 16
            st_min = 40
        if tezavnost == 'Profesionalec':    
            st_vrstic = 16
            st_stolpcev = 30
            st_min = 99
        if tezavnost == 'Po meri':
            st_vrstic = bottle.request.forms.get('polj_tez_vrstice')
            st_stolpcev = bottle.request.forms.get('polj_tez_stolpci')
            st_min = bottle.request.forms.get('polj_tez_mine')
    id_igre = minolovec.nova_igra(st_vrstic, st_stolpcev, st_min)
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('id_igre', secret=SKRIVNOST))
    [igra, st_vrstic, st_stolpcev, st_min, stanje] = minolovec.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje, id_igre=id_igre, st_vrstic=st_vrstic, st_stolpcev=st_stolpcev, st_min=st_min)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('id_igre', secret=SKRIVNOST))
    celica = bottle.request.getunicode('celica')
    vrstica = int(celica[0])
    stolpec = int(celica[1])
    zastavica = celica[2]
    minolovec.ugibaj(id_igre, vrstica, stolpec, zastavica)
    bottle.redirect('/igra/')


bottle.run(reloader=True, debug=True)