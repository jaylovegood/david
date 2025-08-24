from flask import Flask, request, Response, render_template
import os
import base64
from io import BytesIO
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def post_home():

    text = request.form.get('input_text')
    lang = request.form.get('lang', DEFAULT_LANG)

    if not text:
        return render_template("index.html", error="텍스트를 입력하세요.")

    try:
        
        fp = BytesIO()
        gTTS(text, "com", lang).write_to_fp(fp)

        fp.seek(0)

        audio_b64 = base64.b64encode(fp.read()).decode("ascii")
        return render_template("index.html", audio=audio_b64)

    except Exception as e:
        return render_template("index.html", error=f"음성 생성 실패: {e}")

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)