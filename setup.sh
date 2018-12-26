#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    # Find out which version of linux is being user
    if [ -f /etc/os-release ]; then
        # freedesktop.org and systemd
        . /etc/os-release
        OS=$NAME
        VER=$VERSION_ID
    elif type lsb_release >/dev/null 2>&1; then
        # linuxbase.org
        OS=$(lsb_release -si)
        VER=$(lsb_release -sr)
    elif [ -f /etc/lsb-release ]; then
        # For some versions of Debian/Ubuntu without lsb_release command
        . /etc/lsb-release
        OS=$DISTRIB_ID
        VER=$DISTRIB_RELEASE
    elif [ -f /etc/debian_version ]; then
        # Older Debian/Ubuntu/etc.
        OS=Debian
        VER=$(cat /etc/debian_version)
    else
        # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
        OS=$(uname -s)
        VER=$(uname -r)
    fi
    
    # Install git
    if [[ "$OS" == "Ubuntu" ]] || [[ "$OS" == "Debian" ]]; then
        apt-get update
        apt-get install -y git
    else
        >&2 echo "Error: Currently only supports Ubuntu for linux"
    fi
    git clone https://github.com/barvesen/dotfiles.git ./.dotfiles
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        >&2 echo "Error: Does not currently support MacOS"
fi
