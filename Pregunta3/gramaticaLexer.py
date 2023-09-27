# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta3\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\'\n\7\r\7")
        buf.write("\16\7(\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\6\fH\n\f\r\f\16\fI\3\f\3\f\3\r\5\r")
        buf.write("O\n\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\3\2\4\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3")
        buf.write("\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3")
        buf.write("\2\2\2\r&\3\2\2\2\17*\3\2\2\2\21\63\3\2\2\2\23:\3\2\2")
        buf.write("\2\25@\3\2\2\2\27G\3\2\2\2\31N\3\2\2\2\33\34\7*\2\2\34")
        buf.write("\4\3\2\2\2\35\36\7+\2\2\36\6\3\2\2\2\37 \7.\2\2 \b\3\2")
        buf.write("\2\2!\"\7-\2\2\"\n\3\2\2\2#$\7=\2\2$\f\3\2\2\2%\'\t\2")
        buf.write("\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)\16\3\2")
        buf.write("\2\2*+\7g\2\2+,\7p\2\2,-\7e\2\2-.\7g\2\2./\7p\2\2/\60")
        buf.write("\7f\2\2\60\61\7g\2\2\61\62\7t\2\2\62\20\3\2\2\2\63\64")
        buf.write("\7c\2\2\64\65\7r\2\2\65\66\7c\2\2\66\67\7i\2\2\678\7c")
        buf.write("\2\289\7t\2\29\22\3\2\2\2:;\7t\2\2;<\7q\2\2<=\7v\2\2=")
        buf.write(">\7c\2\2>?\7t\2\2?\24\3\2\2\2@A\7o\2\2AB\7q\2\2BC\7x\2")
        buf.write("\2CD\7g\2\2DE\7t\2\2E\26\3\2\2\2FH\t\3\2\2GF\3\2\2\2H")
        buf.write("I\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\b\f\2\2L\30")
        buf.write("\3\2\2\2MO\7\17\2\2NM\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\7")
        buf.write("\f\2\2Q\32\3\2\2\2\6\2(IN\3\b\2\2")
        return buf.getvalue()


class gramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    ENCENDER = 7
    APAGAR = 8
    ROTAR = 9
    MOVER = 10
    WS = 11
    NEWLINE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'+'", "';'", "'encender'", "'apagar'", 
            "'rotar'", "'mover'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "ROTAR", "MOVER", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "ENCENDER", 
                  "APAGAR", "ROTAR", "MOVER", "WS", "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


