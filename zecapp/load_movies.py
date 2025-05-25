from datetime import date, timedelta
import random
from zecapp.models import Movie, MovieDetail, Director, Genre

directors = list(Director.objects.all())
genres = list(Genre.objects.all())

if not directors or not genres:
    print("❌ Please add some directors and genres first.")
else:
    MovieDetail.objects.all().delete()
    Movie.objects.all().delete()

    movie_data = [
        {
            "title": "Edge of Tomorrow",
            "description": "A soldier stuck in a time loop relives a battle against alien invaders.",
        },
        {
            "title": "La La Land",
            "description": "A jazz pianist and an aspiring actress fall in love while pursuing their dreams.",
        },
        {
            "title": "Interstellar",
            "description": "A team travels through a wormhole in space in an attempt to save humanity.",
        },
        {
            "title": "The Grand Budapest Hotel",
            "description": "A whimsical tale of a concierge who is framed for murder at a luxurious European hotel.",
        },
        {
            "title": "Parasite",
            "description": "A poor family infiltrates a wealthy household leading to unforeseen consequences.",
        },
        {
            "title": "The Dark Knight",
            "description": "Batman faces his greatest challenge in the form of the Joker.",
        },
        {
            "title": "Spirited Away",
            "description": "A young girl becomes trapped in a mysterious spirit world and must find her way back.",
        },
        {
            "title": "The Imitation Game",
            "description": "The story of Alan Turing and his efforts to crack Nazi codes during WWII.",
        },
         {
        "title": "Spirited Away",
        "description": "A young girl becomes trapped in a mysterious spirit world and must find her way back.",
    },
    {
        "title": "The Imitation Game",
        "description": "The story of Alan Turing and his efforts to crack Nazi codes during WWII.",
    },
    {
        "title": "Inception",
        "description": "A thief who steals corporate secrets through dream-sharing technology is given an inverse task of planting an idea into a CEO's mind.",
    },
    {
        "title": "The Shawshank Redemption",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    },
    {
        "title": "Forrest Gump",
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, and more through the perspective of an Alabama man with a low IQ.",
    },
    {
        "title": "The Matrix",
        "description": "A computer hacker learns about the true nature of his reality and his role in the war against its controllers.",
    },
    {
        "title": "Gladiator",
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
    },
    {
        "title": "The Lion King",
        "description": "A young lion prince flees his kingdom after the death of his father, only to learn the true meaning of responsibility and bravery.",
    },
    {
        "title": "Titanic",
        "description": "A love story unfolds aboard the ill-fated RMS Titanic during its maiden voyage.",
    },
    {
        "title": "Jurassic Park",
        "description": "Scientists clone dinosaurs to create a theme park, but things go terribly wrong when the creatures escape.",
    },
    ]

    for item in movie_data:
        director = random.choice(directors)
        movie = Movie.objects.create(
            title=item["title"],
            description=item["description"],
            director=director,
        )
        movie.genres.set(random.sample(genres, 2))

        MovieDetail.objects.create(
            movie=movie,
            release_date=date(2010, 1, 1) + timedelta(days=random.randint(0, 365 * 10)),
            duration=random.randint(90, 180),
            budget=random.randint(10_000_000, 250_000_000),
        )

    print("✅ Dummy movie data added.")
