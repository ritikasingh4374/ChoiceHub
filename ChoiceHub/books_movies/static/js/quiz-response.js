let selectedAnswers = {
    genre: null,
    writing_style: null,
    setting: null,
    mood: null,
    length: null,
    pace: null,
    ending: null,
    emotional_tone: null,
    romance: null,
    world_building: null
};

function selectOption(element, category, value) {
    // Store the selected value for the current category
    selectedAnswers[category] = value;

    // Visual feedback to indicate the selected option (you can style this as needed)
    let options = element.parentElement.getElementsByClassName('option');
    for (let i = 0; i < options.length; i++) {
        options[i].classList.remove('selected');
    }
    element.classList.add('selected');

    // Check if all questions have been answered
    if (Object.values(selectedAnswers).every(answer => answer !== null)) {
        // All questions have been answered, redirect to the recommendation page
        // You can also send the answers to the server or handle them as needed
        window.location.href = "{% url 'books_movies/recommendation' %}"; // Update with your actual recommendation page URL
    }
}
