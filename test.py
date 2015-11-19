#!/usr/bin/env python

import database_queries
from os import system
import curses

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def login():
	system("clear")
	INPUT = False
	VERBOSE = True
	if INPUT: # If set to True, variables collected here
  		username = get_param("Enter the Username")
  		database = get_param("Enter the Database")
  		password = get_param("Enter the Password")
  		addy = get_param("Enter a host address: ")
		curses.endwin()

        else:
  		username = 'root' 
  		database = 'TestDC'
  		password = 'password'
  		addy = '192.168.1.181'
  		print 'Username:\t' + username
  		print 'Database:\t' + database
  		print 'Password:\t' + password
  		print 'Address:\t' + addy
  		print '\n'
		wait = raw_input("Press [ENTER] to login in with Default credentials.")
	
	screen.refresh()
	print '\n--------------------------------------------'
	print 'Create Connection with Database'
	print '--------------------------------------------'
	print 'Attempting to connect...',
	con = database_queries.dbConnect(username, password, database, addy) # Attempt connection and save session

	if con['state'] == 0: # If connection flag is set - good!
  		print 'Connected!',
		return True
	elif con['state'] == 1: # If connection flag is not set - fail!
  		print 'Failed',
		return False
	if VERBOSE: # If set prints the failure message received in initial call to connect
  		#print '[' + con['msg'] + ']'
		print "\nI am HERE"
		print '\n'
	wait = raw_input("Press [ENTER]")

def logout():
	system("clear")
	print 'Attempt to disconnect...',
	'''
	con = database_queries.dbClose(con) # Attempt to close connection

	if con['state'] == 1: # Detect if connection state is closed
  		print 'You have been logged out!',
	elif con['state'] == 0: # Connection still exists (or atleast the state indicates that!)
  		print 'Log Out Failed',

	if VERBOSE:
  		print '[' + con['msg'] + ']' # Print associated debug message 
	print '\n'
	'''
	wait = raw_input("Press [ENTER]")

def execute_cmd(cmd_string):
	system("clear")
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Command executed correctly"
	else:
		print "Command terminated with error"
	raw_input("Press enter")
	print ""

def display(self):
	self.panel.top()
	self.panel.show()
	self.window.clear()

        while True:                                                          
		self.window.refresh()                                            
            	curses.doupdate()                                                
            	for index, item in enumerate(self.items):                        
                	if index == self.position:                                   
                    		mode = curses.A_REVERSE                                  
                	else:                                                        
                    		mode = curses.A_NORMAL                                   

                	msg = '%d. %s' % (index, item[0])                            
                	self.window.addstr(1+index, 1, msg, mode)                    

            	key = self.window.getch()                                        

            	if key in [curses.KEY_ENTER, ord('\n')]:                         
                	if self.position == len(self.items)-1:                       
                    		break                                                    
                	else:                                                        
                    		self.items[self.position][1]()                           

            	elif key == curses.KEY_UP:                                       
                	self.navigate(-1)                                            

            	elif key == curses.KEY_DOWN:                                     
                	self.navigate(1)                                             

        self.window.clear()                                                  
        self.panel.hide()                                                    
        panel.update_panels()                                                
        curses.doupdate()

def submenu():
	x=0
	while x != ord('4'):
        	screen = curses.initscr()

		screen.clear()
        	screen.border(0)
        	screen.addstr(2, 2, "Submenu...")
        	screen.addstr(3, 2, "Please enter a number...")
        	screen.addstr(4, 4, "1 - Create New Table")
        	screen.addstr(5, 4, "2 - Delete Table")
	        screen.addstr(6, 4, "3 - Query Table")
        	screen.addstr(7, 4, "4 - Exit")
        	screen.refresh()

        	x = screen.getch()

x = 0

while x != ord('4'):
	screen = curses.initscr()

	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Main Menu...")
	screen.addstr(3, 2, "Please enter a number...")
	screen.addstr(4, 4, "1 - Log In")
	screen.addstr(5, 4, "2 - Submenu TO BE MOVED")
	screen.addstr(6, 4, "3 - Log Out")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
		curses.endwin()
		login()
		#curses.endwin()
		#system("clear")
		raw_input("Press enter")
		print ""

	if x == ord('2'):
                curses.endwin()
                submenu()
                curses.endwin()
                system("clear")
                print ""
	if x == ord('3'):
                curses.endwin()
                logout()
                curses.endwin()
                system("clear")
'''
		curses.endwin()
		execute_cmd()
'''
curses.endwin()

