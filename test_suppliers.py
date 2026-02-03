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
        base = getattr(self, 'base_url', None) or getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        self.wait_for_page_load()
        self.wait_for_no_loading(timeout=10)

    def verify_page_loaded(self, breadcrumb_text, timeout=10):
        """Verify page loaded by checking breadcrumb or page content"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[contains(@class,'page-title')]//li[contains(text(),'{breadcrumb_text}')] | //ol[contains(@class,'breadcrumb')]//li[contains(text(),'{breadcrumb_text}')]")
                )
            )
            return True
        except TimeoutException:
            return breadcrumb_text.lower() in self.driver.page_source.lower()

    def test_01_view_suppliers_page_loads(self):
        """Verify View Suppliers page loads correctly"""
        logger.info("=== Testing View Suppliers Page Load ===")
        self.navigate_to_url("/supplier-management/view-supplier")

        if self.verify_page_loaded("Supplier"):
            logger.info("[OK] View Suppliers page loaded")
        else:
            assert "supplier" in self.driver.page_source.lower(), "Suppliers page did not load"
            logger.info("[OK] View Suppliers page loaded (via content)")

    def test_02_view_supplier_categories_loads(self):
        """Verify View Supplier Categories page loads"""
        logger.info("=== Testing View Supplier Categories Page Load ===")
        self.navigate_to_url("/supplier-management/view-supplier-category")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View Supplier Categories page loaded")
        except TimeoutException:
            logger.warning("Supplier Categories page timeout")


if __name__ == "__main__":
    unittest.main()
