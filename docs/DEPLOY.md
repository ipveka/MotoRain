# 🚀 Deploy Telegram Bot to Render

Deploy MotoRain bot to [Render.com](https://render.com) - **both backend and bot in 1 free instance!**

## Prerequisites

- Telegram bot token from [@BotFather](https://t.me/botfather)
- GitHub account with your code pushed
- Render account (free at [render.com](https://render.com))

---

## Deploy (Single Service - FREE!)

1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `motorain-bot`
   - **Build Command:** `pip install -r backend/requirements.txt && pip install -r telegram_bot/requirements.txt`
   - **Start Command:** `python start_combined.py`
   - **Plan:** Free
5. Click **"Environment"** in sidebar
6. Add environment variables:
   - **Key:** `TELEGRAM_TOKEN` → **Value:** Your bot token from BotFather
   - **Key:** `BACKEND_BASE_URL` → **Value:** `http://localhost:8001`
   - **Key:** `PORT` → **Value:** `8001`
7. Click **"Create Web Service"**
8. Wait 5-10 minutes for deployment

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
