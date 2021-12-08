import random
from db import EnviromentTPH, Base
from time import sleep
from datetime import datetime

from mypi import \
    get_serial, get_mac, get_host_name

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_filename = './data/enviro_data.db'


## following functions to simulate having a pi attached

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


def headings():
    print()
    print(f'{"Device Name":<10}|{"Device Serial #":<18}|'
          f'{"Device MAC":<20}|{"Created at":<28}|'
          f'{"Temp":>8}|{"Humidity":>8}|'
          f'{"Pressure":>8}'
          f'')


def main(_delay):
    engine = create_engine(f'sqlite:///{db_filename}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    counter = 0

    while True:
        # Create a CPU object and set the properties
        enviroTPH = EnviromentTPH()
        enviroTPH.device_name = get_host_name()
        enviroTPH.device_serial = get_serial()
        enviroTPH.device_mac = get_mac()
        enviroTPH.temperature = get_temperature()
        enviroTPH.pressure = get_pressure()
        enviroTPH.humidity = get_humidity()
        enviroTPH.created_at = datetime.now()
        # save the object to the database using SQLAlchemy ORM and
        # commit the action
        session.add(enviroTPH)
        session.commit()

        last_readings = session.query(EnviromentTPH).order_by(EnviromentTPH.Id.desc()).first()

        if counter % 10 == 0:
            headings()
        counter += 1

        print(f'{last_readings.device_name:<10}|{last_readings.device_serial:<18}|'
              f'{last_readings.device_mac:^20}|{last_readings.created_at}  |'
              f'{last_readings.temperature:>8.1f}|{last_readings.humidity:>8.1f}|'
              f'{last_readings.pressure:>8.1f}'
              f'')

        sleep(_delay)


if __name__ == '__main__':
    delay = 5.0
    main(delay)
