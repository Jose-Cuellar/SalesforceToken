from flask import *
import requests
  
app = Flask(__name__)


@app.route("/")
def home():
    messagge = "Serás redirigido a obtener el Access Token de Salesforce"
    return render_template("home.html", messagge=messagge)

@app.route("/get-access-token", methods=["GET","POST"])
def GetTokenSalesforce():
    if request.method == 'GET':
        return render_template("getToken.html")

    if request.method == 'POST':
        refresh_token = "your_refresh_token"
        client_id = "your_client_id"
        client_secret = "your_client_secret"
        params = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret
        }
        url = "https://your_instance.my.salesforce.com/services/oauth2/token"

        res = requests.post(url, params=params)
        response = res.json()
        # print(response)
        return render_template("getToken.html", response=response)


if __name__ == '__main__':  
   app.run()  