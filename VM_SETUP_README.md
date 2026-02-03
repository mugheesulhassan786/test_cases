# VM Test Runner Setup Guide

This guide explains how to run the Selenium tests on an isolated Virtual Machine.

## Files Included

| File | Description |
|------|-------------|
| `run_tests_vm.sh` | Full-featured bash script for Linux VMs (installs Chrome, ChromeDriver, dependencies) |
| `run_tests_simple.sh` | Simplified bash script for pre-configured Linux VMs |
| `run_tests_vm.bat` | Windows batch script for Windows VMs |

## Quick Start

### For Linux VMs (Ubuntu/Debian)

#### Option 1: Full Auto-Setup (Recommended for fresh VMs)

```bash
chmod +x run_tests_vm.sh
./run_tests_vm.sh
```

This will:
1. Install Google Chrome
2. Install ChromeDriver
3. Install Python and dependencies
4. Run all tests in headless mode

#### Option 2: Simple Run (for pre-configured VMs)

If your VM already has Chrome and Python installed:

```bash
chmod +x run_tests_simple.sh
./run_tests_simple.sh
```

### For Windows VMs

```cmd
run_tests_vm.bat
```

Or with options:

```cmd
run_tests_vm.bat --headed --verbose
```

## Command Line Options

### Linux Scripts

| Option | Description |
|--------|-------------|
| `--headed` | Run browser in visible mode (not headless) |
| `--verbose` / `-v` | Enable verbose logging |
| `--setup-only` | Only install dependencies, don't run tests |
| `--test-only` | Only run tests, skip dependency check |

### Windows Script

| Option | Description |
|--------|-------------|
| `--headed` | Run browser in visible mode |
| `--verbose` / `-v` | Enable verbose logging |

## Prerequisites

### For `run_tests_vm.sh` (Full Setup)

- Ubuntu/Debian-based Linux distribution
- `sudo` access
- Internet connection

### For `run_tests_simple.sh` (Pre-configured VMs)

- Python 3.x
- Google Chrome
- pip

### For `run_tests_vm.bat` (Windows)

- Python 3.x
- Google Chrome (recommended)
- pip

## System Requirements

### Minimum

- RAM: 2GB
- Disk: 10GB free space
- CPU: 2 cores

### Recommended

- RAM: 4GB+
- Disk: 20GB free space
- CPU: 4 cores

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HEADLESS` | `true` | Run browser in headless mode |
| `DISPLAY` | `:99` | X11 display for headless mode |

## Troubleshooting

### Chrome Installation Issues

If Chrome installation fails on Linux:

```bash
# Manual Chrome installation
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google.list
sudo apt-get update
sudo apt-get install -y google-chrome-stable
```

### ChromeDriver Issues

The tests use `webdriver-manager` which automatically handles ChromeDriver, so manual installation is usually not required.

### Permission Denied

If you get permission errors:

```bash
chmod +x run_tests_vm.sh
chmod +x run_tests_simple.sh
```

### Xvfb Issues (Linux Headless)

If you encounter display errors on headless Linux:

```bash
sudo apt-get install -y xvfb
export DISPLAY=:99
Xvfb :99 -screen 0 1920x1080x24 &
```

## Viewing Test Results

- Console output shows real-time test progress
- Screenshots of failures are saved in `screenshots/` directory
- Logs are saved to `test_execution.log`

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Tests
        run: |
          chmod +x run_tests_simple.sh
          ./run_tests_simple.sh
```

### GitLab CI Example

```yaml
test:
  image: ubuntu:latest
  script:
    - chmod +x run_tests_vm.sh
    - ./run_tests_vm.sh
  artifacts:
    paths:
      - screenshots/
      - test_execution.log
```

## Notes

- Tests run in **headless mode by default** (no GUI required)
- The script automatically handles ChromeDriver via `webdriver-manager`
- For isolated VMs, no virtual environment is needed
- Internet connection is required for initial setup and web testing
