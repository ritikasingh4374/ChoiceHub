// Select all cards
const cards = document.querySelectorAll('.card');

// Function to show the active card and hide all others
function showCard(cardId) {
    cards.forEach((card) => {
        if (card.id === cardId) {
            card.classList.add('active'); // Show the active card with transition
            card.classList.remove('hidden'); // Remove hidden class to make sure it transitions in
        } else {
            card.classList.remove('active');
            card.classList.add('hidden'); // Hide the inactive card
        }
    });
}

// Function to move to the next card
function nextCard(cardId) {
    const currentCardIndex = Array.from(cards).findIndex(c => c.id === cardId);
    const nextCard = cards[currentCardIndex + 1];

    if (nextCard) {
        showCard(nextCard.id); // Show the next card with a transition
    } else {
        console.log("No more cards.");
    }
}

// Function to handle option click and move to the next card
function submitAnswerAndNext(cardId) {
    nextCard(cardId); // Move to the next card
}

// Add event listeners to option buttons
cards.forEach((card) => {
    const options = card.querySelectorAll('.option');
    options.forEach((option) => {
        option.addEventListener('click', () => {
            submitAnswerAndNext(card.id); // Move to the next card when an option is clicked
        });
    });
});

// Initialize the first card as active
if (cards.length > 0) {
    showCard(cards[0].id); // Show the first card only
} else {
    console.log('No cards found.');
}

let currentQuestionIndex = 1;
const totalQuestions = 10;

// Function to select an option
function selectOption(element, question, value) {
// Remove 'selected' class from all options in the current question
const options = document.querySelectorAll(`#${question} .option`);
options.forEach(option => option.classList.remove('selected'));

// Add 'selected' class to the clicked option
element.classList.add('selected');

// Set the value of the corresponding hidden input
const hiddenInput = document.querySelector(`input[name='${question}']`);
if (hiddenInput) {
hiddenInput.value = value;
} else {
console.error(`Hidden input for ${question} not found.`);
}

// Move to the next question after selection
nextQuestion();
}

// Function to move to the next question
function nextQuestion() {
// Hide the current question card
const currentCard = document.getElementById(`question${currentQuestionIndex}`);
currentCard.style.display = 'none';

// Increment to show the next question
currentQuestionIndex++;

if (currentQuestionIndex <= totalQuestions) {
// Show next question card
const nextCard = document.getElementById(`question${currentQuestionIndex}`);
nextCard.style.display = 'block';
} else {
// All questions answered, store the data in session storage
console.log("All questions answered, storing data in session storage...");

// Collect form data
const formData = new FormData(document.getElementById('quizForm'));

// Convert FormData to a plain object
const dataObject = Object.fromEntries(formData);

// Store data in session storage
sessionStorage.setItem('quizData', JSON.stringify(dataObject));

// Redirect to the recommendation page
window.location.href = '/recommendation';
}
}

// Initially show the first question only
window.onload = function() {
for (let i = 2; i <= totalQuestions; i++) {
document.getElementById(`question${i}`).style.display = 'none';
}
};
