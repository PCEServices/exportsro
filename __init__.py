# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExportSRO
                                 A QGIS plugin
 Permet d'exporter un SRO de la BDD
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-03
        copyright            : (C) 2023 by Romain Lagrange - PCE Services
        email                : romain.lagrange@pceservices.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ExportSRO class from file ExportSRO.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ExportSRO import ExportSRO
    return ExportSRO(iface)
