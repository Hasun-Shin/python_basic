from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/opgg')
def opgg():
    username = request.args.get('userName')
    url = f"https://www.op.gg/summoner/userName={userName}"
    
    req = requests.get(url).text
    data = BeautifulSoup(req, 'html.parser')

    data.select.one()
    
    
    return render_template('opgg.html', ruserName =userName, url =url)



if __name__ == ("__main__"):
  app.run(debug=True)