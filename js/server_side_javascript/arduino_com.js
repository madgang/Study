var express = require('express');
var http = require('http')

var app = express();
var path = require('path');

var server = http.createServer(app);
server.listen(3000);

var serialPort = require('serialPort');
var bodyParser = require('body-parser')

app.locals.pretty = true;
app.set('view engine','jade');
app.set('views','./views');
app.use(bodyParser.urlencoded({extended: false}))

app.get('/arduino',function(req,res){
	res.render('arduino')
});

app.post('/arduino_receiver',function(req,res){
	var title = req.body.title;
	var description = req.body.description;
  com.write(title);
	res.send('title : '+title+' description : '+description);
})

var com = new serialPort('/dev/cu.usbmodem1421',{
  baoudrate : 9600,
  dataBits : 8,
  parity: 'none',
  stopBits : 1,
  flowControl : false
})

com.on('open',function(){
  console.log('Open serial communication')

})
