const fs = require("fs");
const downloadImage = require("./get_posts");
global.XMLHttpRequest = require("xhr2");
const { PythonShell } = require("python-shell");

exports.evaluate = async (req, res) => {
  const imageId = req.query['imageId'];
  if (!fs.existsSync("./images")) {
    fs.mkdirSync("./images");
  }
  const filelist = await getImage(imageId); // get image path
  await downloadImage(filelist);
  const score = await runPython();
  console.log(score);
  await res.status(200).send(score);
};

getImage = (imageId) => {
  let data = [];
  const imagePath =
    "https://drive.google.com/uc?export=view&id=" + imageId;
  data.push(imagePath);
  return data;
};

runPython = () => {
  return new Promise((resolve, reject) => {
    PythonShell.run(
      "/workspace/functions/score.py",
      null,
      async (err, result) => {
        if (err) {
          if (err.traceback === undefined) {
            console.log(err.message);
          } else {
            console.log(err.traceback);
          }
        }
        const score = await result[result.length - 1];
        resolve(score);
      }
    );
  });
};
