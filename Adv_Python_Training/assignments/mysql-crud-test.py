import mysqlcrud

def main():
    sqlobj = mysqlcrud.MySQLCRUD('localhost', 'root', '', 'python-test-db-1')
    
    sqlobj.close()
    pass
main()
