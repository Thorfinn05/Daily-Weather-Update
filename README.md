# 🌦️ Auto-Updating Weather Dashboard

This repository automatically updates every 2 hours with current weather information!

## 🌤️ Current Weather
        
### 📍 Baghajatin, Kolkata, West Bengal, India

<div align="center">
  <table>
    <tr>
      <td align="center" width="25%">
        <h3>🌡️ Temperature</h3>
        <h2>24.3°C</h2>
        <i>Feels like 29.1°C</i>
      </td>
      <td align="center" width="25%">
        <h3>☀️ Condition</h3>
        <h2>Clear sky</h2>
        <i>Cloud Cover: 7%</i>
      </td>
      <td align="center" width="25%">
        <h3>💧 Atmosphere</h3>
        <h2>93%</h2>
        <i>Precipitation: 0.0 mm</i>
      </td>
      <td align="center" width="25%">
        <h3>🌬️ Wind</h3>
        <h2>5.1 km/h</h2>
        <i>Direction: SW (216°)</i>
      </td>
    </tr>
  </table>
</div>

*🕒 Last Updated: 2026-05-09 22:56:12 UTC*


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
