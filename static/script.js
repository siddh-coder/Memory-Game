const gridSize = document.getElementById('game-board').dataset.grid;
const username = document.getElementById('game-board').dataset.username;
const board = document.getElementById('game-board');
const images = ['card1.png', 'card2.png', 'card3.png', 'card4.png', 'card5.png', 'card6.png', 'card7.png', 'card8.png'];

let cards = [];
let flippedCards = [];
let matchedPairs = 0;
let moves = 0;
let timer = 0;
let timerInterval;

// Elements
const moveCounter = document.getElementById('move-counter');
const timeCounter = document.getElementById('time-counter');

// Start the timer
function startTimer() {
    timerInterval = setInterval(() => {
        timer++;
        timeCounter.textContent = timer;
    }, 1000);
}

// Stop the timer
function stopTimer() {
    clearInterval(timerInterval);
}

// Update moves
function updateMoves() {
    moves++;
    moveCounter.textContent = moves;
}

// Generate the board
function generateBoard(size) {
    const totalCards = size === '4x4' ? 16 : 36;
    const pairs = totalCards / 2;

    let cardImages = images.slice(0, pairs).concat(images.slice(0, pairs));
    cardImages.sort(() => Math.random() - 0.5);

    board.style.gridTemplateColumns = `repeat(${Math.sqrt(totalCards)}, 1fr)`;

    for (let i = 0; i < totalCards; i++) {
        const card = document.createElement('div');
        card.classList.add('card');
        card.dataset.image = cardImages[i];

        card.innerHTML = `
            <div class="card-inner">
                <div class="card-front"></div>
                <div class="card-back" style="background-image: url('/static/images/${cardImages[i]}');"></div>
            </div>
        `;

        card.addEventListener('click', flipCard);
        cards.push(card);
        board.appendChild(card);
    }
    startTimer();
}

// Flip cards
function flipCard() {
    if (this.classList.contains('flipped') || flippedCards.length === 2) return;

    this.classList.add('flipped');
    flippedCards.push(this);

    if (flippedCards.length === 2) {
        updateMoves();
        setTimeout(checkMatch, 1000);
    }
}

// Check for a match
function checkMatch() {
    const [card1, card2] = flippedCards;

    if (card1.dataset.image === card2.dataset.image) {
        matchedPairs++;
        if (matchedPairs === cards.length / 2) {
            stopTimer();
            saveGame();
            setTimeout(() => alert(`Congratulations ${username}! You won in ${moves} moves and ${timer} seconds.`), 500);
        }
    } else {
        card1.classList.remove('flipped');
        card2.classList.remove('flipped');
    }
    flippedCards = [];
}

// Save game results to the server
function saveGame() {
    fetch('/save_game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${username}&grid_size=${gridSize}&moves=${moves}&time=${timer}`
    });
}

generateBoard(gridSize);

