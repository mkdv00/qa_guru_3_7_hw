from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github_issue_with_clean_selene(browser_config):
    browser.open('https://github.com/')

    browser.element('input[name="q"]').should(be.blank).type('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#81')).should(be.visible)
