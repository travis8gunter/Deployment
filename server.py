from flask import Flask, request
from game import GamesDB


app = Flask(__name__)

@app.route("/games/<int:game_id>", methods=["OPTIONS"])
def handle_cors_options(game_id):
    return "", 204, {
        "Access-Control-Allow-Origin":"*",
        "Access-Control-Allow-Methods" : "PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
    }

@app.route("/games", methods=["GET"])
def retrieve_all_games():
    db = GamesDB("videogames_db.db")
    games = db.getAll()
    return games, 200, {"Access-Control-Allow-Origin" : "*"}

@app.route("/games/<int:game_id>", methods=["GET"])
def retrieve_one_game(game_id):
    db = GamesDB("videogames_db.db")
    game = db.getOne(game_id)
    if not game:
        return f"game with {game_id} not found", 404, {"Access-Control-Allow-Origin": "*"}
    return game, 200, {"Access-Control-Allow-Origin" : "*"}

@app.route("/games", methods=["POST"])
def create_game():
    print("The request data is: ", request.form)
    title = request.form["title"]
    genre = request.form["genre"]
    rating = request.form["rating"]
    multiplayer = request.form["multiplayer"]
    price = request.form["price"]
    db = GamesDB("videogames_db.db")
    db.create(title, genre, rating, multiplayer, price)
    return "Created", 201, {"Access-Control-Allow-Origin" : "*"}

@app.route("/games/<int:game_id>",methods=["PUT"])
def update_game(game_id):
    print("update game with ID")
    db = GamesDB('videogames_db.db')
    game = db.getOne(game_id)
    if not game:
        return f"game with {game_id} not found", 404, {"Access-Control-Allow-Origin": "*"}
    
    title = request.form["title"]
    genre = request.form["genre"]
    rating = request.form["rating"]
    multiplayer = request.form["multiplayer"]
    price = request.form["price"]
    db.update(title, genre, rating, multiplayer, price, game_id)
    return "Updated", 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/games/<int:game_id>", methods=["DELETE"])
def delete_game(game_id):
    print("delete game with id")
    db = GamesDB('videogames_db.db')  
    game = db.getOne(game_id)
   
    
    db.delete(game_id)
    return "Deleted", 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/users", methods=["POST"])
def create_in_users_collection():
    print("Thee request data is: ", request.form)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    db = GamesDB("videogames_db.db")
    #need to encrypt password before storing in DB
    # need to check if email has already beeen used to avoid duplicate accounts
    if db.get_user_by_email(email):
        return f"User with email{email} already exists", 422, {"Access-Control-Allow-Origin": "*"}
    
    db.createUser(first_name, last_name, email, password)
    return "User created", 201, {"Access-Control-Allow-Origin": "*"}

def run():
    app.run(port=8080)

if __name__ == "__main__":
    run()