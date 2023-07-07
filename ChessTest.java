import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.Test;

public class ChessTest {

    public final String CHROME_DRIVER = "webdriver.chrome.driver";
    public final String DRIVER_PATH = "C:/webdriver/chromedriver.exe";
    public final String URL = "https://www.gamesforthebrain.com/game/checkers/";
    public final String TITLE = "Checkers";
    public final String ACTION = "Select an orange piece to move.";
    public final String CONDITION = "Make a move.";

    @Test
    public void test01() throws InterruptedException {

        System.setProperty(CHROME_DRIVER, DRIVER_PATH);

        WebDriver driver = new ChromeDriver();

        driver.get(URL);
        driver.manage().window().maximize();

        String actual_result = driver.findElement(By.cssSelector("div.page h1")).getText();
        String actual_condition = driver.findElement(By.cssSelector("p#message")).getText();
        Assert.assertEquals(actual_result, TITLE);
        Assert.assertEquals(actual_condition, ACTION);

        driver.findElement(By.cssSelector("div:nth-child(6) > img:nth-child(6)")).click();
        driver.findElement(By.cssSelector("div:nth-child(5) > img:nth-child(7)")).click();
        Thread.sleep(3500);

        String condition_one = driver.findElement(By.cssSelector("p#message")).getText();
        Assert.assertEquals(condition_one, CONDITION);

        driver.findElement(By.cssSelector("div:nth-child(7) > img:nth-child(7)")).click();
        driver.findElement(By.cssSelector("div:nth-child(6) > img:nth-child(6)")).click();
        Thread.sleep(3500);

        driver.findElement(By.cssSelector("div:nth-child(8) > img:nth-child(8)")).click();
        driver.findElement(By.cssSelector("div:nth-child(7) > img:nth-child(7)")).click();
        Thread.sleep(3500);

        driver.findElement(By.cssSelector("div:nth-child(6) > img:nth-child(2)")).click();
        driver.findElement(By.cssSelector("div:nth-child(5) > img:nth-child(3)")).click();
        Thread.sleep(3500);

        driver.findElement(By.cssSelector("div:nth-child(6) > img:nth-child(2)")).getCssValue("onclick");
        driver.findElement(By.cssSelector("div:nth-child(7) > img:nth-child(3)")).click();
        driver.findElement(By.cssSelector("div:nth-child(5) > img:nth-child(1)")).click();
        Thread.sleep(3500);

        driver.findElement(By.cssSelector("p.footnote > a:nth-child(1)")).click();
        Thread.sleep(3500);

        String actual_resulttwo = driver.findElement(By.cssSelector("div.page h1")).getText();
        String actual_conditiontwo = driver.findElement(By.cssSelector("p#message")).getText();
        Assert.assertEquals(actual_resulttwo, TITLE);
        Assert.assertEquals(actual_conditiontwo, ACTION);

        driver.quit();
    }
}