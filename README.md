# Proyecto de segundo parcial de Sistemas Distribuidos

_Se requiere poder visualizar el top 10 de gifs del día mediante una pagina web la cual haga uso de un microservicio y pueda cachear el resultado de la búsqueda de la base de datos una vez se haya realizado._

## Solución y Diseño Implementado 🚀

* El FrontEnd fue implementado mediando NodeJs
*	Se usó Nginx como reverse proxy 
*	El microservicio fue desarrollado en phyton por medio del RPC apache thrift con un API binario
*	La base de datos fue implementada en MySql la cual contiene una columna de numero de accesos, de descripción y el link del gif a presentar.
*	La cache fue implementada mediante Redis la cual asocia los datos a una clave que será el día en que se realice la consulta. 
*	La puesta en producción en la nube se realizó mediante Amazon Web Service AWS con el servicio Elastic Compute Cloud  EC2


## Construido con 🛠️

* [Node.js](https://nodejs.org/) - El framework web usado para FrontEnd
* [NGINX](https://www.nginx.com/) - Para el reverse proxy
* [Apache Thrift](https://thrift.apache.org/) - Para el RPC
* [Python](https://www.python.org/) - Para el Microservicio
* [MySQL](https://www.mysql.com/) - Como Base de Datos de los datos de los Gifs
* [Redis](https://redis.io/) - Implementación de la cache
* [AWS con EC2](https://aws.amazon.com/es/ec2/) - Puesto en producción


## Autores ✒️

* **José Cedeño Vargas** - *repo* - [Marcosan](https://github.com/Marcosan)
* **Marco Mendoza Quelal** - *repo* - [JoseCedeno21](https://github.com/JoseCedeno21)


---
