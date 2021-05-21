from flask import Flask
from flask import render_template
from wordcloud import WordCloud
import io
import base64
from flask_cors import CORS
from flask import request
import jieba
from imageio import imread

app = Flask(__name__,
            template_folder="../frontend/dist",
            static_folder="../frontend/dist/static"
            )

CORS(app)


def get_word_cloud(text):
    # font = "./SimHei.ttf"
    # pil_img = WordCloud(width=500, height=500, font_path=font).generate(text=text).to_image()
    text = ' '.join(jieba.lcut(text))
    # print(text)
    pil_img = WordCloud(font_path="msyh.ttf", width=800, height=300, background_color="white", mask=imread("bg.jpg")).generate(text=text)
    pil_img.to_file("test.png")
    pil_img = pil_img.to_image()

    img = io.BytesIO()
    pil_img.save(img, "PNG")
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    return img_base64


# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# 生成词云图片接口，以base64格式返回
@app.route('/word/cloud/generate', methods=["POST"])
def cloud():
    text = request.json.get("word")
    res = get_word_cloud(text)
    return res


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
