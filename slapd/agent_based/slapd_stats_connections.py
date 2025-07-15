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
# <<<slapd_stats_connections:sep(44)>>>
# ldap-slave1,Total,8555
# ldap-slave1,Current,16


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

def parse_slapd_stats_connections(string_table):
    section = {}
    for instance, key, value in string_table:
        if not instance in section:
            section[instance] = {}
        section[instance][key] = int(value)
    return section

agent_section_slapd_stats_connections = AgentSection(
    name="slapd_stats_connections",
    parse_function=parse_slapd_stats_connections,
)

def discover_slapd_stats_connections(section):
    for instance in section:
        yield Service(item=instance)

def check_slapd_stats_connections(item, params, section):
    map_metric = {
        'Total': 'connections',
        'Current': 'active',
    }
    
    if item in section:
        now = time.time()
        vs = get_value_store()

        for op, value in section[item].items():
            if op == "Total":
                rate = get_rate(
                    vs,
                    "slapd.stats.connections.%s" % op,
                    now,
                    value)
                yield from check_levels(
                    rate,
                    levels_upper=params.get("connections_rate"),
                    metric_name="connections_rate",
                    label="Connection Rate",
                    render_func=lambda x: "%.2f/s" % x,
                )
            yield from check_levels(
                value,
                levels_upper=params.get(op),
                metric_name=map_metric[op],
                label="%s Connections" % op,
                render_func=lambda x: "%d" % x,
            )

check_plugin_slapd_stats_connections = CheckPlugin(
    name="slapd_stats_connections",
    service_name="SLAPD %s Connections",
    sections=["slapd_stats_connections"],
    discovery_function=discover_slapd_stats_connections,
    check_function=check_slapd_stats_connections,
    check_default_parameters={
    },
    check_ruleset_name="slapd_stats_connections",
)
