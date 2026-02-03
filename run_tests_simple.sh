#!/bin/bash
#
# Simple Selenium Test Runner for Pre-configured VM
# Assumes Chrome, ChromeDriver, and Python are already installed
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HEADLESS_MODE="true"
VERBOSE_MODE="false"

# Functions
log() { echo -e "${GREEN}[$(date '+%H:%M:%S')] $1${NC}"; }
warn() { echo -e "${YELLOW}[$(date '+%H:%M:%S')] WARN: $1${NC}"; }
error() { echo -e "${RED}[$(date '+%H:%M:%S')] ERROR: $1${NC}"; }

# Show help
show_help() {
    cat << EOF
Selenium Test Runner for VM

Usage: $0 [OPTIONS]

OPTIONS:
    -h, --help       Show this help message
    --headed         Run in headed mode (browser visible)
    --verbose, -v    Enable verbose output
    --setup-only     Only install dependencies, don't run tests
    --test-only      Only run tests, skip setup

EXAMPLES:
    $0               Run tests in headless mode (default)
    $0 --headed      Run tests with visible browser
    $0 --verbose     Run with detailed logging

EOF
}

# Parse arguments
SETUP_ONLY=false
TEST_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --headed) HEADLESS_MODE="false"; shift ;;
        --verbose|-v) VERBOSE_MODE="true"; shift ;;
        --setup-only) SETUP_ONLY=true; shift ;;
        --test-only) TEST_ONLY=true; shift ;;
        --help|-h) show_help; exit 0 ;;
        *) warn "Unknown option: $1"; shift ;;
    esac
done

cd "$PROJECT_DIR"

echo -e "${BLUE}"
echo "======================================"
echo "  Selenium Test Runner"
echo "======================================"
echo -e "${NC}"

# Setup phase
if [ "$TEST_ONLY" = false ]; then
    log "Setting up environment..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        error "Python3 not found. Please install Python3 first."
        exit 1
    fi
    log "Python version: $(python3 --version)"
    
    # Check Chrome
    if ! command -v google-chrome &> /dev/null; then
        error "Google Chrome not found. Please install Chrome first."
        exit 1
    fi
    log "Chrome version: $(google-chrome --version)"
    
    # Check ChromeDriver
    if ! command -v chromedriver &> /dev/null; then
        warn "ChromeDriver not in PATH. Will use webdriver-manager."
    else
        log "ChromeDriver version: $(chromedriver --version)"
    fi
    
    # Install Python packages
    log "Installing Python dependencies..."
    python3 -m pip install --quiet --upgrade pip
    python3 -m pip install --quiet -r requirements.txt
    log "Dependencies installed"
    
    # Setup display for headless
    if [ "$HEADLESS_MODE" = "true" ]; then
        export DISPLAY=:99
        if ! pgrep -x "Xvfb" > /dev/null 2>&1; then
            if command -v Xvfb &> /dev/null; then
                log "Starting Xvfb..."
                Xvfb :99 -screen 0 1920x1080x24 &
                sleep 1
            fi
        fi
    fi
    
    if [ "$SETUP_ONLY" = true ]; then
        log "Setup complete. Exiting."
        exit 0
    fi
fi

# Test execution phase
log "Starting tests..."
log "Mode: $([ "$HEADLESS_MODE" = "true" ] && echo 'Headless' || echo 'Headed')"

mkdir -p screenshots
export HEADLESS="$HEADLESS_MODE"
export PYTHONUNBUFFERED=1

# Build command
if [ -f "run_single_session.py" ]; then
    CMD="python3 run_single_session.py"
    [ "$HEADLESS_MODE" = "true" ] && CMD="$CMD --headless"
    [ "$VERBOSE_MODE" = "true" ] && CMD="$CMD --verbose"
    log "Running: run_single_session.py"
else
    CMD="python3 -m pytest -v"
    log "Running: pytest"
fi

# Run tests
$CMD
EXIT_CODE=$?

# Summary
echo -e "${BLUE}"
echo "======================================"
echo "  Test Run Complete"
echo "======================================"
echo -e "${NC}"

if [ $EXIT_CODE -eq 0 ]; then
    log "✓ All tests passed!"
else
    warn "✗ Some tests failed (exit code: $EXIT_CODE)"
fi

exit $EXIT_CODE
