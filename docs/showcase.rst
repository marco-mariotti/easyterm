.. raw:: html
	 
    <style> .norm {font-family: monospace}   </style>
    <style> .red {color:red; font-family: monospace}   </style>    
    <style> .blue {color:blue; font-family: monospace} </style>    

.. role:: red

.. role:: blue	  

	  
		   
	     
Showcase of easyterm
====================

Welcome to the showcase page of easyterm.
Here, you'll find concisive examples to show the features
offered by this module.

.. contents:: Contents of Tutorial
	         :depth: 3


Showcase set-up
~~~~~~~~~~~~~~~

For the examples below to work correctly, after :doc:`installing easyterm<installation>`,
open python and run this before anything else::

    >>> from easyterm import *
			 
Printing with colors and other markup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The module :doc:`colorprint` offers functions to easily print elegant messages
to screen (using ANSI terminal colors).

Function :func:`~easyterm.colorprint.write` works like the python built-in ``print``, but
additionally offers argument ``how``, which accept a markup code which defines the color
used to printing to screen the message.

::
 
    >>> write('This is a message with no markup')

:norm:`This is a message with no markup`

    >>> write('This message is colored!', how='red')

:red:`This message is colored!`

     
There are many markups available, as shown here::
   
     >>> for i in 'black blue bright cyan dim green magenta red reverse underscore white yellow reverse,blue,bright red,underscore'.split():
     ...  write('This message is marked with '+i, how=i)

     
.. image:: docs/_static/colorprint_showcase.png

	   

Note that some markups can be combined with others (using commas), as shown in the last two examples above.

.. image:: _static/colorprint_showcase.png


Test

.. image:: ./_static/colorprint_showcase.png

*Note: examples above are colored using html; for most accurate results, run the code in a python terminal*


