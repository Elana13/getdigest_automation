from tests.acceptance.page_model.base_page import BasePage


class AddonPage(BasePage):
    @property
    def url(self):
        return super(AddonPage, self).url + '/en/add-on'
