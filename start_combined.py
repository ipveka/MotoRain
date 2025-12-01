#!/usr/bin/env python3
"""
Start both backend and bot in the same process.
Backend runs in a separate thread, bot runs in main thread.
"""
import os
import sys
import threading
import time
import subprocess

def start_backend():
    """Start the backend server in a thread."""
    print("Starting backend server...")
    os.chdir('backend')
    subprocess.run([
        sys.executable, '-m', 'uvicorn',
        'app_mobile:app',
        '--host', '0.0.0.0',
        '--port', os.environ.get('PORT', '8001')
    ])

def start_bot():
    """Start the telegram bot."""
    print("Waiting for backend to initialize...")
    time.sleep(10)  # Give backend time to start
    print("Starting telegram bot...")
    os.chdir('..')
    subprocess.run([sys.executable, '-m', 'telegram_bot.bot'])

if __name__ == '__main__':
    # Start backend in a thread
    backend_thread = threading.Thread(target=start_backend, daemon=False)
    backend_thread.start()
    
    # Start bot in main thread
    start_bot()
