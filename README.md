# 🌦️ Auto-Updating Weather Dashboard

This repository automatically updates every 2 hours with current weather information!

## 🌤️ Current Weather

**Location:** Kolkata, West Bengal, India

**Temperature:** 27.6°C  
**Feels Like:** 33.2°C  
**Condition:** Partly cloudy  
**Humidity:** 88%  
**Wind Speed:** 9.4 km/h  
**Wind Direction:** SSE (160°)  
**Cloud Cover:** 61%  
**Precipitation:** 0.0 mm  

**Last Updated:** 2026-07-18 16:47:30 UTC  
**Update #:** 1784393250


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
