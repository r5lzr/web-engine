from flask import Flask
from flask import render_template
from flask import request
import chess
import chess.engine
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if sys.platform.startswith("win"):
    engine_rel = os.path.join("engine", "windows", "august3.exe")
else:
    engine_rel = os.path.join("engine", "unix", "august3")

ENGINE_PATH = os.path.join(BASE_DIR, engine_rel)

engine = chess.engine.SimpleEngine.popen_uci(ENGINE_PATH)

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("august3.html")


@app.route("/make_move", methods=["POST"])
def make_move():
    fen = request.form.get("fen")

    board = chess.Board(fen)

    result = engine.play(board, chess.engine.Limit(time=0.1))

    board.push(result.move)

    extractFen = board.fen()

    return {"fen": extractFen, "best_move": str(result.move)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True)

