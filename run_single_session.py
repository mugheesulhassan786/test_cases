#!/usr/bin/env python
"""
Single Session Test Runner for Selenium automation tests

This script runs all tests within a single browser session and login,
improving performance by avoiding repeated logins and browser startups.

Features:
- Single login session for all tests
- Headless/Non-headless mode option
- Detailed console output and logging
"""

import argparse
import sys
import os
import time
import traceback
import inspect
from datetime import datetime
from typing import List, Tuple, Optional, Dict, Any

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException

# Import the BaseTest class
from base_test import BaseTest, logger

# Import test classes
from test_inventory_crud import TestInventoryCRUD
from test_accounting import TestAccounting
from test_hr import TestHR
from test_orders import TestOrders
from test_reviews import TestReviews
from test_leads import TestLeads
from test_content import TestContentManagement
from test_suppliers import TestSuppliers
from test_shipping import TestShipping


class SingleSessionTestRunner(BaseTest):
    """
    Test runner that executes all tests in a single browser session
    """
    
    def __init__(self):
        super().__init__()
        self.results: List[Dict[str, Any]] = []
        self.headless_mode: bool = False
        self.base_url = "https://testing.d1z4wu6myne6l0.amplifyapp.com"
        
    def run_tests(self, headless: bool = False, selected_modules: Optional[List[str]] = None):
        """
        Run all tests in a single session
        
        Args:
            headless: Run browser in headless mode
            selected_modules: List of module names to run (None = all)
        """
        self.headless_mode = headless
        
        print("\n" + "=" * 80)
        print("SINGLE SESSION TEST RUNNER")
        print("=" * 80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Headless Mode: {headless}")
        print("=" * 80 + "\n")
        
        # Setup driver and login once
        try:
            self.setup_driver(headless=headless)
            self.login()
            print("Login successful - Starting test execution\n")
        except Exception as e:
            print(f"FAILED to setup driver or login: {e}")
            traceback.print_exc()
            return 1
        
        # Get all test methods to run
        test_methods = self._collect_test_methods(selected_modules)
        
        print(f"Total tests to run: {len(test_methods)}\n")
        print("-" * 80)
        
        # Run each test
        for idx, (test_class, test_method) in enumerate(test_methods, 1):
            result = self._run_single_test(test_class, test_method, idx, len(test_methods))
            self.results.append(result)
        
        # Print summary
        self._print_summary()
        
        # Teardown
        self.teardown()
        
        # Return exit code
        failed_count = sum(1 for r in self.results if not r['passed'])
        return 0 if failed_count == 0 else 1
    
    def _collect_test_methods(self, selected_modules: Optional[List[str]] = None) -> List[Tuple[type, str]]:
        """
        Collect all test methods from test classes
        
        Args:
            selected_modules: List of module names to run (None = all)
            
        Returns:
            List of tuples (test_class, test_method_name)
        """
        test_methods = []
        
        # All test classes
        all_test_classes = [
            TestInventoryCRUD,
            TestAccounting,
            TestHR,
            TestOrders,
            TestReviews,
            TestLeads,
            TestContentManagement,
            TestSuppliers,
            TestShipping,
        ]
        
        for test_class in all_test_classes:
            class_name = test_class.__name__
            module_name = class_name.lower().replace('test', '')
            
            # Filter by selected modules if specified
            if selected_modules:
                # Check if any selected module matches this class
                match_found = False
                for selected in selected_modules:
                    selected_lower = selected.lower().replace('_', '')
                    if (selected_lower in class_name.lower() or 
                        selected_lower in module_name or
                        selected_lower in module_name.replace('_', '')):
                        match_found = True
                        break
                if not match_found:
                    continue
            
            # Get test methods from class
            for name, method in inspect.getmembers(test_class, predicate=inspect.isfunction):
                if name.startswith('test_'):
                    test_methods.append((test_class, name))
        
        return test_methods
    
    def _close_bundle_listing_modal(self):
        """Specifically close the 'Add Bundle Listing' modal if open"""
        try:
            # Check if Add Bundle Listing modal is open
            modal_selectors = [
                (By.XPATH, '//div[contains(@class,"modal") and contains(.,"Add Bundle Listing")]'),
                (By.XPATH, '//h5[contains(text(),"Add Bundle Listing")]/ancestor::div[contains(@class,"modal")]'),
            ]
            
            for modal_selector in modal_selectors:
                modals = self.driver.find_elements(*modal_selector)
                for modal in modals:
                    if modal.is_displayed():
                        # Try to find and click the X button
                        close_buttons = modal.find_elements(By.XPATH, './/button[contains(@class,"close")]')
                        for btn in close_buttons:
                            if btn.is_displayed():
                                try:
                                    btn.click()
                                    time.sleep(0.5)
                                    return True
                                except:
                                    pass
            
            # Alternative: Try clicking X by position (top right of modal)
            try:
                x_button = self.driver.find_element(
                    By.XPATH, 
                    '//div[contains(@class,"modal") and contains(.,"Add Bundle Listing")]//button[contains(@class,"close") or @aria-label="Close"]'
                )
                if x_button.is_displayed():
                    x_button.click()
                    time.sleep(0.5)
                    return True
            except:
                pass
                
        except Exception as e:
            logger.debug(f"Bundle modal close error: {e}")
        return False
    
    def _cleanup_between_tests(self):
        """Clean up any open modals or overlays between tests"""
        try:
            # First, specifically try to close Add Bundle Listing modal
            self._close_bundle_listing_modal()
            
            # Try to close any open modals by clicking close buttons (including X icon)
            close_button_selectors = [
                (By.CSS_SELECTOR, '.modal .close'),
                (By.CSS_SELECTOR, '.modal .btn-close'),
                (By.CSS_SELECTOR, '.modal [data-dismiss="modal"]'),
                (By.CSS_SELECTOR, '.modal button[class*="close"]'),
                # Specific for modals with show class
                (By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class,"close")]'),
                (By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//span[contains(@class,"close")]'),
                (By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//*[@aria-label="Close"]'),
                (By.CSS_SELECTOR, '.modal.show .close'),
                (By.CSS_SELECTOR, '.modal.show .btn-close'),
                (By.CSS_SELECTOR, '.modal.fade.show button.close'),
            ]
            
            for selector in close_button_selectors:
                try:
                    close_buttons = self.driver.find_elements(*selector)
                    for btn in close_buttons:
                        if btn.is_displayed():
                            try:
                                btn.click()
                                time.sleep(0.3)
                            except:
                                pass
                except:
                    pass
            
            # Try clicking outside modal on the backdrop
            try:
                backdrops = self.driver.find_elements(By.CSS_SELECTOR, '.modal-backdrop.fade.show')
                for backdrop in backdrops:
                    if backdrop.is_displayed():
                        try:
                            backdrop.click()
                            time.sleep(0.3)
                        except:
                            pass
            except:
                pass
            
            # Use JavaScript to forcibly close/hide modals
            try:
                self.driver.execute_script("""
                    // Close all modals
                    var modals = document.querySelectorAll('.modal');
                    modals.forEach(function(modal) {
                        modal.classList.remove('show');
                        modal.style.display = 'none';
                        modal.setAttribute('aria-hidden', 'true');
                    });
                    
                    // Remove backdrop
                    var backdrops = document.querySelectorAll('.modal-backdrop');
                    backdrops.forEach(function(backdrop) {
                        backdrop.remove();
                    });
                    
                    // Remove modal-open class from body
                    document.body.classList.remove('modal-open');
                    document.body.style.overflow = '';
                    document.body.style.paddingRight = '';
                """)
                time.sleep(0.3)
            except:
                pass
            
            # Press Escape key to close modals
            try:
                body = self.driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.ESCAPE)
                time.sleep(0.3)
            except:
                pass
            
            # Wait for modals to disappear
            self.wait_for_overlay_to_disappear(timeout=3)
            
        except Exception as e:
            logger.debug(f"Cleanup error (non-critical): {e}")
    
    def _run_single_test(self, test_class: type, method_name: str, index: int, total: int) -> Dict[str, Any]:
        """
        Run a single test method
        
        Args:
            test_class: The test class
            method_name: Name of the test method
            index: Current test index
            total: Total number of tests
            
        Returns:
            Dictionary with test results
        """
        class_name = test_class.__name__
        result = {
            'class_name': class_name,
            'method_name': method_name,
            'passed': False,
            'duration': 0,
            'error': None,
            'traceback': None
        }
        
        print(f"\n[{index}/{total}] Running: {class_name}.{method_name}")
        print("-" * 40)
        
        start_time = time.time()
        
        try:
            # Clean up any open modals from previous tests
            self._cleanup_between_tests()
            
            # Navigate to Dashboard first to ensure clean state
            try:
                dashboard_link = self.wait_for_clickable(
                    (By.XPATH, '//*[contains(text(), "1. Dashboard") or contains(@href, "dashboard")]'),
                    timeout=5
                )
                dashboard_link.click()
                self.wait_for_page_load()
                time.sleep(0.5)  # Small delay for any animations
            except:
                pass  # If already on dashboard or can't navigate, continue
            
            # Create instance of test class
            test_instance = test_class()
            test_instance.driver = self.driver
            test_instance.wait = self.wait
            test_instance.actions = self.actions
            test_instance.timeout = self.timeout
            test_instance.headless = self.headless
            test_instance.base_url = self.base_url  # Pass base_url for navigation
            
            # Mark as single session mode to skip individual setup/teardown
            test_instance._single_session_mode = True
            
            # Get and run the test method
            test_method = getattr(test_instance, method_name)
            test_method()
            
            result['passed'] = True
            result['duration'] = time.time() - start_time
            print(f"PASSED ({result['duration']:.2f}s)")
            
        except Exception as e:
            result['duration'] = time.time() - start_time
            result['error'] = str(e)
            result['traceback'] = traceback.format_exc()
            print(f"FAILED ({result['duration']:.2f}s)")
            print(f"  Error: {e}")
            
            # Take screenshot on failure
            try:
                screenshot_path = self.take_screenshot(f"failure_{class_name}_{method_name}")
                print(f"  Screenshot saved: {screenshot_path}")
            except Exception as screenshot_error:
                print(f"  Could not save screenshot: {screenshot_error}")
            
            # Clean up after failure to ensure next test starts fresh
            self._cleanup_between_tests()
        
        return result
    
    def _print_summary(self):
        """Print test execution summary"""
        print("\n" + "=" * 80)
        print("TEST EXECUTION SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for r in self.results if r['passed'])
        failed = sum(1 for r in self.results if not r['passed'])
        total = len(self.results)
        total_duration = sum(r['duration'] for r in self.results)
        
        print(f"\nTotal Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Total Duration: {total_duration:.2f}s")
        print(f"Average Duration: {total_duration/total:.2f}s" if total > 0 else "N/A")
        
        if failed > 0:
            print("\nFailed Tests:")
            print("-" * 40)
            for result in self.results:
                if not result['passed']:
                    print(f"  • {result['class_name']}.{result['method_name']}")
                    print(f"    Error: {result['error']}")
        
        print("\n" + "=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Run Selenium tests in a single browser session",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all tests in headed mode (browser visible)
  python run_single_session.py

  # Run all tests in headless mode
  python run_single_session.py --headless

  # Run specific modules only
  python run_single_session.py --modules inventory accounting

  # Run in headless mode with verbose output
  python run_single_session.py --headless --verbose
        """
    )
    
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (no visible window)"
    )
    
    parser.add_argument(
        "--modules",
        nargs="+",
        help="Run only specific modules (e.g., inventory accounting hr)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if args.verbose:
        logger.setLevel("DEBUG")
    
    # Run tests
    runner = SingleSessionTestRunner()
    exit_code = runner.run_tests(
        headless=args.headless,
        selected_modules=args.modules
    )
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
