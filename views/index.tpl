%rebase('base.tpl', title='Minolovec')

    <p>
        Minolovec je igra, kjer poskušamo počistiti minsko polje, tako da poiščemo in odpremo vsa prazna mesta, <br>
        mesta z minamo pa pustimo na miru. Igra se konča če počistimo minsko polje, ali če pomotoma odpremo mino. <br>
        Igro začnete tako, da si izberete eno od standardnih težavnosti <br> 
        (Začetnik: 9x9 mreža, 10 min; Poznavalec: 16x16 mreža, 40 min; Profesionalec: 16x30 mreža, 99 min), <br>
        ali pa vpišete poljubno velikost mreže in poljubno število min ter pritisnete na gumb Po meri.
    </p>

    <form action='/nova_igra/' method='post'>
        <input type='button' name='tezavnost' value='Začetnik'>
    </form>
    <form action='/nova_igra/' method='post'>
        <input type='button' name='tezavnost' value='Poznavalec'>
    </form>
    <form action='/nova_igra/' method='post'>
        <input type='button' name='tezavnost' value='Profesionalec'>
    </form>
    <form action='/nova_igra/' method='post'>
        <input type='text' name='polj_tez_vrstice' value='Število vrstic:'>
        <input type='text' name='polj_tez_stolpci' value='Število stolpcev:'>
        <input type='text' name='polj_tez_mine' value='Število min:'>
        <input type='submit' name='tezavnost' value='Po meri'>
    </form>

    