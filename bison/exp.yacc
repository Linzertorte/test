%{
// 
// Expression Interpreter, Parser Portion

/* This interpreter evaluates arithmetic expressions and assigns
   them to the specified variable names. The grammar is:

   pgm -> stmt*
   stmt -> id = exp 
        |  print id
   exp -> exp + exp | exp - exp | exp * exp | exp / exp 
        | ( exp ) | - exp | id | number 
*/

#include <iostream>
#include <string>
#include <stdlib.h>
#include <map>
#include <list>
#include "exp.h"

using namespace std;

// the root of the abstract syntax tree
 pgm *root;

// for keeping track of line numbers in the program we are parsing
  int line_num = 1;

// function prototypes, we need the yylex return prototype so C++ won't complain
int yylex();
void yyerror(const char * s);

%}

%start program

%union {
  float num;
  char *id;
  exp_node *expnode;
  list<statement *> *stmts;
  statement *st;
  pgm *prog;
}

%error-verbose

%token <num> NUMBER
%token <id> ID
%token NEWLINE
%token EQUALS PRINT
%left PLUS MINUS 
%left TIMES DIVIDE 
%left LPAREN RPAREN
%nonassoc UMINUS
%type <expnode> exp 
%type <stmts> stmtlist
%type <st> stmt
%type <prog> program

%%

program : stmtlist { $$ = new pgm($1); root = $$; }
;

stmtlist : stmtlist NEWLINE    /* empty line */
	   { // just copy up the stmtlist when a blank line occurs
             $$ = $1;
           }
         | stmtlist stmt NEWLINE
            { // copy up the list and add the stmt to it
              $$ = $1;
              $$->push_back($2);
            }
         | stmtlist error NEWLINE
	   { // just copy up the stmtlist when an error occurs
             $$ = $1;
             yyclearin; } 
         |  
           { $$ = new list<statement *>(); }  /* empty string */
;

stmt: ID EQUALS exp { 
  $$ = new assignment_stmt($1, $3);
	   }
       
| PRINT ID {
  $$ = new print_stmt($2);
 }

 ;

exp:	MINUS exp %prec UMINUS {
  $$ = new unary_minus_node($2); }

	|	exp PLUS exp {
	  $$ = new plus_node($1, $3); }

	|	exp MINUS exp {
	  $$ = new minus_node($1, $3); }

	|	exp TIMES exp {
	  $$ = new times_node($1, $3); }

	|	exp DIVIDE exp {
	  $$ = new divide_node($1, $3); }

	|	LPAREN exp RPAREN  {
          $$ = $2; }

	|	NUMBER {
	  $$ = new number_node($1); }

|       ID {
  $$ = new id_node($1); }
;
 
%%
main()
{
  //  yydebug = 1;
  yyparse();
  root->evaluate();
}

void yyerror(const char * s)
{
  fprintf(stderr, "line %d: %s\n", line_num, s);
}

