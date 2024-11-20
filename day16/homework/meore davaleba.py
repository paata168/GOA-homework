# 5 საყვარელი ფილმი
favorite_movies = ["The Matrix", "Inception", "The Dark Knight", "The Shawshank Redemption", "Interstellar"]

# დალაგება ფილმების მიხედვით
sorted_movies = sorted(favorite_movies)

# ფილმების ელემენტების ჩაშენება <a> თეგებში
movies_with_links = [f'="#">{movie}</a>' for movie in sorted_movies]

# დაბეჭდვა
print(movies_with_links)
