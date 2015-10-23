# -*- coding: utf-8 -*-
#
# Copyright 2015 Alexandre Villela (SleX) <https://github.com/sxslex/sxtools/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    by sx.slex@gmail.com

from tabela_fipe import TabelaFipe
import unittest
import pprint


class TestTabelaFipe(unittest.TestCase):

    def test_01_get_tipoveiculo(self):
        tb = TabelaFipe()
        resp = tb.get_tipoveiculo()
        self.assertTrue(isinstance(resp, list))
        # pprint.pprint(resp)

    def test_02_get_marca(self):
        tb = TabelaFipe()
        resp = tb.get_marca(limit=5, offset=0)
        self.assertTrue(isinstance(resp, list))
        self.assertTrue(len(resp) == 5)
        # pprint.pprint(resp)

    def test_03_get_marca(self):
        tb = TabelaFipe()
        resp = tb.get_marca(mar_cod=1, limit=10)
        self.assertTrue(isinstance(resp, list))
        self.assertTrue(len(resp) == 1)
        self.assertTrue(resp[0]['mar_text'] == 'ACURA')

    def test_04_get_marca(self):
        tb = TabelaFipe()
        resp = tb.get_marca(tiv_cod=2, limit=2)
        self.assertTrue(isinstance(resp, list))
        self.assertTrue(len(resp) == 2)
        self.assertTrue(resp[0]['tiv_cod'] == 2)
        # pprint.pprint(resp)

    def test_05_get_modelo(self):
        tb = TabelaFipe()
        resp = tb.get_modelo(mod_codigofipe='006008-9')
        self.assertTrue(isinstance(resp, list))
        self.assertTrue(len(resp) == 1)
        # pprint.pprint(resp)

    def test_06_get_modelo(self):
        tb = TabelaFipe()
        resp = tb.get_modelo(mod_codigofipe='111111-1')
        self.assertTrue(isinstance(resp, list))
        self.assertTrue(len(resp) == 0)
        # pprint.pprint(resp)

    def test_07_get_modelo(self):
        tb = TabelaFipe()
        resp = tb.get_modelo(
            tiv_cod=1, mod_cod=9, mar_cod=3, limit=5, offset=0
        )
        self.assertTrue(isinstance(resp, list))
        self.assertTrue(len(resp) == 1)
        pprint.pprint(resp)
