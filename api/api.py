import requests
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
api_key = config["API_KEY"]




def fetch_image_path(tv_id=None):
    # API details
    #api_key =    #"2d93afa4fe9bcb72ba4e36370e670b79"
    image_url_template = "https://api.themoviedb.org/3/tv/{tv_id}/images"

    # Discover the most popular TV show if tv_id is not provided
    if tv_id is None:
        params = {
            "api_key": api_key,
            "language": "en-US",
            "sort_by": "popularity.desc",
        }

    # Fetch images for the TV show
    image_url = image_url_template.format(tv_id=tv_id)
    image_response = requests.get(image_url, params={"api_key": api_key})
    if image_response.status_code == 200:
        image_data = image_response.json()
        if "posters" in image_data and image_data["posters"]:
            file_path = image_data["posters"][0]["file_path"]
            full_url = f"https://image.tmdb.org/t/p/original{file_path}"
            return full_url
        else:
            raise Exception("No posters found for this TV show.")
    else:
        raise Exception(f"Failed to fetch images. Status code: {image_response.status_code}")

fetch_image_path(tv_id=15)

