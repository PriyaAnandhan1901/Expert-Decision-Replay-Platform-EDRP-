import sqlite3

conn = sqlite3.connect("edrp.db")
cur = conn.cursor()

def try_run(sql):
    try:
        cur.execute(sql)
        print("OK:", sql)
    except Exception as e:
        print("SKIPPED:", sql, "->", e)

try_run("ALTER TABLE decisions ADD COLUMN description VARCHAR;")
try_run("ALTER TABLE alternatives RENAME COLUMN title TO alternative_name;")
try_run("ALTER TABLE alternatives RENAME COLUMN feasibility_score TO feasibility;")
try_run("ALTER TABLE alternatives ADD COLUMN risk_level VARCHAR;")
try_run("ALTER TABLE alternatives ADD COLUMN updated_at DATETIME;")

conn.commit()
conn.close()
print("Done.")