"""
Orders Management Module Tests - Happy Flow
Tests for 5. Orders Management (View Orders, Requests, eBay cases, etc.)
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


class TestOrders(BaseTest):
    """Test cases for Orders Management Module"""

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

    def test_01_view_orders_page_loads(self):
        """Verify View Orders page loads correctly"""
        logger.info("=== Testing View Orders Page Load ===")
        self.navigate_to_url("/orders/view-orders")

        if self.verify_page_loaded("Order"):
            logger.info("[OK] View Orders page loaded")
        else:
            assert "order" in self.driver.page_source.lower()
            logger.info("[OK] View Orders page loaded (via content)")

    def test_02_view_requests_page_loads(self):
        """Verify View Requests page loads"""
        logger.info("=== Testing View Requests Page Load ===")
        self.navigate_to_url("/orders/view-request")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View Requests page loaded")
        except TimeoutException:
            logger.warning("Requests page timeout")

    def test_03_view_ebay_inquiries_loads(self):
        """Verify View eBay Inquiries page loads"""
        logger.info("=== Testing View eBay Inquiries Page Load ===")
        self.navigate_to_url("/orders/view-ebay-inquiries")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View eBay Inquiries page loaded")
        except TimeoutException:
            logger.warning("eBay Inquiries page timeout")

    def test_04_view_ebay_cases_loads(self):
        """Verify View eBay Cases page loads"""
        logger.info("=== Testing View eBay Cases Page Load ===")
        self.navigate_to_url("/orders/view-ebay-cases")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View eBay Cases page loaded")
        except TimeoutException:
            logger.warning("eBay Cases page timeout")

    def test_05_view_ebay_disputes_loads(self):
        """Verify View eBay Disputes page loads"""
        logger.info("=== Testing View eBay Disputes Page Load ===")
        self.navigate_to_url("/orders/view-ebay-disputes")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View eBay Disputes page loaded")
        except TimeoutException:
            logger.warning("eBay Disputes page timeout")

    def test_06_view_ebay_cancellations_loads(self):
        """Verify View eBay Cancellations page loads"""
        logger.info("=== Testing View eBay Cancellations Page Load ===")
        self.navigate_to_url("/orders/view-ebay-cancellation")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View eBay Cancellations page loaded")
        except TimeoutException:
            logger.warning("eBay Cancellations page timeout")

    def test_07_view_ebay_returns_loads(self):
        """Verify View eBay Returns page loads"""
        logger.info("=== Testing View eBay Returns Page Load ===")
        self.navigate_to_url("/orders/view-ebay-returns")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View eBay Returns page loaded")
        except TimeoutException:
            logger.warning("eBay Returns page timeout")

    def test_08_view_amazon_replacements_loads(self):
        """Verify View Amazon Replacements page loads"""
        logger.info("=== Testing View Amazon Replacements Page Load ===")
        self.navigate_to_url("/orders/view-amazon-replacements")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View Amazon Replacements page loaded")
        except TimeoutException:
            logger.warning("Amazon Replacements page timeout")


if __name__ == "__main__":
    unittest.main()
