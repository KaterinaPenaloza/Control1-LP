# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\6\3\31\n\3\r\3\16")
        buf.write("\3\32\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\6\tB\n")
        buf.write("\t\r\t\16\tC\3\t\3\t\3\n\5\nI\n\n\3\n\3\n\2\2\13\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\4\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\2N\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\30\3\2\2\2\7\34\3")
        buf.write("\2\2\2\t%\3\2\2\2\13,\3\2\2\2\r\64\3\2\2\2\17:\3\2\2\2")
        buf.write("\21A\3\2\2\2\23H\3\2\2\2\25\26\7=\2\2\26\4\3\2\2\2\27")
        buf.write("\31\t\2\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\6\3\2\2\2\34\35\7g\2\2\35\36\7p\2\2")
        buf.write("\36\37\7e\2\2\37 \7g\2\2 !\7p\2\2!\"\7f\2\2\"#\7g\2\2")
        buf.write("#$\7t\2\2$\b\3\2\2\2%&\7c\2\2&\'\7r\2\2\'(\7c\2\2()\7")
        buf.write("i\2\2)*\7c\2\2*+\7t\2\2+\n\3\2\2\2,-\7f\2\2-.\7k\2\2.")
        buf.write("/\7d\2\2/\60\7w\2\2\60\61\7l\2\2\61\62\7c\2\2\62\63\7")
        buf.write("t\2\2\63\f\3\2\2\2\64\65\7t\2\2\65\66\7q\2\2\66\67\7v")
        buf.write("\2\2\678\7c\2\289\7t\2\29\16\3\2\2\2:;\7o\2\2;<\7q\2\2")
        buf.write("<=\7x\2\2=>\7g\2\2>?\7t\2\2?\20\3\2\2\2@B\t\3\2\2A@\3")
        buf.write("\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\t\2")
        buf.write("\2F\22\3\2\2\2GI\7\17\2\2HG\3\2\2\2HI\3\2\2\2IJ\3\2\2")
        buf.write("\2JK\7\f\2\2K\24\3\2\2\2\6\2\32CH\3\b\2\2")
        return buf.getvalue()


class gramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NUMBER = 2
    ENCENDER = 3
    APAGAR = 4
    DIBUJAR = 5
    ROTAR = 6
    MOVER = 7
    WS = 8
    NEWLINE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'encender'", "'apagar'", "'dibujar'", "'rotar'", "'mover'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "DIBUJAR", "ROTAR", "MOVER", 
            "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "NUMBER", "ENCENDER", "APAGAR", "DIBUJAR", "ROTAR", 
                  "MOVER", "WS", "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


