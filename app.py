from flask import Flask, render_template, request
import chess
import chess.engine
import os
import sys

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if sys.platform.startswith("win"):
    DEFAULT_ENGINE_PATH = os.path.join(BASE_DIR, "engine", "windows", "august3.exe")
else:
    DEFAULT_ENGINE_PATH = os.path.join(BASE_DIR, "engine", "unix", "august3")

ENGINE_PATH = os.environ.get("CHESS_ENGINE_PATH", DEFAULT_ENGINE_PATH)


@app.route("/")
def root():
    return render_template("august3.html")


@app.route("/make_move", methods=["POST"])
def make_move():
    fen = request.form.get("fen")
    board = chess.Board(fen)

    try:
        with chess.engine.SimpleEngine.popen_uci(ENGINE_PATH) as engine:
            result = engine.play(board, chess.engine.Limit(time=0.1))
    except Exception as e:
        app.logger.exception("Engine failed")
        return {"error": str(e), "engine_path": ENGINE_PATH}, 500

    board.push(result.move)
    return {"fen": board.fen(), "best_move": str(result.move)}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
