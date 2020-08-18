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
                            <button name='celica' value='{{v}} {{s}}'><img src='.../img/minolovec_zastavica.png' alt='X'></button>
                        % else:
                            <button name='celica' value='{{v}} {{s}}'><img src='.../img/minolovec_zaprta.png' alt='X'></button>
                </td>
        </tr>
</table>

<form action="/igra_zastavice/" method="post">
    <button name='odkrivaj_celice'>Odkrivaj celice</button>
</form>