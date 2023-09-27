grammar gramatica;

prog    :   iniciar+ ;

iniciar : stat NEWLINE                # printStat
        | NEWLINE                     # blank
        ;

stat    : ENCENDER stat # On
        | APAGAR  stat # Off
        | DIBUJAR stat # Dib
        | ';' # fin
        ;

NUMBER : [0-9]+;

ENCENDER : 'encender';

APAGAR : 'apagar';

DIBUJAR : 'dibujar';

WS : [ \t\r\n]+->skip;

NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)