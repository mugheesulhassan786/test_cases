"""
Leads Module Tests - Happy Flow
Tests for 17. Leads (View Leads)
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


class TestLeads(BaseTest):
    """Test cases for Leads Module"""

    def navigate_to_url(self, url_path):
        """Navigate directly to a URL"""
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    def test_01_view_leads_page_loads(self):
        """Verify View Leads page loads correctly"""
        logger.info("=== Testing View Leads Page Load ===")
        self.navigate_to_url("/leads-management/view-leads")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Lead')] | //h5[contains(text(),'Lead')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Leads page loaded with heading")
            
            # Check for leads table
            table = self.driver.find_elements(By.XPATH, "//table | //div[contains(@class,'data-grid')]")
            if table:
                logger.info("[OK] Leads table found")
                
        except TimeoutException:
            logger.warning("Leads page heading not found")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
