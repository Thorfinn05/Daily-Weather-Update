#!/usr/bin/env python3
"""
Weather Auto-Update Script
Fetches current weather data and updates README.md
"""

import json
import os
from datetime import datetime
import urllib.request
import urllib.error
import time

def get_weather():
    """Fetch weather data from Open-Meteo API (no auth required)"""
    try:
        # Default location: Maheshtala, West Bengal, India
        # Coordinates: 22.4833° N, 88.2500° E
        # Change these coordinates for your location
        latitude = 22.5726
        longitude = 88.3639
        location_name = "Kolkata, West Bengal, India"
        
        # Open-Meteo API - free, no authentication required
        url = (f"https://api.open-meteo.com/v1/forecast?"
               f"latitude={latitude}&longitude={longitude}"
               f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,"
               f"precipitation,weather_code,cloud_cover,wind_speed_10m,wind_direction_10m"
               f"&timezone=auto")
        
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            data['location_name'] = location_name
            return data
    except urllib.error.URLError as e:
        print(f"Error fetching weather: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def format_weather_data(data):
    """Format weather data into a readable string"""
    if not data:
        return "Weather data unavailable"
    
    try:
        current = data['current']
        location = data.get('location_name', 'Unknown Location')
        
        # Weather code descriptions
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Foggy", 48: "Depositing rime fog",
            51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
            71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
            85: "Slight snow showers", 86: "Heavy snow showers",
            95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
        }
        
        weather_desc = weather_codes.get(current.get('weather_code', 0), "Unknown")
        
        # Wind direction
        wind_dir = current.get('wind_direction_10m', 0)
        directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 
                     'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        wind_direction = directions[int((wind_dir + 11.25) / 22.5) % 16]
        
        # Get current timestamp with run count to ensure uniqueness
        timestamp = datetime.utcnow()
        run_id = int(time.time())  # Unix timestamp ensures every run is unique
        
        weather_info = f"""## 🌤️ Current Weather

**Location:** {location}

**Temperature:** {current.get('temperature_2m', 'N/A')}°C  
**Feels Like:** {current.get('apparent_temperature', 'N/A')}°C  
**Condition:** {weather_desc}  
**Humidity:** {current.get('relative_humidity_2m', 'N/A')}%  
**Wind Speed:** {current.get('wind_speed_10m', 'N/A')} km/h  
**Wind Direction:** {wind_direction} ({wind_dir}°)  
**Cloud Cover:** {current.get('cloud_cover', 'N/A')}%  
**Precipitation:** {current.get('precipitation', 'N/A')} mm  

**Last Updated:** {timestamp.strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Update #:** {run_id}
"""
        return weather_info
    except (KeyError, IndexError) as e:
        print(f"Error parsing weather data: {e}")
        return "Weather data format error"

def update_readme(weather_info):
    """Update README.md with new weather information"""
    readme_content = f"""# 🌦️ Auto-Updating Weather Dashboard

This repository automatically updates every 2 hours with current weather information!

{weather_info}

---

### 📊 Repository Stats
- **Auto-updates:** Every 2 hours
- **Powered by:** GitHub Actions & Open-Meteo API
- **Total Commits:** Check the commit history!

### 🔧 How It Works
This project uses GitHub Actions workflow that runs every 2 hours to:
1. Fetch current weather data from Open-Meteo API
2. Update this README
3. Commit changes automatically

This keeps your GitHub activity streak alive! 🔥

### 🚀 Setup Your Own
1. Fork this repository
2. Enable GitHub Actions in your fork
3. The workflow will start running automatically
4. (Optional) Modify `update_weather.py` to change the location coordinates

### 📍 Change Location
Edit `update_weather.py` and update these values:
```python
latitude = 22.4833    # Your latitude
longitude = 88.2500   # Your longitude
location_name = "Your City, Country"
```

### 📝 Note
This is an automated weather tracker that helps maintain GitHub contribution streaks while providing useful weather information.

---
*Generated automatically by GitHub Actions | Data from [Open-Meteo](https://open-meteo.com/)*
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md updated successfully!")

def main():
    """Main function"""
    print("Fetching weather data...")
    weather_data = get_weather()
    
    print("Formatting weather information...")
    weather_info = format_weather_data(weather_data)
    
    print("Updating README.md...")
    update_readme(weather_info)
    
    print("Done!")

if __name__ == "__main__":
    main()
