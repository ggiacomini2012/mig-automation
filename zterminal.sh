#!/bin/bash

# Read project path from config.json
PROJECT_PATH=$(cat config.json | grep -o '"project_path":"[^"]*"' | cut -d'"' -f4)

# Create aliases
alias bob='echo "Holla, sou bob!"'
alias sublime='open "$PROJECT_PATH"'
alias kill-python='pkill -f python'
alias all-python='ps aux | grep python'
alias cd-project='cd "$PROJECT_PATH"'

# Clear screen and navigate to project directory
clear
cd "$PROJECT_PATH"

# Start shell
exec bash 