from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    game_data = {"gameId": game_id, "board": game.board}

    return jsonify(game_data)


@app.post("/api/score-word")
def score_word():
    """
    Checks valiidity of word, returns result in json.
    examples:
        if not a word: {result: "not-word"}
        if not on board: {result: "not-on-board"}
        if a valid word: {result: "ok"}
    """
    game_id = request.json['gameId']
    word = request.json['word']

    breakpoint()
    if games[game_id].is_word_in_word_list(word) is False:
        return jsonify({'result': "not-word"})
    elif games[game_id].check_word_on_board(word) is False:
        return jsonify({'result': "not-on-board"})
    else:
        return jsonify({'result': "ok"})


