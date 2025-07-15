#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# 2021 Heinlein Consulting GmbH
#      Robert Sander <r.sander@heinlein-support.de>

#################################################################
#---------------------------------------------------------------#
# Author: Markus Weber                                          #
# Contact: markus.weber@lfst.bayern.de                          #
# License: GPL                                                  #
# File: slapd_stats                                             #
# Version: 1.0                                                  #
# Revision: 30.10.2015                                          #
# Description: Monitor openldap via Monitoring DB.              #
#                                                               #
#################################################################


# Example Output:
# <<<slapd_stats_waiters:sep(44)>>>
# ldap-master02,Write,0
# ldap-master02,Read,2

from cmk.agent_based.v2 import (
    check_levels_fixed as check_levels,
    get_rate,
    get_value_store,
    register,
    render,
    Result,
    Metric,
    State,
    ServiceLabel,
    Service,
)
import time

from cmk.agent_based.v2 import AgentSection, SNMPSection, SimpleSNMPSection, CheckPlugin, InventoryPlugin

def parse_slapd_stats_waiters(string_table):
    section = {}
    for instance, key, value in string_table:
        if not instance in section:
            section[instance] = {}
        section[instance][key] = int(value)
    return section

agent_section_slapd_stats_waiters = AgentSection(
    name="slapd_stats_waiters",
    parse_function=parse_slapd_stats_waiters,
)

def discover_slapd_stats_waiters(section):
    for instance in section:
        yield Service(item=instance)

def check_slapd_stats_waiters(item, params, section):
    if item in section:
        for op, value in section[item].items():
            yield from check_levels(
                value,
                levels_upper=params.get(op),
                metric_name="slapd_waiters_%s" % op.lower(),
                label="%s Waiters" % op,
                render_func=lambda x: "%d" % x,
            )

check_plugin_slapd_stats_waiters = CheckPlugin(
    name="slapd_stats_waiters",
    service_name="SLAPD %s Waiters",
    sections=["slapd_stats_waiters"],
    discovery_function=discover_slapd_stats_waiters,
    check_function=check_slapd_stats_waiters,
    check_default_parameters={},
    check_ruleset_name="slapd_stats_waiters",
)
