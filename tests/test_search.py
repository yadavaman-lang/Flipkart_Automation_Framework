
from pages.home_page import HomePage


def test_flipkart_product_search(driver):
    home_page = HomePage(driver)

    # Step 1: Open Flipkart
    home_page.open_homepage()

    # Step 2: Search for a product
    home_page.search_product("laptop")

    # Step 3: Wait for the search page
    home_page.wait_for_search_results()

    # Step 4: Validate the result
    current_url = home_page.get_current_url()

    assert "/search" in current_url.lower(), (
        f"Search results page did not load. URL: {current_url}"
    )

    print("Product search navigation successful!")
    print("Current URL:", current_url)
