######################################################################
# Passing arguments to a R script from command line 
# for example: run the R script as 
#     Rscript --vanilla Rargs_demo.R input.txt output.txt extra_opt 
#
# Peng Zeng @ Auburn University
# updated: 04-18-2021
######################################################################

args = commandArgs(trailingOnly = TRUE); 

cat("There are in total", length(args), "arguments.\n");
if(length(args))
{
    cat("The arguments are:\n"); 
    for(i in 1:length(args))
    {
        cat("Argument ", i, ": ", args[i], "\n", sep = ""); 
    }
}

# args[i] is a string. you may evaluate a string as follows. 

a = "3 + 5"; 
eval(parse(text = a)); 

######################################################################
# THE END
######################################################################
