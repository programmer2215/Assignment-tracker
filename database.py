import sqlite3

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

def create():
    cur.execute('DROP TABLE IF EXISTS Assignments')
    cur.execute('DROP TABLE IF EXISTS Lectures')
    cur.execute('''
CREATE TABLE Assignments(
    name text,
    subject text,
    due text,
    daysLeft integer);''')
    
    cur.execute('''
CREATE TABLE Lectures(
    subject text,
    day text,
    time text);''')


    conn.commit()




