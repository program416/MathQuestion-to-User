from flask import Flask, send_from_directory
import os

# frontend 폴더를 정적 파일 저장소로 설정합니다.
app = Flask(__name__, static_folder='frontend')

# 1. 기본 페이지 (index.html) 접속
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# 2. 폴더 내의 모든 파일(이미지, JS, CSS 등)을 이름대로 불러오기
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # host='0.0.0.0'을 추가하면 같은 와이파이를 쓰는 다른 기기에서도 접속 가능해요.
    app.run(host='0.0.0.0', port=5000)
