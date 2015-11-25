#!/usr/bin/env python2   

#----------------------------------------------------
#   Project Name:       CS419 Final Project - Curses Interface
#
#   Contributers:       Nick Mastrokalos
#                       Bryan Bauer
#                       Darnel Clayton
#
#----------------------------------------------------

import curses
from curses_interface import MyApp

curses.wrapper(MyApp)