# Setup Instructions

## 🚀 Quick Start Guide

Follow these steps to set up your auto-updating weather repository:

### 1. Create a New GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Name your repository (e.g., `weather-auto-update`)
3. Choose **Public** (required for free GitHub Actions)
4. **DO NOT** initialize with README (we already have one)
5. Click "Create repository"

### 2. Upload Your Project Files

#### Option A: Using Git Command Line

```bash
cd weather-auto-commit
git init
git add .
git commit -m "Initial commit: Weather auto-update setup"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

#### Option B: Using GitHub Web Interface

1. Open your new repository
2. Click "uploading an existing file"
3. Drag and drop all files from the `weather-auto-commit` folder
4. Commit the changes

### 3. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. If prompted, click "I understand my workflows, go ahead and enable them"
4. The workflow should now be enabled automatically

### 4. Test the Workflow

#### Manual Trigger (Recommended for First Test)

1. Go to "Actions" tab
2. Click on "Update Weather Data" workflow
3. Click "Run workflow" button
4. Select "main" branch
5. Click "Run workflow"
6. Wait a few seconds and refresh to see it running

#### Automatic Schedule

The workflow will automatically run every 2 hours based on the schedule:
- `0 */2 * * *` means "at minute 0 of every 2nd hour"
- Examples: 00:00, 02:00, 04:00, 06:00, etc. (UTC time)

### 5. Customize Your Location (Optional)

Edit `update_weather.py` and change the location:

```python
# Find this line (around line 15):
location = "Maheshtala"

# Change to your city:
location = "London"  # or any city name
```

Commit the change:
```bash
git add update_weather.py
git commit -m "Update location"
git push
```

### 6. Adjust Update Frequency (Optional)

Edit `.github/workflows/update-weather.yml` to change the schedule:

```yaml
schedule:
  - cron: '0 */2 * * *'  # Every 2 hours
  # - cron: '0 */1 * * *'  # Every hour
  # - cron: '0 */4 * * *'  # Every 4 hours
  # - cron: '0 0 * * *'    # Once daily at midnight
  # - cron: '0 */6 * * *'  # Every 6 hours
```

## 📋 Requirements Checklist

- ✅ GitHub account
- ✅ Public repository (for free GitHub Actions)
- ✅ GitHub Actions enabled
- ✅ Internet connection for the weather API

## 🔍 Troubleshooting

### Workflow Not Running

1. Check if Actions are enabled in repository settings
2. Ensure the repository is public (or you have GitHub Actions minutes)
3. Check the Actions tab for any error messages

### Weather Data Not Updating

1. Check if the API is accessible (wttr.in)
2. Verify the location name is correct
3. Look at workflow logs for error messages

### No Commits Being Made

1. Check if README.md is actually changing
2. Verify the workflow has permission to commit
3. Look for "No changes detected" in workflow logs

## 🎯 Expected Results

- **Commits:** Multiple commits per day (up to 12 with 2-hour schedule)
- **Contribution Graph:** Green squares every day the workflow runs
- **README Updates:** Fresh weather data every 2 hours

## 🔒 Permissions

The workflow uses `GITHUB_TOKEN` which is automatically provided by GitHub. No additional secrets needed!

## ⚡ Tips for Maximum Streak

1. Keep the repository public (free Actions)
2. Use a 2-hour schedule for frequent updates
3. Occasionally check that the workflow is running
4. Don't delete the repository!
5. GitHub Actions have usage limits on private repos

## 📧 Support

If you encounter issues:
1. Check the workflow logs in the Actions tab
2. Verify all files are uploaded correctly
3. Ensure the repository is public
4. Make sure GitHub Actions are enabled

---

**Happy streak building! 🔥**
