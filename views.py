from twitter_end_points import Twitter
from flask import Flask, redirect, url_for, request,jsonify,json
app = Flask(__name__)
# app.url_map.strict_slashes = False
consumer_key = "rb2YySEaGBJgWrXov54FMdsdZ"
consumer_secret = "rXqcQ1WDrbx1HLIGbZ46FQq8X7hLBDSfx7ryI0zaCGQGv0ogSL"
access_token = "1087594166769594368-irKDVWtpq0NolupqwRHp4TsjoMe1Wz"
access_token_secret = "wu451rkJiOMWL0fh5FzBM6WDW6XtI43MSBRno67NJoWvO"


@app.route('/follow',methods = ['POST'])
def follow():
  #to be used when the new user accepts the terms and conditions and has to automatically follow the GS twitter handle
  global twitter
  if request.method == 'POST':
    try:
      screen_name = request.json["name"]
      user_data = twitter.follow(screen_name)
      # data = jsonify(user)
      response = app.response_class(response= json.dumps(user_data),
        status = 200, mimetype= 'application/json')
    except:
      error_data = {"error":" The requested user doesnt exist or the requested user cant be followed!!"}
      response = app.response_class(response= json.dumps(error_data),
        status = 404, mimetype= 'application/json')
    return response



@app.route('/get_user_details',methods = ['POST'])
def get_user_details():
  global twitter
  if request.method == 'POST':
    try:
      screen_name = request.json["name"]
      user_data = twitter.get_user_object(screen_name)
      # data = jsonify(user)
      response = app.response_class(response= json.dumps(user_data),
        status = 200, mimetype= 'application/json')
    except:
      error_data = {"error":" The requested user doesnt exist!!"}
      response = app.response_class(response= json.dumps(error_data),
        status = 404, mimetype= 'application/json')
    return response


@app.route('/send_DM',methods = ['POST'])
def send_DM():
  global twitter
  if request.method == 'POST':
    try:
      screen_name = request.json["name"]
      message = request.json["message"]
      print(screen_name,":",message)
      user_data = twitter.send_DM(screen_name,message)
      # data = jsonify(user)
      response = app.response_class(response= json.dumps(user_data),
        status = 200, mimetype= 'application/json')
    except:
      error_data = {"error":" The requested user doesnt exist or the message cant be sent!!"}
      response = app.response_class(response= json.dumps(error_data),
        status = 404, mimetype= 'application/json')
    return response


if __name__ == "__main__":
  twitter = Twitter(consumer_key,consumer_secret,access_token,access_token_secret)
  app.run(port=7000) 
