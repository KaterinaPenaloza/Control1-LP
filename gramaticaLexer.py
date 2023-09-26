# Generated from c:\\Users\\Kzwy\\Desktop\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\6\6#\n\6\r\6\16\6$\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\6\13F\n\13\r\13\16\13G\3\13\3\13\3\f\5\fM\n\f")
        buf.write("\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2R\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35")
        buf.write("\3\2\2\2\t\37\3\2\2\2\13\"\3\2\2\2\r&\3\2\2\2\17/\3\2")
        buf.write("\2\2\21\66\3\2\2\2\23<\3\2\2\2\25E\3\2\2\2\27L\3\2\2\2")
        buf.write("\31\32\7*\2\2\32\4\3\2\2\2\33\34\7.\2\2\34\6\3\2\2\2\35")
        buf.write("\36\7+\2\2\36\b\3\2\2\2\37 \7=\2\2 \n\3\2\2\2!#\t\2\2")
        buf.write("\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\f\3\2\2")
        buf.write("\2&\'\7g\2\2\'(\7p\2\2()\7e\2\2)*\7g\2\2*+\7p\2\2+,\7")
        buf.write("f\2\2,-\7g\2\2-.\7t\2\2.\16\3\2\2\2/\60\7c\2\2\60\61\7")
        buf.write("r\2\2\61\62\7c\2\2\62\63\7i\2\2\63\64\7c\2\2\64\65\7t")
        buf.write("\2\2\65\20\3\2\2\2\66\67\7o\2\2\678\7q\2\289\7x\2\29:")
        buf.write("\7g\2\2:;\7t\2\2;\22\3\2\2\2<=\7f\2\2=>\7k\2\2>?\7d\2")
        buf.write("\2?@\7w\2\2@A\7l\2\2AB\7c\2\2BC\7t\2\2C\24\3\2\2\2DF\t")
        buf.write("\3\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2")
        buf.write("\2IJ\b\13\2\2J\26\3\2\2\2KM\7\17\2\2LK\3\2\2\2LM\3\2\2")
        buf.write("\2MN\3\2\2\2NO\7\f\2\2O\30\3\2\2\2\6\2$GL\3\b\2\2")
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
    DIBUJAR = 9
    WS = 10
    NEWLINE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "';'", "'encender'", "'apagar'", "'mover'", 
            "'dibujar'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "MOVER", "DIBUJAR", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "ENCENDER", 
                  "APAGAR", "MOVER", "DIBUJAR", "WS", "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


