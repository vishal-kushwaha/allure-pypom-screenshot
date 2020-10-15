''' hook implementations for pypom '''

import os

import allure
from pypom import hookimpl


@hookimpl
def pypom_after_wait_for_page_to_load(page):
    ''' capture the screenshot of a page once it is loaded '''
    file_name = page.__class__.__name__ + '.png'
    page.selenium.get_screenshot_as_file(file_name)
    allure.attach.file(file_name, allure.attachment_type.PNG)
    os.remove(file_name)


@hookimpl
def pypom_after_wait_for_region_to_load(region):
    ''' capture the screenshot of a region once it is loaded '''
    file_name = region.__class__.__name__ + '.png'
    region.root.screenshot(file_name)
    allure.attach.file(file_name, allure.attachment_type.PNG)
    os.remove(file_name)
