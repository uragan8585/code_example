import json
import requests
import os
import sqlite3
import time
import logging
import multiprocessing
import inspect
from multiprocessing.pool import ThreadPool
from typing import Tuple, Any, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pars_api(i_pers: int) -> tuple[Any, Any, Any]:
    data = requests.get(f"https://swapi.dev/api/people/{i_pers + 1}/")
    if data.status_code == 200:
        data_pers = json.loads(data.text)
        return data_pers['name'], data_pers['birth_year'], data_pers['gender']
    else:
        print("The server is unavailable")


def threadpool() -> list[tuple[Any, Any, Any]]:
    with multiprocessing.pool.ThreadPool(
            processes=multiprocessing.cpu_count() *
                      (multiprocessing.cpu_count() * 2)
    ) as pool:
        start = time.time()
        result = pool.map(pars_api, range(10))
        pool.close()
        pool.join()
        end = time.time()
        logger.info(f'Time taken in seconds with threadpool - {end - start}')

        pool.close()
        pool.join()

    return result


def processpool() -> list[tuple[Any, Any, Any]]:
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(pars_api, range(10))
        end = time.time()
        logger.info(f'Time taken in seconds - {end - start}')

        pool.close()
        pool.join()

    return result


def record_db(lst) -> None:
    if not os.path.exists('persons.db'):
        connect = sqlite3.connect('persons.db')
        with connect:
            connect.execute("""
                CREATE TABLE persons (
                id INTEGER PRIMARY KEY,
                name VARCHAR(30),
                age VARCHAR(6),
                sex VARCHAR(6));
            """)

    connect = sqlite3.connect('persons.db')
    with connect:
        sql = """INSERT INTO persons (name, age, sex) values(?, ?, ?)"""
        connect.executemany(sql, lst)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    lts_pers_to_rec_db = threadpool()
    print('Функция на threadpool:')
    print(lts_pers_to_rec_db)
    print(len(lts_pers_to_rec_db))
    print()

    lts_pers_to_rec_db = processpool()
    queue.close()
    queue.join_thread()
    print('Функция на processpool:')
    print(lts_pers_to_rec_db)
    print(len(lts_pers_to_rec_db))

    record_db(lts_pers_to_rec_db)
