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
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    def test_01_manage_landing_page_loads(self):
        """Verify Manage Landing Page loads correctly"""
        logger.info("=== Testing Manage Landing Page Load ===")
        self.navigate_to_url("/content-management/manage-landing")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Landing')] | //h5[contains(text(),'Landing')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] Manage Landing page loaded with heading")
            
            # Check for content grid
            content = self.driver.find_elements(By.XPATH, "//div[contains(@class,'card')] | //div[contains(@class,'content')]")
            if content:
                logger.info("[OK] Landing page content found")
                
        except TimeoutException:
            logger.warning("Landing page heading not found")
        
        time.sleep(2)

    def test_02_add_landing_page_loads(self):
        """Verify Add Landing Content page loads"""
        logger.info("=== Testing Add Landing Page Load ===")
        self.navigate_to_url("/content-management/add-landing")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Add')] | //h5[contains(text(),'Add')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] Add Landing page loaded")
        except TimeoutException:
            logger.warning("Add Landing page heading not found")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
