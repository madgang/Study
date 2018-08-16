var OrientDB = require('orientjs');

var server = OrientDB({
  host:'localhost',
  port:2424,
  username:'root',
  password:'z20011206'
});
var db = server.use('o2');

/**
var db = server.use('o2');
db.record.get('#12:1').then(function(record){
  console.log('load record',record)
});


var db = server.use('o2');
var sql = 'SELECT FROM topic';
db.query(sql).then(function(results){
  console.log(results);
})

var sql = 'SELECT FROM topic WHERE @rid = :rid';
var param = {
      params:{
        rid:'#12:1'
      }
}
db.query(sql,param).then(function(results){
  console.log(results);
})

var sql = 'INSERT INTO topic(title,description) VALUES (:title,:desc) ';
var param = {
      params : {
          title:'Express',
          desc:'Express is framework for web'
      }
}

db.query(sql,param).then(function(results){
  console.log(results)
})


var sql = 'UPDATE topic SET title = :title WHERE  @rid= :rid';

db.query(sql,{params:{title:'ExpressJS',rid:'#12:2'}}).then(function(result){
  console.log(result)
})
*/

var sql = 'delete from topic WHERE  @rid= :rid';

db.query(sql,{params:{rid:'#12:2'}}).then(function(result){
  console.log(result)
})
