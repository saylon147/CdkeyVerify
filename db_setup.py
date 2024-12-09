import sqlite3


def setup_database():
    conn = sqlite3.connect('cdkeys.db')
    cursor = conn.cursor()

    # 创建 CDKey 表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cdkeys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            is_used INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("Database setup complete!")


if __name__ == '__main__':
    setup_database()
