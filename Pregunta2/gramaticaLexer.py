# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta2\\gramatica.g4 by ANTLR 4.9.2
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
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\6\5!\n\5\r\5\16\5\"\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\6\13J\n\13\r\13\16\13K\3\13\3")
        buf.write("\13\3\f\5\fQ\n\f\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\3\2\4\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2V\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2")
        buf.write("\5\33\3\2\2\2\7\35\3\2\2\2\t \3\2\2\2\13$\3\2\2\2\r-\3")
        buf.write("\2\2\2\17\64\3\2\2\2\21<\3\2\2\2\23B\3\2\2\2\25I\3\2\2")
        buf.write("\2\27P\3\2\2\2\31\32\7*\2\2\32\4\3\2\2\2\33\34\7+\2\2")
        buf.write("\34\6\3\2\2\2\35\36\7=\2\2\36\b\3\2\2\2\37!\t\2\2\2 \37")
        buf.write("\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\n\3\2\2\2$")
        buf.write("%\7g\2\2%&\7p\2\2&\'\7e\2\2\'(\7g\2\2()\7p\2\2)*\7f\2")
        buf.write("\2*+\7g\2\2+,\7t\2\2,\f\3\2\2\2-.\7c\2\2./\7r\2\2/\60")
        buf.write("\7c\2\2\60\61\7i\2\2\61\62\7c\2\2\62\63\7t\2\2\63\16\3")
        buf.write("\2\2\2\64\65\7f\2\2\65\66\7k\2\2\66\67\7d\2\2\678\7w\2")
        buf.write("\289\7l\2\29:\7c\2\2:;\7t\2\2;\20\3\2\2\2<=\7t\2\2=>\7")
        buf.write("q\2\2>?\7v\2\2?@\7c\2\2@A\7t\2\2A\22\3\2\2\2BC\7o\2\2")
        buf.write("CD\7q\2\2DE\7x\2\2EF\7g\2\2FG\7t\2\2G\24\3\2\2\2HJ\t\3")
        buf.write("\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2")
        buf.write("MN\b\13\2\2N\26\3\2\2\2OQ\7\17\2\2PO\3\2\2\2PQ\3\2\2\2")
        buf.write("QR\3\2\2\2RS\7\f\2\2S\30\3\2\2\2\6\2\"KP\3\b\2\2")
        return buf.getvalue()


class gramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NUMBER = 4
    ENCENDER = 5
    APAGAR = 6
    DIBUJAR = 7
    ROTAR = 8
    MOVER = 9
    WS = 10
    NEWLINE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "';'", "'encender'", "'apagar'", "'dibujar'", 
            "'rotar'", "'mover'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "DIBUJAR", "ROTAR", "MOVER", 
            "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NUMBER", "ENCENDER", "APAGAR", 
                  "DIBUJAR", "ROTAR", "MOVER", "WS", "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


