#programma, kas izmanto Beautiful Soup, lai izvilktu virsrakstus no vietnes www.delfi.lv un parāda tos HTML veidnē
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_delfi_headlines():
    url = 'https://www.delfi.lv/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all( class_='headline')
    headlines_list = [headline.text.strip() for headline in headlines]
    return headlines_list

@app.route('/')
def index():
    headlines = get_delfi_headlines()
    return render_template('p6.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
