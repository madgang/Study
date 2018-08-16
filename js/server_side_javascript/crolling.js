var request = require("request");
var cheerio = require("cheerio");
var url = "http://www.naver.com";
request(url,function(err,request,body){
  if(err) throw console.error(err);;
  var $ = cheerio.load(body)
  var html = $("body")
  console.log(html)
})
