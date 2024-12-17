from flask import Flask, render_template, request
import os

app = Flask(__name__)

l=[]

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
    d = {"Username" : username,
        "Grid" : grid_size,
        "Moves" : moves,
        "Time" : time}
    l.append(d)
    return "Game saved", 200

def get_best_results():
    if len(l)==0:
        return "N/A", "N/A"

    best_score = float('inf')
    shortest_time = float('inf')

    for x in l:
        best_score = min(best_score, int(x["Moves"]))
        shortest_time = min(shortest_time, int(x["Time"]))

    best_score = best_score if best_score != float('inf') else "N/A"
    shortest_time = shortest_time if shortest_time != float('inf') else "N/A"

    return best_score, shortest_time

if __name__ == '__main__':
    app.run(debug=True)

