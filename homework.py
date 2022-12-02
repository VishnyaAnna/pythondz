

def print_func_name(funk_name, *args):
    print('Название функции: ' + funk_name.__name__.title().replace('_', ' '))
    print('Значение аргументов: ', *args)

def open_browser(browser_name):
    print_func_name(open_browser, browser_name)
    pass

def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)
    pass


open_browser("chrome")
go_to_companyname_homepage("google.com.")
find_registration_button_on_login_page("google.com", "логин")
