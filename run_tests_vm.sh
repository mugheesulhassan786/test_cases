#!/bin/bash
#
# Selenium Test Runner for Isolated VM
# This script sets up the environment and runs the Selenium tests
# Designed for Ubuntu/Debian-based VMs
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$PROJECT_DIR/test_run.log"
HEADLESS_MODE="true"

# Print banner
echo -e "${BLUE}"
echo "=========================================="
echo "  Selenium Test Runner for VM"
echo "=========================================="
echo -e "${NC}"

# Function to log messages
log() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"
}

warn() {
    echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')] WARNING: $1${NC}" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}" | tee -a "$LOG_FILE"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install Chrome
install_chrome() {
    log "Installing Google Chrome..."
    
    # Update package list
    sudo apt-get update -qq
    
    # Install dependencies
    sudo apt-get install -y -qq wget gnupg curl unzip > /dev/null 2>&1
    
    # Download and install Chrome
    if ! command_exists google-chrome; then
        wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt-get install -y -qq /tmp/google-chrome.deb > /dev/null 2>&1 || {
            # Fix dependency issues if any
            sudo apt-get install -y -f -qq > /dev/null 2>&1
        }
        rm -f /tmp/google-chrome.deb
    fi
    
    # Verify installation
    CHROME_VERSION=$(google-chrome --version 2>/dev/null || echo "unknown")
    log "Chrome installed: $CHROME_VERSION"
}

# Function to install ChromeDriver
install_chromedriver() {
    log "Installing ChromeDriver..."
    
    # Get Chrome version
    CHROME_VERSION=$(google-chrome --version | grep -oP '\d+' | head -1)
    log "Chrome major version: $CHROME_VERSION"
    
    # Download matching ChromeDriver
    if [ -n "$CHROME_VERSION" ]; then
        # Try to get the latest compatible chromedriver
        CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION" || echo "")
        
        if [ -z "$CHROMEDRIVER_VERSION" ] || [[ "$CHROMEDRIVER_VERSION" == *"<!DOCTYPE"* ]]; then
            # Fallback to latest stable
            CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
        fi
        
        log "Downloading ChromeDriver version: $CHROMEDRIVER_VERSION"
        
        # Download ChromeDriver
        wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
        unzip -q -o /tmp/chromedriver.zip -d /tmp/
        sudo mv /tmp/chromedriver /usr/local/bin/
        sudo chmod +x /usr/local/bin/chromedriver
        rm -f /tmp/chromedriver.zip
    fi
    
    # Verify installation
    CHROMEDRIVER_VERSION=$(chromedriver --version 2>/dev/null || echo "unknown")
    log "ChromeDriver installed: $CHROMEDRIVER_VERSION"
}

# Function to install Python and pip
install_python() {
    log "Checking Python installation..."
    
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version)
        log "Python found: $PYTHON_VERSION"
    else
        log "Installing Python3..."
        sudo apt-get update -qq
        sudo apt-get install -y -qq python3 python3-pip > /dev/null 2>&1
    fi
    
    # Ensure pip is up to date
    log "Upgrading pip..."
    python3 -m pip install --quiet --upgrade pip
}

# Function to install Python dependencies
install_python_deps() {
    log "Installing Python dependencies..."
    
    cd "$PROJECT_DIR"
    
    if [ -f "requirements.txt" ]; then
        python3 -m pip install --quiet -r requirements.txt
        log "Python dependencies installed successfully"
    else
        warn "requirements.txt not found, installing default packages..."
        python3 -m pip install --quiet selenium webdriver-manager pytest pytest-html pytest-xdist
    fi
}

# Function to setup display for headless mode
setup_display() {
    log "Setting up display environment..."
    
    # Set display for headless operation
    export DISPLAY=:99
    
    # Check if Xvfb is needed and install if not present
    if ! command_exists Xvfb; then
        log "Installing Xvfb..."
        sudo apt-get update -qq
        sudo apt-get install -y -qq xvfb > /dev/null 2>&1
    fi
    
    # Start Xvfb if not already running
    if ! pgrep -x "Xvfb" > /dev/null; then
        log "Starting Xvfb..."
        Xvfb :99 -screen 0 1920x1080x24 > /dev/null 2>&1 &
        sleep 2
    fi
    
    log "Display setup complete"
}

# Function to run tests
run_tests() {
    log "Starting test execution..."
    
    cd "$PROJECT_DIR"
    
    # Create screenshots directory if it doesn't exist
    mkdir -p screenshots
    
    # Set environment variables
    export HEADLESS="$HEADLESS_MODE"
    export PYTHONUNBUFFERED=1
    
    log "Running tests in headless mode..."
    
    # Run the single session test runner
    if [ -f "run_single_session.py" ]; then
        log "Using run_single_session.py for single browser session testing..."
        python3 run_single_session.py --headless --verbose 2>&1 | tee -a "$LOG_FILE"
        TEST_EXIT_CODE=${PIPESTATUS[0]}
    else
        log "Using pytest for testing..."
        python3 -m pytest -v --tb=short 2>&1 | tee -a "$LOG_FILE"
        TEST_EXIT_CODE=${PIPESTATUS[0]}
    fi
    
    return $TEST_EXIT_CODE
}

# Function to print summary
print_summary() {
    echo -e "${BLUE}"
    echo "=========================================="
    echo "  Test Run Complete"
    echo "=========================================="
    echo -e "${NC}"
    
    if [ -f "$LOG_FILE" ]; then
        log "Log file saved to: $LOG_FILE"
        
        # Count test results if available
        PASSED=$(grep -c "PASSED" "$LOG_FILE" 2>/dev/null || echo 0)
        FAILED=$(grep -c "FAILED" "$LOG_FILE" 2>/dev/null || echo 0)
        
        log "Results: $PASSED passed, $FAILED failed"
    fi
}

# Main execution
main() {
    # Clear log file
    > "$LOG_FILE"
    
    log "Starting setup and test execution..."
    log "Project directory: $PROJECT_DIR"
    
    # Check if we're on a supported system
    if ! command_exists apt-get; then
        error "This script requires apt-get (Debian/Ubuntu). Please adapt for your system."
        exit 1
    fi
    
    # Install system dependencies
    log "Installing system dependencies..."
    sudo apt-get update -qq
    sudo apt-get install -y -qq \
        wget \
        gnupg \
        curl \
        unzip \
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
    
    # Install Chrome
    install_chrome
    
    # Install ChromeDriver
    install_chromedriver
    
    # Install Python
    install_python
    
    # Install Python dependencies
    install_python_deps
    
    # Setup display
    setup_display
    
    # Run tests
    run_tests
    EXIT_CODE=$?
    
    # Print summary
    print_summary
    
    if [ $EXIT_CODE -eq 0 ]; then
        log "All tests completed successfully!"
    else
        warn "Some tests failed. Check the log for details."
    fi
    
    exit $EXIT_CODE
}

# Handle script arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --headed)
            HEADLESS_MODE="false"
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --headed    Run tests in headed mode (browser visible)"
            echo "  --help      Show this help message"
            echo ""
            echo "This script sets up the environment and runs Selenium tests on an isolated VM."
            exit 0
            ;;
        *)
            warn "Unknown option: $1"
            shift
            ;;
    esac
done

# Run main function
main
