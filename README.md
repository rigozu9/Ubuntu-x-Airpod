# Ubuntu AirPod Pro Integration

## Problem ❌

I could not skip songs via the "double pinch" method on my AirPods when connected to my PC that runs Linux Ubuntu 20.04. 

## Findings 🔍

When searching for solutions to fix this I found out the "double pinch" signal can only be sent to apples bluetooth devices. 

## Insight 💡

But one pinch still paused the music player so with this realization I came up with a solution to the problem. 

## Solution ⏯️⏭️

Pausing and playing in 1.5 second window will go to the next song. So pinching the Airpod twice in a row with a tiny pause between the pinches will skip a song. 

## Automation ⚙️

I added the script to startup applications, so I can use the skip song method without any manual work.

## Requirements

- Python3
- Linux Ubuntu 22.04
- AirPods Pro