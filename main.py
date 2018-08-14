import webapp2
import webob
import random

class Home(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello, Drew")

class CoinToss(webapp2.RequestHandler):
    def post(self):
        toss = self.request.get('text')
        flip_coin(toss, self)

def flip_coin(toss, self):
    num = random.randint(0, 2)
    toss = toss.lower()

    if toss == "heads":
        if num == 0:
            self.response.write("Heads! You Win :money_mouth_face:")
        else:
            self.response.write("Tails! You Lose :triumph:")

    elif toss == "tails":
        if num == 1:
            self.response.write("Tails! You Win :money_mouth_face:")
        else:
            self.response.write("Heads! You Lose :triumph:")

    else:
        self.response.write("{} is not a valid move.".format(toss))

app = webapp2.WSGIApplication([
    (r'/', Home),
    (r'/coin-toss', CoinToss)
    ],
    debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()

