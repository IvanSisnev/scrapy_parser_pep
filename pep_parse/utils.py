"""
Utils проекта.
"""
import logging


def scrape(obj, xpath: str = None, css: str = None, attrib: str = None):
    """
    Забирает данные из объекта response или Selector c отработкой ошибки.
    :param obj: объект парсинга.
    :param xpath: строка для метода xpath
    :param css: строка для метода css
    :param attrib: строка для метода attrib
    :return: объект Selector
    """
    result = None
    if xpath:
        result = obj.xpath(xpath)
    elif css:
        result = obj.css(css)
    elif attrib:
        result = obj.attrib[attrib]

    if not result:
        error_msg: str = (f'В объекте {obj} не найден тег или аттрибут:'
                          f'\nxpath {xpath}'
                          f'\ncss {css}'
                          f'\nattrib {attrib}')
        logging.critical(msg=error_msg, stack_info=True)
        raise SystemExit(error_msg)

    return result
