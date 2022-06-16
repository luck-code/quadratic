from app import app
from app import db
from flask import render_template
from flask import request
from forms import CoefficientForm
from models import Coefficient
from logics import decide, description


def write_to_db(a, b, c, x1, x2):
    coefs = Coefficient(a=a, b=b, c=c, x1=x1, x2=x2)
    db.session.add(coefs)
    db.session.commit()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['a'] and request.form['b'] and request.form['c'] \
                and request.form['a'].isdigit() and request.form['b'].isdigit() and request.form['c'].isdigit():
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            result = decide(a, b, c)

            try:
                if len(result) == 2:
                    x1 = result['x1']
                    x2 = result['x2']
                    write_to_db(a, b, c, x1, x2)
                    output = description(a, b, c, x1, x2)

                elif len(result) == 1:
                    x1 = result['x1']
                    x2 = None
                    write_to_db(a, b, c, x1, x2)
                    output = description(a, b, c, x1, x2)

                else:
                    x1 = None
                    x2 = None
                    write_to_db(a, b, c, x1, x2)
                    output = description(a, b, c, x1, x2)

            except:
                output = 'Данные не записались. Попробуйте снова. Возможно отсутствует база данных или таблица'

        elif not request.form['a'].isdigit() or \
                not request.form['b'].isdigit() or \
                not request.form['c'].isdigit():
            print("#" * 100)
            output = "Введите, пожалуйста, числовые значения"
        # else:
        #     output = "Введите коэффициенты"

    text = 'Введите коэффициенты А, В и С для решения уравнения: ' \
           'A*x^2 + B*x + c = 0'

    form = CoefficientForm()

    if not 'output' in locals():
        output = 'Введите коэффициенты'

    return render_template('index.html', form=form, text=text, output=output)


@app.route('/results')
def results():
    coefficients = Coefficient.query.order_by(Coefficient.id.desc())  # .all()
    return render_template('results.html', coefficients=coefficients)
