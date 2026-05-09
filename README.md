# 🌦️ Auto-Updating Weather Dashboard

This repository automatically updates every 2 hours with current weather information!

## 🌤️ Current Weather
        
### 📍 Baghajatin, Kolkata, West Bengal, India

<div align="center">
  <table>
    <tr>
      <td align="center" width="25%">
        <h3>🌡️ Temperature</h3>
        <h2>25.4°C</h2>
        <i>Feels like 30.0°C</i>
      </td>
      <td align="center" width="25%">
        <h3>☁️ Condition</h3>
        <h2>Overcast</h2>
        <i>Cloud Cover: 89%</i>
      </td>
      <td align="center" width="25%">
        <h3>💧 Atmosphere</h3>
        <h2>91%</h2>
        <i>Precipitation: 0.0 mm</i>
      </td>
      <td align="center" width="25%">
        <h3>🌬️ Wind</h3>
        <h2>8.7 km/h</h2>
        <i>Direction: NW (307°)</i>
      </td>
    </tr>
  </table>
</div>

*🕒 Last Updated: 2026-05-09 16:37:53 UTC*


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
