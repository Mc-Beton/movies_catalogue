import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzVkNzVlYjM4MWQyMzg2MzM5NjQ1ZGM4MzM0YzljMSIsInN1YiI6IjVlZmUxNzU3NTQzN2Y1MDAzODkxZjg3MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UpL5enr_sVyJsOpXRfFTV9Fcj-ad__lxbZKHrjYvorw"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    return call_tmdb_api(f"movie/popular")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type, 8)
    return data["results"][:how_many]

def get_movie_info(title_api_path):
    return f"{title_api_path}"

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_image_url(poster_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie_cast(movie_id, how_many=4):
     return call_tmdb_api(f"movie/{movie_id}/credits")["cast"][:how_many]

def get_movies_list(list_type, how_many):
    return call_tmdb_api(f"movie/{list_type}")
