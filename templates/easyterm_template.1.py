#! /usr/bin/env python3
from easyterm import command_line_options, printerr, write, check_file_presence

help_msg=""" This program does something.

### Options:
-i            define inputfile [or provide it as 1st argument]
-print_opt    print currently active options
-h | --help   print this help and exit"""

# fill def_opt with default options
def_opt= {'i':'inputfile'}

opt=command_line_options(def_opt, help_msg, 'i')

### opt now contains the options specified at runtime
# write(opt, how='green')

## checking presence of inputfile
input_file=opt['i']
check_file_presence(input_file, 'input_file')

### place your code here
