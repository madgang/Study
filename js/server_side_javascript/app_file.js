var express = require('express');
var app = express();
var fs = require('fs');
var multer = require('multer');
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
app.set('views','./views_file')
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

app.get('/topic/new',function(req,res){
  fs.readdir('data',function(err,files){
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    res.render('new',{topics:files});
  });
});

app.get(['/topic','/topic/:id'],function(req,res){
  fs.readdir('data',function(err,files){
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error')
    }
    var id = req.params.id;

    // ID 값이 있는경우
    // ID 값이 있는 경우 처리
    if(id){
      fs.readFile('data/'+id,'utf-8',function(err,data){
        if(err){
          console.log(err);
          res.status(500).send('Internal Server Error');
        }
        res.render('view',{topics:files, title:id,description:data});
      });
    }else{ // 값이 없는 경우
      res.render('view',{topics:files, title:'Welcome',description:'Hello, Javascript for server'});
    }
  });
});

app.post('/topic',function(req,res){
  var title = req.body.title;
  var description = req.body.description;
  fs.writeFile('data/'+title,description, function(err){
    if(err){
      //Error 처리
      console.log(err);
      res.status(500).send('Internal Server Error');
    }else{
      res.redirect('/topic/'+title);
    }
  });

})

app.listen(3000,function(){//
  console.log('Connected, 3000 port')
})
