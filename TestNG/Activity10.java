package TestNG;

import static org.testng.Assert.assertEquals;

import java.io.FileInputStream;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class Activity10 {

    WebDriver driver;
    WebDriverWait wait;

    @BeforeClass
    public void beforeClass() {
        driver = new FirefoxDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(15));

        // Open browser
        driver.get("https://training-support.net/webelements/simple-form");
    }

    // Read Excel data
    public static List<List<String>> readExcel(String filePath) {
        List<List<String>> data = new ArrayList<>();

        try (FileInputStream file = new FileInputStream(filePath);
             XSSFWorkbook workbook = new XSSFWorkbook(file)) {

            XSSFSheet sheet = workbook.getSheetAt(0);

            for (Row cells : sheet) {
                List<String> rowData = new ArrayList<>();
                for (Cell cell : cells) {
                    switch (cell.getCellType()) {
                        case STRING:
                            rowData.add(cell.getStringCellValue());
                            break;
                        case NUMERIC:
                            rowData.add(String.valueOf(cell.getNumericCellValue()));
                            break;
                        case BOOLEAN:
                            rowData.add(String.valueOf(cell.getBooleanCellValue()));
                            break;
                        default:
                            rowData.add("");
                    }
                }
                data.add(rowData);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return data;
    }

    @DataProvider(name = "Events")
    public static Object[][] signUpInfo() {
        String filePath = "src/test/resources/Activity10.xlsx";
        List<List<String>> data = readExcel(filePath);

        Object[][] result = new Object[data.size() - 1][1];
        for (int i = 1; i < data.size(); i++) {
            result[i - 1][0] = data.get(i);
        }
        return result;
    }

    @Test(dataProvider = "Events")
    public void lregisterTest(List<String> rows) throws InterruptedException {
        // Wait for the page to load
        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("full-name")));

        // Wait for Full Name field to be visible and interactable
        WebElement fullName = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("full-name")));
        fullName.clear();
        fullName.sendKeys(rows.get(0));

        // Wait for Email field to be visible and interactable
        WebElement email = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("email")));
        email.clear();
        email.sendKeys(rows.get(1));

        // Wait for Event Date field to be visible and interactable
        WebElement eventDate = wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("event-date")));
        eventDate.clear();
        eventDate.sendKeys(rows.get(2).replaceAll("\"", ""));

        // Wait for Additional Details field to be visible and interactable
        WebElement details = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("additional-details")));
        details.clear();
        details.sendKeys(rows.get(3));

        // Wait for Submit button to be clickable and click
        WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button[text()='Submit']")));
        submitButton.click();

        // Wait for the confirmation message to be present in the DOM and visible
        WebDriverWait longWait = new WebDriverWait(driver, Duration.ofSeconds(15));
        WebElement confirmation = longWait.until(
                ExpectedConditions.visibilityOfElementLocated(
                        By.id("confirmation-message")
                )
        );

        // Assert confirmation message
        assertEquals(confirmation.getText().trim(), "Your event has been scheduled!");

        // Refresh page for next dataset
        driver.navigate().refresh();
        
        // Wait for page to reload and form to be ready
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("full-name")));
        
        // Additional wait for form to be interactive
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("full-name")));
    }

    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}
