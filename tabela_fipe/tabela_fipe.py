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
# TabelaFipe
#   sx.slex@gmail.com
import os
import sqlite_single
PATH_DB = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    'tabela_fipe.db'
)


class TabelaFipe(object):

    def __init__(self):
        self.db = sqlite_single.SqliteSingle(PATH_DB)

    def get_tipoveiculo(self):
        sql = '''
            SELECT
                tiv_cod,
                tiv_text
            FROM tiv_tipoveiculo
        '''
        resp = self.db.query(
            sql=sql,
            params=[]
        )
        return [
            dict(
                tiv_cod=item[0],
                tiv_text=item[1]
            ) for item in resp
        ]

    def get_marca(self, tiv_cod=None, mar_cod=None, limit=None, offset=None):
        sql = '''
            SELECT
                mar_cod,
                tiv_cod,
                mar_text
            FROM mar_marca
        '''
        where = []
        params = []
        if tiv_cod:
            where.append('tiv_cod=?')
            params.append(tiv_cod)
        if mar_cod:
            where.append('mar_cod=?')
            params.append(mar_cod)
        if where:
            sql += 'WHERE ' + (' AND '.join(where))
        if limit is not None:
            sql += '\nLIMIT ' + str(int(limit))
            if offset is not None:
                sql += '\nOFFSET ' + str(int(offset))
        resp = self.db.query(
            sql=sql,
            params=params
        )
        return [
            dict(
                mar_cod=item[0],
                tiv_cod=item[1],
                mar_text=item[2]
            ) for item in resp
        ]

    def get_modelo(
        self,
        tiv_cod=None,
        tiv_text=None,
        mod_cod=None,
        mar_cod=None,
        mar_text=None,
        mod_codigofipe=None,
        mod_modbase=None,
        mod_text=None,
        limit=None,
        offset=None
    ):
        sql = '''
            select
                mar.tiv_cod,
                mod.mod_cod,
                mar.mar_cod,
                mod.mod_codigofipe,
                tiv.tiv_text,
                mar.mar_text,
                mod.mod_modbase,
                mod.mod_categoria,
                mod.mod_text
            from mod_modelo mod
            left join mar_marca mar on mod.mar_cod=mar.mar_cod
            left join tiv_tipoveiculo tiv on mar.tiv_cod=tiv.tiv_cod
        '''
        where = []
        params = []
        for param, item_where in [
            [tiv_cod, 'mar.tiv_cod = ?'],
            [tiv_text, 'tiv.tiv_text like ?'],
            [mod_cod, 'mod.mod_cod = ?'],
            [mar_cod, 'mar.mar_cod = ?'],
            [mar_text, 'mar.mar_text like ?'],
            [mod_codigofipe, 'mod.mod_codigofipe = ?'],
            [mod_modbase, 'mod.mod_modbase like ?'],
            [mod_text, 'mod.mod_text like ?'],
        ]:
            if param:
                where.append(item_where)
                params.append(param)
        if where:
            sql += 'WHERE ' + (' AND '.join(where))
        if limit is not None:
            sql += '\nLIMIT ' + str(int(limit))
            if offset is not None:
                sql += '\nOFFSET ' + str(int(offset))
        resp = self.db.query(
            sql=sql,
            params=params
        )
        lresp = [
            dict(
                tiv_cod=item[0],
                mod_cod=item[1],
                mar_cod=item[2],
                mod_codigofipe=item[3],
                tiv_text=item[4],
                mar_text=item[5],
                mod_modbase=item[6],
                mod_categoria=item[7],
                mod_text=item[8],
                versoes=[],
            ) for item in resp
        ]
        for lr in lresp:
            resp_ano = self.db.query(
                sql='''
                select ver_anomodelo, ver_combustivel, ver_valor
                from ver_versao
                where mod_cod=?
                ''',
                params=[lr['mod_cod']]
            )
            lr['versoes'] = [
                dict(
                    ano=ver[0],
                    combustivel=ver[1],
                    valor=ver[2]
                ) for ver in resp_ano
            ]
        return lresp
