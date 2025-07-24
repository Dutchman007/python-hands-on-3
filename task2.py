"""
Task 2: Film Night Prep
You're helping your community plan a Friday Film Night for kids. The initial list of movie genres to be shown includes:
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

1. Add the genre "Drama" at the end of the list because parents requested it.
2. Someone mistakenly added "Fantasy" twice. Make sure there's only one "Fantasy" in the list.
3. The organizer wants to know how many genres are now planned to be shown.
4. Display the second and second-to-last genres to verify diversity.

→ Modify the list and display the required results.
"""

genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]
print(genres)

genres.append("Drama")
print(genres)

genres.remove(genres[3])
print(genres)

print(len(genres))

second = genres[1]
second_to_last = genres[5]
print(f"Some of our Movie Genre selections include {second} and {second_to_last}")
