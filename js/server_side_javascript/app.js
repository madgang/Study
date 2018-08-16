/*
*	Hello Nodejsn
*/
var express = require('express');
var app = express();
var bodyParser = require('body-parser')
app.locals.pretty = true;
app.set('view engine','jade');
app.set('views','./views');
app.use(bodyParser.urlencoded({extended: false}))


app.get('/template',function(req,res){
	res.render('temp',{time:Date(),_title:'jade'});
});
app.use(express.static('public'));

app.get('/form',function(req,res){
	res.render('form')
});

app.get('/form_receiver',function(req,res){
	var title = req.query.title;
	var description = req.query.description;
	res.send(title + ' , '+description);
})

app.post('/form_receiver',function(req,res){
	var title = req.body.title;
	var description = req.body.description;
	res.send('title : '+title+' description : '+description);
})


app.get('/topic/:id/:name',function(req,res){
	var topics = [
		'javascript is ...',
		'Nodejs is ...',
		'Express is ...'
	];
	var str = `
		<a href="/topic/0/javacript">Javascript</a><br/>
		<a href="/topic/1/Nodejs">Nodejs</a><br/>
		<a href="/topic/2/Express">Express is</a><br/><br/>
		${topics[req.params.id]} <br/>
		${req.params.name}
	`;
	var output = str + topics[req.query.id];
	res.send(str);
})

app.get('/',function(req, res){
	res.send('Hello world!');
});
app.get('/dynamic',function(req,res){
	var lis = '';
	for(var i=0;i<5;i++){
		lis = lis + '<li>coding</li>';
	}
	var time = Date();
	var output = `
	<!DOCTYPE html>
	<html>
	  <head>
	    <meta charset="utf-8">
	    <title></title>
	  </head>
	  <body>
	    Hello, dynamic!!
			<ul>
			${lis}
			${time}
			</ul>
	  </body>
	</html>`
	res.send(output);
});
app.get('/route',function(req, res){
	res.send('Hello route, <img src="/route.png">')
});
app.get('/login',function(req, res){
	res.send('Login please')
});
app.listen(3001,function(){
	console.log('connected 3001 port');
});
