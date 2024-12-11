import sqlite3
from flask import jsonify


def validate_cdkey(cdkey):
    """验证 CDKey 的合法性"""
    if not cdkey:
        return jsonify({'status': 'error', 'message': 'CDKey is required'}), 400

    conn = sqlite3.connect('cdkeys.db')
    cursor = conn.cursor()

    cursor.execute("SELECT is_used FROM cdkeys WHERE key = ?", (cdkey,))
    row = cursor.fetchone()

    if row is None:
        return jsonify({'status': 'error', 'message': 'Invalid CDKey'}), 400

    if row[0] == 1:
        return jsonify({'status': 'success', 'message': 'CDKey is valid but already used'}), 201

    cursor.execute("UPDATE cdkeys SET is_used = 1 WHERE key = ?", (cdkey,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'CDKey is valid and marked as used'}), 200
