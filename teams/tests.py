#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core import mail
from models import Position
from django.conf import settings
from datetime import datetime
import os

class TeamTestCase(TestCase):
#    fixtures = ['shv_testdata.json']

    def setUp(self):
        self.client = Client()
    
    def list_to_dict(self, list, key = None, value = None):
        return_value = {}
        value_was_none = value is None
        for entry in list:
            if key is None:
                key_value = entry.keys()[0]
                if value_was_none:
                    value = key_value
            else:
                key_value = int(entry[key])
            if value:
                return_value[key_value] = entry[value]
            else:
                return_value[key_value] = entry                
        return return_value

    def test_add_position(self):
        position = Position.objects.create(name='Test Position', slug='test-position')
        self.assertEqual(position.name, 'Test Position')
