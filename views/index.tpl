%rebase('base.tpl', title='Minolovec')

    <p>
        Minolovec je igra, kjer poskušamo počistiti minsko polje, tako da poiščemo in odpremo vsa prazna mesta, <br>
        mesta z minamo pa pustimo na miru. Igra se konča če počistimo minsko polje, ali če pomotoma odpremo mino. <br>
        Igro začnete tako, da si izberete eno od standardnih težavnosti <br> 
        (Začetnik: 9x9 mreža, 10 min; Poznavalec: 16x16 mreža, 40 min; Profesionalec: 16x30 mreža, 99 min), <br>
    </p>

    <form action='/nova_igra/' method='post'>
        <input type='submit' name='tezavnost' value='Začetnik'>
    </form>
    <form action='/nova_igra/' method='post'>
        <input type='submit' name='tezavnost' value='Poznavalec'>
    </form>
    <form action='/nova_igra/' method='post'>
        <input type='submit' name='tezavnost' value='Profesionalec'>
    </form>
    <form action='/nova_igra/' method='post'>
        <input type='submit' name='tezavnost' value='Po meri'> <br>
        Število vrstic: <input type='text' name='polj_tez_vrstice'>
        Število stolpcev: <input type='text' name='polj_tez_stolpci'>
        Število min: <input type='text' name='polj_tez_mine'>
    </form>

    <br>

    <p>
        Če vam velikost minskega polja in število min ne ustrezata, v prazna polja napišite želeno <br>
        število vrstic, stolpcev in min, nato pritisnite gumb: Po meri. V polja vpisujte le naravna števila <br>
        (in ne drugih simbolov kot so presledki, črke,...). Najmanjše možno minsko polje je velikosti 2x2, največje <br>
        pa 24x30. Število min mora biti vsaj za 1 manjše od velikosti minskega polja (največ 668 min).
    </p>
    