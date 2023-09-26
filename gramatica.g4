grammar gramatica;

prog    :   iniciar+ ;

iniciar : stat NEWLINE                # printStat
        | NEWLINE                     # blank
        ;

stat    : ENCENDER stat # On
        | APAGAR  stat # Off
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

NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)