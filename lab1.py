import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import os
import logging

def debug_config():
    logging.basicConfig(level=logging.INFO, format = "[Movies]:%(asctime)s:%(levelname)s:%(messages)s")

def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        logging.debug("{a} found and not zero sieze".format(a=dbfile))
    else:
        logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB connected".format())
    return con

def db_cursor(con):    
    cur = con.cursor()    
    logging.debug("Cursor set".format())    
    return cur

def db_runquery(cur,query):
    cur.execute(query)
    result = cur.fetchall()
    logging.debug("DB Query executed and returned".format())
    return result

def print_years(res):
    plt.hist(res, bins=40)
    plt.ylabel('Number of Movies')
    plt.xlabel('Year Released')
    plt.locator_params(axis='y', integer=True)
    plt.title('COMP662 Movie Database')
    plt.show()


def main():
    # Declare database file name 
    dbfile = 'dbmovies.sqlite'
    # Declare program name
    programname = "My Movie Database"
    debug_config()

    print(programname)
    db_checkfile(dbfile)
    try:
        con = db_connect(dbfile)
        cur = con.cursor()
        allyears = []
        query = 'SELECT year from Movie'
        res = db_runquery(cur, query )
        for result in res:
            allyears.append(result[0])
    
        print_years(allyears)
    except sqlite3.Error as error:
        logging.error("Error executing query", error)
    finally:
        if con:
            con.close()
            logging.debug("[info] db Closed".format())
    print('Done - check completed')
    logging.info("Completed")

if __name__ == "__main__":
    main()

