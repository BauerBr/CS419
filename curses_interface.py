#!/usr/bin/env python                                                      

import curses
import database_queries
from time import sleep

DEBUG = True # automate input vs. manual input


# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
class MyApp(object):

  def __init__(self, stdscreen):
    
    # Init the main curses program
    self.screen = stdscreen

    curses.curs_set(0)
    curses.cbreak() 
    curses.echo()

    # Connect to database
    con = connectToDatabase(self.screen)

<<<<<<< HEAD
    # Menu starting point
    printMainMenu(self.screen, con)

=======
    # Collect db info (host ip, username, etc.)
    un, addy, db, pw = getConnectionInfo(self.screen)
    # un = "root"
    # addy = "192.168.1.181"
    # pw = "password"
    # db = "TestDC"
>>>>>>> 968c38cf256d8c46dfb3950278cb8abb680d6084


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

<<<<<<< HEAD

# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def connectToDatabase(stdscr):

  # Collect db data and validate connection
  while(1):

    # Clear the curses screen
    stdscr.clear()

    # Overwrite connection data in debug mode
    if DEBUG:
        
        username = "root"
        host = "localhost"
        password = "detachment"
        database = "myTestDB"

    else:

      # Collect necessary connection info
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

    # Attempt to connect with db
    con = database_queries.dbConnect(username, password, database, host) 

    # Connection successful
    if con['state'] == 0:

      # Inform user of connection      
      stdscr.addstr(10, 5, "Connection to Database Successful! Press Enter to Continue...")
      stdscr.getstr(1, 1, 0)
      break

    # Connection Failed
    else:

      # Inform user of connection failure & reason
      failure_string = "Connection to Database Failed: %s" % (con['msg'])
      stdscr.addstr(10, 5, failure_string)
      stdscr.addstr(13, 13, "[1] Retry")
      stdscr.addstr(13, 35, "[2] Exit Program")

      # Collect user's navigation selection
      x = stdscr.getch()

      # Exit program; otherwise collect info again
      if x == ord('2'):
          curses.endwin()
          exit()

  # Return successful connection
  return con




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printMainMenu(stdscr, con):
    stdscr.clear()
    stdscr.border(0)
    
    # Print main menu header information
    stdscr.addstr(1, 2, "HOST IP:")
    stdscr.addstr(1, 60, con['host'])
    stdscr.addstr(2, 2, "DB USER:")
    stdscr.addstr(2, 60, con['user'])
    stdscr.addstr(3, 2, "DATABASE NAME:")
    stdscr.addstr(3, 60, con['database'])
=======
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
>>>>>>> 968c38cf256d8c46dfb3950278cb8abb680d6084

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

<<<<<<< HEAD
    # Navigate to submenu
    if x == ord('1'):
        printViewEditSearchSubmenu(stdscr, con)
=======
        stdscr.addstr(10, 5, "Enter the database password:")
        password = stdscr.getstr(10, 38, 15)
        stdscr.clear()
>>>>>>> 968c38cf256d8c46dfb3950278cb8abb680d6084

    return username, host, database, password


<<<<<<< HEAD
    if x == ord('4'):
        printAboutSubmenu(stdscr, con)
=======
def printMainMenu(stdscr):
    x = 0
    while x != ord('5'):
>>>>>>> 968c38cf256d8c46dfb3950278cb8abb680d6084

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





# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printViewEditSearchSubmenu(stdscr, con):
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
        printViewTableSubmenu(stdscr, con)

    if x == ord('2'):
        printEditTableSubmenu(stdscr, con)

    if x == ord('3'):
        printSearchTableSubmenu(stdscr, con)

    if x == ord('4'):
        printMainMenu(stdscr, con)

# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printViewTableSubmenu(stdscr, con):
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
       printViewEditSearchSubmenu(stdscr, con)

# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printEditTableSubmenu(stdscr, con):
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
       printViewEditSearchSubmenu(stdscr, con) 
    
# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented





# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printSearchTableSubmenu(stdscr, con):
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
       printViewEditSearchSubmenu(stdscr, con) 
    
# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printCreateTableSubmenu(stdscr, con):
# TODO: need to write
    x = 0




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printDeleteTableSubmenu(stdscr, con):
# TODO: need to write
    x = 0




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printAboutSubmenu(stdscr, con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- ABOUT --")
    
    string_line0 = "curses_database_interface v1.0"
    string_line1 = "This program has been written by authors Nick Mastrokalos, Bryan Bauer,"
    string_line2 = "and Darnel Clayton for Fall 2015 CS419's final software project."
    stdscr.addstr(8, 4, "Version:")
    stdscr.addstr(9, 4, string_line0)
    stdscr.addstr(11, 4, "Notes:")
    stdscr.addstr(12, 4, string_line1)
    stdscr.addstr(13, 4, string_line2)


    stdscr.addstr(22, 32, "[B] Back")
    # Collect user's navigation selection
    x = stdscr.getch()

    # Navigate to submenu
    if x == ord('b') or x == ord('B'):
       printMainMenu(stdscr, con) 

# TODO: need to refactor with hightlight selection
    curses.endwin() # can erase once highlight is implemented 




# ==================================================
# Name: 
#
# Purpose: 
#
# ==================================================
def printLogOffSubMenu(stdscr, con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(12, 24, "LOGGING OFF...")
    time.sleep(5)
# TODO: log off of database
<<<<<<< HEAD
    curses.endwin()
=======
    curses.endwin()    
>>>>>>> 968c38cf256d8c46dfb3950278cb8abb680d6084
