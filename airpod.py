#!/usr/bin/env python3
import subprocess
import time
from datetime import datetime

WINDOW_SEC = 1.5  # pause→play must happen within this window
COOLDOWN_SEC = 1.0

def wall_ts():
    # Wall-clock timestamp with milliseconds
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def follow_status():
    process = subprocess.Popen(
        ["playerctl", "--follow", "status"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    # print("Listening for playback status... (Ctrl+C to exit)")
    last_status = None
    last_time = 0.0
    last_skip_at = 0.0

    try:
        for line in process.stdout:
            status = line.strip()
            if not status:
                continue

            now = time.monotonic()
            # print(status, wall_ts())

            # Detect Paused -> Playing within WINDOW_SEC
            if last_status in ("Playing", "Paused") and status != last_status:
                if (now - last_time) <= WINDOW_SEC and (now - last_skip_at) >= COOLDOWN_SEC:
                    # print("Next song", wall_ts())
                    subprocess.run(["playerctl", "next"])
                    last_skip_at = now  # start cooldown

            last_status = status
            last_time = now

    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        process.terminate()

if __name__ == "__main__":
    follow_status()
