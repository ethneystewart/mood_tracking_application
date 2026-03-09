from database.db import cursor, conn

def create_moodlog(date, sleepHours, energyLevels, activities, tags, user_id):

    cursor.execute(
        """
        INSERT INTO moodlog (date, sleepHours, energyLevel, activities, tags, user_id)
        VALUES (%s,%s,%s,%s,%s,%s)
        RETURNING *
        """,
        (date, sleepHours, energyLevels, activities, tags, user_id)
    )

    moodlog = cursor.fetchone()
    conn.commit()

    return moodlog


def get_moodlogs():

    cursor.execute("SELECT * FROM moodlog")
    return cursor.fetchall()