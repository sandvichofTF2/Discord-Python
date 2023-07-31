from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return "Hello. I am alive!"


def run():
  app.run(host='0.0.0.0', port=8080)


def webserver():
  t = Thread(target=run)
  t.start()


# I really dont understand most of this anyway lmao