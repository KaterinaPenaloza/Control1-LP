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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\6\6!\n\6\r\6\16\6\"\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\6\13D\n\13\r\13\16\13E\3\13\3\13\2\2\f\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\4\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\2J\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3")
        buf.write("\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13 \3\2\2\2\r$\3\2\2")
        buf.write("\2\17-\3\2\2\2\21\64\3\2\2\2\23:\3\2\2\2\25C\3\2\2\2\27")
        buf.write("\30\7=\2\2\30\4\3\2\2\2\31\32\7*\2\2\32\6\3\2\2\2\33\34")
        buf.write("\7.\2\2\34\b\3\2\2\2\35\36\7+\2\2\36\n\3\2\2\2\37!\t\2")
        buf.write("\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\f\3")
        buf.write("\2\2\2$%\7g\2\2%&\7p\2\2&\'\7e\2\2\'(\7g\2\2()\7p\2\2")
        buf.write(")*\7f\2\2*+\7g\2\2+,\7t\2\2,\16\3\2\2\2-.\7c\2\2./\7r")
        buf.write("\2\2/\60\7c\2\2\60\61\7i\2\2\61\62\7c\2\2\62\63\7t\2\2")
        buf.write("\63\20\3\2\2\2\64\65\7o\2\2\65\66\7q\2\2\66\67\7x\2\2")
        buf.write("\678\7g\2\289\7t\2\29\22\3\2\2\2:;\7f\2\2;<\7k\2\2<=\7")
        buf.write("d\2\2=>\7w\2\2>?\7l\2\2?@\7c\2\2@A\7t\2\2A\24\3\2\2\2")
        buf.write("BD\t\3\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3")
        buf.write("\2\2\2GH\b\13\2\2H\26\3\2\2\2\5\2\"E\3\b\2\2")
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

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "','", "')'", "'encender'", "'apagar'", "'mover'", 
            "'dibujar'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "MOVER", "DIBUJAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "ENCENDER", 
                  "APAGAR", "MOVER", "DIBUJAR", "WS" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


