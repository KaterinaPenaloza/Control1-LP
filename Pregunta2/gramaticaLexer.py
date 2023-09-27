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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\6\7\62\n\7\r\7\16")
        buf.write("\7\63\3\7\3\7\3\b\5\b9\n\b\3\b\3\b\2\2\t\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2>\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\24\3\2")
        buf.write("\2\2\7\30\3\2\2\2\t!\3\2\2\2\13(\3\2\2\2\r\61\3\2\2\2")
        buf.write("\178\3\2\2\2\21\22\7=\2\2\22\4\3\2\2\2\23\25\t\2\2\2\24")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2")
        buf.write("\27\6\3\2\2\2\30\31\7g\2\2\31\32\7p\2\2\32\33\7e\2\2\33")
        buf.write("\34\7g\2\2\34\35\7p\2\2\35\36\7f\2\2\36\37\7g\2\2\37 ")
        buf.write("\7t\2\2 \b\3\2\2\2!\"\7c\2\2\"#\7r\2\2#$\7c\2\2$%\7i\2")
        buf.write("\2%&\7c\2\2&\'\7t\2\2\'\n\3\2\2\2()\7f\2\2)*\7k\2\2*+")
        buf.write("\7d\2\2+,\7w\2\2,-\7l\2\2-.\7c\2\2./\7t\2\2/\f\3\2\2\2")
        buf.write("\60\62\t\3\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\b\7\2\2\66\16\3\2")
        buf.write("\2\2\679\7\17\2\28\67\3\2\2\289\3\2\2\29:\3\2\2\2:;\7")
        buf.write("\f\2\2;\20\3\2\2\2\6\2\26\638\3\b\2\2")
        return buf.getvalue()


class gramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NUMBER = 2
    ENCENDER = 3
    APAGAR = 4
    DIBUJAR = 5
    WS = 6
    NEWLINE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'encender'", "'apagar'", "'dibujar'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "DIBUJAR", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "NUMBER", "ENCENDER", "APAGAR", "DIBUJAR", "WS", 
                  "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


