# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta1\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\5\6!\n\6\3\6\6\6$\n\6\r\6\16\6%\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\6\n?\n\n\r\n\16\n@\3")
        buf.write("\n\3\n\3\13\5\13F\n\13\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\3\2\4\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\2L\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2")
        buf.write("\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13 \3\2\2\2\r\'\3\2\2\2")
        buf.write("\17\60\3\2\2\2\21\67\3\2\2\2\23>\3\2\2\2\25E\3\2\2\2\27")
        buf.write("\30\7*\2\2\30\4\3\2\2\2\31\32\7+\2\2\32\6\3\2\2\2\33\34")
        buf.write("\7.\2\2\34\b\3\2\2\2\35\36\7=\2\2\36\n\3\2\2\2\37!\7/")
        buf.write("\2\2 \37\3\2\2\2 !\3\2\2\2!#\3\2\2\2\"$\t\2\2\2#\"\3\2")
        buf.write("\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\f\3\2\2\2\'(\7g\2")
        buf.write("\2()\7p\2\2)*\7e\2\2*+\7g\2\2+,\7p\2\2,-\7f\2\2-.\7g\2")
        buf.write("\2./\7t\2\2/\16\3\2\2\2\60\61\7c\2\2\61\62\7r\2\2\62\63")
        buf.write("\7c\2\2\63\64\7i\2\2\64\65\7c\2\2\65\66\7t\2\2\66\20\3")
        buf.write("\2\2\2\678\7o\2\289\7q\2\29:\7x\2\2:;\7g\2\2;<\7t\2\2")
        buf.write("<\22\3\2\2\2=?\t\3\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@")
        buf.write("A\3\2\2\2AB\3\2\2\2BC\b\n\2\2C\24\3\2\2\2DF\7\17\2\2E")
        buf.write("D\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\7\f\2\2H\26\3\2\2\2\7")
        buf.write("\2 %@E\3\b\2\2")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


