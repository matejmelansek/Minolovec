%rebase('base.tpl', title='Minolovec')

<h2>Če želiš odkrivati celice pritisni na gumb: Odkrivaj celice</h2>

<form action='/igra/' method='post'>
    <table>
        % for v in range(st_vrstic):
            <tr>
                % for s in range(st_stolpcev):
                    <td>
                        % celica = igra.postavitev_min[v][s]
                        % if celica.odprta == True and celica.mina == True:
                            <img src='../img/minolovec_mina.png' alt='M'>
                        % elif celica.odprta == True and celica.mina == False:
                            <img src='../img/minolovec_{{celica.mine_v_okolici(v,s)}}.png' alt='{{celica.mine_v_okolici(v,s)}}'>
                        % elif celica.odprta == False and celica.zastavica == True:
                            <img src='../img/minolovec_zastavica.png' alt='F'>
                        % elif celica.odprta == False and celica.zastavica == False:
                            <input type='submit' name='celica' value='{{v}} {{s}}'><img src='../img/minolovec_zaprta.png' alt='X'></button>
                        %end
                    </td>
                %end
            </tr>
        %end
    </table>
</form>


<form action="/igra/" method="post">
    <input type='submit' name='odkrivaj_celice' value='Odkrivaj celice'>
</form>