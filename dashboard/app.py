from flask import Flask, render_template, jsonify
from db import Database

import random

app = Flask(__name__)


def get_temperature():
    temp = random.gauss(55, 10)
    if temp < -10:
        return -10.0
    elif temp > 50:
        return 50.0
    else:
        return round(temp, 1)


def get_pressure():
    press = random.gauss(55, 10)
    if press < 0:
        return 0.0
    elif press > 200:
        return 200.0
    else:
        return round(press, 1)


def get_humidity():
    press = random.gauss(55, 10)
    if press < 0:
        return 0.0
    elif press > 100:
        return 100
    else:
        return round(press, 0)


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

@app.route('/temp-historic')
def tempHistoric():
    return render_template('temp-historic.html')


@app.route('/api/cpu-load')
def cpu_load_latest():
    return jsonify(get_CPULoad())


@app.route('/api/current-temp')
def curTemp():
    return jsonify(get_temperature())


@app.route('/api/current-humidity')
def curHum():
    return jsonify(get_humidity())


@app.route('/api/current-pressure')
def curPress():
    return jsonify(get_pressure())


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
