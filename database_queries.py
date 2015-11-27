import mysql.connector
from mysql.connector import errorcode


# ---------------------------------------------------------
# NAME:       dbConnect(...)
# RETURN:     returns a dict with a successful db connection,
#             connection state, and connection message.
#               cnx['con']
#               cnx['state']
#               cnx['msg']
# PARAMETERS: username, password, database, addy of db host 
#             machine
# ---------------------------------------------------------
def dbConnect(username, password, database, addy):
  
  # dict will store session and state
  cnx = {
    'con' : 'None',
    'state' : 'None', # 1-no connection, 2-connection
    'user' : username,
    'password' : password,
    'host' : addy,
    'database' : database,
    'msg' : 'None' }

  # variables required for connection
  config = {
    'user': username,
    'password': password,
    'database': database,
    'host': addy,
    'raise_on_warnings': True }

  # attempt connection
  try:
    cnx['con'] = mysql.connector.connect(**config)
    cnx['state'] = 0
    cnx['msg'] = 'Connected to database'

  # catch connection failures and return
  except mysql.connector.Error as err:
    cnx['state'] = 1    
    cnx['con'] = None
    
    # bad username or password
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      cnx['msg'] = 'Username or Password invalid'
      return cnx

    # database doesn't exist or bad name
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      cnx['msg'] = 'Database does not exist'
      return cnx
    
    # undisclosed error
    else:
      cnx['msg'] = "Cannot connect to host address"
      return cnx 

  # return a successful connection
  else:
    return cnx


# ---------------------------------------------------------
# NAME:       dbClose(...)
# RETURN:     returns a dict with a closed db connection,
#             connection state, and connection message.
#               cnx['con']
#               cnx['state'] = 1
#               cnx['msg']
# PARAMETERS: a dict with an active db connection and state
#               cnx['con']
#               cnx['state'] = 0
#               cnx['msg']
# ---------------------------------------------------------
def dbClose(cnx):
  # connection exists; terminate
  if cnx['state'] == 0:
    cnx['con'].close()
    cnx['state'] = 1
    cnx['msg'] = 'Connection terminated'
    return cnx
  
  # no connection to terminate; save message
  else:
    cnx['msg'] = 'No connection with database to close'
    return cnx


# ---------------------------------------------------------
# NAME:       dbTables(...)   
# RETURN:     returns a dict with a ['tables'] property that
#             includes tuples for each table in the db  
#               cnx['con']
#               cnx['state']
#               cnx['msg']
#               cnx['tables'] 
# PARAMETERS: a dict with an active db connection and state
#               cnx['con']
#               cnx['state']
#               cnx['msg']
# ---------------------------------------------------------
def dbTables(cnx):
  # check for active connection
  if cnx['state'] == 0:

    try:
      # create table query
      query = ('SHOW TABLES')
      cursor = cnx['con'].cursor()
      cursor.execute(query)
      cnx['tables'] = cursor.fetchall()
      
      # update query msg
      cnx['msg'] = 'Tables retreived'
      cnx['tbl_cnt'] = len(cnx['tables'])
      cursor.close()
      return cnx

    except mysql.connector.Error as err:
      cnx['msg'] = err
      return cnx

  # no active connection - query aborted
  else:
    cnx['msg'] = 'No database connection'
    return cnx




# ---------------------------------------------------------
# NAME:       dbQuery(...)
# RETURN:     returns a message of success/failure and in the
#             case of SELECT, returns values as a dict
#               cnx['con']
#               cnx['state']
#               cnx['msg']
#               cnx['rows'] //SELECT only
#               cnx['row_cnt'] //SELECT only
# PARAMETERS: A string that is a valid SQL query and a dict
#             with a connection to the database.
#               cnx['con']
#               cnx['state']
#               cnx['msg']
# ---------------------------------------------------------
def dbQuery(cnx, queryString):
  
  # make sure it's a string
  query = str(queryString) 

  # determine type of query using first word
  try: 
    split_query = query.split()
    query_selection = split_query[0]
    query_selection_upper = query_selection.upper()

  except: # ensures that blank entries are caught (or strings that can't be split)
    cnx['msg'] = 'Failed query'
    return cnx

  # prepare connection cursor for request
  cursor = cnx['con'].cursor(dictionary=True)

  # SELECT query
  if query_selection_upper == 'SELECT':
    try:
      cursor.execute(query)
      cnx['rows'] = cursor.fetchall()
      cnx['msg'] = 'Successful SELECT submitted'
      cnx['row_cnt'] = len(cnx['rows'])
      cursor.close()
      return cnx

    except mysql.connector.Error as e:
      cnx['msg'] = 'Failed SELECT query'
      cursor.close()
      return cnx

  # DELETE query
  elif query_selection_upper == 'DELETE':
     try:
      cursor.execute(query)
      cnx['msg'] = 'Successful DELETE query submitted'
      cnx['con'].commit()
      cursor.close()
      return cnx

     except mysql.connector.Error as e:
      cursor.close()
      cnx['msg'] = 'Failed DELETE query'
      return cnx

  # INSERT query
  elif query_selection_upper == 'INSERT':
     try:
      cursor.execute(query)
      cnx['msg'] = 'Successful INSERT query submitted'
      cnx['con'].commit()
      cursor.close()
      return cnx

     except mysql.connector.Error as e:
      cursor.close()
      cnx['msg'] = 'Failed INSERT query'
      return cnx  


  # other query type
  else:
    cursor.close()
    cnx['msg'] = 'Query selected ' + query_selection_upper + ' is not SELECT/DELETE/INSERT'
    return cnx
