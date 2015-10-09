======
TabelaFipe
======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/sxslex/TabelaFipe
   :target: https://gitter.im/sxslex/TabelaFipe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://travis-ci.org/sxslex/TabelaFipe.svg?branch=master
    :target: https://travis-ci.org/sxslex/TabelaFipe

Simple access library of data from the "Table Fipe".

Vehicle information: Manufacturer, Model, Vehicle, versions and prices.

Installing
--------

For install sxtools, run on terminal: ::

    $ [sudo] cd TabelaFipe
    $ [sudo] python setup.py install

Using sxtools
--------

.. code-block:: python


    from TabelaFipe import TabelaFipe

    tab_fipe = TabelaFipe()

    info = tab_fipe.get_by_codefipe('006008-9')

    print('Marca: ' + info['marca'])
    print('Modelo: ' + info['modelo'])
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

* Source hosted at `GitHub <https://github.com/sxslex/TabelaFipe>`_

Pull requests are very welcomed! Make sure your patches are well tested.

Running the tests
--------

All you need is: ::

    $ source alias.sh
    $ nt TabelaFipe tests/*.py


