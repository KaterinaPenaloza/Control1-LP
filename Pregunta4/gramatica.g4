grammar gramatica;      //se define el nombre de la gramatica que se utilizara para generar el analizador lexico y sintactico

prog    :   iniciar+ ;  //define la regla llamada "prog" e indica que "prog" repetira una o mas veces la regla "iniciar"

//Aqui se definen las reglas "iniciar" y "stat"
//iniciar tiene 2 alternativas 
iniciar : stat NEWLINE    # printStat  //iniciar con una regla "stat" seguida de una "NEWLINE"

        | NEWLINE         # blank      //indica que puede ser simplemente una "NEWLINE" 
        ;
//stat tiene 4 alternativas
stat    : ENCENDER stat # On  //indica que puede comenzar con la palabra "ENCENDER" y luego con la declaración "stat"
        | APAGAR  stat # Off  //indica que puede comenzar con la palabra "APAGAR" y luego con la declaración "stat"
        | ROTAR '(' NUMBER ')' stat # Rot | ROTAR '(' NUMBER ',' NUMBER ')'  stat # Rot2  //indica que puede comenzar con la palabra "ROTAR" seguida de un numero entre parentesis o dos numeros separados por una ","
        | MOVER '(' NUMBER ')' stat # Mov | MOVER '(' NUMBER ',' NUMBER ')'  stat # Mov2   //indica que puede comenzar con la palabra "MOVER" seguida de un numero entre parentesis o dos numeros separados por una ","
        | ROTAR '(' MOVER '(' NUMBER ',' NUMBER ')' '+' NUMBER ')' stat # Rot3   //indica que puede comenzar con la palabra "ROTAR" seguida de un numero entre parentesis o dos numeros separados por una ","
        | REPETIR NUMBER ':' stat # Rep
        //| REPETIR '(' stat '*' NUMBER ')' stat # Rep   //indica que puede comenzar con la palabra "REPETIR" seguida de un numero entre parentesis o dos numeros separados por una ","
        //| REPETIR '(' stat MULTIPLICAR NUMBER')' stat # Rep
        | ';' # fin  //representa una declaración en blanco
        ;


NUMBER : ('-'? [0-9]+); //define la regla "NUMBER" que representa un numero, el cual puede iniciar opcionalmente con un numero negativo y luego tener opcionalmente 1 o mas digitos

ENCENDER : 'encender';  //representa la palabra clave "ENCENDER"

APAGAR : 'apagar';      //representa la palabra clave "APAGAR"

ROTAR : 'rotar';        //representa la palabra clave "ROTAR"

MOVER : 'mover';        //representa la palabra clave "MOVER"

REPETIR : 'repetir';    //representa la palabra clave "REPETIR"

MULTIPLICAR : '*';      //representa la palabra clave "MULTIPLICAR"

WS : [ \t\r\n]+->skip;  //se utiliza para reconocer y descartar espacios en blanco

NEWLINE:'\r'? '\n' ;     // se utiliza para reconocer lineas nuevas