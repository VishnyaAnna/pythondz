

def name():
    name = 'chrome'
    return name

def call_name(brouser):
    return brouser
print(call_name(name()))


def open_browser(browser_name):
    new_name = 'open_' + browser_name
    return new_name
print(open_browser(call_name(name()).upper()))

def go_to_companyname_homepage(page_url):
    new_name_url = 'https://www.google.com/' + page_url
    return new_name_url
print(go_to_companyname_homepage(call_name(name())))


def find_registration_button_on_login_page(page_url = "chrome.com", button_text = "login"):
    call_name(name())
print(find_registration_button_on_login_page(page_url="chome.com", button_text="login"))
