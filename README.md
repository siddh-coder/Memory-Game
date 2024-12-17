# Memory Game

This is a fun and interactive Memory Game built using **Flask** as the backend and **JavaScript** for the frontend. Players can select a grid size (4x4 or 6x6) and test their memory skills by matching cards. The game includes animations, a moves counter, a timer, and session history for best scores.

---

## Features

- **Grid Selection**: Choose between 4x4 and 6x6 grids.
- **Moves Counter**: Tracks the number of moves made by the player.
- **Timer**: Tracks the time taken to solve the game.
- **Session History**:
  - Stores the best score and the shortest time for the current session.
- **Smooth Animations**: Engaging animations for flipping cards and transitioning.
- **Dynamic Background**: Gradient background animation for a lively look.

---

## Project Structure

```
/project
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── static/              # Static assets (CSS, JS, images)
│   ├── styles.css       # Styling for the game
│   ├── script.js        # Frontend game logic
│   ├── images/          # Card images
├── templates/           # HTML templates
│   ├── index.html       # Home page
│   ├── game.html        # Game page
└── history.txt          # Session history file (created dynamically)
```

---

## Installation

### Prerequisites
- Python 3.8+
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open the game in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. **Home Page**:
   - Enter your username.
   - Select the grid size (4x4 or 6x6).

2. **Game Page**:
   - Flip cards by clicking on them.
   - Match pairs to complete the game.
   - Your moves and time will be tracked.

3. **Session Records**:
   - View the best score (least moves) and the shortest time for the session.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

---

