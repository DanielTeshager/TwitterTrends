from flask import Flask, jsonify, render_template, request
import json
import get_trends

app = Flask(__name__)

@app.route('/data')
def get_data():
    #get city name from the request
    city = request.args.get('city')
    #get the trends for that city
    trends = get_trends.get_twitter_trends_for_location(city)
    print(trends)
    #return the trends as json
    return jsonify(trends[0]['trends'])


@app.route('/')
def index():
    # render the index.html
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5008)
