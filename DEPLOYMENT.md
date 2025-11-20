# 🚀 Deployment Guide - Streamlit Community Cloud (FREE)

This guide will walk you through deploying Operation SecureFlow to Streamlit Community Cloud - completely free!

## Prerequisites
- GitHub account (free)
- Streamlit Community Cloud account (free - sign up with GitHub)

## Step-by-Step Deployment

### 1. Push Your Code to GitHub

First, create a new repository on GitHub:
1. Go to https://github.com/new
2. Name your repository: `operation-secureflow` (or any name you prefer)
3. Keep it **Public** (required for free Streamlit hosting)
4. **Do NOT** initialize with README (we already have one)
5. Click "Create repository"

Then push your local code to GitHub:

```bash
# Add your GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/operation-secureflow.git

# Rename branch to main (optional but recommended)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 2. Sign Up for Streamlit Community Cloud

1. Go to https://share.streamlit.io/
2. Click "Sign up"
3. Choose "Continue with GitHub"
4. Authorize Streamlit to access your GitHub account

### 3. Deploy Your App

1. Once logged in, click **"New app"**
2. Fill in the deployment form:
   - **Repository:** Select `YOUR_USERNAME/operation-secureflow`
   - **Branch:** `main`
   - **Main file path:** `secureflow_demo.py`
   - **App URL (optional):** Choose a custom subdomain like `secureflow-demo`

3. Click **"Deploy!"**

### 4. Wait for Deployment

Streamlit will:
- Clone your repository
- Install dependencies from `requirements.txt`
- Start your app
- Provide you with a public URL

This typically takes 2-3 minutes.

### 5. Access Your Live App

Once deployed, your app will be available at:
```
https://YOUR-APP-NAME.streamlit.app
```

For example: `https://secureflow-demo.streamlit.app`

## Updating Your App

Any time you push changes to GitHub, Streamlit will automatically redeploy:

```bash
# Make your changes to the code
git add .
git commit -m "Update features"
git push
```

The app will automatically update within 1-2 minutes!

## Troubleshooting

### Issue: "App is sleeping"
**Solution:** Free tier apps sleep after inactivity. Just click "Wake up" or visit the URL to restart it.

### Issue: Dependencies not installing
**Solution:** Ensure `requirements.txt` lists all packages with correct versions.

### Issue: App crashing on startup
**Solution:** Check the logs in the Streamlit Cloud dashboard. Common issues:
- Missing environment variables
- Incorrect file paths
- Memory limits exceeded

## Features of Free Tier

- **Unlimited public apps**
- **1 private app**
- **1 GB RAM per app**
- **1 CPU core**
- **Automatic SSL certificates**
- **Auto-updates from GitHub**
- **Community support**

## Current Status

Your local repository is ready for deployment! You just need to:
1. Create a GitHub repository
2. Push the code
3. Deploy via Streamlit Community Cloud

---

## Alternative: Deploy via CLI

You can also use GitHub CLI for faster setup:

```bash
# Install GitHub CLI (if not installed)
brew install gh  # macOS
# or visit: https://cli.github.com/

# Authenticate
gh auth login

# Create repository and push
gh repo create operation-secureflow --public --source=. --remote=origin --push

# Then deploy via Streamlit Cloud web interface
```

---

**Need help?** Visit https://docs.streamlit.io/streamlit-community-cloud
