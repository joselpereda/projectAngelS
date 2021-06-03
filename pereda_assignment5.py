### --------------------------------------------------------------------------------------
### C:\Users\jopered\AppData\Local\Programs\Python\Python39\python.exe
### Assignment 5 - Visualizing Data
### Author: Jose Pereda
### SDCE Student ID: 5696529
### Submission date: May 26, 2021
### --------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import os
import logging

from numpy.core.einsumfunc import _compute_size_by_dict

def debug_config():
    logging.basicConfig(level=logging.INFO, format = "%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

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

def print_higher_ed_degrees(yr,architect, compsci, engineering, foreignlan):
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(yr, architect, label='Architecture')           # Plot Architecture degrees data
    ax.plot(yr, compsci, label='Computer Science')    # Plot Computer Science degrees data
    ax.plot(yr, engineering, label='Engineering')             # Plot Engineering data
    ax.plot(yr, foreignlan, label='Foreign Languages')   # Plot Foreign Languages data
    ax.set_xlabel('Year')                                       # Add an x-label to the axes
    ax.set_ylabel('Degrees %')                                     # Add a y-label to the axes
    ax.set_title("% of Bachelor's Degrees for USA Women by Major (1970-2011)\nDegrees Over time")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()

# showing Angel a python program
def main():
    # Declare database file name 
    dbfile = 'degrees2.db'
    # Declare program name
    programname = "Bachelors Degrees for US Women by Major"
    debug_config()

    print(programname)
    db_checkfile(dbfile)
    try:
        con = db_connect(dbfile)
        cur = con.cursor()

        # Declare array variables for each degree type
        allyears = []
        architecture = []
        computerscience = []
        engineering = []
        foreignlanguage = []

        # query degreees.db for the degrees data of interest
        query = 'SELECT Year, Architecture, ComputerScience, Engineering, ForeignLanguages from degrees'
        res = db_runquery(cur, query)
        
        # Put queary results into array variables
        for result in res:
            allyears.append(result[0])
            architecture.append(result[1])
            computerscience.append(result[2])
            engineering.append(result[3])
            foreignlanguage.append(result[4])

        # Plot the results
        print_higher_ed_degrees(allyears, architecture, computerscience, engineering, foreignlanguage)

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
