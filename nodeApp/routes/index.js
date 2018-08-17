var express = require('express');
var router = express.Router();
var thrift = require('thrift');
var Calculator = require('../thrift/topgifs');
var ttypes = require('../thrift/topgifs_types');
const assert = require('assert');

/* GET home page. */
router.get('/', function(req, res, next) {
	var transport = thrift.TBufferedTransport;
	var protocol = thrift.TBinaryProtocol;

	var connection = thrift.createConnection("localhost", 9090, {
	  transport : transport,
	  protocol : protocol
	});

	connection.on('error', function(err) {
	  assert(false, err);
	});

	// Create a Calculator client with the connection
	var client = thrift.createClient(Calculator, connection);


	client.getGifs(function(err, response){
		//console.log(response);
		res.render('index', { data: JSON.parse(response) });
		//$(".loader").hide();
		//var refresh = document.getElementById("refresh");
		//close the connection once we're done
	    connection.end();
	})
  
});

router.get('/refrescar',function(req,res){

	//console.log("hola");
  	var transport = thrift.TBufferedTransport;
	var protocol = thrift.TBinaryProtocol;

	var connection = thrift.createConnection("localhost", 9090, {
	    transport : transport,
	    protocol : protocol
	});

	connection.on('error', function(err) {
	    assert(false, err);
	});

	// Create a Calculator client with the connection
	var client = thrift.createClient(Calculator, connection);

	client.updateGifs(function(err, response){

		//console.log(response);

		//close the connection once we're done
	    connection.end();
	    res.redirect('/')
	})

})

module.exports = router;

//data-toggle="modal" data-target="#exampleModal" href="/refrescar"