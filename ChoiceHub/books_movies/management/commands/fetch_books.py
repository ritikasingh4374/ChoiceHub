# books/management/commands/fetch_books.py

import requests
from django.core.management.base import BaseCommand
from books_movies.models import Book

class Command(BaseCommand):
    help = 'Fetch all books from an external API and store them in the database'

    def handle(self, *args, **kwargs):
        genres = [
            'art', 'biography', 'computers', 'fantasy', 'historical fiction', 
            'horror', 'mystery', 'romance', 'science fiction', 'thriller', 
            'young adult', 'children', 'non-fiction', 'self-help', 
            'health', 'business', 'travel', 'cookbooks', 'education'
        ]

        max_results_per_request = 40
        for genre in genres:
            start_index = 0
            total_items = float('inf')
            
            while start_index < total_items:
                api_url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre.replace(' ', '+')}&startIndex={start_index}&maxResults={max_results_per_request}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    books_data = response.json()
                    total_items = books_data.get('totalItems', 0)
                    
                    if total_items == 0:
                        break
                    
                    for item in books_data.get('items', []):
                        book_info = item['volumeInfo']
                        title = book_info.get('title', 'Unknown Title')
                        author = ', '.join(book_info.get('authors', ['Unknown Author']))
                        book_genre = ', '.join(book_info.get('categories', ['Unknown Genre']))
                        description = book_info.get('description', '')
                        cover_image = book_info.get('imageLinks', {}).get('thumbnail', '')
                        reviews = ''  # Logic for fetching reviews can be implemented if available

                        # Logic to derive other details
                        themes = description[:200]
                        character_vs_plot = 'Character' if 'character' in description.lower() else 'Plot'
                        writing_style = 'Fast-paced' if len(description) < 500 else 'Descriptive'
                        setting = 'Unknown'
                        mood = 'Dark' if 'mystery' in description.lower() else 'Light-hearted'

                        book_exists = Book.objects.filter(title=title, author=author).exists()

                        if not book_exists:
                            Book.objects.create(
                                title=title,
                                author=author,
                                genre=book_genre,
                                themes=themes,
                                character_vs_plot=character_vs_plot,
                                writing_style=writing_style,
                                setting=setting,
                                mood=mood,
                                api_source='Google Books API',
                                cover_image=cover_image,
                                description=description,
                                reviews=reviews
                            )
                            self.stdout.write(self.style.SUCCESS(f'Successfully added book: {title}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Book "{title}" by {author} already exists. Skipping...'))

                    start_index += max_results_per_request
                else:
                    self.stdout.write(self.style.ERROR(f"Failed to fetch data for genre: {genre}. Status code: {response.status_code}"))
                    break
