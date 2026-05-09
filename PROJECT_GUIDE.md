# 🌦️ Weather Auto-Commit Project

## 📖 Overview

This project automatically fetches and displays current weather data every 2 hours, committing the changes to your GitHub repository. This helps maintain your GitHub contribution streak while providing useful weather information!

## ✨ Features

- 🔄 **Automatic Updates**: Runs every 2 hours via GitHub Actions
- 🌡️ **Real Weather Data**: Fetches live weather from Open-Meteo API (free, no auth)
- 📊 **Beautiful Display**: Updates README with formatted weather information
- 🔥 **Streak Keeper**: Creates commits automatically to maintain your GitHub activity
- 🚀 **Zero Maintenance**: Set it and forget it!

## 📂 Project Structure

```
weather-auto-commit/
├── .github/
│   └── workflows/
│       └── update-weather.yml    # GitHub Actions workflow
├── update_weather.py              # Main Python script
├── README.md                      # Auto-updated weather display
├── SETUP.md                       # Setup instructions
├── .gitignore                     # Git ignore file
└── requirements.txt               # Python dependencies (none needed)
```

## 🚀 Quick Setup

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Name: `weather-auto-update` (or any name you like)
3. Visibility: **Public** (required for free GitHub Actions)
4. Don't initialize with README
5. Click "Create repository"

### Step 2: Upload Files

Upload all files from this folder to your new repository:

**Using Git:**
```bash
cd weather-auto-commit
git init
git add .
git commit -m "🌤️ Initial setup: Weather auto-update"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git push -u origin main
```

**Using GitHub Web UI:**
- Click "uploading an existing file"
- Drag all files and commit

### Step 3: Enable Actions

1. Go to repository → "Actions" tab
2. Click "I understand my workflows, go ahead and enable them"
3. Done! The workflow is now active

### Step 4: First Run (Optional but Recommended)

Manually trigger the first run:
1. Actions tab → "Update Weather Data"
2. Click "Run workflow" → "Run workflow"
3. Watch it execute!

## ⚙️ Configuration

### Change Location

Edit `update_weather.py` (lines 16-18):

```python
latitude = 22.4833    # Change to your latitude
longitude = 88.2500   # Change to your longitude  
location_name = "Your City, Country"
```

**How to find coordinates:**
- Google Maps: Right-click location → Click coordinates
- Or search: "latitude longitude of [your city]"

### Change Update Frequency

Edit `.github/workflows/update-weather.yml` (line 7):

```yaml
schedule:
  - cron: '0 */2 * * *'  # Current: Every 2 hours
  
# Other options:
# - cron: '0 */1 * * *'  # Every hour (24 commits/day)
# - cron: '0 */4 * * *'  # Every 4 hours (6 commits/day)
# - cron: '0 */6 * * *'  # Every 6 hours (4 commits/day)
# - cron: '0 0,12 * * *' # Twice daily (2 commits/day)
```

**Cron format:** `minute hour day month weekday`

## 📊 Expected Results

### Commits Per Day
- Every 2 hours = **12 commits/day**
- Every 4 hours = **6 commits/day**
- Every 6 hours = **4 commits/day**

### Contribution Graph
Your GitHub profile will show green squares every day! 🟩

### README Updates
Your repository's README will always show fresh weather data.

## 🔧 How It Works

1. **GitHub Actions** triggers on schedule (cron)
2. **Python script** fetches weather from Open-Meteo API
3. **Script updates** README.md with new data
4. **Git commits** and pushes changes automatically
5. **Your streak** stays alive! 🔥

## ⚡ Pro Tips

### Maximum Streak Benefits
- Use **public repository** (free unlimited Actions)
- Set to **every 2 hours** for frequent updates
- **Don't delete** the repository!
- Occasionally check it's running

### Avoid Issues
- Keep repository **public** (or have Actions minutes)
- Don't modify workflow file carelessly
- GitHub Actions may have delays (normal)
- Weather API is free with no rate limits

## 🐛 Troubleshooting

### Workflow Not Running?
- ✅ Check: Actions enabled in Settings → Actions
- ✅ Check: Repository is public
- ✅ Check: Workflow file has correct syntax
- ✅ Wait: First cron run may take time

### No Commits Being Made?
- Look at Actions logs for errors
- Ensure weather data is actually changing
- Verify GITHUB_TOKEN permissions (default is fine)

### Weather Not Updating?
- Check Actions logs for API errors
- Verify coordinates are correct (valid range: lat ±90, lon ±180)
- Open-Meteo API should work without auth

## 📜 License & Credits

- **Open-Meteo API**: Free weather data (no attribution required)
- **GitHub Actions**: Free for public repositories
- **Your code**: Do whatever you want with it!

## 🎯 Benefits

✅ Maintain GitHub streak effortlessly  
✅ Learn GitHub Actions and automation  
✅ Show weather data on your profile  
✅ Impress recruiters with green squares  
✅ Set-and-forget solution  

## 🤝 Contributing

This is your personal streak keeper! Fork it, modify it, improve it.

Ideas for enhancement:
- Add weather forecast (7-day)
- Include weather charts/graphs
- Add multiple locations
- Send notifications on weather changes
- Include air quality data
- Add sunrise/sunset times

## 📞 Support

If something doesn't work:
1. Check the SETUP.md file
2. Review Actions logs in your repository
3. Verify all files uploaded correctly
4. Ensure repository is public

---

**Happy streak building! May your squares always be green! 🟩🔥**
