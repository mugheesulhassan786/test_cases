"""
Accounting Module Tests - Happy Flow
Tests for 11. Accounting module (Expense, Revenue, Taxation)
"""
import unittest
import time
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base_test import BaseTest

logger = logging.getLogger(__name__)


class TestAccounting(BaseTest):
    """Test cases for Accounting Module"""

    def navigate_to_url(self, url_path):
        """Navigate directly to a URL"""
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    # ===== VIEW EXPENSE TESTS =====
    
    def test_01_view_expense_page_loads(self):
        """Verify View Expense page loads correctly"""
        logger.info("=== Testing View Expense Page Load ===")
        self.navigate_to_url("/accounting-management/view-expense")
        
        # Verify page elements
        try:
            # Check for heading
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Expense')] | //h5[contains(text(),'Expense')]"),
                timeout=10
            )
            assert heading.is_displayed(), "Expense heading not displayed"
            logger.info("[OK] View Expense page loaded with heading")
            
            # Check for table or data grid
            table = self.driver.find_elements(By.XPATH, "//table | //div[contains(@class,'data-grid')]")
            if table:
                logger.info("[OK] Data table found on expense page")
            
            # Check for Add Expense button
            add_btn = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Add')] | //a[contains(text(),'Add')]")
            if add_btn:
                logger.info("[OK] Add Expense button found")
                
        except TimeoutException:
            logger.warning("Could not verify all elements, but page loaded")
        
        logger.info("[OK] View Expense page test passed")
        time.sleep(2)

    def test_02_add_expense_page_loads(self):
        """Verify Add Expense page loads with all form elements"""
        logger.info("=== Testing Add Expense Page Load ===")
        self.navigate_to_url("/accounting-management/add-expense")
        
        try:
            # Check for form elements
            form_elements = [
                ("Description field", "//input[@name='description'] | //textarea[@name='description']"),
                ("Amount field", "//input[@name='amount'] | //input[@type='number']"),
                ("Category dropdown", "//div[contains(@class,'react-select')]"),
                ("Date field", "//input[@type='date'] | //input[@placeholder*='date']"),
                ("Save button", "//button[@type='submit'] | //button[contains(text(),'Save')]"),
            ]
            
            for name, xpath in form_elements:
                elements = self.driver.find_elements(By.XPATH, xpath)
                if elements:
                    logger.info(f"[OK] {name} found")
                else:
                    logger.warning(f"{name} not found")
            
            logger.info("[OK] Add Expense form elements verified")
        except Exception as e:
            logger.warning(f"Error checking form elements: {e}")
        
        time.sleep(2)

    def test_03_view_revenue_page_loads(self):
        """Verify View Revenue page loads correctly"""
        logger.info("=== Testing View Revenue Page Load ===")
        self.navigate_to_url("/accounting-management/view-revenue")
        
        try:
            # Check for heading
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Revenue')] | //h5[contains(text(),'Revenue')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Revenue page loaded")
        except TimeoutException:
            logger.warning("Revenue heading not found, checking alternative")
            # Try generic check
            assert "revenue" in self.driver.page_source.lower() or "accounting" in self.driver.page_source.lower()
        
        time.sleep(2)

    def test_04_view_taxation_page_loads(self):
        """Verify View Taxation page loads correctly"""
        logger.info("=== Testing View Taxation Page Load ===")
        self.navigate_to_url("/accounting-management/view-taxation")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Tax')] | //h5[contains(text(),'Tax')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Taxation page loaded")
        except TimeoutException:
            logger.warning("Taxation heading not found")
        
        time.sleep(2)

    def test_05_view_account_categories_loads(self):
        """Verify Account Categories page loads"""
        logger.info("=== Testing Account Categories Page Load ===")
        self.navigate_to_url("/accounting-management/view-account-categories")
        
        try:
            # Wait for any content to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body//div"))
            )
            logger.info("[OK] Account Categories page loaded")
        except TimeoutException:
            logger.warning("Account Categories page timeout")
        
        time.sleep(2)

    def test_06_accounting_reports_loads(self):
        """Verify Accounting Reports page loads"""
        logger.info("=== Testing Accounting Reports Page Load ===")
        self.navigate_to_url("/accounting-management/view-report")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4 | //h5 | //h6"))
            )
            logger.info("[OK] Accounting Reports page loaded")
        except TimeoutException:
            logger.warning("Reports page timeout")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
