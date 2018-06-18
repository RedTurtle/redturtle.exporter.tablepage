# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import redturtle.exporter.tablepage


class RedturtleExporterTablepageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=redturtle.exporter.tablepage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.exporter.tablepage:default')


REDTURTLE_EXPORTER_TABLEPAGE_FIXTURE = RedturtleExporterTablepageLayer()


REDTURTLE_EXPORTER_TABLEPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_EXPORTER_TABLEPAGE_FIXTURE,),
    name='RedturtleExporterTablepageLayer:IntegrationTesting',
)


REDTURTLE_EXPORTER_TABLEPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_EXPORTER_TABLEPAGE_FIXTURE,),
    name='RedturtleExporterTablepageLayer:FunctionalTesting',
)


REDTURTLE_EXPORTER_TABLEPAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_EXPORTER_TABLEPAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RedturtleExporterTablepageLayer:AcceptanceTesting',
)
