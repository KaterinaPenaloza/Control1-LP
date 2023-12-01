# Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta2//gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,49,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,47,8,2,1,2,0,0,3,0,2,4,0,0,53,0,7,1,0,0,0,2,15,1,0,
        0,0,4,46,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,
        9,10,1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,11,0,0,13,16,1,0,
        0,0,14,16,5,11,0,0,15,11,1,0,0,0,15,14,1,0,0,0,16,3,1,0,0,0,17,18,
        5,6,0,0,18,47,3,4,2,0,19,20,5,7,0,0,20,47,3,4,2,0,21,22,5,8,0,0,
        22,23,5,1,0,0,23,24,5,5,0,0,24,25,5,2,0,0,25,47,3,4,2,0,26,27,5,
        8,0,0,27,28,5,1,0,0,28,29,5,5,0,0,29,30,5,3,0,0,30,31,5,5,0,0,31,
        32,5,2,0,0,32,47,3,4,2,0,33,34,5,9,0,0,34,35,5,1,0,0,35,36,5,5,0,
        0,36,37,5,2,0,0,37,47,3,4,2,0,38,39,5,9,0,0,39,40,5,1,0,0,40,41,
        5,5,0,0,41,42,5,3,0,0,42,43,5,5,0,0,43,44,5,2,0,0,44,47,3,4,2,0,
        45,47,5,4,0,0,46,17,1,0,0,0,46,19,1,0,0,0,46,21,1,0,0,0,46,26,1,
        0,0,0,46,33,1,0,0,0,46,38,1,0,0,0,46,45,1,0,0,0,47,5,1,0,0,0,3,9,
        15,46
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "<INVALID>", 
                     "'encender'", "'apagar'", "'rotar'", "'mover'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "ENCENDER", "APAGAR", "ROTAR", 
                      "MOVER", "WS", "NEWLINE" ]

    RULE_prog = 0
    RULE_iniciar = 1
    RULE_stat = 2

    ruleNames =  [ "prog", "iniciar", "stat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    ENCENDER=6
    APAGAR=7
    ROTAR=8
    MOVER=9
    WS=10
    NEWLINE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3024) != 0)):
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
            if token in [4, 6, 7, 8, 9]:
                localctx = gramaticaParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.stat()
                self.state = 12
                self.match(gramaticaParser.NEWLINE)
                pass
            elif token in [11]:
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
            self.state = 46
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
                localctx = gramaticaParser.FinContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.match(gramaticaParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





