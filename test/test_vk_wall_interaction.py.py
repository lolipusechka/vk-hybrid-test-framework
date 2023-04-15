import logging as log

from pages.feed_page import FeedPage
from pages.id_page import IdPage
from pages.login_page import LoginPage
from pages.my_profile_page import MyProfilePage
from src.api.utils.vk_api_utils import *
from src.core.base.base_test import BaseTest
from src.core.browser.browser import Browser
from src.utils.random_utils import randomword


class Test(BaseTest):
    @staticmethod
    def test(setup):
        login_page = LoginPage()
        id_page = IdPage()
        feed_page = FeedPage()
        my_profile_page = MyProfilePage()
        config = get_config("test_config.example.json")

        log.getLogger().info(f"Step 1: [UI] Go to {config['url']}")
        Browser.go_to(config["url"])
        assert login_page.is_displayed(), "Login Page is not displayed"
        log.getLogger().info("Login Page is displayed")

        log.getLogger().info("Step 2: [UI] Login")
        login_page.sing_in(config["login"])
        assert id_page, "ID Page is not displayed"
        log.getLogger().info("ID Page is displayed")
        id_page.input_password(config["password"])
        assert feed_page.is_displayed(), "Feed Page is not displayed"
        log.getLogger().info("Feed Page is displayed")

        log.getLogger().info('Step 3: [UI] Go to "My Profile"')
        feed_page.go_to_my_profile()
        assert my_profile_page.is_displayed(), "My Profile Page is not displayed"
        log.getLogger().info("My Profile Page pages is displayed")

        log.getLogger().info("Step 4: [API] Using an API request, create a post with "
                             "randomly generated text on the wall and get the post id from the response")
        random_msg1 = randomword(10)
        log.getLogger().info(f"Random msg = '{random_msg1}'")
        post = wall_post(random_msg1)

        log.getLogger().info("Step 5: [UI] Without refreshing the pages, "
                             "make sure that a post with the right text from the right user appeared on the wall")
        text_from_post_random1 = my_profile_page.get_text_from_post(post)
        assert text_from_post_random1 == random_msg1, "Actual text is not equals expected text"
        author_from_post_random1 = my_profile_page.get_author_from_post(post)
        if (author_from_post_random1.lower() == config["profileNameRU"].lower()
                or author_from_post_random1.lower() == config["profileNameEN"].lower()):
            assert True
        else:
            assert False, "Actual Author is not equals expected Author"
        log.getLogger().info("Actual Author is equals expected Author")

        log.getLogger().info("Step 6: [API] Edit post via API request - change text and add (upload) any picture")
        random_msg2 = randomword(15)
        photo = save_wall_photo("cane.jpg")
        wall_edit(photo, post, random_msg2)

        log.getLogger().info("Step 7: [UI] Without refreshing the pages, make sure that the text of the message has "
                             "changed and the uploaded picture has been added "
                             "(make sure that the pictures are the same)")
        text_from_post_random1 = my_profile_page.get_text_from_post(post)
        assert text_from_post_random1 == random_msg2, "Actual text is not equals expected text"
        log.getLogger().info("Actual text is equals expected text")
        assert my_profile_page.get_photo_from_post(post).id == photo.id, "Actual image is not equals expected image"
        log.getLogger().info("Actual image is equals expected image")

        log.getLogger().info("Step 8: [API] Using an API request to add a comment to a post with random text")
        random_comment = randomword(5)
        comment = wall_create_comment(post, random_comment)

        log.getLogger().info("Step 9: [UI] Without refreshing the pages, make sure that a comment from the "
                             "correct user has been added to the desired post")
        author_from_comment = my_profile_page.get_author_from_comment(comment, post)
        if (author_from_comment.lower() == config["profileNameRU"].lower()
                or author_from_comment.lower() == config["profileNameEN"].lower()):
            assert True
        else:
            assert False, "Actual Author is not equals expected Author"
        log.getLogger().info("Actual Author is equals expected Author")

        log.getLogger().info("Step 10: [UI] Via UI like the post")
        my_profile_page.click_on_btn_reaction_post(post)

        log.getLogger().info("Step 11: [API] Through an API request, "
                             "make sure that the post has a like from the correct user")
        users = wall_get_likes(post).users
        b = False
        for user in users:
            if user.id == int(config["user_id"]):
                b = True
                break
        assert b, "There is no like from expected user"
        log.getLogger().info("There is like from expected user")

        log.getLogger().info("Step 12: [API] Delete created post via API request")
        wall_delete(post)

        log.getLogger().info("Step 13: [UI] Without refreshing the pages, make sure that the post is deleted")
        b = my_profile_page.is_post_exist(post)
        assert b, "Post is not deleted"
        log.getLogger().info("Post is deleted")
