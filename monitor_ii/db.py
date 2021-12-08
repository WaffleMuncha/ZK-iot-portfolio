from datetime import datetime
import sqlite3

from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




class CPU(Base):
    __tablename__ = 'device_general'
    id = Column(Integer, primary_key=True)
    host_name = Column(String)
    serial = Column(String)
    host_mac = Column(String)
    load = Column(Float)
    cpu_temp = Column(Float)
    gpu_temp = Column(Float)
    created_at = Column(DateTime)

    def __init__(self):
        self.host_name = "UNKNOWN"
        self.host_mac = "ZZ:ZZ:ZZ:ZZ:ZZ:ZZ"
        self.created_at = datetime.now()
        self.serial = "UNKNOWN"
        self.load = -999.99
        self.cpu_temp = -999.99
        self.gpu_temp = -999.99


class Storage(Base):
    __tablename__ = 'device_storage'
    id = Column(Integer, primary_key=True)
    host_name = Column(String)
    host_mac = Column(String)
    total_storage = Column(Integer)
    free_storage = Column(Integer)
    used_storage = Column(Integer)
    created_at = Column(DateTime)

    def __init__(self):
        self.host_name = "UNKNOWN"
        self.host_mac = "ZZ:ZZ:ZZ:ZZ:ZZ:ZZ"
        self.created_at = datetime.now()
        self.total_storage = None
        self.free_storage = None
        self.used_storage = None


class EnviromentTPH(Base):
    __tablename__ = 'tph_storage'
    __filename = './data/enviro_data.db'
    Id = Column(Integer, primary_key=True)
    device_name = Column(String)
    device_mac = Column(String)
    device_serial = Column(String)
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    created_at = Column(DateTime)

    def __init__(self):
        self.device_name = 'UNKNOWN'
        self.device_mac = 'ZZ:ZZ:ZZ:ZZ:ZZ:ZZ'
        self.device_serial = 'UNKNOWN'
        self.temperature = None
        self.pressure = None
        self.humidity = None
        self.created_at = datetime.now()

    def get_last_hum(self, value="1", json=True) -> object:
        """
            This method returns the last <value> items of stored data.
            For example, calling `get_last(13)` will return the last
            thirteen items of recorded data.

            :param value:   An Integer
            :param json:    A boolean identifying if results to be JSON, or a
                            Dictionary
            :return:        JSON | Dictionary
        """
        try:
            if not value.isnumeric():
                value = 1
        except AttributeError:
            value = abs(int(value))
        else:
            value = abs(int(value))

        query = f"SELECT humidity FROM {self.__tablename__}" \
                f"    ORDER BY created_at DESC" \
                f"    LIMIT {value}"
        return self.__retrieve(query, json=json)

    def get_last_temp(self, value="1", json=True) -> object:
        """
            This method returns the last <value> items of stored data.
            For example, calling `get_last(13)` will return the last
            thirteen items of recorded data.

            :param value:   An Integer
            :param json:    A boolean identifying if results to be JSON, or a
                            Dictionary
            :return:        JSON | Dictionary
        """
        try:
            if not value.isnumeric():
                value = 1
        except AttributeError:
            value = abs(int(value))
        else:
            value = abs(int(value))

        query = f"SELECT temperature FROM {self.__tablename__}" \
                f"    ORDER BY created_at DESC" \
                f"    LIMIT {value}"
        return self.__retrieve(query, json=json)
    def get_last_pressure(self, value="1", json=True) -> object:
        """
            This method returns the last <value> items of stored data.
            For example, calling `get_last(13)` will return the last
            thirteen items of recorded data.

            :param value:   An Integer
            :param json:    A boolean identifying if results to be JSON, or a
                            Dictionary
            :return:        JSON | Dictionary
        """
        try:
            if not value.isnumeric():
                value = 1
        except AttributeError:
            value = abs(int(value))
        else:
            value = abs(int(value))

        query = f"SELECT pressure FROM {self.__tablename__}" \
                f"    ORDER BY created_at DESC" \
                f"    LIMIT {value}"
        return self.__retrieve(query, json=json)

    def __retrieve(self, query, json=False):
        """
        Convenience method that opens connection, retrieves a cursor,
        executes a query, retrieves the query results, closes the
        connection, and then returns results

        SHOULD NOT be used for actions that modify database, tables or data.
        """
        connection = sqlite3.connect(self.__filename)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        count = 0
        if json:
            # Create an array of dictionaries
            results = []
            for row in rows:
                # For each row in the rows,
                # Grab the table's field names (from SQLite) and
                # (using ZIP) associate each field name with the
                # corresponding value from  the row
                # Then append the dictionary to the results list
                results.append(dict(zip(
                    [c[0] for c in cursor.description], row)))
        else:
            # Create an "indexed" dictionary
            results = {}
            for row in rows:
                # For each row in the rows,
                # Grab the table's field names (from SQLite) and
                # (using ZIP) associate each field name with the
                # corresponding value from  the row
                # Then create a dictionary of the resulting row with a
                # unique ID for the resulting row of data.
                results[count] = dict(zip(
                    [c[0] for c in cursor.description], row))
                count += 1
        connection.close()
        return results
