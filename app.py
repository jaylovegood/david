from flask import Flask, request, Response, render_template
import os
import base64
from io import BytesIO
from gtts import gTTS
import socket

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def post_home():

    text = request.form.get('input_text')
    lang = request.form.get('lang', DEFAULT_LANG)

    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '

    if not text:
        return render_template("index.html", error="텍스트를 입력하세요.", computername=hostname)

    try:
        
        fp = BytesIO()
        gTTS(text, "com", lang).write_to_fp(fp)

        fp.seek(0)

        audio_b64 = base64.b64encode(fp.read()).decode("ascii")
        return render_template("index.html", audio=audio_b64, computername=hostname)

    except Exception as e:
        return render_template("index.html", error=f"음성 생성 실패: {e}", computername=hostname)

@app.route('/menu', methods=["GET", "POST"])
def menu():
    if request.method == "GET":
        return render_template("menu.html")
    elif request.method == "POST":
        menu = request.form.get("button")
        if (menu == "americano"):
            desc = "2샷 에스프레소가 들어갑니다."
        elif (menu == "drip_coffee"):
            desc = "핸드드립 방식으로 내린 커피입니다."
        elif (menu == "green_tea"):
            desc = "제주산 녹차잎으로 우립니다."
        return render_template("menu.html", desc=desc)
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)


@app.route("/test2")
def test2():
    return render_template('test2.html')


@app.route("/test3")
def test3():
    return render_template('test3.html')
