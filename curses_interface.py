#!/usr/bin/env python
import curses
import database_queries
from time import sleep

DEBUG = True # automate input vs. manual input


# ==================================================
# Name: MyApp(object)
#
# Purpose: Serves as the primary starting point of
# the application. creates an curses object, sets
# curses options, establishes connection with db,
# and directs user to db connect screen.
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

    # Menu starting point
    printMainMenu(self.screen, con)





# ==================================================
# Name: connectToDatabase(stdscr)
#
# Purpose: Collects db connection information from
# the user including host IP address, db name, db
# user, and password. validates success/failure of
# db connection and informs user. Upon completion,
# redirects to main menu.
# ==================================================
def connectToDatabase(stdscr):

  # Collect db data and validate connection
  while(1):

    # Clear the curses screen
    stdscr.clear()

    # Overwrite connection data in debug mode
    if DEBUG:
        username = "root"
        host = "192.168.1.181"
        password = "password"
        database = "TestDC"

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
# Name: printMainMenu(stdscr, con)
#
# Purpose: Serves as the main menu of the application.
# accepts user input and navigates to submenus as
# directed. Submenus redirect to this menu as well.
# makes use of the con[] dictionary provided by
# databases_queries.py.
# ==================================================
def printMainMenu(stdscr, con):
    x = 0
    while x != ord('5'):
        
        stdscr.clear()
        stdscr.border(0)
    
<<<<<<< HEAD
    # Print main menu header information
    stdscr.addstr(1, 2, "HOST IP:")
    stdscr.addstr(1, 60, con['host'])
    stdscr.addstr(2, 2, "DB USER:")
    stdscr.addstr(2, 60, con['user'])
    stdscr.addstr(3, 2, "DATABASE NAME:")
    stdscr.addstr(3, 60, con['database'])

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
        printViewEditSearchSubmenu(stdscr, con)

    if x == ord('2'):
        printCreateTableSubmenu(stdscr, con)

    if x == ord('3'):
        printDeleteTableSubmenu(stdscr, con)

    if x == ord('4'):
        printAboutSubmenu(stdscr, con)

    if x == ord('5'):
        printLogOffSubMenu(stdscr, con)
=======
        # Print main menu header information
        stdscr.addstr(1, 2, "HOST IP:")
        stdscr.addstr(1, 60, con['host'])
        stdscr.addstr(2, 2, "DB USER:")
        stdscr.addstr(2, 60, con['user'])
        stdscr.addstr(3, 2, "DATABASE NAME:")
        stdscr.addstr(3, 60, con['database'])

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
            printViewEditSearchSubmenu(stdscr, con)

        if x == ord('2'):
            curses.endwin()

        if x == ord('3'):
            curses.endwin()

        if x == ord('4'):
            printAboutSubmenu(stdscr, con)

        #if x == ord('5'):
    curses.endwin()
>>>>>>> ec793ca20c1c1a91ec991adf92ea6e0ff48e765b

# TODO: need to refactor with hightlight selection





# ==================================================
# Name: printViewEditSearchSubmenu(stdscr, con)
#
# Purpose: This is the submenu that allows a user to 
# view, edit, or search an existing table in the db
# that has been connected to. user can also return
# to the main menu.
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
    exit()




# ==================================================
# Name: printViewTableSubmenu(stdscr, con)
#
# Purpose: Menu for viewing tables in the database.
# returns all tables in a column format. Tables,
# that exceed screen space will be provided in add'l
# spaces.
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
    exit()




# ==================================================
# Name: printEditTableSubmenu(stdscr, con)
#
# Purpose: Provides a list of tables that can be
# edited. User will select a table for editing, or
# can return to the next higher submenu.
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
    exit()





# ==================================================
# Name: printSearchTableSubmenu(stdscr, con)
#
# Purpose: Provides a list of tables that can be
# searched. User will select a table for search, or
# can return to the next higher submenu.
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
    exit()




# ==================================================
# Name: printCreateTableSubmenu(stdscr, con)
#
# Purpose: Redirects from main menu to the create
# table menu. In current instantiation, user is
# provided with the ability to enter a "create"
# query which will be submitted to db. 
#
# NOTE: user can technically enter a select, insert,
# or delete query and, upon successful submission,
# it will work. 
# ==================================================
def printCreateTableSubmenu(stdscr, con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 28, "-- CREATE TABLE --")

    # Draw input table
    stdscr.addstr(8, 6, "Enter a sql statement:")
    stdscr.addstr(10, 5, "+")
    stdscr.addstr(10, 6, "--------------------------------------------------------------------")
    stdscr.addstr(10, 74, "+")
    stdscr.addstr(11, 5, "|")
    stdscr.addstr(12, 5, "|")
    stdscr.addstr(13, 5, "|")
    stdscr.addstr(11, 74, "|")
    stdscr.addstr(12, 74, "|")
    stdscr.addstr(13, 74, "|")
    stdscr.addstr(14, 5, "+")
    stdscr.addstr(14, 6, "--------------------------------------------------------------------")
    stdscr.addstr(14, 74, "+")

    # Collect user input
    user_input = stdscr.getstr(12, 7, 66)
    
    # Attempt to submit query
    database_queries.dbQuery(con, user_input)

    # create query success; return to main menu
    if queryCheck(con) == 1:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- CREATE TABLE --")
        stdscr.addstr(10, 5, "Query Success! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr, con)

    # create query failure; return to main menu
    else:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- CREATE TABLE --")
        stdscr.addstr(10, 5, "Query Failure! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr, con)




# ==================================================
# Name: queryCheck(con)
#
# Purpose: Verifies connection message and validates
# if query is success (return 1) or failure (return 0).
# ==================================================
def queryCheck(con):
    # Parse query message response
    response = con['msg'].split() 

    # Successful query
    if response[0] == 'Successful':
        return 1
    
    # Failed query
    else:
        return 0 




# ==================================================
# Name: printDeleteTableSubmenu(stdscr, con)
#
# Purpose: Redirects from main menu to the create
# table menu. In current instantiation, user is
# provided with the ability to enter a "Delete"
# query which will be submitted to db. 
#
# NOTE: user can technically enter a select, insert,
# or delete query and, upon successful submission,
# it will work. 
# ==================================================
def printDeleteTableSubmenu(stdscr, con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 28, "-- DELETE TABLE --")

    # Draw input table
    stdscr.addstr(8, 6, "Enter a sql statement:")
    stdscr.addstr(10, 5, "+")
    stdscr.addstr(10, 6, "--------------------------------------------------------------------")
    stdscr.addstr(10, 74, "+")
    stdscr.addstr(11, 5, "|")
    stdscr.addstr(12, 5, "|")
    stdscr.addstr(13, 5, "|")
    stdscr.addstr(11, 74, "|")
    stdscr.addstr(12, 74, "|")
    stdscr.addstr(13, 74, "|")
    stdscr.addstr(14, 5, "+")
    stdscr.addstr(14, 6, "--------------------------------------------------------------------")
    stdscr.addstr(14, 74, "+")

    # Collect user input
    user_input = stdscr.getstr(12, 7, 66)
    
    # Attempt to submit query
    database_queries.dbQuery(con, user_input)

    # Delete query success; return to main menu
    if queryCheck(con) == 1:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- DELETE TABLE --")
        stdscr.addstr(10, 5, "Query Success! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr, con)

    # Delete query failure; return to main menu
    else:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- DELETE TABLE --")
        stdscr.addstr(10, 5, "Query Failure! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr, con)




# ==================================================
# Name: printAboutSubmenu(stdscr, con)
#
# Purpose: accessed from the main menu, prints info
# about the program including version.
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
    exit()




# ==================================================
# Name: printLogOffSubMenu(stdscr, con)
#
# Purpose: accessed from the main menu, starts the
# process of logging off. After confirmation,
# disconnects from db and exits program. Otherwise,
# returns to the main menu.
# ==================================================
def printLogOffSubMenu(stdscr, con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- LOG OFF --")
    stdscr.addstr(10, 13, "Are you sure you'd like to log off?")
    stdscr.addstr(13, 13, "[1] Log Off")
    stdscr.addstr(13, 35, "[2] Return to Program")

    # Collect user's navigation selection
    x = stdscr.getch()

# TODO: need to refactor with hightlight selection

    # If user wants to disconnect... Exit
    if x == ord('1'):
        # Close connection with db and exit
        database_queries.dbClose(con)
        curses.endwin()
        exit()

    # Return to main menu
    if x == ord('2'):
        printMainMenu(stdscr, con)