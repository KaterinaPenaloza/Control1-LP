# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta4\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\5\7+\n\7\3\7\6\7.\n\7\r\7\16\7/\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\6\16Y\n\16\r\16")
        buf.write("\16\16Z\3\16\3\16\3\17\5\17`\n\17\3\17\3\17\2\2\20\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2f\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7#\3\2\2\2\t%\3\2")
        buf.write("\2\2\13\'\3\2\2\2\r*\3\2\2\2\17\61\3\2\2\2\21:\3\2\2\2")
        buf.write("\23A\3\2\2\2\25G\3\2\2\2\27M\3\2\2\2\31U\3\2\2\2\33X\3")
        buf.write("\2\2\2\35_\3\2\2\2\37 \7*\2\2 \4\3\2\2\2!\"\7+\2\2\"\6")
        buf.write("\3\2\2\2#$\7.\2\2$\b\3\2\2\2%&\7-\2\2&\n\3\2\2\2\'(\7")
        buf.write("=\2\2(\f\3\2\2\2)+\7/\2\2*)\3\2\2\2*+\3\2\2\2+-\3\2\2")
        buf.write("\2,.\t\2\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2")
        buf.write("\60\16\3\2\2\2\61\62\7g\2\2\62\63\7p\2\2\63\64\7e\2\2")
        buf.write("\64\65\7g\2\2\65\66\7p\2\2\66\67\7f\2\2\678\7g\2\289\7")
        buf.write("t\2\29\20\3\2\2\2:;\7c\2\2;<\7r\2\2<=\7c\2\2=>\7i\2\2")
        buf.write(">?\7c\2\2?@\7t\2\2@\22\3\2\2\2AB\7t\2\2BC\7q\2\2CD\7v")
        buf.write("\2\2DE\7c\2\2EF\7t\2\2F\24\3\2\2\2GH\7o\2\2HI\7q\2\2I")
        buf.write("J\7x\2\2JK\7g\2\2KL\7t\2\2L\26\3\2\2\2MN\7t\2\2NO\7g\2")
        buf.write("\2OP\7r\2\2PQ\7g\2\2QR\7v\2\2RS\7k\2\2ST\7t\2\2T\30\3")
        buf.write("\2\2\2UV\7,\2\2V\32\3\2\2\2WY\t\3\2\2XW\3\2\2\2YZ\3\2")
        buf.write("\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\b\16\2\2]\34\3")
        buf.write("\2\2\2^`\7\17\2\2_^\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\f")
        buf.write("\2\2b\36\3\2\2\2\7\2*/Z_\3\b\2\2")
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
    REPETIR = 11
    MULTIPLICAR = 12
    WS = 13
    NEWLINE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'+'", "';'", "'encender'", "'apagar'", 
            "'rotar'", "'mover'", "'repetir'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ENCENDER", "APAGAR", "ROTAR", "MOVER", "REPETIR", 
            "MULTIPLICAR", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "ENCENDER", 
                  "APAGAR", "ROTAR", "MOVER", "REPETIR", "MULTIPLICAR", 
                  "WS", "NEWLINE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


