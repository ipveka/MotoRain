# 🚀 Deploy Telegram Bot to Render

Deploy MotoRain bot to [Render.com](https://render.com).

## ⚠️ Important Note

**Render's free tier doesn't support Chrome/Selenium** (needed for radar scraping). You have two options:

### Option A: Deploy Backend + Bot Separately (Recommended)
- **Backend:** Deploy to a service that supports Chrome (Railway, Fly.io, or paid Render)
- **Bot:** Deploy to Render free tier
- **Cost:** ~$5-7/month

### Option B: Run Bot Only on Render (Free)
- Deploy only the bot to Render
- Run backend locally on your computer
- **Cost:** $0 (but your PC must stay on)

---

## Option B: Bot Only (FREE)

This deploys just the Telegram bot. You'll run the backend locally.

### 1. Deploy Bot to Render

1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **"New +"** → **"Background Worker"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `motorain-bot`
   - **Build Command:** `pip install -r telegram_bot/requirements.txt && pip install -r backend/requirements.txt`
   - **Start Command:** `python telegram_bot/bot.py`
   - **Plan:** Free
5. Click **"Environment"** in sidebar
6. Add environment variables:
   - **Key:** `TELEGRAM_TOKEN` → **Value:** Your bot token from BotFather
   - **Key:** `BACKEND_BASE_URL` → **Value:** Your backend URL (see step 2)
7. Click **"Create Background Worker"**

### 2. Run Backend Locally

On your computer:
```bash
cd backend
python -m uvicorn app_mobile:app --host 0.0.0.0 --port 8001
```

Then expose it with [ngrok](https://ngrok.com) (free):
```bash
ngrok http 8001
```

Copy the ngrok URL (e.g., `https://abc123.ngrok.io`) and set it as `BACKEND_BASE_URL` in Render.

---

## Option A: Full Deployment (Paid)

For a fully cloud-hosted solution, use **Railway** or **Fly.io** instead of Render:

### Railway ($5/month)
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
railway init
railway up

# Set environment variable
railway variables set TELEGRAM_TOKEN=your_token
```

### Fly.io (Free tier available)
```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Deploy backend
fly launch --name motorain-backend

# Deploy bot
fly launch --name motorain-bot
fly secrets set TELEGRAM_TOKEN=your_token
```

See [Railway](https://railway.app) or [Fly.io](https://fly.io) for details

---

## Test It!

1. Open Telegram and find your bot
2. Send `/start`
3. Enter addresses when prompted
4. You should get a radar map!

---

## Troubleshooting

### Bot not responding?
- Check bot logs: Go to bot service → Logs tab
- Verify `TELEGRAM_TOKEN` is correct
- Ensure `BACKEND_BASE_URL` starts with `https://`

### "Radar data not available"?
- Wait 2-3 minutes after backend starts (radar scraping takes time)
- Check backend logs for errors

### Backend failing?
- Check logs for specific errors
- Ensure Python 3.8+ is being used
- Verify all dependencies are in `requirements.txt`

---

## Cost

- **Free tier:** Both services free, backend spins down after 15 min inactivity
- **Always-on:** $7/month per service ($14 total) for no spin-down

---

**That's it!** Your bot is live 24/7 on Render.
