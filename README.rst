barix-man-rest
==============

REST API for the management of Barix devices

*Caution:* This is no official project of Barix AG.

All mentioned trademarks belong to their respective owners and are used for reference only. Barix, Annuncicom, Barionet, Exstreamer, Instreamer, SonicIP and IPzator are trademarks of Barix AG, Switzerland, and are registered in certain countries.

Requirements
------------

* MySQL database installed and running.


Usage
-----

* Copy `buildout.cfg.template` to `buildout.cfg` and adapt it to your needs.
* Bootstrap the package using::

  $ python3.6 bootstrap.py
  $ bin/buildout

Run the tests
-------------

Call::

  $ bin/test
