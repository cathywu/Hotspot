import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

# WB_REST_API_KEY = 'fbzpn6ambx9de5nusf49rv4d'
# WB_GEO_API_KEY = '2unavy5kacmhfh95u5cahfvw'
# GN_USERNAME = 'ms_test201302'
# GN_SERVER = 'ws.geonames.net'

@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
