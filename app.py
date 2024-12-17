from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Recreate history file at the start of each session
HISTORY_FILE = "game_history.txt"
if os.path.exists(HISTORY_FILE):
    os.remove(HISTORY_FILE)

with open(HISTORY_FILE, "w") as f:
    f.write("Game History\n-----------------\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    username = request.form.get('username', 'Player')
    grid_size = request.form.get('grid', '4x4')

    # Get best score and shortest time for the current session
    best_score, shortest_time = get_best_results()

    return render_template('game.html', 
                           username=username, 
                           grid_size=grid_size, 
                           best_score=best_score, 
                           shortest_time=shortest_time)

@app.route('/save_game', methods=['POST'])
def save_game():
    username = request.form.get('username', 'Player')
    grid_size = request.form.get('grid_size')
    moves = request.form.get('moves')
    time = request.form.get('time')  # Time taken to solve in seconds

    with open(HISTORY_FILE, "a") as f:
        f.write(f"Username: {username}, Grid: {grid_size}, Moves: {moves}, Time: {time} seconds\n")
    return "Game saved", 200

def get_best_results():
    """Reads the history file and returns the best score (moves) and shortest time."""
    if not os.path.exists(HISTORY_FILE):
        return "N/A", "N/A"

    best_score = float('inf')
    shortest_time = float('inf')

    with open(HISTORY_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Moves" in line and "Time" in line:
                try:
                    moves = int(line.split("Moves: ")[1].split(",")[0].strip())
                    time = float(line.split("Time: ")[1].split(" ")[0].strip())

                    best_score = min(best_score, moves)
                    shortest_time = min(shortest_time, time)
                except ValueError:
                    continue

    best_score = best_score if best_score != float('inf') else "N/A"
    shortest_time = shortest_time if shortest_time != float('inf') else "N/A"

    return best_score, shortest_time

if __name__ == '__main__':
    app.run(debug=True)

