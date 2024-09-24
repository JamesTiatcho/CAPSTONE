import sqlite3

def view_users():
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        print("Database connected successfully.")

        cursor.execute("SELECT * FROM User")
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    view_users()
