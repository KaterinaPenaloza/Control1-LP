// Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta4//gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramaticaParser}.
 */
public interface gramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(gramaticaParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(gramaticaParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStat}
	 * labeled alternative in {@link gramaticaParser#iniciar}.
	 * @param ctx the parse tree
	 */
	void enterPrintStat(gramaticaParser.PrintStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStat}
	 * labeled alternative in {@link gramaticaParser#iniciar}.
	 * @param ctx the parse tree
	 */
	void exitPrintStat(gramaticaParser.PrintStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link gramaticaParser#iniciar}.
	 * @param ctx the parse tree
	 */
	void enterBlank(gramaticaParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link gramaticaParser#iniciar}.
	 * @param ctx the parse tree
	 */
	void exitBlank(gramaticaParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by the {@code On}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterOn(gramaticaParser.OnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code On}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitOn(gramaticaParser.OnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Off}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterOff(gramaticaParser.OffContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Off}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitOff(gramaticaParser.OffContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rot}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterRot(gramaticaParser.RotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Rot}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitRot(gramaticaParser.RotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rot2}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterRot2(gramaticaParser.Rot2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code Rot2}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitRot2(gramaticaParser.Rot2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code Mov}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterMov(gramaticaParser.MovContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mov}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitMov(gramaticaParser.MovContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mov2}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterMov2(gramaticaParser.Mov2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code Mov2}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitMov2(gramaticaParser.Mov2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code Rot3}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterRot3(gramaticaParser.Rot3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code Rot3}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitRot3(gramaticaParser.Rot3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code fin}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterFin(gramaticaParser.FinContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fin}
	 * labeled alternative in {@link gramaticaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitFin(gramaticaParser.FinContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rep}
	 * labeled alternative in {@link gramaticaParser#repetir}.
	 * @param ctx the parse tree
	 */
	void enterRep(gramaticaParser.RepContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Rep}
	 * labeled alternative in {@link gramaticaParser#repetir}.
	 * @param ctx the parse tree
	 */
	void exitRep(gramaticaParser.RepContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FinRep}
	 * labeled alternative in {@link gramaticaParser#finR}.
	 * @param ctx the parse tree
	 */
	void enterFinRep(gramaticaParser.FinRepContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FinRep}
	 * labeled alternative in {@link gramaticaParser#finR}.
	 * @param ctx the parse tree
	 */
	void exitFinRep(gramaticaParser.FinRepContext ctx);
}