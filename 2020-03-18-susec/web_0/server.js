var express = require("express")
var bodyParser = require('body-parser')
var crypto = require('crypto')
var app = express();
app.use(bodyParser.urlencoded())
app.use(bodyParser.json())

const port = 3000;

app.listen(port, () => {
  console.log("Server up!");
});

function sha1(s) {
  return crypto.createHash("sha1")
    .update(s)
    .digest("hex");
}
app.post("/flag", (req, res) => {
  const {
    first,
    second
  } = req.body;
  console.log(first.length)
  console.log(second.length)
  const salt = "pepper";

  if (!first || !second || first.length !== second.length) {
    res.send("bad input");
    return;
  }

  if (first !== second && sha1(salt + first) === sha1(salt + second)) {
    res.send(flag); // have some flag
    return;
  }

  res.send("access denied");
})