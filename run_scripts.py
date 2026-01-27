#!/usr/bin/env python3
"""
CLI Menu-based Script Runner
This script provides a menu interface to run all scripts in the repository.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple
import platform

# ANSI color codes for better UI
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Disable colors on Windows if not supported
if platform.system() == 'Windows':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except:
        # If colors don't work, disable them
        for attr in dir(Colors):
            if not attr.startswith('_'):
                setattr(Colors, attr, '')


class ScriptRunner:
    def __init__(self, base_dir: str = None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent
        self.scripts: Dict[str, List[Tuple[str, Path]]] = {}
        self.all_scripts: List[Tuple[str, Path]] = []
        
    def scan_scripts(self):
        """Scan directory recursively for Python and shell scripts."""
        print(f"{Colors.CYAN}Scanning for scripts...{Colors.END}")
        
        # Supported extensions
        extensions = {'.py', '.sh', '.bat', '.ps1'}
        
        for root, dirs, files in os.walk(self.base_dir):
            # Skip hidden directories and common ignore patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', 'venv', '.venv', 'env', '.env']]
            
            for file in files:
                file_path = Path(root) / file
                ext = file_path.suffix.lower()
                
                # Skip the runner script itself
                if file_path.name == 'run_scripts.py':
                    continue
                
                if ext in extensions:
                    rel_path = file_path.relative_to(self.base_dir)
                    category = rel_path.parent.name if rel_path.parent != Path('.') else 'Root'
                    
                    if category not in self.scripts:
                        self.scripts[category] = []
                    
                    script_info = (file_path.name, file_path)
                    self.scripts[category].append(script_info)
                    self.all_scripts.append(script_info)
        
        # Sort scripts within each category
        for category in self.scripts:
            self.scripts[category].sort(key=lambda x: x[0])
        
        print(f"{Colors.GREEN}Found {len(self.all_scripts)} scripts in {len(self.scripts)} categories{Colors.END}\n")
    
    def display_menu(self):
        """Display the main menu."""
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}  Script Runner - Test Cases Repository{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}\n")
        
        print(f"{Colors.CYAN}Categories:{Colors.END}")
        categories = sorted(self.scripts.keys())
        
        for idx, category in enumerate(categories, 1):
            script_count = len(self.scripts[category])
            print(f"  {Colors.YELLOW}{idx:2d}.{Colors.END} {Colors.BOLD}{category}{Colors.END} ({script_count} script{'s' if script_count != 1 else ''})")
        
        print(f"\n  {Colors.YELLOW}{len(categories) + 1:2d}.{Colors.END} {Colors.BOLD}All Scripts{Colors.END} ({len(self.all_scripts)} total)")
        print(f"  {Colors.YELLOW} 0.{Colors.END} {Colors.BOLD}Exit{Colors.END}")
        print(f"\n{Colors.HEADER}{'='*60}{Colors.END}\n")
    
    def display_category_scripts(self, category: str):
        """Display scripts in a specific category."""
        scripts = self.scripts[category]
        print(f"\n{Colors.CYAN}{Colors.BOLD}Scripts in '{category}':{Colors.END}\n")
        
        for idx, (name, path) in enumerate(scripts, 1):
            rel_path = path.relative_to(self.base_dir)
            print(f"  {Colors.YELLOW}{idx:2d}.{Colors.END} {name}")
            print(f"      {Colors.BLUE}Path: {rel_path}{Colors.END}")
        
        print(f"\n  {Colors.YELLOW} 0.{Colors.END} {Colors.BOLD}Back to Main Menu{Colors.END}\n")
    
    def display_all_scripts(self):
        """Display all scripts in a flat list."""
        print(f"\n{Colors.CYAN}{Colors.BOLD}All Scripts:{Colors.END}\n")
        
        for idx, (name, path) in enumerate(self.all_scripts, 1):
            rel_path = path.relative_to(self.base_dir)
            category = rel_path.parent.name if rel_path.parent != Path('.') else 'Root'
            print(f"  {Colors.YELLOW}{idx:3d}.{Colors.END} {name}")
            print(f"      {Colors.BLUE}Category: {category} | Path: {rel_path}{Colors.END}")
        
        print(f"\n  {Colors.YELLOW} 0.{Colors.END} {Colors.BOLD}Back to Main Menu{Colors.END}\n")
    
    def run_script(self, script_path: Path):
        """Run a script with appropriate interpreter."""
        print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}Running: {script_path.name}{Colors.END}")
        print(f"{Colors.BLUE}Path: {script_path.relative_to(self.base_dir)}{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}\n")
        
        try:
            ext = script_path.suffix.lower()
            
            if ext == '.py':
                # Run Python script using the same interpreter that's running this script
                # This ensures virtual environment packages are available
                python_exe = sys.executable
                result = subprocess.run(
                    [python_exe, str(script_path)],
                    cwd=str(script_path.parent),
                    capture_output=False,
                    text=True
                )
                return_code = result.returncode
                
            elif ext == '.sh':
                # Run shell script (Unix/Linux/Mac)
                if platform.system() == 'Windows':
                    print(f"{Colors.YELLOW}Warning: Shell script detected. On Windows, you may need WSL or Git Bash.{Colors.END}")
                    # Try to run with bash if available
                    result = subprocess.run(
                        ['bash', str(script_path)],
                        cwd=str(script_path.parent),
                        capture_output=False,
                        text=True
                    )
                    return_code = result.returncode
                else:
                    result = subprocess.run(
                        ['bash', str(script_path)],
                        cwd=str(script_path.parent),
                        capture_output=False,
                        text=True
                    )
                    return_code = result.returncode
                    
            elif ext == '.bat':
                # Run batch script (Windows)
                result = subprocess.run(
                    [str(script_path)],
                    cwd=str(script_path.parent),
                    shell=True,
                    capture_output=False,
                    text=True
                )
                return_code = result.returncode
                
            elif ext == '.ps1':
                # Run PowerShell script
                result = subprocess.run(
                    ['powershell', '-ExecutionPolicy', 'Bypass', '-File', str(script_path)],
                    cwd=str(script_path.parent),
                    capture_output=False,
                    text=True
                )
                return_code = result.returncode
            else:
                print(f"{Colors.RED}Unsupported script type: {ext}{Colors.END}")
                return False
            
            print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
            if return_code == 0:
                print(f"{Colors.GREEN}{Colors.BOLD}✓ Script completed successfully!{Colors.END}")
            else:
                print(f"{Colors.RED}{Colors.BOLD}✗ Script exited with code: {return_code}{Colors.END}")
            print(f"{Colors.CYAN}{'='*60}{Colors.END}\n")
            
            return return_code == 0
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Script execution interrupted by user.{Colors.END}\n")
            return False
        except Exception as e:
            print(f"\n{Colors.RED}{Colors.BOLD}Error running script: {str(e)}{Colors.END}\n")
            return False
    
    def get_user_choice(self, max_option: int, prompt: str = "Enter your choice") -> int:
        """Get and validate user input."""
        while True:
            try:
                choice = input(f"{Colors.CYAN}{prompt}: {Colors.END}").strip()
                choice_int = int(choice)
                if 0 <= choice_int <= max_option:
                    return choice_int
                else:
                    print(f"{Colors.RED}Invalid choice. Please enter a number between 0 and {max_option}.{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Invalid input. Please enter a number.{Colors.END}")
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Exiting...{Colors.END}")
                return 0
    
    def run(self):
        """Main execution loop."""
        self.scan_scripts()
        
        if not self.scripts:
            print(f"{Colors.RED}No scripts found in the directory!{Colors.END}")
            return
        
        while True:
            self.display_menu()
            categories = sorted(self.scripts.keys())
            max_choice = len(categories) + 1
            choice = self.get_user_choice(max_choice, "Select an option")
            
            if choice == 0:
                print(f"\n{Colors.GREEN}Thank you for using Script Runner!{Colors.END}\n")
                break
            
            elif choice == len(categories) + 1:
                # Show all scripts
                while True:
                    self.display_all_scripts()
                    script_choice = self.get_user_choice(len(self.all_scripts), "Select a script to run (0 to go back)")
                    
                    if script_choice == 0:
                        break
                    elif 1 <= script_choice <= len(self.all_scripts):
                        script_path = self.all_scripts[script_choice - 1][1]
                        self.run_script(script_path)
                        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                    else:
                        print(f"{Colors.RED}Invalid choice.{Colors.END}")
            
            else:
                # Show category scripts
                category = categories[choice - 1]
                while True:
                    self.display_category_scripts(category)
                    scripts = self.scripts[category]
                    script_choice = self.get_user_choice(len(scripts), "Select a script to run (0 to go back)")
                    
                    if script_choice == 0:
                        break
                    elif 1 <= script_choice <= len(scripts):
                        script_path = scripts[script_choice - 1][1]
                        self.run_script(script_path)
                        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                    else:
                        print(f"{Colors.RED}Invalid choice.{Colors.END}")


def main():
    """Entry point."""
    try:
        # Check if running in a virtual environment
        in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
        if not in_venv:
            print(f"{Colors.YELLOW}Note: Not running in a virtual environment. Make sure dependencies are installed.{Colors.END}")
            print(f"{Colors.YELLOW}To use a virtual environment: python -m venv venv && venv\\Scripts\\activate{Colors.END}\n")
        
        runner = ScriptRunner()
        runner.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Exiting...{Colors.END}\n")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}An error occurred: {str(e)}{Colors.END}")
        sys.exit(1)


if __name__ == "__main__":
    main()
