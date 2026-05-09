# ⚡ QUICK START - Weather Auto-Commit

## 🎯 What You Got

A complete GitHub project that:
- ✅ Updates weather every 2 hours automatically
- ✅ Commits changes to keep your GitHub streak alive
- ✅ Requires ZERO maintenance after setup
- ✅ Works with free GitHub Actions

## 🚀 Setup in 5 Minutes

### 1️⃣ Create GitHub Repo
- Go to: https://github.com/new
- Name: `weather-auto-update`
- Make it **PUBLIC** (important!)
- DON'T add README
- Click "Create repository"

### 2️⃣ Upload These Files
Choose one method:

**Method A - Command Line (Git):**
```bash
cd weather-auto-commit
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git push -u origin main
```

**Method B - Web Upload:**
- Open your new repo
- Click "uploading an existing file"
- Drag ALL files from `weather-auto-commit` folder
- Commit!

### 3️⃣ Enable GitHub Actions
- Go to "Actions" tab in your repo
- Click "Enable Actions" if prompted
- Done!

### 4️⃣ Test It (Optional)
- Actions tab → "Update Weather Data" workflow
- Click "Run workflow"
- Watch it work!

## 📁 Files Included

```
weather-auto-commit/
├── .github/workflows/
│   └── update-weather.yml    # The automation magic
├── update_weather.py          # Fetches & formats weather
├── README.md                  # Gets auto-updated
├── PROJECT_GUIDE.md          # Full documentation
├── SETUP.md                  # Detailed setup guide
├── requirements.txt          # No dependencies!
└── .gitignore               # Git ignore rules
```

## ⚙️ Customize (Optional)

### Change Your Location
Edit `update_weather.py` lines 16-18:
```python
latitude = YOUR_LATITUDE
longitude = YOUR_LONGITUDE
location_name = "Your City, Country"
```

Find coordinates: Google Maps → Right-click → Click coordinates

### Change Update Frequency
Edit `.github/workflows/update-weather.yml` line 7:
```yaml
- cron: '0 */2 * * *'  # Every 2 hours (current)
- cron: '0 */1 * * *'  # Every hour (more commits!)
- cron: '0 */4 * * *'  # Every 4 hours
```

## 📊 What to Expect

- **Commits per day**: 12 (with 2-hour schedule)
- **First update**: Within 2 hours of setup
- **Manual trigger**: Anytime via Actions tab
- **Green squares**: Every single day! 🟩

## ✅ Checklist

Before you start:
- [ ] GitHub account ready
- [ ] Want to create PUBLIC repo
- [ ] Files downloaded/unzipped
- [ ] 5 minutes of time

After setup:
- [ ] Files uploaded to GitHub
- [ ] Actions enabled
- [ ] First workflow run successful
- [ ] README shows weather data

## 🎯 Success Indicators

You'll know it's working when:
1. Actions tab shows green checkmarks ✅
2. README displays current weather 🌤️
3. Commit history shows auto-commits 📝
4. Your profile shows activity 🟩

## 🐛 Quick Fixes

**Not running?**
- Make repo public
- Check Actions are enabled

**No commits?**
- Check Actions logs for errors
- Weather might be unchanged (normal)

**Wrong location?**
- Update coordinates in `update_weather.py`
- Commit the change

## 📖 Need More Help?

Read these files in order:
1. **SETUP.md** - Step-by-step setup
2. **PROJECT_GUIDE.md** - Complete documentation
3. **Actions logs** - See what's happening

## 🎉 That's It!

Your GitHub streak keeper is ready. It will:
- Run automatically every 2 hours
- Fetch real weather data
- Update your README
- Commit changes
- Keep your streak alive 🔥

**No further action needed from you!**

---

Made with ❤️ for GitHub streak enthusiasts

Questions? Check PROJECT_GUIDE.md for full details!
