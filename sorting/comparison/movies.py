movies = [
  {
    title: "Beetlejuice",
    year: 1988,
    genres: ["Comedy", "Fantasy"],
  },
  {
    title: "The Cotton Club",
    year: 1984,
    genres: ["Crime", "Drama", "Music"],
  },
  {
    title: "The Shawshank Redemption",
    year: 1994,
    genres: ["Crime", "Drama"],
  },
  {
    title: "Crocodile Dundee",
    year: 1986,

    genres: ["Adventure", "Comedy"],
  },
  {
    title: "Valkyrie",
    year: 2008,
    genres: ["Drama", "History", "Thriller"],
  },
  {
    title: "Ratatouille",
    year: 2007,
    genres: ["Animation", "Comedy", "Family"],
  },
  {
    title: "City of God",
    year: 2002,

    genres: ["Crime", "Drama"],
  },
  {
    title: "Memento",
    year: 2000,

    genres: ["Mystery", "Thriller"],
  },
  {
    title: "The Intouchables",
    year: 2011,

    genres: ["Biography", "Comedy", "Drama"],
  },
  {
    title: "Stardust",
    year: 2007,
    genres: ["Adventure", "Family", "Fantasy"],
  },
]

def sort_movies_by_year(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_movies_by_title(movies):
    def remove_leading_words(title):
        words_to_remove = ["A", "An", "The"]
        for word in words_to_remove:
            if title.startswith(word + " "):
                return title[len(word) + 1:]
        return title

    return sorted(movies, key=lambda movie: remove_leading_words(movie['title']))

# Test the functions with the provided sample data
movies = [
    # The sample data provided in movies.py
]

# Test #1
result1 = sort_movies_by_year(movies)
print([movie['title'] for movie in result1])  # Output should match expected1

# Test #2
result2 = sort_movies_by_title(movies)
print([movie['title'] for movie in result2])  # Output should match expected2
