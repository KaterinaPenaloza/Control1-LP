// Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta4//gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gramaticaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, NUMBER=8, ENCENDER=9, 
		APAGAR=10, ROTAR=11, MOVER=12, REPETIR=13, WS=14, NEWLINE=15;
	public static final int
		RULE_prog = 0, RULE_iniciar = 1, RULE_stat = 2, RULE_repetir = 3, RULE_finRep = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "iniciar", "stat", "repetir", "finRep"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "','", "'+'", "';'", "':'", "'/'", null, "'encender'", 
			"'apagar'", "'rotar'", "'mover'", "'repetir'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "NUMBER", "ENCENDER", 
			"APAGAR", "ROTAR", "MOVER", "REPETIR", "WS", "NEWLINE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<IniciarContext> iniciar() {
			return getRuleContexts(IniciarContext.class);
		}
		public IniciarContext iniciar(int i) {
			return getRuleContext(IniciarContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				iniciar();
				}
				}
				setState(13); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 40480L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IniciarContext extends ParserRuleContext {
		public IniciarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iniciar; }
	 
		public IniciarContext() { }
		public void copyFrom(IniciarContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlankContext extends IniciarContext {
		public TerminalNode NEWLINE() { return getToken(gramaticaParser.NEWLINE, 0); }
		public BlankContext(IniciarContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterBlank(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitBlank(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintStatContext extends IniciarContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(gramaticaParser.NEWLINE, 0); }
		public PrintStatContext(IniciarContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterPrintStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitPrintStat(this);
		}
	}

	public final IniciarContext iniciar() throws RecognitionException {
		IniciarContext _localctx = new IniciarContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_iniciar);
		try {
			setState(19);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
			case ENCENDER:
			case APAGAR:
			case ROTAR:
			case MOVER:
				_localctx = new PrintStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				stat();
				setState(16);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(18);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MovContext extends StatContext {
		public TerminalNode MOVER() { return getToken(gramaticaParser.MOVER, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public MovContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterMov(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitMov(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RotContext extends StatContext {
		public TerminalNode ROTAR() { return getToken(gramaticaParser.ROTAR, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public RotContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterRot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitRot(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Mov2Context extends StatContext {
		public TerminalNode MOVER() { return getToken(gramaticaParser.MOVER, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(gramaticaParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(gramaticaParser.NUMBER, i);
		}
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public Mov2Context(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterMov2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitMov2(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Rot3Context extends StatContext {
		public TerminalNode ROTAR() { return getToken(gramaticaParser.ROTAR, 0); }
		public TerminalNode MOVER() { return getToken(gramaticaParser.MOVER, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(gramaticaParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(gramaticaParser.NUMBER, i);
		}
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public Rot3Context(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterRot3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitRot3(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FinContext extends StatContext {
		public FinContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterFin(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitFin(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Rot2Context extends StatContext {
		public TerminalNode ROTAR() { return getToken(gramaticaParser.ROTAR, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(gramaticaParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(gramaticaParser.NUMBER, i);
		}
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public Rot2Context(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterRot2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitRot2(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OffContext extends StatContext {
		public TerminalNode APAGAR() { return getToken(gramaticaParser.APAGAR, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public OffContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOff(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOff(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OnContext extends StatContext {
		public TerminalNode ENCENDER() { return getToken(gramaticaParser.ENCENDER, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public RepetirContext repetir() {
			return getRuleContext(RepetirContext.class,0);
		}
		public OnContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterOn(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitOn(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stat);
		try {
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				_localctx = new OnContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				match(ENCENDER);
				setState(24);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(22);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(23);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 2:
				_localctx = new OffContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				match(APAGAR);
				setState(29);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(27);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(28);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 3:
				_localctx = new RotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(31);
				match(ROTAR);
				setState(32);
				match(T__0);
				setState(33);
				match(NUMBER);
				setState(34);
				match(T__1);
				setState(37);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(35);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(36);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 4:
				_localctx = new Rot2Context(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(39);
				match(ROTAR);
				setState(40);
				match(T__0);
				setState(41);
				match(NUMBER);
				setState(42);
				match(T__2);
				setState(43);
				match(NUMBER);
				setState(44);
				match(T__1);
				setState(47);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(45);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(46);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 5:
				_localctx = new MovContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(49);
				match(MOVER);
				setState(50);
				match(T__0);
				setState(51);
				match(NUMBER);
				setState(52);
				match(T__1);
				setState(55);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(53);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(54);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 6:
				_localctx = new Mov2Context(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(57);
				match(MOVER);
				setState(58);
				match(T__0);
				setState(59);
				match(NUMBER);
				setState(60);
				match(T__2);
				setState(61);
				match(NUMBER);
				setState(62);
				match(T__1);
				setState(65);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(63);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(64);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 7:
				_localctx = new Rot3Context(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(67);
				match(ROTAR);
				setState(68);
				match(T__0);
				setState(69);
				match(MOVER);
				setState(70);
				match(T__0);
				setState(71);
				match(NUMBER);
				setState(72);
				match(T__2);
				setState(73);
				match(NUMBER);
				setState(74);
				match(T__1);
				setState(75);
				match(T__3);
				setState(76);
				match(NUMBER);
				setState(77);
				match(T__1);
				setState(80);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case ENCENDER:
				case APAGAR:
				case ROTAR:
				case MOVER:
					{
					setState(78);
					stat();
					}
					break;
				case REPETIR:
					{
					setState(79);
					repetir();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 8:
				_localctx = new FinContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(82);
				match(T__4);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepetirContext extends ParserRuleContext {
		public RepetirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repetir; }
	 
		public RepetirContext() { }
		public void copyFrom(RepetirContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RepContext extends RepetirContext {
		public TerminalNode REPETIR() { return getToken(gramaticaParser.REPETIR, 0); }
		public TerminalNode NUMBER() { return getToken(gramaticaParser.NUMBER, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public FinRepContext finRep() {
			return getRuleContext(FinRepContext.class,0);
		}
		public RepContext(RepetirContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterRep(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitRep(this);
		}
	}

	public final RepetirContext repetir() throws RecognitionException {
		RepetirContext _localctx = new RepetirContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_repetir);
		try {
			_localctx = new RepContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(REPETIR);
			setState(86);
			match(NUMBER);
			setState(87);
			match(T__5);
			setState(88);
			stat();
			setState(89);
			finRep();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FinRepContext extends ParserRuleContext {
		public FinRepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_finRep; }
	 
		public FinRepContext() { }
		public void copyFrom(FinRepContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FRContext extends FinRepContext {
		public FRContext(FinRepContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).enterFR(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticaListener ) ((gramaticaListener)listener).exitFR(this);
		}
	}

	public final FinRepContext finRep() throws RecognitionException {
		FinRepContext _localctx = new FinRepContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_finRep);
		try {
			_localctx = new FRContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000f^\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0004\u0000\f\b\u0000\u000b\u0000\f\u0000\r\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\u0014\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002\u0019\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002\u001e\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002&\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u00020\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u00028\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002B\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002Q\b\u0002\u0001\u0002"+
		"\u0003\u0002T\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0000\u0000"+
		"\u0005\u0000\u0002\u0004\u0006\b\u0000\u0000h\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0002\u0013\u0001\u0000\u0000\u0000\u0004S\u0001\u0000\u0000"+
		"\u0000\u0006U\u0001\u0000\u0000\u0000\b[\u0001\u0000\u0000\u0000\n\f\u0003"+
		"\u0002\u0001\u0000\u000b\n\u0001\u0000\u0000\u0000\f\r\u0001\u0000\u0000"+
		"\u0000\r\u000b\u0001\u0000\u0000\u0000\r\u000e\u0001\u0000\u0000\u0000"+
		"\u000e\u0001\u0001\u0000\u0000\u0000\u000f\u0010\u0003\u0004\u0002\u0000"+
		"\u0010\u0011\u0005\u000f\u0000\u0000\u0011\u0014\u0001\u0000\u0000\u0000"+
		"\u0012\u0014\u0005\u000f\u0000\u0000\u0013\u000f\u0001\u0000\u0000\u0000"+
		"\u0013\u0012\u0001\u0000\u0000\u0000\u0014\u0003\u0001\u0000\u0000\u0000"+
		"\u0015\u0018\u0005\t\u0000\u0000\u0016\u0019\u0003\u0004\u0002\u0000\u0017"+
		"\u0019\u0003\u0006\u0003\u0000\u0018\u0016\u0001\u0000\u0000\u0000\u0018"+
		"\u0017\u0001\u0000\u0000\u0000\u0019T\u0001\u0000\u0000\u0000\u001a\u001d"+
		"\u0005\n\u0000\u0000\u001b\u001e\u0003\u0004\u0002\u0000\u001c\u001e\u0003"+
		"\u0006\u0003\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001c\u0001"+
		"\u0000\u0000\u0000\u001eT\u0001\u0000\u0000\u0000\u001f \u0005\u000b\u0000"+
		"\u0000 !\u0005\u0001\u0000\u0000!\"\u0005\b\u0000\u0000\"%\u0005\u0002"+
		"\u0000\u0000#&\u0003\u0004\u0002\u0000$&\u0003\u0006\u0003\u0000%#\u0001"+
		"\u0000\u0000\u0000%$\u0001\u0000\u0000\u0000&T\u0001\u0000\u0000\u0000"+
		"\'(\u0005\u000b\u0000\u0000()\u0005\u0001\u0000\u0000)*\u0005\b\u0000"+
		"\u0000*+\u0005\u0003\u0000\u0000+,\u0005\b\u0000\u0000,/\u0005\u0002\u0000"+
		"\u0000-0\u0003\u0004\u0002\u0000.0\u0003\u0006\u0003\u0000/-\u0001\u0000"+
		"\u0000\u0000/.\u0001\u0000\u0000\u00000T\u0001\u0000\u0000\u000012\u0005"+
		"\f\u0000\u000023\u0005\u0001\u0000\u000034\u0005\b\u0000\u000047\u0005"+
		"\u0002\u0000\u000058\u0003\u0004\u0002\u000068\u0003\u0006\u0003\u0000"+
		"75\u0001\u0000\u0000\u000076\u0001\u0000\u0000\u00008T\u0001\u0000\u0000"+
		"\u00009:\u0005\f\u0000\u0000:;\u0005\u0001\u0000\u0000;<\u0005\b\u0000"+
		"\u0000<=\u0005\u0003\u0000\u0000=>\u0005\b\u0000\u0000>A\u0005\u0002\u0000"+
		"\u0000?B\u0003\u0004\u0002\u0000@B\u0003\u0006\u0003\u0000A?\u0001\u0000"+
		"\u0000\u0000A@\u0001\u0000\u0000\u0000BT\u0001\u0000\u0000\u0000CD\u0005"+
		"\u000b\u0000\u0000DE\u0005\u0001\u0000\u0000EF\u0005\f\u0000\u0000FG\u0005"+
		"\u0001\u0000\u0000GH\u0005\b\u0000\u0000HI\u0005\u0003\u0000\u0000IJ\u0005"+
		"\b\u0000\u0000JK\u0005\u0002\u0000\u0000KL\u0005\u0004\u0000\u0000LM\u0005"+
		"\b\u0000\u0000MP\u0005\u0002\u0000\u0000NQ\u0003\u0004\u0002\u0000OQ\u0003"+
		"\u0006\u0003\u0000PN\u0001\u0000\u0000\u0000PO\u0001\u0000\u0000\u0000"+
		"QT\u0001\u0000\u0000\u0000RT\u0005\u0005\u0000\u0000S\u0015\u0001\u0000"+
		"\u0000\u0000S\u001a\u0001\u0000\u0000\u0000S\u001f\u0001\u0000\u0000\u0000"+
		"S\'\u0001\u0000\u0000\u0000S1\u0001\u0000\u0000\u0000S9\u0001\u0000\u0000"+
		"\u0000SC\u0001\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000T\u0005\u0001"+
		"\u0000\u0000\u0000UV\u0005\r\u0000\u0000VW\u0005\b\u0000\u0000WX\u0005"+
		"\u0006\u0000\u0000XY\u0003\u0004\u0002\u0000YZ\u0003\b\u0004\u0000Z\u0007"+
		"\u0001\u0000\u0000\u0000[\\\u0005\u0007\u0000\u0000\\\t\u0001\u0000\u0000"+
		"\u0000\n\r\u0013\u0018\u001d%/7APS";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}