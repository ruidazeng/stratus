const puppeteer = require('puppeteer');


for (let i = 0; i < 1; ++i) {
    (async () => {
        const browser = await puppeteer.launch({ headless: false });
        const page = await browser.newPage();
        await page.goto('http://stratus-final.ml/');

        //click on predict button 
        const button = await page.$('#predictbutton');
        await button.evalute( button => button.click() )

        await browser.close();
    })();
}
