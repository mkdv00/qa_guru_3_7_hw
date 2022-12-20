import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github_issue_with_context_manager(browser_config):
    with allure.step('Open browser'):
        browser.open('https://github.com/')

    with allure.step('Search for "eroshenkoam/allure-example"'):
        browser.element('input[name="q"]').should(be.blank).type('eroshenkoam/allure-example').press_enter()

    with allure.step('Click by repository'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Click by Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('Find Issue #81'):
        browser.element(by.partial_text('#81')).should(be.visible)
