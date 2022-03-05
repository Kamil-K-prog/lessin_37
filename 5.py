from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astr_sel():
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html lang="ru" xmlns="http://www.w3.org/1999/html" xmlns="http://www.w3.org/1999/html">
        <head>
            <meta charset="UTF-8">
            <title>Привет, Марс!</title>
            <link rel="stylesheet" href="static/css/style_5.css">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel
                    ="stylesheet" integrity
                          ="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
                  crossorigin="anonymous">
        </head>
        <body>
        <h1 class="naming">Анкета претендента</h1>
        <h2 class="naming">На участие в миссии</h2>
        <div class="form-group">
            <form method="post" class="login_form" enctype="multipart/form-data">
                <div>
                <input type="text" placeholder="Введите фамилию" name="surname" class="form-control" id="surname"> <br>
                <input type="text" placeholder="Введите имя" name="name" class="form-control" id="name"><br>
                <input type="text" placeholder="Введите адрес электронной почты" name="email" class="form-control"
                       id="email">
                </div>
                <div class="form-group">
                    <label>Какое у Вас образование?</label>
                    <select class="form-control" name="education">
                        <option>Начальное</option>
                        <option>Среднее</option>
                        <option>Высшее</option>
                    </select>
                </div>
                <div>
                    <label>Какие у Вас есть профессии?</label>
                    <div>
                        <p><input type="checkbox" name="professions" value="Инженер-исследователь">Инженер-исследователь</p>
                        <p><input type="checkbox" name="professions" value="Инженер-строитель">Инженер-строитель</p>
                        <p><input type="checkbox" name="professions" value="Пилот">Пилот</p>
                        <p><input type="checkbox" name="professions" value="Метеоролог">Метеоролог</p>
                        <p><input type="checkbox" name="professions" value="Инженер по жизнеобеспечению">Инженер по
                            жизнеобеспечению</p>
                        <p><input type="checkbox" name="professions" value="Инженер по радиационной защите">Инженер по радиационной защите</p>
                        <p><input type="checkbox" name="professions" value="Врач">Врач</p>
                        <p><input type="checkbox" name="professions" value="Экзобиолог">Экзобиолог</p>
                    </div>
                </div>
                <div class="form-group">
                    <label for="form-check">Укажите пол</label>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                        <label class="form-check-label" for="male">
                            Мужской
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                        <label class="form-check-label" for="female">
                            Женский
                        </label>
                    </div>
                </div>
                <div class="form-group">
                    <label>Почему вы хотите принять участие в миссии?</label>
                    <textarea rows="3" class="form-control" name="why_is_this_mission"></textarea>
                </div>
                <div>
                    <label>Приложите фотографию</label>
                    <input type="file" class="form-control-file" name="photo">
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept" value="да">
                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
                crossorigin="anonymous"></script>
        </body>
        </html>
        """
    elif request.method == 'POST':
        print("Имя:", request.form['name'])
        print('Фамилия:', request.form['surname'])
        print('Адрес эл. почты:', request.form['email'])
        print('Образование:', request.form['education'])
        print('Профессии:', request.form['professions'])
        print('Пол:', request.form['sex'])
        print('Причина участия:', request.form['why_is_this_mission'])
        print('Готов остаться на Марсе:', request.form['accept'])
        return 'SUCCESS'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
