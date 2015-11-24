#!/usr/bin/env python2                                                       
import curses                                                                
from curses import panel 
from os import system                                                    


def get_param(prompt_string):
	screen = curses.initscr()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input
	
def login():
screen = curses.initscr()
	system("clear")
	INPUT = True
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
	
class Menu(object):                                                          

    def __init__(self, items, stdscreen):                                    
        self.window = stdscreen.subwin(0,0)                                  
        self.window.keypad(1)                                                
        self.panel = panel.new_panel(self.window)                            
        self.panel.hide()
        panel.update_panels() 
			
        self.position = 0                                                    
        self.items = items                                                                                     

    def navigate(self, n):                                                   
        self.position += n                                                   
        if self.position < 0:                                                
            self.position = 0                                                
        elif self.position >= len(self.items):                               
            self.position = len(self.items)-1                                

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

class MyApp(object):                                                         
    def __init__(self, stdscreen):                                           
        self.screen = stdscreen                                              
        curses.curs_set(0)                                                   

        submenu_items = [                                                    
                ('beep', curses.beep),                                       
                ('flash', curses.flash)
                ]                                                            
        submenu = Menu(submenu_items, self.screen)                           

        main_menu_items = [                                                  
                ('Log In', login() ),                                       
                ('Log Out',logout() ),                                     
                ('submenu', submenu.display),
				('Exit', curses.endwin())
                ]                                                            
        main_menu = Menu(main_menu_items, self.screen)                       
        main_menu.display()                                                  

if __name__ == '__main__':                                                       
    curses.wrapper(MyApp)   

def login2():
	login()
