grammar gramatica;

prog    :   iniciar+ ;

iniciar : stat NEWLINE                # printStat
        | NEWLINE                     # blank
        ;

stat    : ENCENDER stat # On
        | APAGAR  stat # Off
        | MOVER '(' NUMBER ')' stat # Mov | MOVER '(' NUMBER ',' NUMBER ')'  stat # Mov2
        | ';' # fin
        ;

NUMBER : ('-'? [0-9]+);

ENCENDER : 'encender';

APAGAR : 'apagar';

MOVER : 'mover';

WS : [ \t\r\n]+->skip;

NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)