import sqlite3


def get_unused_cdkeys():
    """查询未使用的 CDKey"""
    conn = sqlite3.connect('cdkeys.db')
    cursor = conn.cursor()

    cursor.execute("SELECT key FROM cdkeys WHERE is_used = 0")
    unused_cdkeys = [row[0] for row in cursor.fetchall()]

    conn.close()
    return unused_cdkeys
