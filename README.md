# Corrected Selenium Test Automation

This repository contains corrected Selenium test cases that match the actual website structure of the Gamer PC Admin Dashboard.

## 🎯 Key Corrections Made

### 1. **Updated Menu Selectors**

The original tests were using incorrect menu item names. The corrected tests now use the exact menu text as it appears on the website:

| Original (Incorrect)         | Corrected                                        |
| ---------------------------- | ------------------------------------------------ |
| `Users` or `User`            | `10.1 View Users` (under HR Management)          |
| `Accounting` or `accounting` | `11. Accounting`                                 |
| `HR` or `Human Resource`     | `10. HR Management`                              |
| `Payroll`                    | `10.6 Assign Payroll` / `10.7 Processed Payroll` |
| `Policies`                   | `18. Policies`                                   |
| `Orders` or `orders`         | `5. Orders Management`                           |
| `Content Management`         | `13. Content Management`                         |
| `Guides`                     | `19. Guides`                                     |
| `Gamers` or `gamer`          | `15. Gamers Community`                           |
| `16. Calendar`               | `16. Calendar`                                   |
| `3. Inventory`               | `3. Inventory`                                   |

### 2. **Fixed XPath Syntax Errors**

- Corrected invalid XPath expressions like `//*[@placeholder*="search"]` to valid syntax `//*[contains(@placeholder, "search")]`

### 3. **Updated Navigation Logic**

- Tests now correctly navigate through parent menus before accessing submenus
- Added proper waits for page loads and element visibility

### 4. **Added Customer Tracking Tests**

- Added new test class `TestCustomerTracking` for the `9. Customer-Tracking` section

## 📁 Website Menu Structure

Based on analysis of the Gamer PC Admin Dashboard:

```
1. Dashboard
2. Suppliers
3. Inventory
   - 3.1 View Product Catalogue
   - 3.2 View Stock
   - 3.3 View Listing
   - 3.4 Discounts
   - 3.5 Profit
   - 3.6 GTIN
4. Bundles
5. Orders Management
   - 5.1 View Orders
   - 5.2 View Requests
   - 5.3 View eBay Inquiries
   - 5.4 View eBay Cases
   - 5.5 View eBay Disputes
   - 5.6 View eBay Cancellation
   - 5.7 View eBay Returns
   - 5.8 View Amazon Replacements
6. Shipping & Delivery
7. Reviews
8. Complaints & Ticketing
9. Customer-Tracking
10. HR Management
    - 10.1 View Users
    - 10.2 View Teams
    - 10.3 Employee Shifts
    - 10.4 Attendance
    - 10.5 Manage Leaves
    - 10.6 Assign Payroll
    - 10.7 Processed Payroll
    - 10.8 Manage Documents
11. Accounting
    - 11.1 View Account Categories
    - 11.2 View Recurring Expense
    - 11.3 View Expense
    - 11.4 View Taxation
    - 11.5 View Revenue
    - 11.6 View Report
12. Communications
13. Content Management
14. Affiliate Program
15. Gamers Community
16. Calendar
17. Leads
18. Policies
19. Guides
20. My Tasks
21. Performance Analysis
22. System Settings
```

## 🛠️ Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

### Run all tests:

```bash
python run_tests.py
```

### Run with verbose output:

```bash
python run_tests.py -v
```

### Run in headless mode:

```bash
python run_tests.py --headless
```

### Run specific test file:

```bash
python run_tests.py test_inventory.py
```

### Run tests in parallel:

```bash
python run_tests.py --parallel -w 4
```

### Generate HTML report:

```bash
python run_tests.py --html-report
```

### Using pytest directly:

```bash
# Run all tests
pytest -v

# Run specific test file
pytest test_inventory.py -v

# Run specific test class
pytest test_inventory.py::TestInventory -v

# Run specific test method
pytest test_inventory.py::TestInventory::test_inventory_navigation -v
```

## 📊 Test Files

| File                         | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| `base_test.py`               | Base test class with common utilities                    |
| `test_inventory.py`          | Inventory module tests (3. Inventory)                    |
| `test_accounting.py`         | Accounting module tests (11. Accounting)                 |
| `test_hr.py`                 | HR module tests (10. HR Management, 18. Policies)        |
| `test_client_orders.py`      | Orders Management tests (5. Orders Management)           |
| `test_content_management.py` | Content Management tests (13. Content Management)        |
| `test_user_section.py`       | User tests (10.1 View Users, 9. Customer-Tracking)       |
| `test_gamers.py`             | Gamers Community tests (15. Gamers Community)            |
| `test_guides.py`             | Guides tests (19. Guides)                                |
| `test_calender.py`           | Calendar and My Tasks tests (16. Calendar, 20. My Tasks) |

## 🔧 Configuration

### Default Settings:

- **Base URL**: `https://gamerpc-admin-git-testing-decimal-pro-team.vercel.app`
- **Admin Email**: `admin@gmail.com`
- **Admin Password**: `Bmr@1234`
- **Default Timeout**: 20 seconds

## 📝 Notes

- All menu items include their numbering (e.g., "3. Inventory", "11. Accounting")
- Submenu items include parent number (e.g., "3.3 View Listing", "10.1 View Users")
- Tests use `contains(text(), ...)` for flexible matching
- Proper waits are implemented for dynamic page elements
