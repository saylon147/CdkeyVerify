import os
from flask import Flask, request, jsonify
from services.generate import generate_cdkey
from services.query import get_unused_cdkeys
from services.validate import validate_cdkey
from db_setup import setup_database

app = Flask(__name__)

# 检查并初始化数据库
if not os.path.exists("cdkeys.db"):
    print("Database not found. Initializing database...")
    setup_database()


# 生成 CDKey 的接口
@app.route('/generate', methods=['POST'])
def generate_cdkeys_route():
    data = request.json
    count = data.get('count', 10)  # 默认为生成 10 个
    cdkeys = generate_cdkey(count)
    return jsonify({'status': 'success', 'generated_cdkeys': cdkeys}), 200


# 获取未使用的 CDKey 接口
@app.route('/unused', methods=['GET'])
def get_unused_cdkeys_route():
    unused_cdkeys = get_unused_cdkeys()
    return jsonify({'status': 'success', 'unused_cdkeys': unused_cdkeys}), 200


# 验证 CDKey 的接口
@app.route('/validate', methods=['POST'])
def validate_cdkey_route():
    data = request.json
    cdkey = data.get('cdkey')
    return validate_cdkey(cdkey)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
