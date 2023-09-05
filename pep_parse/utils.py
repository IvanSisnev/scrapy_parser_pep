"""
Utils проекта.
"""

def scrape(obj, xpath: str =None, css: str =None, attrib: str =None):
    """
    Забирает данные из объекта response или Selector c отработкой ошибки.
    :param obj: объект парсинга.
    :param xpath: строка для метода xpath
    :param css: строка для метода css
    :param attrib: строка для метода attrib
    :return: объект Selector
    """
    try:
        result = None
        if xpath:
            result = obj.xpath(xpath)
        elif css:
            result = obj.css(css)
        elif attrib:
            result = obj.attrib[attrib]
        if result:
            return result
    except:
        pass

        # except IOError as exc:
        #     error_msg: str = ('Не удалось записать данные в файл.')
        #     logging.exception(msg=error_msg, stack_info=True)
        #     raise SystemExit(error_msg) from exc


