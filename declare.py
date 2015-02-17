#!/usr/bin/python3

import sqlite3;
import os;

#insert NUM info to table
disp = os.environ["$NUM"]
cur.execute("INSERT INTO leftpart(Display) VALUES %s" % disp)

# insert USER info to table
usr = os.environ["$USER"]
cur.execute("INSERT INTO leftpart(USER) VALUES %s" % usr)
