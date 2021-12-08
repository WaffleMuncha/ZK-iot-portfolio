from flask import Flask, render_template, jsonify
from db import Database

import random
app = Flask(__name__)



def get_CPULoad():
    press = random.gauss(55, 10)
    if press < 0:
        return 0.0
    elif press > 100:
        return 100
    else:
        return round(press, 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cpu-load')
def cpu_load_latest():
    return jsonify(get_CPULoad())


@app.route('/static-cpu')
def static_chart():
    return render_template('static-chart.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cpu')
def chart_cpu():
    return render_template('chart-cpu.html')


if __name__ == '__main__':
    app.run()
