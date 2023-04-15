from selenium.webdriver.common.by import By

from src.api.models.comment import Comment
from src.api.models.photo import Photo
from src.api.models.post import Post
from src.core.base.base_form import BaseForm
from src.core.browser.browser import Browser
from src.core.element.button import Button
from src.core.element.label import Label
from src.utils.action_utils import pause
from src.utils.json_parser import get_config


class MyProfilePage(BaseForm):
    __config = get_config("api_config.example.json")
    __owner_id = __config["owner_id"]
    __uniq_element = Label(By.XPATH, "//div[@class='ProfileWrapper']", "Unique element")

    def __init__(self):
        super().__init__(self.__uniq_element, "My Profile Page")

    def __get_post_element(self, post: Post):
        return Label(By.XPATH, f"//div[@id='wpt{self.__owner_id}_{post.id}']",
                     f"Post {post.id}")

    def __get_post_text_element(self, post: Post):
        return Label(By.XPATH,
                     f"//div[@id='wpt{self.__owner_id}_{post.id}']//div[contains(@class, 'wall_post_text')]",
                     "Text from post")

    def __get_post_author_element(self, post: Post):
        return Label(By.XPATH, f"//div[@id='post{self.__owner_id}_{post.id}']//a[@class='author']",
                     "Author of post")

    def __get_post_image_element(self, post: Post):
        return Label(By.XPATH, f"//div[@id='wpt{self.__owner_id}_{post.id}']//a[@aria-label='photo']",
                     "Image of post")

    def __get_post_comment_text_element(self, comment: Comment):
        return Label(By.XPATH, f"//div[@id='wpt{self.__owner_id}_{comment.id}']//div[@class='wall_reply_text']",
                     "Text from comment")

    def __get_post_comment_author_element(self, comment: Comment):
        return Label(By.XPATH, f"//div[@id='post{self.__owner_id}_{comment.id}']//a[@class='author']",
                     "Author of comment")

    def __get_post_reaction_button(self, post: Post):
        return Button(
            By.XPATH,
            f"//div[@data-reaction-target-object='wall{self.__owner_id}_{post.id}']",
            "Like Button")

    def __get_show_next_comments_btn(self, post: Post):
        return Button(By.XPATH,
                      f"//a[@href='/wall{self.__owner_id}_{post.id}' and contains(@onclick, 'showNextReplies')]",
                      "Show Next Comments Button")

    def __scroll_to_img_from_post(self, post: Post):
        label = self.__get_post_image_element(post)
        Browser.scroll_to_element(label.get_web_element(), label.name)

    def get_text_from_post(self, post: Post) -> str:
        pause()
        label = self.__get_post_text_element(post)
        label.wait_for_displayed()
        return label.get_text()

    def get_author_from_post(self, post: Post) -> str:
        pause()
        label = self.__get_post_author_element(post)
        label.wait_for_displayed()
        return label.get_text()

    def get_photo_from_post(self, post: Post) -> Photo:
        pause()
        self.__scroll_to_img_from_post(post)
        label = self.__get_post_image_element(post)
        label.wait_for_displayed()
        # Attribute returned string like ownerId_photoId, this did split string with
        # '_' and return second element of array
        text = label.get_text_from_attribute("href")
        return Photo(int(label.get_text_from_attribute("href").split("_")[1]))

    def get_text_from_comment(self, comment: Comment, post: Post):
        pause()
        self.__scroll_to_img_from_post(post)
        label = self.__get_post_comment_text_element(comment)
        if not label.is_visible():
            self.click_on_btn_show_next_comment(post)
        label.wait_for_displayed()
        return label.get_text()

    def get_author_from_comment(self, comment: Comment, post: Post):
        pause()
        self.__scroll_to_img_from_post(post)
        label = self.__get_post_comment_author_element(comment)
        button = self.__get_show_next_comments_btn(post)
        if button.is_visible():
            self.click_on_btn_show_next_comment(post)
        label.wait_for_displayed()
        return label.get_text()

    def click_on_btn_show_next_comment(self, post: Post):
        button = self.__get_show_next_comments_btn(post)
        button.wait_for_clickable()
        button.click_element()

    def click_on_btn_reaction_post(self, post: Post):
        button = self.__get_post_reaction_button(post)
        button.wait_for_clickable()
        button.click_element()

    def is_post_exist(self, post: Post):
        pause()
        label = self.__get_post_element(post)
        label.wait_for_not_displayed()
        b = label.is_visible()
        return not b
