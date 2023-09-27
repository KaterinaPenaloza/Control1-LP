# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta4\\gramatica.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\5\3\22\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4F\n\4\3\4\2\2\5\2\4\6\2\2\2N\2\t\3\2\2\2")
        buf.write("\4\21\3\2\2\2\6E\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13")
        buf.write("\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\5")
        buf.write("\6\4\2\16\17\7\20\2\2\17\22\3\2\2\2\20\22\7\20\2\2\21")
        buf.write("\r\3\2\2\2\21\20\3\2\2\2\22\5\3\2\2\2\23\24\7\t\2\2\24")
        buf.write("F\5\6\4\2\25\26\7\n\2\2\26F\5\6\4\2\27\30\7\13\2\2\30")
        buf.write("\31\7\3\2\2\31\32\7\b\2\2\32\33\7\4\2\2\33F\5\6\4\2\34")
        buf.write("\35\7\13\2\2\35\36\7\3\2\2\36\37\7\b\2\2\37 \7\5\2\2 ")
        buf.write("!\7\b\2\2!\"\7\4\2\2\"F\5\6\4\2#$\7\f\2\2$%\7\3\2\2%&")
        buf.write("\7\b\2\2&\'\7\4\2\2\'F\5\6\4\2()\7\f\2\2)*\7\3\2\2*+\7")
        buf.write("\b\2\2+,\7\5\2\2,-\7\b\2\2-.\7\4\2\2.F\5\6\4\2/\60\7\13")
        buf.write("\2\2\60\61\7\3\2\2\61\62\7\f\2\2\62\63\7\3\2\2\63\64\7")
        buf.write("\b\2\2\64\65\7\5\2\2\65\66\7\b\2\2\66\67\7\4\2\2\678\7")
        buf.write("\6\2\289\7\b\2\29:\7\4\2\2:F\5\6\4\2;<\7\r\2\2<=\7\3\2")
        buf.write("\2=>\5\6\4\2>?\7\16\2\2?@\7\b\2\2@A\7\4\2\2AB\5\6\4\2")
        buf.write("BC\7\20\2\2CF\3\2\2\2DF\7\7\2\2E\23\3\2\2\2E\25\3\2\2")
        buf.write("\2E\27\3\2\2\2E\34\3\2\2\2E#\3\2\2\2E(\3\2\2\2E/\3\2\2")
        buf.write("\2E;\3\2\2\2ED\3\2\2\2F\7\3\2\2\2\5\13\21E")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'+'", "';'", "<INVALID>", 
                     "'encender'", "'apagar'", "'rotar'", "'mover'", "'repetir'", 
                     "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "ENCENDER", "APAGAR", 
                      "ROTAR", "MOVER", "REPETIR", "MULTIPLICAR", "WS", 
                      "NEWLINE" ]

    RULE_prog = 0
    RULE_iniciar = 1
    RULE_stat = 2

    ruleNames =  [ "prog", "iniciar", "stat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    ENCENDER=7
    APAGAR=8
    ROTAR=9
    MOVER=10
    REPETIR=11
    MULTIPLICAR=12
    WS=13
    NEWLINE=14

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gramaticaParser.T__4) | (1 << gramaticaParser.ENCENDER) | (1 << gramaticaParser.APAGAR) | (1 << gramaticaParser.ROTAR) | (1 << gramaticaParser.MOVER) | (1 << gramaticaParser.REPETIR) | (1 << gramaticaParser.NEWLINE))) != 0)):
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
            if token in [gramaticaParser.T__4, gramaticaParser.ENCENDER, gramaticaParser.APAGAR, gramaticaParser.ROTAR, gramaticaParser.MOVER, gramaticaParser.REPETIR]:
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



    class MovContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOVER(self):
            return self.getToken(gramaticaParser.MOVER, 0)
        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


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


    class RotContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(gramaticaParser.ROTAR, 0)
        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRot" ):
                listener.enterRot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRot" ):
                listener.exitRot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRot" ):
                return visitor.visitRot(self)
            else:
                return visitor.visitChildren(self)


    class Mov2Context(StatContext):

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
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMov2" ):
                listener.enterMov2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMov2" ):
                listener.exitMov2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMov2" ):
                return visitor.visitMov2(self)
            else:
                return visitor.visitChildren(self)


    class Rot3Context(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(gramaticaParser.ROTAR, 0)
        def MOVER(self):
            return self.getToken(gramaticaParser.MOVER, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMBER)
            else:
                return self.getToken(gramaticaParser.NUMBER, i)
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRot3" ):
                listener.enterRot3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRot3" ):
                listener.exitRot3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRot3" ):
                return visitor.visitRot3(self)
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


    class RepContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REPETIR(self):
            return self.getToken(gramaticaParser.REPETIR, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatContext,i)

        def MULTIPLICAR(self):
            return self.getToken(gramaticaParser.MULTIPLICAR, 0)
        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)
        def NEWLINE(self):
            return self.getToken(gramaticaParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRep" ):
                listener.enterRep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRep" ):
                listener.exitRep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRep" ):
                return visitor.visitRep(self)
            else:
                return visitor.visitChildren(self)


    class Rot2Context(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(gramaticaParser.ROTAR, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMBER)
            else:
                return self.getToken(gramaticaParser.NUMBER, i)
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRot2" ):
                listener.enterRot2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRot2" ):
                listener.exitRot2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRot2" ):
                return visitor.visitRot2(self)
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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.OnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(gramaticaParser.ENCENDER)
                self.state = 18
                self.stat()
                pass

            elif la_ == 2:
                localctx = gramaticaParser.OffContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(gramaticaParser.APAGAR)
                self.state = 20
                self.stat()
                pass

            elif la_ == 3:
                localctx = gramaticaParser.RotContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(gramaticaParser.ROTAR)
                self.state = 22
                self.match(gramaticaParser.T__0)
                self.state = 23
                self.match(gramaticaParser.NUMBER)
                self.state = 24
                self.match(gramaticaParser.T__1)
                self.state = 25
                self.stat()
                pass

            elif la_ == 4:
                localctx = gramaticaParser.Rot2Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(gramaticaParser.ROTAR)
                self.state = 27
                self.match(gramaticaParser.T__0)
                self.state = 28
                self.match(gramaticaParser.NUMBER)
                self.state = 29
                self.match(gramaticaParser.T__2)
                self.state = 30
                self.match(gramaticaParser.NUMBER)
                self.state = 31
                self.match(gramaticaParser.T__1)
                self.state = 32
                self.stat()
                pass

            elif la_ == 5:
                localctx = gramaticaParser.MovContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.match(gramaticaParser.MOVER)
                self.state = 34
                self.match(gramaticaParser.T__0)
                self.state = 35
                self.match(gramaticaParser.NUMBER)
                self.state = 36
                self.match(gramaticaParser.T__1)
                self.state = 37
                self.stat()
                pass

            elif la_ == 6:
                localctx = gramaticaParser.Mov2Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.match(gramaticaParser.MOVER)
                self.state = 39
                self.match(gramaticaParser.T__0)
                self.state = 40
                self.match(gramaticaParser.NUMBER)
                self.state = 41
                self.match(gramaticaParser.T__2)
                self.state = 42
                self.match(gramaticaParser.NUMBER)
                self.state = 43
                self.match(gramaticaParser.T__1)
                self.state = 44
                self.stat()
                pass

            elif la_ == 7:
                localctx = gramaticaParser.Rot3Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.match(gramaticaParser.ROTAR)
                self.state = 46
                self.match(gramaticaParser.T__0)
                self.state = 47
                self.match(gramaticaParser.MOVER)
                self.state = 48
                self.match(gramaticaParser.T__0)
                self.state = 49
                self.match(gramaticaParser.NUMBER)
                self.state = 50
                self.match(gramaticaParser.T__2)
                self.state = 51
                self.match(gramaticaParser.NUMBER)
                self.state = 52
                self.match(gramaticaParser.T__1)
                self.state = 53
                self.match(gramaticaParser.T__3)
                self.state = 54
                self.match(gramaticaParser.NUMBER)
                self.state = 55
                self.match(gramaticaParser.T__1)
                self.state = 56
                self.stat()
                pass

            elif la_ == 8:
                localctx = gramaticaParser.RepContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.match(gramaticaParser.REPETIR)
                self.state = 58
                self.match(gramaticaParser.T__0)
                self.state = 59
                self.stat()
                self.state = 60
                self.match(gramaticaParser.MULTIPLICAR)
                self.state = 61
                self.match(gramaticaParser.NUMBER)
                self.state = 62
                self.match(gramaticaParser.T__1)
                self.state = 63
                self.stat()
                self.state = 64
                self.match(gramaticaParser.NEWLINE)
                pass

            elif la_ == 9:
                localctx = gramaticaParser.FinContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 66
                self.match(gramaticaParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





