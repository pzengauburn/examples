/**********************************************************************
 * prxmatch(perl-regular-expression, source) 
 * Searches for a pattern match and returns the position at which 
 * the pattern is found. 
 * 
 * In the example, 
 *    / / : mark the beginning and end of a regular expression
 *    |   : works as "or"
 *    \b  : marks the a word boundary. 
 *          for example "/\bthe\b/" matches "the", but not "other".
 * 
 * Refer to the following link for more information 
 * http://support.sas.com/documentation/cdl/en/lefunctionsref/63354/HTML/default/viewer.htm#p0s9ilagexmjl8n1u7e1t1jfnzlk.htm
 * 
 * Peng Zeng (Auburn University)
 * 05-22-2019
 **********************************************************************/

data example; 
   input str $50.;
   check1 = prxmatch('/HONDA/', upcase(str));
   check2 = prxmatch('/GEO METRO/', upcase(str));
   check3 = prxmatch('/HONDA|CIVIC/', upcase(str));
   check4 = prxmatch('/HONDA|CIVIC|GEO METRO/', upcase(str));
   check5 = prxmatch('/\bHONDA\b|\bCIVIC\b|\bGEO METRO\b/', upcase(str));
datalines; 
Honda Chevy solu 
world Civic 
New honda old
Geo new one
bug gEo mEtro
b metro geo
ahonda 
civicon
;

proc print data = example; run;
