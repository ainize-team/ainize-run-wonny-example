const fs = require("fs");
const request = require("request");
const async = require("async");

download = (uri, filename, callback) => {
  request.head(uri, (err, res, body) => {
    request(uri)
      .pipe(fs.createWriteStream(filename))
      .on("close", callback);
  });
};

downloadImage = async(filelist, imageHash) => {
	return new Promise((resolve, reject) => {
		let filepath = [], filename = [];
		filepath.push(filelist[0]);
		filename.push(`./images/${imageHash}/test.jpg`);
		const threads = 1;
		async.eachLimit(filepath, threads, function(url, next) { // check async module
			download(url, filename[0], next);
		}, function() {
			resolve();
		})
	})
}

module.exports = downloadImage;