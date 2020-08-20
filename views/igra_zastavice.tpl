%rebase('base.tpl', title='Minolovec')

<h2>Če želiš odkrivati celice pritisni na gumb: Odkrivaj celice</h2>

<form action='/igra_zastavice/' method='post'>
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
                            <button id='close-image' name='celica1' value='{{v}} {{s}}'><img src='../img/minolovec_zastavica.png' width='30px' height='30px'></button>
                        % elif celica.odprta == False and celica.zastavica == False:
                            <button id='close-image' name='celica1' value='{{v}} {{s}}'><img src='../img/minolovec_zaprta.png' width='30px' height='30px'></button>
                        %end
                    </td>
                %end
            </tr>
        %end
    </table>
</form>



<form action="/igra/" method="get">
    <button type='submit'>Odkrivaj celice</button>
</form>