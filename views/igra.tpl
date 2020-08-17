%rebase('base.tpl', title='Minolovec')

<table>
    % for v in range(st_vrstic):
        <tr>
            % for s in range(st_stolpcev):
                <td>
                    % celica = igra.[v][s]
                    % if celica.odprta == True:
                        % if celica.mina == True:
                        % else:
                    % else:
                        % if celica.zastavica == True:
                            % 
                        % else:
                            % 
                </td>
        </tr>
</table>