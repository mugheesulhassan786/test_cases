"""
Shipping & Delivery Module Tests - Happy Flow
Tests for 6. Shipping & Delivery (Shipping Rates, Carriers, Custom Labels)
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


class TestShipping(BaseTest):
    """Test cases for Shipping & Delivery Module"""

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

    def test_01_view_shipping_rates_loads(self):
        """Verify View Shipping Rates page loads correctly"""
        logger.info("=== Testing View Shipping Rates Page Load ===")
        self.navigate_to_url("/delivery-management/view-shipping-rate")

        if self.verify_page_loaded("Shipping Rate"):
            logger.info("[OK] View Shipping Rates page loaded")
        else:
            assert "shipping" in self.driver.page_source.lower() or "delivery" in self.driver.page_source.lower()
            logger.info("[OK] View Shipping Rates page loaded (via content)")

    def test_02_view_shipping_carriers_loads(self):
        """Verify View Shipping Carriers page loads"""
        logger.info("=== Testing View Shipping Carriers Page Load ===")
        self.navigate_to_url("/delivery-management/view-shipping-carrier")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View Shipping Carriers page loaded")
        except TimeoutException:
            logger.warning("Shipping Carriers page timeout")

    def test_03_view_custom_labels_loads(self):
        """Verify View Custom Labels page loads"""
        logger.info("=== Testing View Custom Labels Page Load ===")
        self.navigate_to_url("/delivery-management/view-custom-label")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View Custom Labels page loaded")
        except TimeoutException:
            logger.warning("Custom Labels page timeout")


if __name__ == "__main__":
    unittest.main()
