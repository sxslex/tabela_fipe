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

    def get_by_codefipe(self, codefipe):
        resp = self.db.query(
            sql='''
                select
                    mod.mod_cod,
                    mod.mod_codigofipe,
                    tiv.tiv_text,
                    mar.mar_text,
                    mod.mod_modbase,
                    mod.mod_text
                from mod_modelo mod
                left join mar_marca mar on mod.mar_cod=mar.mar_cod
                left join tiv_tipoveiculo tiv on mar.tiv_cod=tiv.tiv_cod
                where mod.mod_codigofipe = ?
            ''',
            params=[codefipe]
        )
        if not resp:
            return None
        dresp = dict(
            mod_cod=resp[0][0],
            codigo_fipe=resp[0][1],
            tipo=resp[0][2],
            marca=resp[0][3],
            modelo=resp[0][4],
            versoes=[]
        )
        resp_ano = self.db.query(
            sql='''
            select ver_anomodelo, ver_combustivel, ver_valor
            from ver_versao
            where mod_cod=?
            ''',
            params=[dresp['mod_cod']]
        )
        dresp['versoes'] = [
            dict(
                ano=ver[0],
                combustivel=ver[1],
                valor=ver[2]
            ) for ver in resp_ano
        ]
        return dresp

    def get_marca(self, mar_cod=None, tiv_cod=None, limit=None, offset=None):
        sql = '''
            SELECT
                mar_cod,
                tiv_cod,
                mar_text
            FROM mar_marca
        '''
        where = []
        params = []
        if mar_cod:
            where.append('mar_cod=?')
            params.append(mar_cod)
        if tiv_cod:
            where.append('tiv_cod=?')
            params.append(tiv_cod)
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
                mar_cod=ver[0],
                tiv_cod=ver[1],
                mar_text=ver[2]
            ) for ver in resp
        ]
