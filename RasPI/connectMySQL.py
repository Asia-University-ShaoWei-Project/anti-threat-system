import mysql.connector
from datetime import date


def connect_INSTER():
  try:
    db = mysql.connector.connect(
        host="localhost",
        user="user",
        passwd="password",
        database="date"
    )

    cur = db.cursor()
    sql = "INSERT INTO `date` (`date`, `time`) VALUE (%s, %s)"
    today = date.today()
    val = (today.strftime('%Y/%m/%d'), today.strftime('%H:%M:%S'))
    try:
      cur.execute(sql, val)
    except:
      print('save error')
    db.commit()
    cur.close()
  except:
    print('connect error')
