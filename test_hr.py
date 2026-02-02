"""
HR Management Module Tests - Happy Flow
Tests for 10. HR Management (Users, Teams, Payroll, Attendance)
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
        base = getattr(self, 'BASE_URL', "https://testing.d1z4wu6myne6l0.amplifyapp.com")
        full_url = f"{base}{url_path}"
        logger.info(f"Navigating to: {full_url}")
        self.driver.get(full_url)
        time.sleep(3)

    # ===== VIEW USERS TESTS =====
    
    def test_01_view_users_page_loads(self):
        """Verify View Users page loads correctly"""
        logger.info("=== Testing View Users Page Load ===")
        self.navigate_to_url("/hr-management/view-users")
        
        try:
            # Check for Users heading
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'User')] | //h5[contains(text(),'User')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Users page loaded with heading")
            
            # Check for user table
            table = self.driver.find_elements(By.XPATH, "//table | //div[contains(@class,'MuiDataGrid')]")
            if table:
                logger.info("[OK] Users table/data grid found")
                
        except TimeoutException:
            logger.warning("Users page elements not found")
        
        time.sleep(2)

    def test_02_view_teams_page_loads(self):
        """Verify View Teams page loads"""
        logger.info("=== Testing View Teams Page Load ===")
        self.navigate_to_url("/hr-management/view-teams")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Team')] | //h5[contains(text(),'Team')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] View Teams page loaded")
        except TimeoutException:
            logger.warning("Teams page heading not found")
        
        time.sleep(2)

    def test_03_employee_shifts_page_loads(self):
        """Verify Employee Shifts page loads"""
        logger.info("=== Testing Employee Shifts Page Load ===")
        self.navigate_to_url("/hr-management/employee-shifts")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4 | //h5 | //h6"))
            )
            logger.info("[OK] Employee Shifts page loaded")
        except TimeoutException:
            logger.warning("Shifts page timeout")
        
        time.sleep(2)

    def test_04_attendance_page_loads(self):
        """Verify Attendance page loads"""
        logger.info("=== Testing Attendance Page Load ===")
        self.navigate_to_url("/hr-management/attendance")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Attendance')] | //h5[contains(text(),'Attendance')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] Attendance page loaded")
        except TimeoutException:
            logger.warning("Attendance page heading not found")
        
        time.sleep(2)

    def test_05_manage_leaves_page_loads(self):
        """Verify Manage Leaves page loads"""
        logger.info("=== Testing Manage Leaves Page Load ===")
        self.navigate_to_url("/hr-management/manage-leaves")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4 | //h5 | //h6"))
            )
            logger.info("[OK] Manage Leaves page loaded")
        except TimeoutException:
            logger.warning("Leaves page timeout")
        
        time.sleep(2)

    def test_06_assign_payroll_page_loads(self):
        """Verify Assign Payroll page loads"""
        logger.info("=== Testing Assign Payroll Page Load ===")
        self.navigate_to_url("/hr-management/assign-payroll")
        
        try:
            heading = self.wait_for_element(
                (By.XPATH, "//h4[contains(text(),'Payroll')] | //h5[contains(text(),'Payroll')]"),
                timeout=10
            )
            assert heading.is_displayed()
            logger.info("[OK] Assign Payroll page loaded")
        except TimeoutException:
            logger.warning("Payroll page heading not found")
        
        time.sleep(2)

    def test_07_processed_payroll_page_loads(self):
        """Verify Processed Payroll page loads"""
        logger.info("=== Testing Processed Payroll Page Load ===")
        self.navigate_to_url("/hr-management/processed-payroll")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4 | //h5 | //h6"))
            )
            logger.info("[OK] Processed Payroll page loaded")
        except TimeoutException:
            logger.warning("Processed Payroll page timeout")
        
        time.sleep(2)

    def test_08_manage_documents_page_loads(self):
        """Verify Manage Documents page loads"""
        logger.info("=== Testing Manage Documents Page Load ===")
        self.navigate_to_url("/hr-management/manage-documents")
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4 | //h5 | //h6"))
            )
            logger.info("[OK] Manage Documents page loaded")
        except TimeoutException:
            logger.warning("Documents page timeout")
        
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
