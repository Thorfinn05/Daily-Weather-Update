# 🌦️ Auto-Updating Weather Dashboard

This repository automatically updates every 2 hours with current weather information!

## 🌤️ Current Weather

**Location:** Kolkata, West Bengal, India

**Temperature:** 32.6°C  
**Feels Like:** 37.9°C  
**Condition:** Thunderstorm  
**Humidity:** 71%  
**Wind Speed:** 16.9 km/h  
**Wind Direction:** SSW (202°)  
**Cloud Cover:** 66%  
**Precipitation:** 0.0 mm  

**Last Updated:** 2026-05-26 02:33:26 UTC  
**Update #:** 1779762806


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
