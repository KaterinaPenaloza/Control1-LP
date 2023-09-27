grammar gramatica;

prog    :   iniciar+ ;

iniciar : stat NEWLINE                # printStat
        | NEWLINE                     # blank
        ;

stat    : ENCENDER stat # On
        | APAGAR  stat # Off
        | DIBUJAR stat # Dib
        | ROTAR stat # ROTA
        | MOVER stat # Mov  
        | ';' # fin
        ;

NUMBER : [0-9]+;

ENCENDER : 'encender';

APAGAR : 'apagar';

DIBUJAR : 'dibujar';

ROTAR : 'rotar';

MOVER : 'mover';

WS : [ \t\r\n]+->skip;

NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)