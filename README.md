# 🌦️ Auto-Updating Weather Dashboard

This repository automatically updates every 2 hours with current weather information!

## 🌤️ Current Weather

**Location:** Kolkata, West Bengal, India

**Temperature:** 28.4°C  
**Feels Like:** 34.0°C  
**Condition:** Thunderstorm  
**Humidity:** 89%  
**Wind Speed:** 14.3 km/h  
**Wind Direction:** S (185°)  
**Cloud Cover:** 37%  
**Precipitation:** 0.0 mm  

**Last Updated:** 2026-05-15 17:14:56 UTC  
**Update #:** 1778865296


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
