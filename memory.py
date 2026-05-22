import sqlite3
from pathlib import Path



DB_PATH = Path(__file__).parent / "db.sqlite3"


def get_connection():
    return sqlite3.connect(str(DB_PATH),check_same_thread=False)


def create_table_courses():
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
              CREATE TABLE IF NOT EXISTS courses(
              video_url TEXT PRIMARY KEY,
              course TEXT NOT NULL,
              timestamp DEFAULT CURRENT_TIMESTAMP)
              """)
    conn.commit()
    conn.close()

def save_course(video_url,course):
    conn=get_connection()
    c=conn.cursor()
    c.execute("INSERT OR REPLACE INTO courses(video_url,course) VALUES(?,?)",(video_url,course))
    conn.commit()
    conn.close()

def get_cached_course(video_url):
    conn=get_connection()
    c=conn.cursor()
    c.execute("SELECT course FROM courses WHERE video_url=?", (video_url,))
    result=c.fetchone()
    conn.close()

    if result:
        return  result[0]
    else:
        return None
    
