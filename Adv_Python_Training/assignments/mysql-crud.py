import mysql.connector


class MySQLCRUD:
    db = None
    cursor = None
    dictionary_errorMesseges = {
        'ERROR_CONNECTION': "Unable to connect to database please check credentials and connection",
        'ERROR_CLOSING_CONNECTION': "Unable to close connection",
        'ERROR_INSERT_ERROR': "Unable to insert",
        'ERROR_WRONG_DATA': "Provided data is wrong",
        'ERROR_UNABLE_TO_EXECUTE': "Unable to execute query"
    }

    def __init__(self, hostName='localhost', dbUserName='root', dbPassword='', dbName=''):
        try:
            if dbName != '':
                self.db = mysql.connector.connect(
                    host=hostName,
                    user=dbUserName,
                    passwd=dbPassword,
                    database=dbName
                )
            else:
                self.db = mysql.connector.connect(
                    host=hostName,
                    user=dbUserName,
                    passwd=dbPassword
                )
            self.cursor = self.db.cursor()
        except:
            print(self.dictionary_errorMesseges['ERROR_CONNECTION'])

    def execute(self, query=''):
        if query != '':
            try:
                self.cursor.execute(query)
                return myresult
            except:
                print(self.dictionary_errorMesseges['ERROR_UNABLE_TO_EXECUTE'])
                return None
        else:
            print(self.dictionary_errorMesseges['ERROR_WRONG_DATA'])
            return None

    def close(self):
        try:
            self.MySqlDB.close()
        except:
            print(self.dictionary_errorMesseges['ERROR_CLOSING_CONNECTION'])

    def insert(self, tableName='', coloumnName=None, values=None):
        if tableName == '' or coloumnName == None or values == None:
            print(self.dictionary_errorMesseges['ERROR_WRONG_DATA'])
            return None
        elif len(coloumnName) != len(values):
            print(self.dictionary_errorMesseges['ERROR_WRONG_DATA'])
            return None
        else:
            try:
                escappedString = ''
                for value in values:
                    escappedString += '%s,'

                escappedString = escappedString[0, (len(escappedString)-1), 1]
                query = "INSERT INTO "+tableName + \
                    " (" + (",".join(coloumnName))+") " + \
                    "VALUES ("+escappedString+")"
                print(query)
                valuesTouple = tuple(values)
                self.cursor.execute(query, valuesTouple)
                self.db.commit()
                return True
            except:
                print(self.dictionary_errorMesseges['ERROR_INSERT_ERROR'])
                return False

    def fetch(self, tableName, coloumnsName):
        pass

    def fetchQuery(self, query=''):
        if query == '':
            print(self.dictionary_errorMesseges['ERROR_WRONG_DATA'])
            return None
        else:
            try:
                self.cursor.execute(query)
                myresult = self.cursor.fetchall()
                return myresult
            except:
                print(self.dictionary_errorMesseges['ERROR_UNABLE_TO_EXECUTE'])
                return None
