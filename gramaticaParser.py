# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("!\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\37\n\3\3\3\2\2\4\2\4\2\2\2#\2\7\3\2\2\2")
        buf.write("\4\36\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7")
        buf.write("\3\2\2\2\t\n\3\2\2\2\n\3\3\2\2\2\13\f\7\b\2\2\f\37\7\3")
        buf.write("\2\2\r\16\7\t\2\2\16\37\7\3\2\2\17\20\7\n\2\2\20\21\7")
        buf.write("\4\2\2\21\22\7\7\2\2\22\23\7\5\2\2\23\24\7\7\2\2\24\25")
        buf.write("\7\6\2\2\25\37\7\3\2\2\26\27\7\13\2\2\27\30\7\4\2\2\30")
        buf.write("\31\7\7\2\2\31\32\7\5\2\2\32\33\7\7\2\2\33\34\7\6\2\2")
        buf.write("\34\37\7\3\2\2\35\37\7\3\2\2\36\13\3\2\2\2\36\r\3\2\2")
        buf.write("\2\36\17\3\2\2\2\36\26\3\2\2\2\36\35\3\2\2\2\37\5\3\2")
        buf.write("\2\2\4\t\36")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "<INVALID>", 
                     "'encender'", "'apagar'", "'mover'", "'dibujar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "ENCENDER", "APAGAR", "MOVER", 
                      "DIBUJAR", "WS" ]

    RULE_prog = 0
    RULE_stat = 1

    ruleNames =  [ "prog", "stat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    ENCENDER=6
    APAGAR=7
    MOVER=8
    DIBUJAR=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = gramaticaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.stat()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gramaticaParser.T__0) | (1 << gramaticaParser.ENCENDER) | (1 << gramaticaParser.APAGAR) | (1 << gramaticaParser.MOVER) | (1 << gramaticaParser.DIBUJAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MovContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOVER(self):
            return self.getToken(gramaticaParser.MOVER, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMBER)
            else:
                return self.getToken(gramaticaParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMov" ):
                listener.enterMov(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMov" ):
                listener.exitMov(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMov" ):
                return visitor.visitMov(self)
            else:
                return visitor.visitChildren(self)


    class FinContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFin" ):
                listener.enterFin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFin" ):
                listener.exitFin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFin" ):
                return visitor.visitFin(self)
            else:
                return visitor.visitChildren(self)


    class DibContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIBUJAR(self):
            return self.getToken(gramaticaParser.DIBUJAR, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMBER)
            else:
                return self.getToken(gramaticaParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDib" ):
                listener.enterDib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDib" ):
                listener.exitDib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDib" ):
                return visitor.visitDib(self)
            else:
                return visitor.visitChildren(self)


    class OffContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def APAGAR(self):
            return self.getToken(gramaticaParser.APAGAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOff" ):
                listener.enterOff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOff" ):
                listener.exitOff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOff" ):
                return visitor.visitOff(self)
            else:
                return visitor.visitChildren(self)


    class OnContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENCENDER(self):
            return self.getToken(gramaticaParser.ENCENDER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn" ):
                listener.enterOn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn" ):
                listener.exitOn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn" ):
                return visitor.visitOn(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = gramaticaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gramaticaParser.ENCENDER]:
                localctx = gramaticaParser.OnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(gramaticaParser.ENCENDER)
                self.state = 10
                self.match(gramaticaParser.T__0)
                pass
            elif token in [gramaticaParser.APAGAR]:
                localctx = gramaticaParser.OffContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(gramaticaParser.APAGAR)
                self.state = 12
                self.match(gramaticaParser.T__0)
                pass
            elif token in [gramaticaParser.MOVER]:
                localctx = gramaticaParser.MovContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(gramaticaParser.MOVER)
                self.state = 14
                self.match(gramaticaParser.T__1)
                self.state = 15
                self.match(gramaticaParser.NUMBER)
                self.state = 16
                self.match(gramaticaParser.T__2)
                self.state = 17
                self.match(gramaticaParser.NUMBER)
                self.state = 18
                self.match(gramaticaParser.T__3)
                self.state = 19
                self.match(gramaticaParser.T__0)
                pass
            elif token in [gramaticaParser.DIBUJAR]:
                localctx = gramaticaParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(gramaticaParser.DIBUJAR)
                self.state = 21
                self.match(gramaticaParser.T__1)
                self.state = 22
                self.match(gramaticaParser.NUMBER)
                self.state = 23
                self.match(gramaticaParser.T__2)
                self.state = 24
                self.match(gramaticaParser.NUMBER)
                self.state = 25
                self.match(gramaticaParser.T__3)
                self.state = 26
                self.match(gramaticaParser.T__0)
                pass
            elif token in [gramaticaParser.T__0]:
                localctx = gramaticaParser.FinContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.match(gramaticaParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





