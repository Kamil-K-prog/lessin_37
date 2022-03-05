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
    prom_lst = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    url_img = url_for('static', filename='images/mars_1.gif')
    url_style = url_for('static', filename='css/style.css')

    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
    <link rel="stylesheet" href="{}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel
            ="stylesheet" integrity
                  ="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
          crossorigin="anonymous">
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="{}">
<div class="alert alert-secondary" role="alert">
    {}
</div>
<div class="alert alert-success" role="alert">
    {}
</div>
<div class="alert alert-danger" role="alert">
    {}
</div>
<div class="alert alert-warning" role="alert">
    {}
</div>
<div class="alert alert-info" role="alert">
    {}
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
</body>
</html>
    """.format(url_style, url_img, prom_lst[0], prom_lst[1], prom_lst[2], prom_lst[3], prom_lst[4])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
