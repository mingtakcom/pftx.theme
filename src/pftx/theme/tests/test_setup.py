# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from pftx.theme.testing import PFTX_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that pftx.theme is properly installed."""

    layer = PFTX_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pftx.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'pftx.theme'))

    def test_browserlayer(self):
        """Test that IPftxThemeLayer is registered."""
        from pftx.theme.interfaces import (
            IPftxThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IPftxThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PFTX_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['pftx.theme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if pftx.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'pftx.theme'))

    def test_browserlayer_removed(self):
        """Test that IPftxThemeLayer is removed."""
        from pftx.theme.interfaces import \
            IPftxThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPftxThemeLayer,
            utils.registered_layers(),
        )
