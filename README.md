# edgedriver-autoinstaller
Automatically download and install [edgedriver](https://edgedriver.chromium.org/) that supports the currently installed version of edge. This installer supports Linux, MacOS and Windows operating systems.

## Installation

```bash
pip install edgedriver-autoinstaller
```

## Usage
Just type `import edgedriver_autoinstaller` in the module you want to use edgedriver.

## Example
```
from selenium import webdriver
import edgedriver_autoinstaller


edgedriver_autoinstaller.install()  # Check if the current version of edgedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add edgedriver to path

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
```
