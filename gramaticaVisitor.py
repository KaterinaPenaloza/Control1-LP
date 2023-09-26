# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#On.
    def visitOn(self, ctx:gramaticaParser.OnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Dib.
    def visitDib(self, ctx:gramaticaParser.DibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        return self.visitChildren(ctx)



del gramaticaParser