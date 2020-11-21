from selenium import webdriver
from time import sleep


def main():

    url = "https://www.genkotsu-hb.com/shop/sasagase.php"
    driver = webdriver.PhantomJS()
    driver.get(url)

    sleep(2)
    map_box_element = driver.find_element_by_class_name("map_box")
    frame_element = map_box_element.find_element_by_tag_name("iframe")
    driver.switch_to.frame(frame_element)

    maps_link = driver.find_element_by_class_name("google-maps-link")
    a_tag = maps_link.find_element_by_tag_name("a")
    href_value = a_tag.get_attribute("href")
    print(href_value)


if __name__ == '__main__':
    main()
