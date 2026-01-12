import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class BavitTest {
    public static void main(String[] args) {
        // --------------------------
        // Browser options
        // --------------------------
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--disable-blink-features=AutomationControlled");
        options.addArguments("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36");

        WebDriver driver = new ChromeDriver(options);
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20));

        try {
            // --------------------------
            // 3) Login
            // --------------------------
            driver.get("https://bavit-test.vercel.app/admin/login");
            driver.manage().window().maximize();
            Thread.sleep(2000);

            // Scroll down a bit
            for (int i = 0; i < 2; i++) {
                ((org.openqa.selenium.JavascriptExecutor) driver).executeScript("window.scrollBy(0, 800);");
                Thread.sleep(500);
            }

            WebElement emailField = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//input[@name='email']")));
            emailField.sendKeys("admin@gmail.com");

            WebElement passwordField = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//input[@type='password']")));
            passwordField.sendKeys("Bmr@1234");

            WebElement loginButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button[@type='submit']")));
            loginButton.click();
            Thread.sleep(2000);

            // ----------------------------------------------------------------------------------------------
            // 4) Navigate to inventory -> View listing -> Add listing
            // ----------------------------------------------------------------------------------------------

            WebElement accounting = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//span[text()='13. Accounting']")));
            accounting.click();
            Thread.sleep(1000);

            // ✅ Scroll inside sidebar element
            WebElement element = driver.findElement(By.xpath("//*[@id='layout-wrapper']/div[1]"));
            ((org.openqa.selenium.JavascriptExecutor) driver).executeScript(
                "const el = arguments[0]; el.scrollTop = (el.scrollHeight - el.clientHeight) / 2;", element);
            Thread.sleep(2000);

            WebElement viewRecurringExpenses = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//a[text()='13.2 View Recurring Expense']")));
            viewRecurringExpenses.click();
            Thread.sleep(1000);

            WebElement addExpenseCategory = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id='layout-wrapper']/div[3]/div/div/div/div/div[1]/div[2]/div/div[2]/button/i")));
            addExpenseCategory.click();
            Thread.sleep(2000);

            // ---------------------------------
            // Fill the form fields
            // ---------------------------------
            WebElement title = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@placeholder='Enter recurring expense title']")));
            title.sendKeys("tester");
            Thread.sleep(2000);

            WebElement amount = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@placeholder='0.00']")));
            amount.sendKeys("20000");
            Thread.sleep(2000);

            // Frequency dropdown
            WebElement frequency = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id='frequency']/div/div[1]/div[2]")));
            frequency.click();

            WebElement firstOption = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//div[contains(@id,'react-select') and @role='option'][1]")));
            firstOption.click();
            Thread.sleep(2000);

            // Enter date
            WebElement enterDate = wait.until(ExpectedConditions.presenceOfElementLocated(
                    By.xpath("//*[@id='layout-wrapper']/div[3]/div/div/div/div/form/div[3]/div[1]/div/div/div/div[1]")));
            enterDate.sendKeys("19 09 2025");
            Thread.sleep(6000);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // driver.quit(); // Uncomment to close browser after test
        }
    }
}

