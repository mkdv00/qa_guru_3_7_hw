import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_with_decorators(browser_config):
    open_browser('https://github.com/')
    search_for_repo('eroshenkoam/allure-example')
    click_by_repo('eroshenkoam/allure-example')
    click_by_issue_tab()
    find_issue('#81')


@allure.step('Open browser')
def open_browser(url):
    browser.open(url)


@allure.step('Search for {repo}')
def search_for_repo(repo):
    browser.element('input[name="q"]').should(be.blank).type(repo).press_enter()


@allure.step('Click by repository {repo}')
def click_by_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Click by Issues tab')
def click_by_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Find Issue {issue}')
def find_issue(issue):
    browser.element(by.partial_text(issue)).should(be.visible)
