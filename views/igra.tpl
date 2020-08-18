%rebase('base.tpl', title='Minolovec')

<table>
    % for v in range(st_vrstic):
        <tr>
            % for s in range(st_stolpcev):
                <td>
                    % celica = igra.[v][s]
                    % if celica.odprta == True:
                        % if celica.mina == True:
                            <img src='.../img/minolovec_mina.png' alt='M'>
                        % else:
                            <img src='.../img/minolovec_{{celica.mine_v_okolici(v,s)}}.png' alt='{{celica.mine_v_okolici(v,s)}}'>
                    % else:
                        % if celica.zastavica == True:
                            <img src='.../img/minolovec_zastavica.png' alt='F'>
                        % else:
                            <button name='celica' value='{{v}} {{s}}'><img src='.../img/minolovec_zaprta.png' alt='X'></button>
                </td>
        </tr>
</table>

<form action="/igra_zastavice/" method="post">
    <button name='postavljaj_zastavice'>Postavljaj zastavice</button>
</form>

% if stanje == model.ZMAGA:
<h1>ČESTITAM, POČISTILI STE MINSKO POLJE!</h1>
<form action="/nova_igra/" method="post">
    <button>Nova igra</button>
</form>

% elif stanje == model.PORAZ:
<h1>žAL STE ZADELI MINO.</h1>
<form action="/nova_igra/" method="post">
    <button>Nova igra</button>
</form>