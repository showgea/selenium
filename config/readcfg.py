import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
cfg_path = os.path.join(cur_path, 'config.ini')
print(cfg_path)

con = configparser.ConfigParser()
con.read(cfg_path)

server = con.get("email", "server")
port = con.get("email", "port")
sender = con.get("email", "sender")
psw = con.get("email", "psw")
reciever = con.get("email", "reciever")
