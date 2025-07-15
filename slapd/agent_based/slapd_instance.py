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
# Version: 1.1                                                  #
# Revision: 08.03.2016                                          #
# Description: Monitor openldap via Monitoring DB.              #
#                                                               #
#################################################################


# Example Output:
# <<<slapd_instance:sep(124)>>>
# ldap-slave1|0.0000
# <<<slapd_instance:sep(124)>>>
# ldap-slave2|ERROR - could not bind as cn=Monitor : Invalid credentials at ./slapd.pl line 344
#  at ./slapd.pl line 344

from cmk.agent_based.v2 import (
    AgentSection,
    CheckPlugin,
    CheckResult,
    check_levels,
    DiscoveryResult,
    render,
    Result,
    State,
    Service,
    StringTable,
)

def parse_slapd_instance(string_table: StringTable):
    section = {}
    for instance, conn_time in string_table:
        section[instance] = conn_time
    return section

agent_section_slapd_instance = AgentSection(
    name="slapd_instance",
    parse_function=parse_slapd_instance,
)

def discover_slapd_instance(section) -> DiscoveryResult:
    for instance in section:
        yield Service(item=instance)

def check_slapd_instance(item: str, params, section) -> CheckResult:
    if item in section:
        value = section[item]
        if value.startswith("ERROR"):
            yield Result(state=State.CRIT,
                         summary=value)
        else:
            yield from check_levels(
                float(value),
                levels_upper=params.get('maxConnectionTime'),
                metric_name="connection_time",
                label="Time to connect",
                render_func=render.timespan,
            )

check_plugin_slapd_instance = CheckPlugin(
    name="slapd_instance",
    service_name="SLAPD %s",
    sections=["slapd_instance"],
    discovery_function=discover_slapd_instance,
    check_function=check_slapd_instance,
    check_default_parameters={
        'maxConnectionTime': ("fixed", (0.5, 0.8)),
    },
    check_ruleset_name="slapd_instance",
)
