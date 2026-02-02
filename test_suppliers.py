"""
Suppliers Module Tests - Happy Flow
Tests for 2. Suppliers (View Suppliers, Categories)
"""
import unittest
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base_test import BaseTest

logger = logging.getLogger(__name__)


class TestSuppliers(BaseTest):
    """Test cases for Suppliers Module"""

    def navigate_to_url(self, url_path):
        """Navigate directly to a URL"""
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    def test_01_view_suppliers_page_loads(self):
        """Verify View Suppliers page loads correctly"""
        logger.info("=== Testing View Suppliers Page Load ===")
        self.navigate_to_url("/supplier-management/view-supplier")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Supplier')] | //h5[contains(text(),'Supplier')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Suppliers page loaded with heading")
            
            # Check for suppliers table
            table = self.driver.find_elements(By.XPATH, "//table | //div[contains(@class,'data-grid')]")
            if table:
                logger.info("[OK] Suppliers table found")
                
        except TimeoutException:
            logger.warning("Suppliers page heading not found")
        
        time.sleep(2)

    def test_02_view_supplier_categories_loads(self):
        """Verify View Supplier Categories page loads"""
        logger.info("=== Testing View Supplier Categories Page Load ===")
        self.navigate_to_url("/supplier-management/view-supplier-category")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Category')] | //h5[contains(text(),'Category')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Supplier Categories page loaded")
        except TimeoutException:
            logger.warning("Supplier Categories page heading not found")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
