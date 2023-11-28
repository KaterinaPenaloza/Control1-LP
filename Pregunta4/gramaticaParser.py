# Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta4//gramatica.g4 by ANTLR 4.13.1
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
        4,1,15,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,3,2,25,8,2,1,
        2,1,2,1,2,3,2,30,8,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,56,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,81,8,2,1,2,3,2,84,8,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,104,0,11,1,0,
        0,0,2,19,1,0,0,0,4,83,1,0,0,0,6,85,1,0,0,0,8,91,1,0,0,0,10,12,3,
        2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,
        1,1,0,0,0,15,16,3,4,2,0,16,17,5,15,0,0,17,20,1,0,0,0,18,20,5,15,
        0,0,19,15,1,0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,21,24,5,9,0,0,22,25,
        3,4,2,0,23,25,3,6,3,0,24,22,1,0,0,0,24,23,1,0,0,0,25,84,1,0,0,0,
        26,29,5,10,0,0,27,30,3,4,2,0,28,30,3,6,3,0,29,27,1,0,0,0,29,28,1,
        0,0,0,30,84,1,0,0,0,31,32,5,11,0,0,32,33,5,1,0,0,33,34,5,8,0,0,34,
        37,5,2,0,0,35,38,3,4,2,0,36,38,3,6,3,0,37,35,1,0,0,0,37,36,1,0,0,
        0,38,84,1,0,0,0,39,40,5,11,0,0,40,41,5,1,0,0,41,42,5,8,0,0,42,43,
        5,3,0,0,43,44,5,8,0,0,44,47,5,2,0,0,45,48,3,4,2,0,46,48,3,6,3,0,
        47,45,1,0,0,0,47,46,1,0,0,0,48,84,1,0,0,0,49,50,5,12,0,0,50,51,5,
        1,0,0,51,52,5,8,0,0,52,55,5,2,0,0,53,56,3,4,2,0,54,56,3,6,3,0,55,
        53,1,0,0,0,55,54,1,0,0,0,56,84,1,0,0,0,57,58,5,12,0,0,58,59,5,1,
        0,0,59,60,5,8,0,0,60,61,5,3,0,0,61,62,5,8,0,0,62,65,5,2,0,0,63,66,
        3,4,2,0,64,66,3,6,3,0,65,63,1,0,0,0,65,64,1,0,0,0,66,84,1,0,0,0,
        67,68,5,11,0,0,68,69,5,1,0,0,69,70,5,12,0,0,70,71,5,1,0,0,71,72,
        5,8,0,0,72,73,5,3,0,0,73,74,5,8,0,0,74,75,5,2,0,0,75,76,5,4,0,0,
        76,77,5,8,0,0,77,80,5,2,0,0,78,81,3,4,2,0,79,81,3,6,3,0,80,78,1,
        0,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,84,5,5,0,0,83,21,1,0,0,0,83,
        26,1,0,0,0,83,31,1,0,0,0,83,39,1,0,0,0,83,49,1,0,0,0,83,57,1,0,0,
        0,83,67,1,0,0,0,83,82,1,0,0,0,84,5,1,0,0,0,85,86,5,13,0,0,86,87,
        5,8,0,0,87,88,5,6,0,0,88,89,3,4,2,0,89,90,3,8,4,0,90,7,1,0,0,0,91,
        92,5,7,0,0,92,9,1,0,0,0,10,13,19,24,29,37,47,55,65,80,83
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'+'", "';'", "':'", 
                     "'/'", "<INVALID>", "'encender'", "'apagar'", "'rotar'", 
                     "'mover'", "'repetir'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "ENCENDER", "APAGAR", "ROTAR", "MOVER", 
                      "REPETIR", "WS", "NEWLINE" ]

    RULE_prog = 0
    RULE_iniciar = 1
    RULE_stat = 2
    RULE_repetir = 3
    RULE_finRep = 4

    ruleNames =  [ "prog", "iniciar", "stat", "repetir", "finRep" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    ENCENDER=9
    APAGAR=10
    ROTAR=11
    MOVER=12
    REPETIR=13
    WS=14
    NEWLINE=15

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.iniciar()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 40480) != 0)):
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
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 9, 10, 11, 12]:
                localctx = gramaticaParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.stat()
                self.state = 16
                self.match(gramaticaParser.NEWLINE)
                pass
            elif token in [15]:
                localctx = gramaticaParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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

        def repetir(self):
            return self.getTypedRuleContext(gramaticaParser.RepetirContext,0)


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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.OnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(gramaticaParser.ENCENDER)
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 22
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 23
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                localctx = gramaticaParser.OffContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(gramaticaParser.APAGAR)
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 27
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 28
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                localctx = gramaticaParser.RotContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(gramaticaParser.ROTAR)
                self.state = 32
                self.match(gramaticaParser.T__0)
                self.state = 33
                self.match(gramaticaParser.NUMBER)
                self.state = 34
                self.match(gramaticaParser.T__1)
                self.state = 37
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 35
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 36
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                localctx = gramaticaParser.Rot2Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(gramaticaParser.ROTAR)
                self.state = 40
                self.match(gramaticaParser.T__0)
                self.state = 41
                self.match(gramaticaParser.NUMBER)
                self.state = 42
                self.match(gramaticaParser.T__2)
                self.state = 43
                self.match(gramaticaParser.NUMBER)
                self.state = 44
                self.match(gramaticaParser.T__1)
                self.state = 47
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 45
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 46
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 5:
                localctx = gramaticaParser.MovContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.match(gramaticaParser.MOVER)
                self.state = 50
                self.match(gramaticaParser.T__0)
                self.state = 51
                self.match(gramaticaParser.NUMBER)
                self.state = 52
                self.match(gramaticaParser.T__1)
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 53
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 54
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 6:
                localctx = gramaticaParser.Mov2Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(gramaticaParser.MOVER)
                self.state = 58
                self.match(gramaticaParser.T__0)
                self.state = 59
                self.match(gramaticaParser.NUMBER)
                self.state = 60
                self.match(gramaticaParser.T__2)
                self.state = 61
                self.match(gramaticaParser.NUMBER)
                self.state = 62
                self.match(gramaticaParser.T__1)
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 63
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 64
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 7:
                localctx = gramaticaParser.Rot3Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.match(gramaticaParser.ROTAR)
                self.state = 68
                self.match(gramaticaParser.T__0)
                self.state = 69
                self.match(gramaticaParser.MOVER)
                self.state = 70
                self.match(gramaticaParser.T__0)
                self.state = 71
                self.match(gramaticaParser.NUMBER)
                self.state = 72
                self.match(gramaticaParser.T__2)
                self.state = 73
                self.match(gramaticaParser.NUMBER)
                self.state = 74
                self.match(gramaticaParser.T__1)
                self.state = 75
                self.match(gramaticaParser.T__3)
                self.state = 76
                self.match(gramaticaParser.NUMBER)
                self.state = 77
                self.match(gramaticaParser.T__1)
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 9, 10, 11, 12]:
                    self.state = 78
                    self.stat()
                    pass
                elif token in [13]:
                    self.state = 79
                    self.repetir()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 8:
                localctx = gramaticaParser.FinContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.match(gramaticaParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_repetir

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepContext(RepetirContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.RepetirContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REPETIR(self):
            return self.getToken(gramaticaParser.REPETIR, 0)
        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)
        def stat(self):
            return self.getTypedRuleContext(gramaticaParser.StatContext,0)

        def finRep(self):
            return self.getTypedRuleContext(gramaticaParser.FinRepContext,0)


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



    def repetir(self):

        localctx = gramaticaParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repetir)
        try:
            localctx = gramaticaParser.RepContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(gramaticaParser.REPETIR)
            self.state = 86
            self.match(gramaticaParser.NUMBER)
            self.state = 87
            self.match(gramaticaParser.T__5)
            self.state = 88
            self.stat()
            self.state = 89
            self.finRep()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinRepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_finRep

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FRContext(FinRepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FinRepContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFR" ):
                listener.enterFR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFR" ):
                listener.exitFR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFR" ):
                return visitor.visitFR(self)
            else:
                return visitor.visitChildren(self)



    def finRep(self):

        localctx = gramaticaParser.FinRepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_finRep)
        try:
            localctx = gramaticaParser.FRContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





