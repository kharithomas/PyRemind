#!/usr/bin/python

# A simple program to remind users of a custom message using AppleScript x Python

import os

# Check for more system sounds in /System/Library/Sounds

# Basso.aiff     -- good, but error-like (low keys on keyboard)
# Blow.aiff      -- good
# Bottle.aiff    -- too short
# Frog.aiff      -- chirp
# Funk.aiff      -- thud
# Glass.aiff     -- good (like the end of a timer)
# Hero.aiff      -- good
# Morse.aiff     -- 'pop'
# Ping.aiff      -- good
# Pop.aiff       -- shorter 'pop'
# Purr.aiff      -- good
# Sosumi.aiff    -- good
# Submarine.aiff -- good
# Tink.aiff      -- too quiet

def notify(title, message, subtitle="", sound="Frog"):
    os.system("""osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'""".format(message, title, subtitle, sound))


# Setting variables
title = "PyRemind"
message  = "Good morning! Make sure to eat breakfast!"

# Calling the function
notify(title = title, message = message)
