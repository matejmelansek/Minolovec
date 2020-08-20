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
                            <img src='../img/minolovec_mina.jpg' width='30px' height='30px' alt='M'>
                        % elif celica.odprta == True and celica.mina == False:
                            <img src='../img/minolovec_{{igra.mine_v_okolici(v,s)}}.png' width='30px' height='30px' alt='{{igra.mine_v_okolici(v,s)}}'>
                        % elif celica.odprta == False and celica.zastavica == True:
                            <img src='../img/minolovec_zastavica.png' width='30px' height='30px' alt='F'>
                        % elif celica.odprta == False and celica.zastavica == False:
                            <button id='close-image' name='celica1' value='{{v}} {{s}}'><img src='../img/minolovec_zaprta.png' width='30px' height='30px'></button>
                        %end
                    </td>
                %end
            </tr>
        %end
    </table>
</form>
<br>
%if not(stanje == model.ZMAGA or stanje == model.PORAZ):
<form action='/igra_zastavice/' method='get'>
    <button type='submit'>Postavljaj zastavice</button>
</form>
%end

% if stanje == model.ZMAGA:
<h2>ČESTITAM, POČISTILI STE MINSKO POLJE!</h2>
<p>Če želite igrati ponovno na enako velikem minskem polju pritisnite gumb: Nova igra - enaka mreža. <br> 
Če pa želite novo minsko polje pritisnite gumb: Nova igra - nova mreža.</p>
<form action='/nova_igra/' method='post'>
    <button type='submit' name='tezavnost' value='{{st_vrstic}} {{st_stolpcev}} {{st_min}}'>Nova igra - enaka mreža</button>
</form>
<form action='/nova_igra1/' method='get'>
    <button type='submit'>Nova igra - nova mreza</button>
</form>

% elif stanje == model.PORAZ:
<h2>ŽAL STE ZADELI MINO.</h2>
<p>Če želite igrati ponovno na enako velikem minske polju pritisnite gumb: Nova igra - enaka mreža. <br> 
Če pa želite novo minsko polje pritisnite gumb: Nova igra - nova mreža.</p>
<form action='/nova_igra/' method='post'>
    <button type='submit' name='tezavnost' value='{{st_vrstic}} {{st_stolpcev}} {{st_min}}'>Nova igra - enaka mreža</button>
</form>
<form action='/nova_igra1/' method='get'>
    <button type='submit'>Nova igra - nova mreža</button>
</form>
