var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var { evaluate } = require('/workspace/functions/index');
const cors = require('cors');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json())

app.use(cors());
app.get('/evaluate', evaluate);

const server = app.listen(8080, () => {
  const host = server.address().address;
  const port = server.address().port;
  console.log(`Example app listening at http://${host}:${port}`);
});