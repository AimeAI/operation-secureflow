# 🚀 Deploy to Render (FREE) - Get Your Live Link

## Quick Deploy (2 Minutes)

### Step 1: Sign Up for Render
1. Go to: **https://render.com/**
2. Click **"Get Started"** or **"Sign Up"**
3. Choose **"Sign up with GitHub"**
4. Authorize Render to access your repositories

### Step 2: Deploy Your App
1. Once logged in, click **"New +"** in the top right
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - If prompted, click **"Configure account"** to grant Render access
   - Search for and select: **`operation-secureflow`**
4. Configure the service:
   - **Name:** `operation-secureflow` (or your preferred name)
   - **Region:** Choose closest to you (e.g., Oregon, Ohio, Frankfurt)
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run secureflow_demo.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`
5. Select **Free** plan
6. Click **"Create Web Service"**

### Step 3: Wait for Deployment
- Render will build and deploy your app (3-5 minutes)
- Watch the logs to see progress
- Once you see "Your service is live 🎉", it's ready!

### Step 4: Get Your Live Link
Your app will be available at:
```
https://operation-secureflow.onrender.com
```

Or whatever name you chose:
```
https://[your-service-name].onrender.com
```

---

## ⚡ Alternative: One-Click Deploy

Click this button to deploy directly:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/AimeAI/operation-secureflow)

---

## 🎯 What You Get (FREE):

- ✅ **750 hours/month** free (enough for full-time hosting)
- ✅ **Public URL with SSL**
- ✅ **Automatic deploys** from GitHub
- ✅ **512MB RAM, shared CPU**
- ✅ **Sleep after 15 min inactivity** (wakes up automatically)

---

## 📝 Notes

- **Free tier sleeps:** App goes to sleep after 15 minutes of inactivity
- **Wake up time:** First request after sleep takes ~30 seconds
- **Keep alive:** Use a service like UptimeRobot to ping your app every 14 minutes
- **Upgrade:** $7/month for always-on service

---

## 🔧 Troubleshooting

**Issue:** Build fails with "requirements not found"
- **Solution:** Make sure `requirements.txt` is in the root directory

**Issue:** App crashes on startup
- **Solution:** Check logs in Render dashboard. Common issues:
  - Port binding (should use `$PORT` environment variable)
  - Missing dependencies

**Issue:** App is slow to respond
- **Solution:** Free tier has limited resources. Upgrade to paid plan for better performance.

---

## 🎉 Next Steps

Once deployed:
1. Share your live link: `https://[your-app].onrender.com`
2. Test all features (Security Monitor, Performance Analytics, etc.)
3. Any changes you push to GitHub will auto-deploy!

---

**Your GitHub Repo:** https://github.com/AimeAI/operation-secureflow
**Ready to deploy!** Just follow the steps above.
