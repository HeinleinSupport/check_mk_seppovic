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
# <<<slapd_stats_operations:sep(44)>>>
# ldap-instance1,Delete,0,0
# ldap-instance1,Bind,82095,82095
# ldap-instance1,Add,0,0
# ldap-instance1,Abandon,0,0
# ldap-instance1,Extended,14978,14978
# ldap-instance1,Search,74380,74379
# ldap-instance1,Modify,0,0
# ldap-instance1,Unbind,16423,16423
# ldap-instance1,Modrdn,0,0
# ldap-instance1,Compare,0,0

from cmk.agent_based.v2 import (
    AgentSection,
    CheckPlugin,
    CheckResult,
    check_levels,
    DiscoveryResult,
    get_rate,
    get_value_store,
    Result,
    Service,
    State,
    StringTable,
)
import time

def parse_slapd_stats_operations(string_table: StringTable):
    section = {}
    for line in string_table:
        if len(line) == 4:
            instance, op, initiated, completed = line
            if not instance in section:
                section[instance] = {}
            section[instance][op] = (int(initiated), int(completed))
        elif len(line) == 2:
            instance, error = line
            if not instance in section:
                section[instance] = {}
            section[instance]["error"] = error
    return section

agent_section_slapd_stats_operations = AgentSection(
    name="slapd_stats_operations",
    parse_function=parse_slapd_stats_operations,
)

def discover_slapd_stats_operations(section) -> DiscoveryResult:
    for instance in section:
        yield Service(item=instance)

def check_slapd_stats_operations(item, params, section) -> CheckResult:
    now = time.time()
    vs = get_value_store()
    deviance = 0

    if item in section:
        if "error" in section[item]:
            yield Result(
                state=State.CRIT,
                summary=section[item]["error"],
            )
        else:
            for op, (initiated, completed) in section[item].items():
                deviance = max(deviance, abs(initiated - completed))
                rate = get_rate(
                    vs,
                    "slapd.stats.operations.%s" % op,
                    now,
                    completed)
                yield from check_levels(
                    rate,
                    levels_upper=params.get(op),
                    metric_name="slapd_%s" % op.lower(),
                    label="%s rate" % op,
                    render_func=lambda x: "%.2f/s" % x,
                    notice_only=True,
                )
            yield from check_levels(
                deviance,
                levels_upper=params.get("deviance"),
                label="Max. deviance of initiated and completed operations",
            )

check_plugin_slapd_stats_operations = CheckPlugin(
    name="slapd_stats_operations",
    service_name="SLAPD %s Operations",
    sections=["slapd_stats_operations"],
    discovery_function=discover_slapd_stats_operations,
    check_function=check_slapd_stats_operations,
    check_default_parameters={
    },
    check_ruleset_name="slapd_stats_operations",
)
