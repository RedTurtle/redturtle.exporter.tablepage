# -*- coding: utf-8 -*-
from collective.tablepage.interfaces import IDataStorage
from plone import api
from plone.memoize import view
from ploneorg.jsonify.jsonify import GetItem as BaseGetItemView
from redturtle.exporter.base.browser.jsonify import get_json_object
from redturtle.exporter.base.browser.wrapper import Wrapper

import json
import pprint
import sys
import traceback


class GetItemTablePage(BaseGetItemView):

    def __call__(self):
        """
        Table page
        """
        try:
            context_dict = Wrapper(self.context)
            context_dict.update({
                'table_rows': self.get_table_rows()})

        except Exception, e:
            tb = pprint.pformat(traceback.format_tb(sys.exc_info()[2]))
            return 'ERROR: exception wrapping object: %s\n%s' % (str(e), tb)

        return get_json_object(self, context_dict)

    @property
    @view.memoize
    def headers(self):
        return map(lambda x: x.get('id'), self.context.getPageColumns())

    def get_table_rows(self):
        storage = IDataStorage(self.context)
        return [self.generate_row(data) for index, data in enumerate(storage)]

    def generate_row(self, data):
        row = {k: data.get(k) for k in self.headers}
        row['__uuid__'] = data.get('__uuid__')
        row['__creator__'] = data.get('__creator__')
        return row
