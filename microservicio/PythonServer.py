#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import date,timedelta
sys.path.append('gen-py')

from topgifs import topgifs
from topgifs.ttypes import *

import redis #pip install redis
import MySQLdb
import json
import random

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

#conexión con redis
conn = redis.Redis('localhost')

conn2 = MySQLdb.connect (
    host = "localhost", 
    user = "root", 
    passwd =  "root", 
    db = "distribuidos")
cursor = conn2.cursor()

import socket

class topgifsHandler:
  def __init__(self):
    self.log = {}

  def updateGifs(self):
    cursor.execute("""UPDATE gifs SET num_acceso = FLOOR(1 + rand() * 1000000)""")
    conn.flushdb()
    return "actualizacion realizada"

  def getGifs(self):
    fecha = date.today()
    key = str(fecha)
    if(conn.get(key)):
        imagenes = conn.get(key)
        return imagenes
    else:
        result = cursor.execute("""SELECT * FROM gifs ORDER BY num_acceso DESC LIMIT 10""")
        #imagenes = cursor.fetchall()
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        gifs = json.dumps(json_data)
        #print gifs
        conn.set(key,gifs)
        return gifs


if __name__ == '__main__':
    handler = topgifsHandler()
    processor = topgifs.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print "Iniciando microservicio en python..."
    server.serve()
