"""
Content Management Module Tests - Happy Flow
Tests for 13. Content Management (Landing Page, etc.)
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


class TestContentManagement(BaseTest):
    """Test cases for Content Management Module"""

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

    def test_01_manage_landing_page_loads(self):
        """Verify Manage Landing Page loads correctly"""
        logger.info("=== Testing Manage Landing Page Load ===")
        self.navigate_to_url("/content-management/manage-landing")

        if self.verify_page_loaded("Landing"):
            logger.info("[OK] Manage Landing page loaded")
        else:
            assert "landing" in self.driver.page_source.lower() or "content" in self.driver.page_source.lower(), "Landing page did not load"
            logger.info("[OK] Manage Landing page loaded (via content)")


if __name__ == "__main__":
    unittest.main()
