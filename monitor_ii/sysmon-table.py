from time import sleep
import os
from sqlalchemy import create_engine, Column, Float, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import psutil

db_folder = './data/'
db_filename = 'monitor_data.db'

Base = declarative_base()

if not os.path.isdir(db_folder):
    os.makedirs(db_folder)
    print(f"Created {db_folder} folder")
else:
    print(f"Folder {db_folder} exists")


class CPU(Base):
    __tablename__ = 'device_general'
    id = Column(Integer, primary_key=True)
    load = Column(Float)
    created_at = Column(DateTime)

    def __init__(self):
        self.load = -999.99
        self.created_at = datetime.now()


def monCPU():
    return psutil.cpu_percent(interval=None, percpu=False)


def headings():
    print(f'{"DateTime":<10}'
          f'{"CPU":<20}')


def main(_delay):
    engine = create_engine(f'sqlite:///{db_folder + db_filename}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    counter = 0

    while counter < 5:
        cpu = CPU()
        cpu.load = monCPU()
        cpu.created_at = datetime.now()
        session.add(cpu)
        session.commit()

        if counter == 0:
            headings()

        last_readings = session.query(CPU).order_by(CPU.created_at).first()

        print(f'{last_readings.created_at:}|'
              f'{last_readings.load:^20}')

        counter += 1
        sleep(_delay)


if __name__ == "__main__":
    delay = 5
    main(delay)
