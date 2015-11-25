#!/usr/bin/env python                                                      

import curses
import database_queries
from time import sleep

DEBUG = True
CON = {}

#----------------------------------------------------
class MyApp(object):

  def __init__(self, stdscreen):
    
    # Init the main curses program
    self.screen = stdscreen
    curses.curs_set(0)
    curses.cbreak() 
    curses.echo()


    # Collect db info (host ip, username, etc.)
    un, addy, db, pw = getConnectionInfo(self.screen)
    # un = "root"
    # addy = "192.168.1.181"
    # pw = "password"
    # db = "TestDC"

# TODO: establish connection with database and either quit or retry with failure
    CON = database_queries.dbConnect(un, pw, db, addy) 

    if CON['state'] == 0:
        # Good credentials, continue to menu starting point
        printStatus(self.screen, CON['state'])
        printMainMenu(self.screen)

    else:
        # Unsuccessful connnection
        while CON['state'] != 0:
            printStatus(self.screen, CON['state'])
            # Bad credentials, try again until OK
            un, addy, db, pw = getConnectionInfo(self.screen)
            CON = database_queries.dbConnect(un, pw, db, addy)
        else:
            #Credentials finally validated, continue to main menu
            printStatus(self.screen, CON['state'])
            printMainMenu(self.screen)

#----------------------------------------------------
def printStatus(stdscr, status):

    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(6, 30, "-- STATUS MESSAGE --")

    if status == 0:
        stdscr.addstr(11, 6, "CONNECTION SUCCESSFUL")

    else:
        stdscr.addstr(9, 6, "CONNECTION FAILED")
        stdscr.addstr(11, 6, "VERIFY YOUR CREDENTIALS AND TRY AGAIN")

    stdscr.addstr(13, 6, "PRESS ANY KEY TO CONTINUE")
    justWait = stdscr.getch()


def getConnectionInfo(stdscr):
    stdscr.clear()
    stdscr.border(0)    

    if DEBUG:
        username = "root"
        host = "192.168.1.181"
        password = "password"
        database = "TestDC"

    else:
        # collect necessary connection info
        stdscr.addstr(10, 5, "Enter the database host address:")
        host = stdscr.getstr(10, 38, 15)
        stdscr.clear()

        stdscr.addstr(10, 5, "Enter the database username:")
        username = stdscr.getstr(10, 38, 15)
        stdscr.clear()

        stdscr.addstr(10, 5, "Enter the database name:")
        database = stdscr.getstr(10, 38, 15)
        stdscr.clear()

        stdscr.addstr(10, 5, "Enter the database password:")
        password = stdscr.getstr(10, 38, 15)
        stdscr.clear()

    return username, host, database, password


def printMainMenu(stdscr):
    x = 0
    while x != ord('5'):

        stdscr.clear()
        stdscr.border(0)
    
        # Print main menu header information
        stdscr.addstr(1, 2, "HOST IP:")
    #TODO:  <------- INSERT CODE HERE FOR OBTAINING IP--------------->
        stdscr.addstr(1, 60, "XXX.XXX.XXX.XXX")
        stdscr.addstr(2, 2, "DB USER:")
    #TODO:  <------- INSERT CODE HERE FOR OBTAINING USER NAME--------------->
        stdscr.addstr(2, 60, "NAME_HERE")
        stdscr.addstr(3, 2, "DATABASE NAME:")
    #TODO:  <------- INSERT CODE HERE FOR OBTAINING DATABASE--------------->
        stdscr.addstr(3, 60, "DATABASE_NAME")

        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 30, "-- MAIN MENU --")

        # Print main menu options
        stdscr.addstr(9, 6, "[1]  View / Edit / Search Table")
        stdscr.addstr(11, 6, "[2]  Create Table")
        stdscr.addstr(13, 6, "[3]  Delete Table")
        stdscr.addstr(15, 6, "[4]  About")
        stdscr.addstr(17, 6, "[5]  Log Off / Exit")
        stdscr.refresh()

        # Collect user's navigation selection
        x = stdscr.getch()

        # Navigate to submenu
        if x == ord('1'):
            printViewEditSearchSubmenu(stdscr)

        if x == ord('2'):
            curses.endwin()

        if x == ord('3'):
            curses.endwin()

        if x == ord('4'):
            printAboutSubmenu(stdscr)

    #    if x == ord('5'):
    curses.endwin()

# TODO: need to refactor with hightlight selection


def printViewEditSearchSubmenu(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 20, "-- VIEW / EDIT / SEARCH SUBMENU --")
    stdscr.addstr(9, 6, "[1] View Table")
    stdscr.addstr(11, 6, "[2] Edit Table")
    stdscr.addstr(13, 6, "[3] Search Table")
    stdscr.addstr(15, 6, "[4] Back to Main Menu")
 
    # Collect user's navigation selection
    x = stdscr.getch()

    # Navigate to submenu
    if x == ord('1'):
        printViewTableSubmenu(stdscr)

    if x == ord('2'):
        printEditTableSubmenu(stdscr)

    if x == ord('3'):
        printSearchTableSubmenu(stdscr)

    if x == ord('4'):
        printMainMenu(stdscr)

# TODO: need to refactor with hightlight selection


def printViewTableSubmenu(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- VIEW TABLE --")
    
    # Loop list of tables and print to screen
    i = 0
    y = 9
    x = 6
    for i in range(5):
        menu_string = "[%s] tablename" % (i)
        stdscr.addstr(y, x, menu_string)
        y += 2

# TODO: need to rewrite for loop with actual table names
    
    stdscr.addstr(22, 45, "[B] Back")
    # Collect user's navigation selection
    x = stdscr.getch()

    # Navigate to submenu
    if x == ord('b') or x == ord('B'):
       printViewEditSearchSubmenu(stdscr)

# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented


def printEditTableSubmenu(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- EDIT TABLE --")
    
    # Loop list of tables and print to screen
    i = 0
    y = 9
    x = 6
    for i in range(5):
        menu_string = "[%s] tablename" % (i)
        stdscr.addstr(y, x, menu_string)
        y += 2

# TODO: need to rewrite for loop with actual table names

    stdscr.addstr(22, 45, "[B] Back")
    # Collect user's navigation selection
    x = stdscr.getch()

    # Navigate to submenu
    if x == ord('b') or x == ord('B'):
       printViewEditSearchSubmenu(stdscr) 
    
# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented


def printSearchTableSubmenu(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 28, "-- SEARCH TABLE --")
    
    # Loop list of tables and print to screen
    i = 0
    y = 9
    x = 6
    for i in range(5):
        menu_string = "[%s] tablename" % (i)
        stdscr.addstr(y, x, menu_string)
        y += 2

# TODO: need to rewrite for loop with actual table names

    stdscr.addstr(22, 45, "[B] Back")
    # Collect user's navigation selection
    x = stdscr.getch()

    # Navigate to submenu
    if x == ord('b') or x == ord('B'):
       printViewEditSearchSubmenu(stdscr) 
    
# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented


def printCreateTableSubmenu(stdscr):
# TODO: need to write
    x = 0


def printDeleteTableSubmenu(stdscr):
# TODO: need to write
    x = 0


def printAboutSubmenu(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- ABOUT --")
    string_line1 = "This program has been written by authors Nick Mastrokalos, Bryan Bauer,"
    string_line2 = "and Darnel Clayton for Fall 2015 CS419's final software project."
    stdscr.addstr(8, 4, string_line1)
    stdscr.addstr(9, 4, string_line2)


    stdscr.addstr(22, 32, "[B] Back")
    # Collect user's navigation selection
    x = stdscr.getch()

    # Navigate to submenu
    if x == ord('b') or x == ord('B'):
       printMainMenu(stdscr) 

# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented 


def printLogOffSubMenu(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(12, 24, "LOGGING OFF...")
    time.sleep(5)
# TODO: log off of database
    curses.endwin()    
