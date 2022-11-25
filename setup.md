# Setting up ChromeDriver for using Selenium
1. Get the zip file using wget
` > wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip `

2. Unzip the chrome driver file
` > unzip chromedriver_linux64.zip `

3. Configure ChromeDriver on your system
` > sudo mv chromedriver /usr/bin/chromedriver `
` > sudo chowm root:root /usr/bin/chromedriver `
` > sudo chmod +x /usr/bin/chromedriver `
