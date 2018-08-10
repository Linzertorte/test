var http = require('http');
var fs = require('fs');

var download = function(url, dest, cb) {
  var file = fs.createWriteStream(dest);
  var request = http.get(url, function(response) {
    response.pipe(file);
    file.on('finish', function() {
      file.close(cb);
    });
  });
}

function download_album(album_id,page) {
  var url = 'http://www.ximalaya.com/revision/play/album?sort=-1&pageSize=30'+
  '&albumId=' + album_id + '&pageNum=' + page
  http.get(url, function(res){
    var body = '';
    res.on('data', function(chunk){
      body += chunk;
    });
    res.on('end', function(){
      album = JSON.parse(body);
      var i = 0;
      for(i = 0 ;i < album.data.tracksAudioPlay.length;i ++) {
        console.log(album.data.tracksAudioPlay[i].trackName)
        download(album.data.tracksAudioPlay[i].src,
          album.data.tracksAudioPlay[i].trackName+".m4a",
          function() { console.log("done!");}
        );
      };
      if(album.data.hasMore) download_album(album_id,page+1)
    });
  }).on('error', function(e){
    console.log("Got an error: ", e);
  });
}

// download_album(12960645,1)
// Example: nodejs xima.js 12960645
download_album(process.argv[2],1)
