======
tabela_fipe
======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/sxslex/tabela_fipe
   :target: https://gitter.im/sxslex/tabela_fipe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://travis-ci.org/sxslex/tabela_fipe.svg?branch=master
    :target: https://travis-ci.org/sxslex/tabela_fipe

Simple access library of data from the "Table Fipe".

Vehicle information: Manufacturer, Model, Vehicle, versions and prices.

Installing
--------

For install sxtools, run on terminal: ::

    $ [sudo] cd tabela_fipe
    $ [sudo] python setup.py install

Using sxtools
--------

.. code-block:: python


    from tabela_fipe import TabelaFipe

    tab_fipe = TabelaFipe()

    info = tab_fipe.get_modelo(mod_codigofipe='006008-9')

    print('Marca: ' + info['mar_text'])
    print('Modelo: ' + info['mod_text'])
    print('Categoria: ' + info['mod_categoria'])
    print('Versoes: ')
    for ver in info['versoes']:
        print(
            '\t%s a %s custa %.2f reais ' % (
                ver['ano'],
                ver['combustivel'],
                ver['valor']
            )
        )


Development
--------

* Source hosted at `GitHub <https://github.com/sxslex/tabela_fipe>`_

Pull requests are very welcomed! Make sure your patches are well tested.

Running the tests
--------

All you need is: ::

    $ nosetests -dsv --with-yanc --with-coverage --cover-package tabela_fipe tests/*.py


