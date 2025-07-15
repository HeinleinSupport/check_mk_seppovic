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
# <<<slapd_stats_statistics:sep(44)>>>
# ldap-slave1,Entries,111386
# ldap-slave1,Referrals,0
# ldap-slave1,PDU,213505
# ldap-slave1,Bytes,17979195

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

def parse_slapd_stats_statistics(string_table):
    section = {}
    for instance, key, value in string_table:
        if not instance in section:
            section[instance] = {}
        section[instance][key] = int(value)
    return section

agent_section_slapd_stats_statistics = AgentSection(
    name="slapd_stats_statistics",
    parse_function=parse_slapd_stats_statistics,
)

def discover_slapd_stats_statistics(section):
    for instance in section:
        yield Service(item=instance)

def check_slapd_stats_statistics(item, params, section):
    map_metric = {
        'Entries': 'slapd_entries_sent',
        'Referrals': 'slapd_referrals_sent',
        'PDU': 'slapd_pdu_sent',
        'Bytes': 'net_data_sent',
    }

    if item in section:
        now = time.time()
        vs = get_value_store()

        for op, value in section[item].items():
            rate = get_rate(
                vs,
                "slapd.stats.statistics.%s" % op,
                now,
                value)
            yield from check_levels(
                rate,
                levels_upper=params.get(op),
                metric_name=map_metric[op],
                label="Rate of sent %s" %op,
                render_func=lambda x: "%.2f/s" % x,
            )
 
check_plugin_slapd_stats_statistics = CheckPlugin(
    name="slapd_stats_statistics",
    service_name="SLAPD %s statistics",
    sections=["slapd_stats_statistics"],
    discovery_function=discover_slapd_stats_statistics,
    check_function=check_slapd_stats_statistics,
    check_default_parameters={},
    check_ruleset_name="slapd_stats_statistics",
)
