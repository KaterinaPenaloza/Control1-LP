# Generated from c:\\Users\\Kzwy\\Desktop\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\35\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\3\3\3\3\3\3\5\3\22\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\33\n\4\3\4\2\2\5\2\4\6\2\2\2\36\2\t\3\2\2\2\4\21")
        buf.write("\3\2\2\2\6\32\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2")
        buf.write("\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4")
        buf.write("\2\16\17\7\t\2\2\17\22\3\2\2\2\20\22\7\t\2\2\21\r\3\2")
        buf.write("\2\2\21\20\3\2\2\2\22\5\3\2\2\2\23\24\7\5\2\2\24\33\5")
        buf.write("\6\4\2\25\26\7\6\2\2\26\33\5\6\4\2\27\30\7\7\2\2\30\33")
        buf.write("\5\6\4\2\31\33\7\3\2\2\32\23\3\2\2\2\32\25\3\2\2\2\32")
        buf.write("\27\3\2\2\2\32\31\3\2\2\2\33\7\3\2\2\2\5\13\21\32")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "<INVALID>", "'encender'", "'apagar'", 
                     "'dibujar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMBER", "ENCENDER", "APAGAR", 
                      "DIBUJAR", "WS", "NEWLINE" ]

    RULE_prog = 0
    RULE_iniciar = 1
    RULE_stat = 2

    ruleNames =  [ "prog", "iniciar", "stat" ]

    EOF = Token.EOF
    T__0=1
    NUMBER=2
    ENCENDER=3
    APAGAR=4
    DIBUJAR=5
    WS=6
    NEWLINE=7

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

        def iniciar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.IniciarContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.IniciarContext,i)


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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.iniciar()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gramaticaParser.T__0) | (1 << gramaticaParser.ENCENDER) | (1 << gramaticaParser.APAGAR) | (1 << gramaticaParser.DIBUJAR) | (1 << gramaticaParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IniciarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_iniciar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(IniciarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.IniciarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(gramaticaParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(IniciarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.IniciarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)

        def NEWLINE(self):
            return self.getToken(gramaticaParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)



    def iniciar(self):

        localctx = gramaticaParser.IniciarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_iniciar)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gramaticaParser.T__0, gramaticaParser.ENCENDER, gramaticaParser.APAGAR, gramaticaParser.DIBUJAR]:
                localctx = gramaticaParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.stat()
                self.state = 12
                self.match(gramaticaParser.NEWLINE)
                pass
            elif token in [gramaticaParser.NEWLINE]:
                localctx = gramaticaParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(gramaticaParser.NEWLINE)
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


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



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
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


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
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


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
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


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
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gramaticaParser.ENCENDER]:
                localctx = gramaticaParser.OnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(gramaticaParser.ENCENDER)
                self.state = 18
                self.stat()
                pass
            elif token in [gramaticaParser.APAGAR]:
                localctx = gramaticaParser.OffContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(gramaticaParser.APAGAR)
                self.state = 20
                self.stat()
                pass
            elif token in [gramaticaParser.DIBUJAR]:
                localctx = gramaticaParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(gramaticaParser.DIBUJAR)
                self.state = 22
                self.stat()
                pass
            elif token in [gramaticaParser.T__0]:
                localctx = gramaticaParser.FinContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 23
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





