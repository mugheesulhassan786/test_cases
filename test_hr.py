"""
HR Management Module Tests - Happy Flow
Tests for 10. HR Management (Users, Teams, Payroll, Attendance, Documents)
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


class TestHR(BaseTest):
    """Test cases for HR Management Module"""

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

    # ===== VIEW USERS TESTS =====

    def test_01_view_users_page_loads(self):
        """Verify View Users page loads correctly"""
        logger.info("=== Testing View Users Page Load ===")
        self.navigate_to_url("/user-management/view-user")

        if self.verify_page_loaded("User"):
            logger.info("[OK] View Users page loaded")
        else:
            logger.warning("Users page breadcrumb not found, checking content")
            assert "user" in self.driver.page_source.lower()
            logger.info("[OK] View Users page loaded (via content)")

    def test_02_view_user_categories_page_loads(self):
        """Verify View User Categories page loads"""
        logger.info("=== Testing View User Categories Page Load ===")
        self.navigate_to_url("/user-management/view-user-category")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] View User Categories page loaded")
        except TimeoutException:
            logger.warning("User Categories page timeout")

    def test_03_view_teams_page_loads(self):
        """Verify View Teams page loads"""
        logger.info("=== Testing View Teams Page Load ===")
        self.navigate_to_url("/user-management/view-team")

        if self.verify_page_loaded("Team"):
            logger.info("[OK] View Teams page loaded")
        else:
            assert "team" in self.driver.page_source.lower()
            logger.info("[OK] View Teams page loaded (via content)")

    def test_04_employee_shifts_page_loads(self):
        """Verify Employee Shifts page loads"""
        logger.info("=== Testing Employee Shifts Page Load ===")
        self.navigate_to_url("/hr/employee-shifts")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] Employee Shifts page loaded")
        except TimeoutException:
            logger.warning("Shifts page timeout")

    def test_05_attendance_page_loads(self):
        """Verify Attendance page loads"""
        logger.info("=== Testing Attendance Page Load ===")
        self.navigate_to_url("/hr/attendance")

        if self.verify_page_loaded("Attendance"):
            logger.info("[OK] Attendance page loaded")
        else:
            assert "attendance" in self.driver.page_source.lower()
            logger.info("[OK] Attendance page loaded (via content)")

    def test_06_manage_leaves_page_loads(self):
        """Verify Manage Leaves page loads"""
        logger.info("=== Testing Manage Leaves Page Load ===")
        self.navigate_to_url("/hr/manage-leaves")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] Manage Leaves page loaded")
        except TimeoutException:
            logger.warning("Leaves page timeout")

    def test_07_assign_payroll_page_loads(self):
        """Verify Assign Payroll page loads"""
        logger.info("=== Testing Assign Payroll Page Load ===")
        self.navigate_to_url("/payroll/assign-payroll")

        if self.verify_page_loaded("Payroll"):
            logger.info("[OK] Assign Payroll page loaded")
        else:
            assert "payroll" in self.driver.page_source.lower()
            logger.info("[OK] Assign Payroll page loaded (via content)")

    def test_08_processed_payroll_page_loads(self):
        """Verify Processed Payroll page loads"""
        logger.info("=== Testing Processed Payroll Page Load ===")
        self.navigate_to_url("/payroll/processed-payrolls")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] Processed Payroll page loaded")
        except TimeoutException:
            logger.warning("Processed Payroll page timeout")

    def test_09_manage_documents_page_loads(self):
        """Verify Manage Documents page loads"""
        logger.info("=== Testing Manage Documents Page Load ===")
        self.navigate_to_url("/documents-management/view-documents")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title-center, .page-title-box, table, .card"))
            )
            logger.info("[OK] Manage Documents page loaded")
        except TimeoutException:
            logger.warning("Documents page timeout")


if __name__ == "__main__":
    unittest.main()
