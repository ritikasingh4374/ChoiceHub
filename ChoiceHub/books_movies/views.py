from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .forms import LoginForm
from .models import Book, Registration
from django.urls import reverse
import json
from django.http import HttpResponseRedirect
from .forms import BookPreferenceForm

# View for the index page
def index(request):
    return render(request, 'index.html')

# View to display the list of books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books_movies/book_list.html', {'books': books})

# View for user registration
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Registration.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'register.html')

        # Create a new registration
        registration = Registration(name=name, email=email, password=password)
        registration.save()  # Password is hashed in the model's save() method

        # Add a success message
        messages.success(request, 'Registration successful!')

        # Log the user in by saving their session
        request.session['user_id'] = registration.id

        return redirect('index')  # Redirect to the home page after registration

    return render(request, 'register.html')

# View for user login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Registration.objects.get(email=email)  # Check if email exists
                if check_password(password, user.password):  # Verify password using check_password
                    request.session['user_id'] = user.id  # Save user ID in session
                    messages.success(request, "Login successful!")
                    return redirect('index')  # Redirect to home page after login
                else:
                    messages.error(request, "Invalid login credentials")
            except Registration.DoesNotExist:
                messages.error(request, "User not found. Please register.")
    else:
        form = LoginForm()
    
    return render(request, 'books_movies/login.html', {'form': form})

# View for user logout
def logout_view(request):
    request.session.flush()  # Clear the session data to log out
    return redirect('login')  # Redirect to the login page after logout

def quiz(request):
    return render(request, 'books_movies/quiz.html')


def book_recommendations_view(request):
    # Get the filtered book IDs from the session
    book_ids = request.session.get('filtered_books', [])
    print(12324)
    if book_ids:
        # Fetch the actual book objects from the database
        books = Book.objects.filter(id__in=book_ids)
        print(f"Rendering {books.count()} books")  # Debugging statement
    else:
        books = []
        print("No books found")

    return render(request, 'books_movies/recommendation.html', {'books': books})

def book_quiz_view(request):
    # Start with all books in temp_db1 (queryset for efficiency)
    temp_db1 = Book.objects.all()

    # Dictionary of attributes to filter on
    filter_attributes = {
        'genre': 'Genre',
        'writing_style': 'Writing Style',
        'setting': 'Setting',
        'mood': 'Mood',
        'length': 'Length',
        'pace': 'Pace',
        'ending': 'Ending',
        'emotional_tone': 'Emotional Tone',
        'romance': 'Romance',
        'narrative_style': 'Narrative Style',
        'world_building_importance': 'World-building Importance',
    }
    print(temp_db1)
    if request.method == 'POST':
        form = BookPreferenceForm(request.POST)
        print(answers)

        if form.is_valid():
            # Store answers in session
            answers = form.cleaned_data
            request.session['quiz_answers'] = answers
            # Filter books progressively using the answers
            for question_key, answer in answers.items():
                if question_key in filter_attributes and answer:  # Ensure answer is not empty
                    # Filter books based on the current attribute
                    temp_db1 = temp_db1.filter(**{question_key: answer})

                    # If the filtered books are 4 or fewer, stop filtering and redirect
                    if temp_db1.count() <= 4:
                        book_ids = list(temp_db1.values_list('id', flat=True))  # Get book IDs
                        # Store filtered books in session
                        request.session['recommendations'] = book_ids
                        return redirect('recommendations')

            # After processing all questions, redirect with the filtered books
            book_ids = list(temp_db1.values_list('id', flat=True))  # Get final filtered book IDs
            request.session['recommendations'] = book_ids
            return redirect('recommendations')

    else:
        form = BookPreferenceForm()

    return render(request, 'books_movies/recommendation.html', {'form': form})
