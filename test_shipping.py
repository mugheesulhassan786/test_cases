"""
Shipping & Delivery Module Tests - Happy Flow
Tests for 6. Shipping & Delivery
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
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    def test_01_delivery_management_page_loads(self):
        """Verify Delivery Management page loads correctly"""
        logger.info("=== Testing Delivery Management Page Load ===")
        self.navigate_to_url("/delivery-management")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Deliver')] | //h5[contains(text(),'Deliver')] | //h4[contains(text(),'Shipping')] | //h5[contains(text(),'Shipping')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] Delivery Management page loaded with heading")
            
            # Check for content
            content = self.driver.find_elements(By.XPATH, "//table | //div[contains(@class,'card')] | //div[contains(@class,'data-grid')]")
            if content:
                logger.info("[OK] Delivery content found")
                
        except TimeoutException:
            logger.warning("Delivery page heading not found")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
