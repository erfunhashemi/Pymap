from geopy.geocoders import Nominatim
import folium
from selenium import webdriver
import time
import os

def get_location_image(location):
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="location_image_app")
    
    # Geocode the location
    location = geolocator.geocode(location)
    
    if not location:
        return "Location not found!"
    
    # Get the coordinates
    lat, lon = location.latitude, location.longitude
    
    # Create a map centered around the location
    map = folium.Map(location=[lat, lon], zoom_start=15)
    
    # Add a marker for the location
    folium.Marker([lat, lon], popup=location.address).add_to(map)
    
    # Save the map to an HTML file
    map.save("location_map.html")
    
    # Use Selenium to open the HTML file and take a screenshot
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("file:///" + os.path.abspath("location_map.html"))
    
    # Give the map some time to load
    time.sleep(3)
    
    # Take a screenshot and save it
    screenshot_path = "location_map.png"
    driver.save_screenshot(screenshot_path)
    
    # Close the browser
    driver.quit()
    
    return screenshot_path

# Example usage
location = "Eiffel Tower, Paris"  # <-- Input your location here
image_path = get_location_image(location)
print(f"Map image saved to: {image_path}")
