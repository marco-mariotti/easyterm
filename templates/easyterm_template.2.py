#! /usr/bin/env python3
import os, shutil
from easyterm import write, printerr, random_folder, command_line_options, NoTracebackError, check_file_presence

help_msg="""
### Input/Output:
-s     define some string option, for an inputfile
-n     define some integer number option
-f     define some floating point number option
-x     define some list type option 

### Options:
-temp         temporary folder. A randomly named subfolder is created inside, and deleted when exiting
-print_opt    print currently active options
-h | --help  print this help and exit"""

command_line_synonyms={'t':'temp'}
def_opt= {'s':'',
          'n':0,
          'f':0.,
          'x':[],
          'temp':'/tmp/'}


temp_folder=None

##### start main program function
def main(args={}):
  """We're encapsulating nearly the whole program in a function which is executed when 
  the script is directly executed. This provides the alternative of being able 
  to run the same thing as module: importing this 'main' function and running it with 
  a 'args' dictionary containing options and arguments, equivalent to opt
  """
  
  ### loading options
  if not args:
    opt=command_line_options(def_opt,
                             help_msg,
                             positional_keys='', #### debug                             
                             synonyms=command_line_synonyms)
  else:   
    opt=args

  # writing options
  write(opt, how='green')
    
  # checking input: option -s is a file path
  input_file=opt['s']
  check_file_presence(input_file, 'input_file')

  # showing a message when a compulsory option is not provided
  if opt['n']==0:
    raise NoTracebackError('ERROR option -n is compulsory!')
  
  # creating a temporary folder with random name inside the -temp argument
  temp_folder=random_folder(opt['temp'])
  write(f'Using temporary folder={temp_folder}')
  
  ### insert your code here



##### end main program function

### function executed when program execution is over
def close_program():
  if temp_folder is not None and os.path.isdir(temp_folder):
    # deleting temporary folder
    shutil.rmtree(temp_folder)

if __name__ == "__main__":
  try:
    main()
    close_program()  
  except Exception as e:
    close_program()
    raise e from None
