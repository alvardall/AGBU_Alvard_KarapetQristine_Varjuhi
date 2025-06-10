
     count = 0
    for locator in locators:
        try:
            driver.find_element(self.elem_count, locator["value"])
            count += 1
        except Exception as e:
            print(f"Element not found for selector: {locator['value']} — {e}")
    print(f" Total elements found: {count}")