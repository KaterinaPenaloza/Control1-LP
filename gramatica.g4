grammar gramatica;

prog:   stat+ ;

stat    : ENCENDER ';' # On
        | APAGAR ';' # Off
        | MOVER '(' NUMBER ',' NUMBER ')' ';' # Mov
        | DIBUJAR '(' NUMBER ',' NUMBER ')' ';' # Dib
        | ';' #fin
        ;

NUMBER : [0-9]+;

ENCENDER : 'encender';

APAGAR : 'apagar';

MOVER : 'mover';

DIBUJAR : 'dibujar';

WS : [ \t\r\n]+->skip;