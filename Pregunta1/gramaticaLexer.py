# Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta1//gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,71,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,3,4,31,8,4,1,4,4,4,34,8,4,11,4,12,4,35,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,8,4,8,61,8,8,11,8,12,8,62,1,8,1,8,1,9,3,9,68,8,9,1,9,1,9,0,0,10,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,2,1,0,48,57,3,
        0,9,10,13,13,32,32,74,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,
        0,0,0,9,30,1,0,0,0,11,37,1,0,0,0,13,46,1,0,0,0,15,53,1,0,0,0,17,
        60,1,0,0,0,19,67,1,0,0,0,21,22,5,40,0,0,22,2,1,0,0,0,23,24,5,41,
        0,0,24,4,1,0,0,0,25,26,5,44,0,0,26,6,1,0,0,0,27,28,5,59,0,0,28,8,
        1,0,0,0,29,31,5,45,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,
        32,34,7,0,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,
        0,0,0,36,10,1,0,0,0,37,38,5,101,0,0,38,39,5,110,0,0,39,40,5,99,0,
        0,40,41,5,101,0,0,41,42,5,110,0,0,42,43,5,100,0,0,43,44,5,101,0,
        0,44,45,5,114,0,0,45,12,1,0,0,0,46,47,5,97,0,0,47,48,5,112,0,0,48,
        49,5,97,0,0,49,50,5,103,0,0,50,51,5,97,0,0,51,52,5,114,0,0,52,14,
        1,0,0,0,53,54,5,109,0,0,54,55,5,111,0,0,55,56,5,118,0,0,56,57,5,
        101,0,0,57,58,5,114,0,0,58,16,1,0,0,0,59,61,7,1,0,0,60,59,1,0,0,
        0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,
        6,8,0,0,65,18,1,0,0,0,66,68,5,13,0,0,67,66,1,0,0,0,67,68,1,0,0,0,
        68,69,1,0,0,0,69,70,5,10,0,0,70,20,1,0,0,0,5,0,30,35,62,67,1,6,0,
        0
    ]

class gramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUMBER = 5
    ENCENDER = 6
    APAGAR = 7
    MOVER = 8
    WS = 9
    NEWLINE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "';'", "'encender'", "'apagar'", "'mover'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "MOVER", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "ENCENDER", 
                  "APAGAR", "MOVER", "WS", "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


