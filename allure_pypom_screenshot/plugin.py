''' hook implementations for pypom '''

import os

import allure
from pypom import hookimpl


@hookimpl
def pypom_after_wait_for_page_to_load(page):
    ''' capture the screenshot of a page once it is loaded '''
    pass


@hookimpl
def pypom_after_wait_for_region_to_load(region):
    ''' capture the screenshot of a region once it is loaded '''
    pass
