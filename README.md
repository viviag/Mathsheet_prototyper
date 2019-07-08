### Mathsheet_prototyper
Extremely special and very small tool to extract prototypical problems from set of files with cloned ones. Done for MCCME.

This is probable place for any such script by me valid for mathematical page making.

Selects set of files matching given special file name, extracts first problems from them and build up new file against given preamble.

What these files are? They are TeX files with suffix matching `_\d+.tex` in filename.
What is problem?

Problem is this:
```
\newcommand{\problem}[1]{\pagebreak[3]\addvspace{12pt plus 3pt}\refstepcounter{problem}%
	\everypar{\hskip-\parindent\llap{\makebox[15mm][l]{\smash{\fbox{\makebox[1.75em][c]{\bf %\;#1
							\theproblem
		}}}}}\ignorespaces\everypar{}}}
```
This is legacy code in LaTeX, sense is probably unclear. It's just special clause like `section` for numbered problem in an exercise book.

#### Usage

```
python prototypes_backwards.py "prefix" preamble.tex
```

As being very special tool, it doesn't offer binary.

"prefix" is prefix of files to be matched.

**preamble.tex** is a compilable file to be used as skeleton for exercise list file, which is an expected result.
It should be used to place in all needed imports and macros. 

_viviag_
