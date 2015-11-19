import database_queries # Contains functions for interacting with a mysql database

INPUT = False # Allows you to select whether database configuration variables are hardcoded or entered in the console
VERBOSE = True # Prints additional debug statements on the success/failure of calls to the database_queries.py file


print '\n********************************************'
print 'TEST SCRIPT FOR DATABASE FUNCTIONS'
print '********************************************\n'

if INPUT: # If set to True, variables collected here
  print '--------------------------------------------'
  print 'Collect Variables Required for Connection...'
  print '--------------------------------------------'
  username = raw_input('Enter a username: ')
  database = raw_input('Enter a database: ')
  password = raw_input('Enter a password: ')
  addy = raw_input('Enter a host address: ')

else: # If set to False, variables are hardcoded here
  print '--------------------------------------------'
  print 'Variables Set for Connection'
  print '--------------------------------------------'
  username = 'root'
  database = 'TestDC'
  password = 'password'
  addy = '192.168.1.181'
  print 'Username:\t' + username
  print 'Database:\t' + database
  print 'Password:\t' + password
  print 'Address:\t' + addy
  print '\n'

print '\n--------------------------------------------'
print 'Create Connection with Database'
print '--------------------------------------------'
print 'Attempting to connect...',
con = database_queries.dbConnect(username, password, database, addy) # Attempt connection and save session

if con['state'] == 0: # If connection flag is set - good!
  print 'Connected!',
elif con['state'] == 1: # If connection flag is not set - fail!
  print 'Failed',

#if VERBOSE: # If set prints the failure message received in initial call to connect
  #print '[' + con['msg'] + ']'
print '\n'


print '\n--------------------------------------------'
print 'Get Tables from the Database'
print '--------------------------------------------'
print 'Attempt to query for table list...',
con = database_queries.dbTables(con) # Attempt to get tables in database

if con['msg'] == 'Tables retreived': # Check return msg for success
  print 'Passed!',
  
  if VERBOSE: # Print associated status message associated with call
    print '[' + con['msg'] + ']\n'

  for idx, table in enumerate(con['tables']): # Print out each table name line by line
    print 'Table ' + str(idx) + ': ' + table[0] + '\n'

else: # Call to retrieve table(s) must have failed. 
  print 'Failed',
  if VERBOSE:
    print '[' + con['msg'] + ']' # Print associated message related to call failure


print '\n--------------------------------------------'
print 'Send Query (SELECT/DELETE/INSERT) to the Database'
print '--------------------------------------------'
user_query = raw_input('Enter a proper SQL query: ') # Intended to collect a mysql query from the user
print '\nYou entered: ' + user_query + '\n\n'

# attempt to get tables in database
print 'Attempting to send query to the database...',
con = database_queries.dbQuery(con, user_query) # Attempt to get tables in database

response = con['msg'].split() # Parse response message to determine if query worked or not
if response[0] == 'Successful':
  print 'Passed!',

  if VERBOSE:
    print '[' + con['msg'] + ']' # Print associated success message

  if response[1] == 'SELECT': # Print rows of a table if SELECT was chosen
    # print each row
    print '\nROWS IN SELECT:'
    for idx,row in enumerate(con['rows']):
      print 'row ' + str(idx) + ': ' + str(row)
    # print row count of table
    print 'Row Count: ' + str(con['row_cnt']) # Print the number of rows in the SELECT call

else: # Query failed
  print 'Failed!', 

  if VERBOSE:
    print '[' + con['msg'] + ']' # Print asssociated failure message


print '\n--------------------------------------------'
print 'Close Connection with Database'
print '--------------------------------------------'
print 'Attempt to disconnect...',
con = database_queries.dbClose(con) # Attempt to close connection

if con['state'] == 1: # Detect if connection state is closed
  print 'Disconnected!',
elif con['state'] == 0: # Connection still exists (or atleast the state indicates that!)
  print 'Failed',

if VERBOSE:
  print '[' + con['msg'] + ']' # Print associated debug message 

print '\n'
