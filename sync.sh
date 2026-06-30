#!/bin/bash
cd /home/ubuntu/ai-investing
git add .
git commit -m "sync: $(date '+%Y-%m-%d %H:%M')" || echo "No changes"
git push origin main
