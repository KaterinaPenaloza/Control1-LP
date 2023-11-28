# Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta3//gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStat.
    def visitPrintStat(self, ctx:gramaticaParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#blank.
    def visitBlank(self, ctx:gramaticaParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#On.
    def visitOn(self, ctx:gramaticaParser.OnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot.
    def visitRot(self, ctx:gramaticaParser.RotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot2.
    def visitRot2(self, ctx:gramaticaParser.Rot2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov2.
    def visitMov2(self, ctx:gramaticaParser.Mov2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot3.
    def visitRot3(self, ctx:gramaticaParser.Rot3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        return self.visitChildren(ctx)



del gramaticaParser