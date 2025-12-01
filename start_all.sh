#!/bin/bash
# Start both backend and bot in one container

# Start backend in background
cd backend && uvicorn app_mobile:app --host 0.0.0.0 --port $PORT &

# Wait a bit for backend to initialize
sleep 5

# Start bot in foreground
cd ../telegram_bot && python bot.py
