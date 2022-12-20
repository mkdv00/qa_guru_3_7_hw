from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

import allure


@allure.story('Search for the issue')
@allure.feature('Issues')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kudaevma')
@allure.link('https://github.com/', name='Testing')
@allure.tag('web')
def test_with_labels(browser_config):
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


def test_with_dynamic_allure(browser_config):
    allure.dynamic.story('Search for the issue')
    allure.dynamic.feature('Issues')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'kudaevma')
    allure.dynamic.link('https://github.com/', name='Testings')
    allure.dynamic.tag('web')

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
