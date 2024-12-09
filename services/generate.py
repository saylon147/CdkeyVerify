import sqlite3
import random
import string


def generate_cdkey(count):
    """生成指定数量的 CDKey"""
    char_pool = string.ascii_uppercase.replace('O', '').replace('I', '') + string.digits
    cdkeys = []

    conn = sqlite3.connect('cdkeys.db')
    cursor = conn.cursor()

    for _ in range(count):
        cdkey = ''.join(random.choices(char_pool, k=8))
        try:
            cursor.execute("INSERT INTO cdkeys (key) VALUES (?)", (cdkey,))
            cdkeys.append(cdkey)
        except sqlite3.IntegrityError:
            continue  # 如果 CDKey 重复，跳过

    conn.commit()
    conn.close()
    return cdkeys
