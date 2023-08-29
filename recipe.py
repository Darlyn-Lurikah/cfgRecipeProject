import os
import requests

recipe_api_key = os.getenv("RECIPE_API_KEY")
print(recipe_api_key)
recipe_api_id = os.getenv("RECIPE_API_ID")
print(recipe_api_id)
api_url = f"https://api.edamam.com/api/recipes/v2?type=public&app_id={recipe_api_id}&app_key={recipe_api_key}"

r = requests.get(api_url)

print(r.status_code)
