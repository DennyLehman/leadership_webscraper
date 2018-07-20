# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:24:42 2018

@author: Denny.Lehman
"""

import psycopg2
class database:
    def __init__(self):
        self._username = 'username'
        self._password = 'password'
        self._port = '5439'
        self._host = 'host'
        self._dbname = 'db'
    
    def query(self, sql_statement):
        data = 'error occured'
        with psycopg2.connect(dbname=self._dbname,host=self._host,port=self._port, user=self._username, password=self._password ) as conn:
            cur = conn.cursor()
            print(sql_statement)
            cur.execute(sql_statement)
            data = cur.fetchall()
            # conn.close()
        try:
            conn.close()
        except:
            print('Already closed')
        
        return data
    
    def get_dbname(self):
        print(self._dbname)
    
    def get_hostname(self):
        print(self._hostname)
        
    def connection_info(self):
        print('Database connection info:',
                '\nhost: ', self._host, '\ndbname: ', self._dbname, '\nport: ', self._port, '\nusername: ', self._username, '\npassword: hidden')
        
        
import pandas as pd
if __name__ == '__main__':
    print('hello world')
    myDB = database()
    myDB.connection_info()
    sql = "SELECT TOP 10 * FROM public.finance_data_tape_vw;"
    d = myDB.query(sql)
    df = pd.DataFrame(myDB.query(sql))
    print(df.head())
    
        
    
        
        
