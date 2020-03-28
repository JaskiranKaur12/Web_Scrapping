from bs4 import BeautifulSoup
import re

ITEM_HTML = '''
<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''
class ParsedItemLocators:
    """
    Locators for an item in HTML page.
    """
    NAME_LOCATOR='article.product_pod h3 a'
    LINK_LOCATOR='article.product_pod h3 a'
    PRICE_LOCATOR='article.product_pod div p'
    RATING_LOCATOR='article.product_pod p.star-rating'

class ParsedItem:
    #Encapsulation
    """A class that will take an HTML page or part of it and
     properties of an item"""

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR  # CSS locator
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR  # CSS locator
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_link = self.soup.select_one(locator)
        item_price = item_link.string
        price = item_price.split('£')
        # exp='£([0-9]+/.[0-9]+)' #Alternate way
        # matches = re.search(exp, item_price)
        # print(matches.group(1))
        return float(price[1])

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_tag = self.soup.select_one(locator)
        # classes = [ classes for classes in star_tag.attrs['class'] if classes!='star-rating']
        rating_classes = list(filter(lambda x: x != 'star-rating', star_tag.attrs['class']))
        return rating_classes[0]

item= ParsedItem(ITEM_HTML)
print(item.rating)
