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
    AgentSection,
    CheckPlugin,
    CheckResult,
    check_levels,
    DiscoveryResult,
    Result,
    Service,
    State,
    StringTable,
)

def parse_slapd_stats_waiters(string_table: StringTable):
    section = {}
    for line in string_table:
        if len(line) == 3:
            instance, key, value = line
            if not instance in section:
                section[instance] = {}
            section[instance][key] = int(value)
        elif len(line) == 2:
            instance, error = line
            if not instance in section:
                section[instance] = {}
            section[instance]["error"] = error
    return section

agent_section_slapd_stats_waiters = AgentSection(
    name="slapd_stats_waiters",
    parse_function=parse_slapd_stats_waiters,
)

def discover_slapd_stats_waiters(section) -> DiscoveryResult:
    for instance in section:
        yield Service(item=instance)

def check_slapd_stats_waiters(item: str, params, section) -> CheckResult:
    if item in section:
        if "error" in section[item]:
            yield Result(
                state=State.CRIT,
                summary=section[item]["error"],
            )
        else:
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
