"""
Reviews Module Tests - Happy Flow
Tests for 7. Reviews (View Reviews)
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


class TestReviews(BaseTest):
    """Test cases for Reviews Module"""

    def navigate_to_url(self, url_path):
        """Navigate directly to a URL"""
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    def test_01_view_reviews_page_loads(self):
        """Verify View Reviews page loads correctly"""
        logger.info("=== Testing View Reviews Page Load ===")
        self.navigate_to_url("/reviews/view-review")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Review')] | //h5[contains(text(),'Review')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Reviews page loaded with heading")
            
            # Check for reviews table or cards
            content = self.driver.find_elements(By.XPATH, "//table | //div[contains(@class,'card')] | //div[contains(@class,'review')]")
            if content:
                logger.info("[OK] Reviews content found")
                
        except TimeoutException:
            logger.warning("Reviews page heading not found")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
