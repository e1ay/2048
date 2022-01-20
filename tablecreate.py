import sqlite3


bd = sqlite3.connect('database.sqlite')
cur = bd.cursor()
cur.execute("""
SELECT name gamer, max(score) score from RECORDS
GROUP by name
ORDER by score DESC
limit 3
""")
result = cur.fetchall()
print(result)
cur.close()