from database.db import cursor, conn

def create_reflection(reflection, moodlog_id):

    cursor.execute(
        """
        INSERT INTO reflection (moodlog_id, reflection)
        VALUES (%s, %s)
        RETURNING *
        """,
        (moodlog_id, reflection)
    )

    reflection = cursor.fetchone()
    conn.commit()

    return reflection

def get_reflections(moodlog_id):

    cursor.execute(
        """
        SELECT * FROM reflection
        WHERE moodlog_id = %s
        """,
        (moodlog_id,)
    )

    return cursor.fetchall()