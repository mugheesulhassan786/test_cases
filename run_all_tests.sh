#!/bin/bash
#
# Minimal Test Runner for Fresh Ubuntu VM
# Installs all dependencies and runs tests in a single session
# Usage: ./run_all_tests.sh [OPTIONS]
#

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Defaults
HEADLESS="--headless"
VERBOSE=""
SKIP_SETUP=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --headed)
            HEADLESS=""
            shift
            ;;
        -v|--verbose)
            VERBOSE="--verbose"
            shift
            ;;
        --skip-setup)
            SKIP_SETUP=true
            shift
            ;;
        --help|-h)
            echo "Usage: ./run_all_tests.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --headed       Run with visible browser (default: headless)"
            echo "  -v, --verbose  Enable verbose output"
            echo "  --skip-setup   Skip setup (Python, Chrome, dependencies)"
            echo "  -h, --help     Show this help"
            echo ""
            echo "Examples:"
            echo "  ./run_all_tests.sh           # Full setup + run all tests headless"
            echo "  ./run_all_tests.sh --headed  # Run with visible browser"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Selenium Test Runner for Ubuntu VM  ${NC}"
echo -e "${BLUE}========================================${NC}"

# Setup phase
if [ "$SKIP_SETUP" = false ]; then
    echo -e "${GREEN}[SETUP] Installing dependencies...${NC}"
    
    # Update package list
    echo -e "${GREEN}[SETUP] Updating package list...${NC}"
    sudo apt-get update -qq
    
    # Install Python and pip if not present
    if ! command -v python3 &> /dev/null; then
        echo -e "${GREEN}[SETUP] Installing Python3...${NC}"
        sudo apt-get install -y -qq python3 python3-pip
    fi
    echo -e "${GREEN}[SETUP] Python version: $(python3 --version)${NC}"
    
    # Install Chrome
    if ! command -v google-chrome &> /dev/null; then
        echo -e "${GREEN}[SETUP] Installing Google Chrome...${NC}"
        sudo apt-get install -y -qq wget gnupg curl unzip
        wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt-get install -y -qq /tmp/google-chrome.deb || sudo apt-get install -y -f -qq
        rm -f /tmp/google-chrome.deb
    fi
    echo -e "${GREEN}[SETUP] Chrome version: $(google-chrome --version)${NC}"
    
    # Install ChromeDriver
    if ! command -v chromedriver &> /dev/null; then
        echo -e "${GREEN}[SETUP] Installing ChromeDriver...${NC}"
        CHROME_VERSION=$(google-chrome --version | grep -oP '\d+' | head -1)
        CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION" 2>/dev/null || curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
        wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
        unzip -q -o /tmp/chromedriver.zip -d /tmp/
        sudo mv /tmp/chromedriver /usr/local/bin/
        sudo chmod +x /usr/local/bin/chromedriver
        rm -f /tmp/chromedriver.zip
    fi
    echo -e "${GREEN}[SETUP] ChromeDriver version: $(chromedriver --version)${NC}"
    
    # Install system dependencies for Chrome/Selenium
    echo -e "${GREEN}[SETUP] Installing system dependencies...${NC}"
    sudo apt-get install -y -qq \
        xvfb \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig1 \
        libxss1 \
        libappindicator3-1 \
        libxtst6 \
        xdg-utils \
        fonts-liberation \
        libasound2 \
        libgbm1 \
        libgtk-3-0 \
        > /dev/null 2>&1
    
    # Install Python packages
    echo -e "${GREEN}[SETUP] Installing Python packages...${NC}"
    python3 -m pip install --quiet --upgrade pip
    python3 -m pip install --quiet -r requirements.txt
    
    echo -e "${GREEN}[SETUP] Setup complete!${NC}"
fi

# Setup display for headless mode
if [ -n "$HEADLESS" ]; then
    echo -e "${GREEN}[SETUP] Setting up virtual display...${NC}"
    export DISPLAY=:99
    if ! pgrep -x "Xvfb" > /dev/null 2>&1; then
        Xvfb :99 -screen 0 1920x1080x24 > /dev/null 2>&1 &
        sleep 1
    fi
fi

# Create screenshots directory
mkdir -p screenshots

# Run tests
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}[TEST] Running all tests...${NC}"
echo -e "${BLUE}========================================${NC}"

python3 run_single_session.py $HEADLESS $VERBOSE

EXIT_CODE=$?

echo -e "${BLUE}========================================${NC}"
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed!${NC}"
else
    echo -e "${RED}✗ Some tests failed${NC}"
fi
echo -e "${BLUE}========================================${NC}"

exit $EXIT_CODE
