# web engine

Host a chess engine behind a simple Flask API + web UI, allowing for player interaction.

## Explanation
- Serves a chessboard UI at `/`
- When the player makes a move, the browser sends `POST /make_move` with the current FEN
- Flask backend passes that position to a local UCI engine, gets the engine’s best move, and updates the board
- Backend returns JSON containing the updated FEN and best move
- UI updates the displayed position and waits for the player’s next move

## Running project locally
This app expects an engine binary in your repo, replace engine executables if you want to use your own:
```
Linux: engine/unix/august3
Windows: engine/windows/august3.exe
```

On Linux, make sure the binary is executable:
```
chmod +x engine/unix/august3
```

### Run with Docker (Recommended)
Run command at project root. This will automatically pull Docker image for this project to set up environment.
```
docker compose up --build
```

### Run with Python venv
- Create + activate a venv
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- Install dependencies
```
pip install -r requirements.txt
```
- Run
```
python app.py
```

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.
