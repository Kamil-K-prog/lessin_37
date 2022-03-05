from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    prom_lst = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]

    return '<br>'.join(prom_lst)


@app.route('/image_mars')
def img_mars():
    return f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='images/mars_1.gif')}" alt='...'>
        <p>Вот она какая, красная планета</p>
    </body>
    </html>
    '''

@app.route('/promotion_image')
def prm_img():
    pass

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
