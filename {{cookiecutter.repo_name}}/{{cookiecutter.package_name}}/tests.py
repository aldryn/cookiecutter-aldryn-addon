# -*- coding: utf-8 -*-
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.test import TestCase
#
# from cms import api
# from cms.models import CMSPlugin
# from cms.test_utils.testcases import BaseCMSTestCase, URL_CMS_PLUGIN_ADD
# from cms.utils import get_cms_setting
#
# from .cms_plugins import MyCMSPlugin
#
#
# class GalleryPluginTestCase(TestCase, BaseCMSTestCase):
#     su_username = 'user'
#     su_password = 'pass'
#
#     def setUp(self):
#         self.template = get_cms_setting('TEMPLATES')[0][0]
#         self.language = settings.LANGUAGES[0][0]
#         self.page = api.create_page('page', self.template, self.language, published=True)
#         self.placeholder = self.page.placeholders.all()[0]
#         self.superuser = self.create_superuser()
#
#     def create_superuser(self):
#         return User.objects.create_superuser(self.su_username, 'email@example.com', self.su_password)
#
#     def test_something(self):
#         self.assertEqual(2, 1+1)
