grammar gramatica;

prog    :   iniciar+ ;

iniciar : stat NEWLINE                # printStat
        | NEWLINE                     # blank
        ;

stat    : ENCENDER stat # On
        | APAGAR  stat # Off
        | ROTAR '(' NUMBER ')' stat # Rot | ROTAR '(' NUMBER ',' NUMBER ')'  stat # Rot2
        | MOVER '(' NUMBER ')' stat # Mov | MOVER '(' NUMBER ',' NUMBER ')'  stat # Mov2
        | ';' # fin
        ;

NUMBER : ('-'? [0-9]+);

ENCENDER : 'encender';

APAGAR : 'apagar';

ROTAR : 'rotar';

MOVER : 'mover';

WS : [ \t\r\n]+->skip;

NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)