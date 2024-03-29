// myModule.js
const { spawn } = require("child_process");

function runPythonScript(rawArgs) {

  const python = spawn("python", [`${__dirname}/linter.py`, rawArgs]);

  //   // collect data from script
  python.stdout.on("data", function (data) {
    console.log(data.toString());
  });

  python.stderr.on("data", (data) => {
    console.log("stdErr: ", data.toString("utf8"));
  });

  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
  });
}

module.exports = { runPythonScript };
