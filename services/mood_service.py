from database.db import cursor, conn

def create_mood(mood, sentiment, moodlog_id):

    cursor.execute(
        """
        INSERT INTO mood (mood, sentiment, moodlog_id)
        VALUES (%s,%s,%s)
        RETURNING *
        """,
        (mood, sentiment, moodlog_id)
    )
    mood = cursor.fetchone()
    conn.commit()

    return mood

def get_moods():

    cursor.execute("SELECT * FROM mood")
    return cursor.fetchall()