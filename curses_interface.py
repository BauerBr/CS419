#!/usr/bin/env python
import curses
import database_queries
from time import sleep

DEBUG = True # automate input vs. manual db connection info


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
    printMainMenu(self.screen,con)





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
        host = "localhost"
        password = "detachment"
        database = "employees"

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
        selection = -2
        option = 0
        while selection < 0:
            graphics = [0]*2
            graphics[option] = curses.A_REVERSE
            failure_string = "Connection to Database Failed: %s" % (con['msg'])
            stdscr.addstr(10, 5, failure_string)
            stdscr.addstr(13, 13, "Retry",graphics[0])
            stdscr.addstr(13, 35, "Exit Program",graphics[1])
            stdscr.refresh()
        # Collect user's navigation selection
            action = stdscr.getch()
            if action == curses.KEY_RIGHT:
                option = (option - 1) % 2
            elif action == curses.KEY_LEFT:
                option = (option + 1) % 2
            elif action == (ord('\n')):
                selection = option
            stdscr.clear()
        # If user wants to disconnect... Exit
            #if selection == 0:
                #add in retry statement
        # Return to main menu
            if selection == 1:
                curses.endwin()
                exit()
  # Return successful connection
    return con




# ==================================================
# Name: printMainMenu(stdscr,con)
#
# Purpose: Serves as the main menu of the application.
# accepts user input and navigates to submenus as
# directed. Submenus redirect to this menu as well.
# makes use of the con[] dictionary provided by
# databases_queries.py.
# ==================================================
def printMainMenu(stdscr,con):
    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.keypad(1)
    selection = -2
    option = 0
    # Print main menu options
    while selection < 0:
        stdscr.border(0)
        # Print main menu header information
        stdscr.addstr(1, 2, "HOST IP:")
        #stdscr.addstr(1, 60, con['host'])
        stdscr.addstr(2, 2, "DB USER:")
        #stdscr.addstr(2, 60, con['user'])
        stdscr.addstr(3, 2, "DATABASE NAME:")
        #stdscr.addstr(3, 60, con['database'])

        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 30, "-- MAIN MENU --")

        graphics = [0]*5
        graphics[option] = curses.A_REVERSE
        stdscr.addstr(9, 6, "View / Edit Table",graphics[0])
        stdscr.addstr(11, 6, "Create Table", graphics[1])
        stdscr.addstr(13, 6, "Delete Table",graphics[2])
        stdscr.addstr(15, 6, "About",graphics[3])
        stdscr.addstr(17, 6, "Log Off / Exit",graphics[4])
        stdscr.refresh()
    # Collect user's navigation selection
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 5
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 5
        elif action == (ord('\n')):
            selection = option
        stdscr.clear()

        # Navigate to submenu
        if selection == 0:
            printViewEditSubmenu(stdscr,con)
        # Navigate to CreateTable
        elif selection == 1:
            printCreateTableSubmenu(stdscr,con)
        # Navigate to DeleteTable
        elif selection == 2:
            printDeleteTableSubmenu(stdscr,con)
        # Navigate to About    
        elif selection == 3:
            printAboutSubmenu(stdscr,con)
        # Navigate to LogOff
        elif selection == 4:
            printLogOffSubMenu(stdscr,con)


    # Navigate to submenu
    # if user_input == ord('1'):
       # printViewEditSubmenu(stdscr,con)
	
    # if user_input == ord('2'):
        # printCreateTableSubmenu(stdscr,con)

    # if user_input == ord('3'):
        # printDeleteTableSubmenu(stdscr,con)

    # if user_input == ord('4'):
        # printAboutSubmenu(stdscr,con)

    # if user_input == ord('5'):
        # printLogOffSubMenu(stdscr,con)






# ==================================================
# Name: printViewEditSubmenu(stdscr,con)
#
# Purpose: This is the submenu that allows a user to 
# view, edit, or search an existing table in the db
# that has been connected to. user can also return
# to the main menu.
# ==================================================
def printViewEditSubmenu(stdscr,con):
    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.keypad(1)
    selection = -2
    option = 0
    # Print View Edit options
    while selection < 0:
        graphics = [0]*5
        graphics[option] = curses.A_REVERSE
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 20, "-- VIEW / EDIT TABLE --")
        stdscr.addstr(9, 6, "View Table",graphics[0])
        stdscr.addstr(11, 6, "Edit Table",graphics[1])
        stdscr.addstr(13, 6, "Back to Main Menu",graphics[2])
        

        stdscr.refresh()
         # Collect user's navigation selection
        action = stdscr.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 3
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 3
        elif action == (ord('\n')):
            selection = option
        stdscr.clear()

        # Navigate to submenu
        if selection == 0:
            printViewTableSubmenu(stdscr,con)
        # Navigate to CreateTable
        elif selection == 1:
            printEditTableSubmenu(stdscr,con)
        # Navigate to DeleteTable
        elif selection == 2:
            printMainMenu(stdscr,con)

        # if user_input == ord('1'):
        #     printViewTableSubmenu(stdscr,con)

        # if user_input == ord('2'):
        #     printEditTableSubmenu(stdscr,con)

        # if user_input == ord('3'):
        #     printMainMenu(stdscr,con)





# ==================================================
# Name: printViewTableSubmenu(stdscr,con)
#
# Purpose: Menu for viewing tables in the database.
# returns all tables in a column format. Tables,
# that exceed screen space will be provided in add'l
# spaces.
# ==================================================
def printViewTableSubmenu(stdscr,con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- VIEW TABLE --")
    stdscr.addstr(22, 45, "[B] Back")

    # Attempt to get tables in database so that they can be printed
    con = database_queries.dbTables(con) 

    # Detect if no tables exist
    if con['tbl_cnt'] == 0:
        stdscr.addstr(9, 6, "No tables in database")
        
        # Collect user's navigation selection
        user_input = stdscr.getch()
        
#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

        # Navigate to submenu
        if user_input == ord('b') or user_input == ord('B'):
            printViewEditSubmenu(stdscr,con)

        # TODO: need to refactor with hightlight selection
        curses.endwin() # can erase once highlight is implemented
        exit()

    # At least 1 table exists so print them
    else:
        y = 8
        x = 6 
        # Print out each table name line by line up to 6 per screen
        for idx, table in enumerate(con['tables']): 
            table_string = "[" + str(idx + 1) + "] " + table[0]
            stdscr.addstr(y, x, table_string)    
            y += 2

            # Detect the last row that can fit on a page (6th)
            if idx != 0 and idx % 5 == 0:
                
                # Detect if there are add'l rows past multiple of 6th
                if (idx + 1) < con['tbl_cnt']:
                    stdscr.addstr(22, 15, "[N] Next")
                
                #Collect user's navigation selection
                user_input = stdscr.getch()

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

                # Navigate to submenu
                if user_input == ord('b') or user_input == ord('B'):
                    printViewEditSubmenu(stdscr,con)

                # Paginate
                elif user_input == ord('n') or user_input == ord('N'):
                    stdscr.clear()
                    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
                    stdscr.addstr(6, 30, "-- VIEW TABLE --")
                    stdscr.addstr(22, 45, "[B] Back")
                    y = 8
                    x = 6

                # Navigate to view table
                elif user_input >= ord('1') and user_input <= unichr(con['tbl_cnt']):
                    printViewTableContentsSubmenu(stdscr, con, int(chr(user_input)) - 1)

        # Collect user's navigation selection
        user_input = stdscr.getch()

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

        # Navigate to submenu
        if user_input == ord('b') or user_input == ord('B'):
            printViewEditSubmenu(stdscr,con)

        # Navigate to view table
        elif user_input >= ord('1') and user_input <= unichr(con['tbl_cnt']):
            printViewTableContentsSubmenu(stdscr, con, int(chr(user_input)) - 1)



# ==================================================
# Name: printViewTableContentsSubmenu(stdscr, con, idx)
#
# Purpose: displays a table's contents upon selection
# from the table select menu. rows will paginate in
# instances that each row exceeds the rows allowed on
# the screen. idx is the table desired in con['tables'].
# ==================================================
def printViewTableContentsSubmenu(stdscr, con, idx):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- VIEW TABLE --")
    stdscr.addstr(22, 45, "[B] Back")    
    
    # Create the query string to retrieve the contents of the selected table
    table_string = "SELECT * FROM " + str(con['tables'][idx][0])

    # Conduct SELECT query; results in con['rows']
    con = database_queries.dbQuery(con, table_string)

#---------------------------------------------------------------------
# TODO: NEED TO REDO FOR LOOP TO PRINT OUT ROWS WITH LINES AND COLUMNS
#---------------------------------------------------------------------
    y = 8
    x = 6 
    # Print out each row line by line up to 6 per screen
    for idx, row in enumerate(con['rows']):
        row_string = "[" + str(idx + 1) + "] " + str(row)
        stdscr.addstr(y, x, row_string)    
        y += 2

        # Detect the last row that can fit on a page (6th)
        if idx != 0 and idx % 5 == 0:
            
            # Detect if there are add'l rows past multiple of 6th
            if (idx + 1) < con['row_cnt']:
                stdscr.addstr(22, 15, "[N] Next")
            
            #Collect user's navigation selection
            user_input = stdscr.getch()

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

            # Navigate to submenu
            if user_input == ord('b') or user_input == ord('B'):
                printViewEditSubmenu(stdscr,con)

            # Paginate
            elif user_input == ord('n') or user_input == ord('N'):
                stdscr.clear()
                stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
                stdscr.addstr(6, 30, "-- VIEW TABLE --")
                stdscr.addstr(22, 45, "[B] Back")
                y = 8
                x = 6

    # Collect user's navigation selection
    user_input = stdscr.getch()

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

    # Navigate to submenu
    if user_input == ord('b') or user_input == ord('B'):
        printViewEditSubmenu(stdscr,con)

    



# ==================================================
# Name: printEditTableSubmenu(stdscr,con)
#
# Purpose: Provides a list of tables that can be
# edited. User will select a table for editing, or
# can return to the next higher submenu.
# ==================================================
def printEditTableSubmenu(stdscr,con):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 30, "-- EDIT TABLE --")
    stdscr.addstr(22, 45, "[B] Back")

    # Attempt to get tables in database so that they can be printed
    con = database_queries.dbTables(con) 

    # Detect if no tables exist
    if con['tbl_cnt'] == 0:
        stdscr.addstr(9, 6, "No tables in database")
        
        # Collect user's navigation selection
        user_input = stdscr.getch()

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------
        
        # Navigate to submenu
        if user_input == ord('b') or user_input == ord('B'):
            printViewEditSubmenu(stdscr,con)

        # TODO: need to refactor with hightlight selection
        curses.endwin() # can erase once highlight is implemented
        exit()

    # At least 1 table exists so print them
    else:
        y = 8
        x = 6 
        # Print out each table name line by line up to 6 per screen
        for idx, table in enumerate(con['tables']): 
            table_string = "[" + str(idx + 1) + "] " + table[0]
            stdscr.addstr(y, x, table_string)    
            y += 2

            # Detect the last row that can fit on a page (6th)
            if idx != 0 and idx % 5 == 0:
                
                # Detect if there are add'l rows past multiple of 6th
                if (idx + 1) < con['tbl_cnt']:
                    stdscr.addstr(22, 15, "[N] Next")
                
                #Collect user's navigation selection
                user_input = stdscr.getch()

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

                # Navigate to submenu
                if user_input == ord('b') or user_input == ord('B'):
                    printViewEditSubmenu(stdscr,con)

                # Paginate
                elif user_input == ord('n') or user_input == ord('N'):
                    stdscr.clear()
                    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
                    stdscr.addstr(6, 30, "-- EDIT TABLE --")
                    stdscr.addstr(22, 45, "[B] Back")
                    y = 8
                    x = 6

                # Navigate to view table
                elif user_input >= ord('1') and user_input <= unichr(con['tbl_cnt']):
                    printEditTableContentsSubmenu(stdscr, con, int(chr(user_input)) - 1)

                
        # Collect user's navigation selection
        user_input = stdscr.getch()
        
#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

        # Navigate to submenu
        if user_input == ord('b') or user_input == ord('B'):
            printViewEditSubmenu(stdscr,con)

        # Navigate to view table
        elif user_input >= ord('1') and user_input <= unichr(con['tbl_cnt']):
            printEditTableContentsSubmenu(stdscr, con, int(chr(user_input)) - 1)




# ==================================================
# Name: printEditTableContentsSubmenu(stdscr, con, idx)
#
# Purpose: provides an interface for users to enter
# edit queries for the desired table.
#
# NOTE: current functionality will allow any form of 
# SELECT, INSERT, or DELETE query.
#
# ==================================================
def printEditTableContentsSubmenu(stdscr, con, idx):
    stdscr.clear()
    stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
    stdscr.addstr(6, 28, "-- EDIT TABLE --")

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
    
#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

    # Attempt to submit query
    database_queries.dbQuery(con, user_input)

    # Edit query success; return to main menu
    if queryCheck(con) == 1:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- EDIT TABLE --")
        stdscr.addstr(10, 5, "Query Success! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr,con)

    # Edit query failure; return to main menu
    else:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- EDIT TABLE --")
        stdscr.addstr(10, 5, "Query Failure! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printEditTableSubmenu(stdscr,con)





# ==================================================
# Name: printCreateTableSubmenu(stdscr,con)
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
def printCreateTableSubmenu(stdscr,con):
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

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

    # Attempt to submit query
    database_queries.dbQuery(con, user_input)

    # create query success; return to main menu
    if queryCheck(con) == 1:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- CREATE TABLE --")
        stdscr.addstr(10, 5, "Query Success! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr,con)

    # create query failure; return to main menu
    else:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- CREATE TABLE --")
        stdscr.addstr(10, 5, "Query Failure! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr,con)




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
# Name: printDeleteTableSubmenu(stdscr,con)
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
def printDeleteTableSubmenu(stdscr,con):
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

#---------------------------------------------------------------------
# TODO: NEED TO REFACTOR WITH HIGHLIGHT
#---------------------------------------------------------------------

    # Attempt to submit query
    database_queries.dbQuery(con, user_input)

    # Delete query success; return to main menu
    if queryCheck(con) == 1:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- DELETE TABLE --")
        stdscr.addstr(10, 5, "Query Success! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr,con)

    # Delete query failure; return to main menu
    else:
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 28, "-- DELETE TABLE --")
        stdscr.addstr(10, 5, "Query Failure! Press Enter to Continue...")
        stdscr.getstr(1, 1, 0)
        printMainMenu(stdscr,con)




# ==================================================
# Name: printAboutSubmenu(stdscr,con)
#
# Purpose: accessed from the main menu, prints info
# about the program including version.
# ==================================================
def printAboutSubmenu(stdscr,con):

    stdscr.clear()
    selection = -2
    option = 0    
    while selection < 0:
        graphics = [0]*1
        graphics[option] = curses.A_REVERSE


        stdscr.refresh()
         # Collect user's navigation selection
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


        stdscr.addstr(22, 32, "Back",graphics[0])
        action = stdscr.getch()
        if action == (ord('\n')):
            selection = option
        stdscr.clear()

        # Navigate to submenu
        if selection == 0:
            printMainMenu(stdscr,con) 




# ==================================================
# Name: printLogOffSubMenu(stdscr,con)
#
# Purpose: accessed from the main menu, starts the
# process of logging off. After confirmation,
# disconnects from db and exits program. Otherwise,
# returns to the main menu.
# ==================================================
def printLogOffSubMenu(stdscr,con):
    selection = -2
    option = 0
    while selection < 0:
        graphics = [0]*2
        graphics[option] = curses.A_REVERSE

        stdscr.refresh()
        stdscr.clear()
        stdscr.addstr(4, 2, "----------------------------------------------------------------------------")
        stdscr.addstr(6, 30, "-- LOG OFF --")
        stdscr.addstr(10, 13, "Are you sure you'd like to log off?")
        stdscr.addstr(13, 13, "Log Off",graphics[0])
        stdscr.addstr(13, 35, "Return to Program",graphics[1])

    # Collect user's navigation selection
        action = stdscr.getch()
        if action == curses.KEY_RIGHT:
            option = (option - 1) % 2
        elif action == curses.KEY_LEFT:
            option = (option + 1) % 2
        elif action == (ord('\n')):
            selection = option
        stdscr.clear()
    # If user wants to disconnect... Exit
        if selection == 0:
            # Close connection with db and exit
            database_queries.dbClose(con)
            curses.endwin()
            exit()

    # Return to main menu
        if selection == 1:
            printMainMenu(stdscr,con)