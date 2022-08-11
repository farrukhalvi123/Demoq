from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Pages.Dynamic_Properties_Pages import dynamic_properties
from Pages.Practiceformelements import practiceform
from selenium import webdriver
from Constants.URLS import TestData
import logging
import os

from Pages.draganddrop import draganddropclass
from Pages.framespage import handling_frames
from Pages.Login import login


@given("Launch the browser")
def step_impl(context):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-notifications")
        # options.add_argument("download.default_directory=C:\\Users\\786 Computers\\PycharmProjects\\E2E-Web\\TestData\\Downloaded_Files")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        context.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        context.driver.maximize_window()
    elif TestData.BROWSER == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-notifications")
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        os.environ['WDM_LOCAL'] = '1'
        os.environ['WDM_SSL_VERIFY'] = '0'

    elif TestData.BROWSER == 'edge':
        context.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())


@when(u"Open the practice form")
def step_impl(context):
    try:
        context.driver.get(TestData.practiceformpage)
        context.practice = practiceform(context.driver)
    except Exception as e:
        print(e)
        context.driver.close()
        assert False, "Test failed in opening DEMOQA"


@when("Open Drag and Drop Page")
def step_impl(context):
    try:
        context.driver.get(TestData.draganddroppage)
        context.draganddrop = draganddropclass(context.driver)
    except Exception as e:
        print(e)
        context.driver.close()
        assert False, "Test failed in opening DEMOQA"


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
    context.driver.quit()


@when("Open Iframe Page")
def step_impl(context):
    context.driver.get(TestData.frames_url)
    context.frames_handle = handling_frames(context.driver)


@when("Open Dynamic Properties Page")
def step_impl(context):
    context.driver.get(TestData.dynamicprop)
    context.dynamic_prop = dynamic_properties(context.driver)


@when("Open the iris URL")
def step_impl(context):
    context.driver.get(TestData.iris_app_login_page)
    context.loginpage = login(context.driver)
