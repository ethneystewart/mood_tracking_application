import psycopg2
from database.db import cursor, conn


def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return users


def create_user(first_name, last_name, email):

    try:
        cursor.execute(
            """
            INSERT INTO users (firstName, lastName, email)
            VALUES (%s, %s, %s)
            RETURNING *
            """,
            (first_name, last_name, email)
        )

        user = cursor.fetchone()
        conn.commit()

        return user

    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return {"error": "Email already exists"}