#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$SCRIPT_DIR/bin/activate"

# Run the Python script
python3 "$SCRIPT_DIR/webm-to-mp4-gui-app.py"

# The virtual environment will be automatically deactivated when the script exits