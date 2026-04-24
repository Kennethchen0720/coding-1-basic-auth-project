#!/usr/bin/env python3
# Seed the database with sample data.
# Run this script once with: python seed_db.py

# Once you have seeded your data, you can run sqlite3 users.db in the terminal
# This opens a sqlite3 shell and you can run commands like:
# - .tables to see all tables
# - SELECT * FROM users; to see all users
# - .exit to exit the shell
# *Note: If you try to seed data and get an error about "UNIQUE constraint failed: users.username", it means you have already seeded the database.
# If you need to seed the database again, simply delete the users.db file and run the seed script again.

from database import get_db, init_db
import bcrypt

def seed_database():
    sample_users = [
        ("alice", "Password123!"),
        ("bob", "SecurePass456@"),
        ("charlie", "MyPassword789#"),
    ]
    sample_data = [
        ("alice", "Password123!", "2", "23"),
        ("bob", "SecurePass456@", "2", "23"),
        ("charlie", "MyPassword789#", "2", "23"),
    ]
    init_db()
    
    conn = get_db()
    

    try:
        for username, password in sample_users:
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_pw)
            )
            print(f"Created user: {username}")
        
        conn.commit()
        print("\nDatabase seeding complete!")
    
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        try:
            for id, user, title, content in sample_data:
                hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            conn.execute(
                "INSERT INTO users (id, user, title, content) VALUES (?, ?, ?, ?)",
                (id, user, title, content)
            )
            print(f"Created user: {username}")
        
        except conn.commit():
            print("\nDatabase seeding complete!")
    
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()