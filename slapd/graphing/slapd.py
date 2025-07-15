#!/usr/bin/env python3

#
# (c) 2021 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.


from cmk.graphing.v1 import Title, metrics

UNIT_COUNTER = metrics.Unit(metrics.DecimalNotation(''), metrics.StrictPrecision(2))
UNIT_PER_SECOND = metrics.Unit(metrics.DecimalNotation('/s'))

metric_slapd_abandon = metrics.Metric(
    name='slapd_abandon',
    title=Title("Abandon Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.DARK_PINK,
)
metric_slapd_add = metrics.Metric(
    name='slapd_add',
    title=Title("Add Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.ORANGE,
)
metric_slapd_bind = metrics.Metric(
    name='slapd_bind',
    title=Title("Bind Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.ORANGE,
)
metric_slapd_compare = metrics.Metric(
    name='slapd_compare',
    title=Title("Compare Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.YELLOW,
)
metric_slapd_delete = metrics.Metric(
    name='slapd_delete',
    title=Title("Delete Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.YELLOW,
)
metric_slapd_entries_sent = metrics.Metric(
    name='slapd_entries_sent',
    title=Title("Entries sent"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.YELLOW,
)
metric_slapd_extended = metrics.Metric(
    name='slapd_extended',
    title=Title("Extended Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.GREEN,
)
metric_slapd_modify = metrics.Metric(
    name='slapd_modify',
    title=Title("Modify Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.CYAN,
)
metric_slapd_modrdn = metrics.Metric(
    name='slapd_modrdn',
    title=Title("ModRDN Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.CYAN,
)
metric_slapd_pdu_sent = metrics.Metric(
    name='slapd_pdu_sent',
    title=Title("PDUs sent"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.CYAN,
)
metric_slapd_referrals_sent = metrics.Metric(
    name='slapd_referrals_sent',
    title=Title("Referrals sent"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.DARK_BLUE,
)
metric_slapd_search = metrics.Metric(
    name='slapd_search',
    title=Title("Search Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.BLUE,
)
metric_slapd_unbind = metrics.Metric(
    name='slapd_unbind',
    title=Title("Unbind Ops completed"),
    unit=UNIT_PER_SECOND,
    color=metrics.Color.DARK_BLUE,
)
metric_slapd_waiters_read = metrics.Metric(
    name='slapd_waiters_read',
    title=Title("Read Waiters"),
    unit=UNIT_COUNTER,
    color=metrics.Color.YELLOW,
)
metric_slapd_waiters_write = metrics.Metric(
    name='slapd_waiters_write',
    title=Title("Write Waiters"),
    unit=UNIT_COUNTER,
    color=metrics.Color.BLUE,
)
