#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, Response
from jsonrpcserver import methods #pip install flask jsonrpcserver
from flask_cache import Cache
import redis #pip install redis
from flaskext.mysql import MySQL #pip install flask-mysql

#conexión con redis
conn = redis.Redis('localhost')

app = Flask(__name__)

#configuración de cache con redis
cache = Cache(app, config={'CACHE_TYPE': 'redis'})
cache.init_app(app)

#configuración de base de datos MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'distribuidos'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

connMysql = mysql.connect()
cursor = connMysql.cursor()

@methods.add
def prueba():
    key = "prueba5"
    if(conn.get(key)):
        imagenes = conn.get(key)
        return imagenes
    else:
        cursor.execute("SELECT * FROM gifs ORDER BY num_acceso DESC LIMIT 10")
        imagenes = cursor.fetchall()
        conn.set(key,imagenes)
        return imagenes


@app.route('/', methods=['POST'])
def index():
    req = request.get_data().decode()
    response = methods.dispatch(req)
    return Response(str(response), response.http_status,mimetype='application/json')

if __name__ == '__main__':
    app.run()




