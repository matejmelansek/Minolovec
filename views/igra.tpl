%rebase('base.tpl', title='Minolovec')
%import model

<h2>Če želiš postavljati zastavice pritisni na gumb: Postavljaj zastavice</h2>

<form action='/igra/' method='post'>
    <table>
        % for v in range(st_vrstic):
            <tr>
                % for s in range(st_stolpcev):
                    <td>
                        % mreza = igra.postavitev_min
                        % celica = mreza[v][s]
                        % if celica.odprta == True and celica.mina == True:
                            <img src='../img/minolovec_mina.png' alt='M'>
                        % elif celica.odprta == True and celica.mina == False:
                            <img src='../img/minolovec_{{igra.mine_v_okolici(v,s)}}.png' alt='{{igra.mine_v_okolici(v,s)}}'>
                        % elif celica.odprta == False and celica.zastavica == True:
                            <img src='../img/minolovec_zastavica.png' alt='F'>
                        % elif celica.odprta == False and celica.zastavica == False:
                            <input type='image' name='celica1' value='{{v}} {{s}}' src='../img/minolovec_zaprta.png' alt='X'/>
                        %end
                    </td>
                %end
            </tr>
        %end
    </table>
</form>

<form action="/igra_zastavice/" method="post">
    <input type='submit' name='postavljaj_zastavice' value='Postavljaj zastavice'>
</form>
<br>
% if stanje == model.ZMAGA:
<h1>ČESTITAM, POČISTILI STE MINSKO POLJE!</h1>
<form action="/nova_igra/" method="post">
    <button>Nova igra</button>
</form>

% elif stanje == model.PORAZ:
<h1>ŽAL STE ZADELI MINO.</h1>
<form action="/nova_igra/" method="post">
    <button>Nova igra</button>
</form>