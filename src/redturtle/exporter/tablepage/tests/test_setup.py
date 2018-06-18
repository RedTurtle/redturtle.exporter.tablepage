# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from redturtle.exporter.tablepage.testing import REDTURTLE_EXPORTER_TABLEPAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that redturtle.exporter.tablepage is properly installed."""

    layer = REDTURTLE_EXPORTER_TABLEPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if redturtle.exporter.tablepage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'redturtle.exporter.tablepage'))

    def test_browserlayer(self):
        """Test that IRedturtleExporterTablepageLayer is registered."""
        from redturtle.exporter.tablepage.interfaces import (
            IRedturtleExporterTablepageLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IRedturtleExporterTablepageLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = REDTURTLE_EXPORTER_TABLEPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['redturtle.exporter.tablepage'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if redturtle.exporter.tablepage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'redturtle.exporter.tablepage'))

    def test_browserlayer_removed(self):
        """Test that IRedturtleExporterTablepageLayer is removed."""
        from redturtle.exporter.tablepage.interfaces import \
            IRedturtleExporterTablepageLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IRedturtleExporterTablepageLayer,
            utils.registered_layers())
