from instapy import InstaPy  # ! Importing the InstaPy Module

# $ The InstaPy Module only works with Firefox Browser

browser = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# % Body of the Program.

session = InstaPy(username="USERNAME", password="PASSWORD",
                  browser_executable_path=browser)
session.login()
session.end()

