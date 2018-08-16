var express = require('express');
var app = express();
var fs = require('fs');
var multer = require('multer');
var OrientDB = require('orientjs');

var server = OrientDB({
  host:'localhost',
  port:2424,
  username:'root',
  password:'z20011206'
});
var db = server.use('o2');

var _storage = multer.diskStorage({
  destination:function(req,file,cb){
    cb(null,'uploads/')
  },
  filename:function(req,file,cb){
    cb(null,file.originalname+'_test')
  }
})


var upload = multer({storage:_storage});
var bodyParser = require('body-parser'); // Post 방식 설정
app.use('/user',express.static('uploads'))
// 기본 설정
app.set('views','./views_orientdb')
app.set('view engine','jade');// jade 설정

app.use(bodyParser.urlencoded({extended:false}));//body-parsr 설정

app.locals.pretty = true;// Source Code  정렬

app.get('/upload',function(req,res){
  res.render('upload')
});

app.post('/upload',upload.single('userfile'),function(req,res){
  console.log(req.file);
  res.send('uploaded '+req.file)
});


app.get('/topic/add',function(req,res){
  var sql = 'SELECT FROM topic';
  db.query(sql).then(function(topics){
    res.render('add',{topics:topics});
  });
})

app.post('/topic/add',function(req,res){
  var title = req.body.title;
  var description = req.body.description;
  var author = req.body.author
  var sql = 'INSERT INTO topic(title,description,author) VALUES(:title,:description,:author)'
  db.query(sql,{
    params:{
      title:title,
      description:description,
      author:author
    }
  }).then(function(results){
    res.redirect('/topic/'+encodeURIComponent(results[0]['@rid']));
  });
});

app.post('/topic/:id/add',function(req,res){
  var title = req.body.title;
  var description = req.body.description;
  var author = req.body.author;
  var id = req.params.id;
  var sql = 'update topic SET title=:title,description=:description,author=:author WHERE @rid=:rid'
  db.query(sql,{
    params:{
      title:title,
      description:description,
      author:author,
      rid:id
    }
  }).then(function(results){
    res.redirect('/topic/'+encodeURIComponent(id));
  });
});

app.get('/topic/:id/edit',function(req,res){
  var sql = 'SELECT FROM topic';
  var id = req.params.id;
  db.query(sql).then(function(topics){
    var sql = 'SELECT FROM topic WHERE @rid =:rid';
    var id = req.params.id;
    if(id){
      db.query(sql,{params:{rid:id}}).then(function(topic){
      res.render('edit',{topics:topics,topic:topic[0]})
      });
    }else {
      res.render('edit',{topics:topics});
    }


  });
});

app.get('/topic/:id/delete',function(req,res){
  var sql = 'DELETE FROM topic WHERE @rid=:id';
  var id = req.params.id;
  db.query(sql,{
      params:{
          id:id
      }
    }).then(function(topics){
      res.redirect('/topic')
  });
});

app.get(['/topic','/topic/:id'],function(req,res){
  var sql = 'SELECT FROM topic';
  db.query(sql).then(function(topics){
    var sql = 'SELECT FROM topic WHERE @rid =:rid';
    var id = req.params.id;
    if(id){
      db.query(sql,{params:{rid:id}}).then(function(topic){
      res.render('view',{topics:topics,topic:topic[0]})
      });
    }
    else {
      res.render('view',{topics:topics})
    }
  });
});


app.listen(3000,function(){//
  console.log('Connected, 3000 port')
})
