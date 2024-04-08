from flask import Flask
from animeflv.animeflv import AnimeFLV

app = Flask(__name__)
animeflv = AnimeFLV()

@app.route('/')
def index():
    return 'Welcome animeflv-api!!'

if __name__ == '__main__':
    app.run(debug=True)
