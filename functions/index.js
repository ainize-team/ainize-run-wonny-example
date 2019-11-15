const fs = require("fs");
const downloadImage = require("./get_posts");
global.XMLHttpRequest = require("xhr2");
const { PythonShell } = require("python-shell");
const sha1 = require("sha1");

exports.evaluate = async (req, res) => {
  const imagePath = req.query["image"];
  if (!fs.existsSync(`./images`)) {
    fs.mkdirSync(`./images`);
  }
  const filelist = await getImage(imagePath); // get image path
  const imageHash = sha1(imagePath);
  await downloadImage(filelist, imageHash);
  const score = await runPython(imageHash);
  await res.status(200).send(score);
};

getImage = imagePath => {
  let data = [];
  data.push(imagePath);
  return data;
};

runPython = imageHash => {
  return new Promise((resolve, reject) => {
    PythonShell.run(
      "/workspace/functions/score.py",
      { args: [imageHash] },
      async (err, result) => {
        if (err) {
          if (err.traceback === undefined) {
            console.log(err.message);
          } else {
            console.log(err.traceback);
          }
        }
        console.log(result);
        const score = await result[result.length - 1];
        resolve(score);
      }
    );
  });
};
