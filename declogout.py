#!/usr/bin/python3

import sqlite3;
import os;

сonn = sqlite3.connect('/tmp/leftpart')
c = conn.cursor()

# delete NUM info from table
disp = os.environ["$NUM"]
cur.execute("DELETE FROM leftpart(Display) WHERE disp")

# delete USER info from table
usr = os.environ["$USER"]
cur.execute("DELETE FROM leftpart(USER) WHERE usr")

conn.close()