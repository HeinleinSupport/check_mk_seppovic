#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# 2021 Heinlein Consulting GmbH
#      Robert Sander <r.sander@heinlein-support.de>

#################################################################
#---------------------------------------------------------------#
# Author: Markus Weber                                          #
# Contact: markus.weber@lfst.bayern.de                          #
# License: GPL                                                  #
# File: slapd_syncrepl                                          #
# Version: 1.1                                                  #
# Revision: 08.03.2016                                          #
# Description: Monitor openldap via Monitoring DB.              #
#                                                               #
#################################################################


# Example Output:
# <<<slapd_syncrepl:sep(44)>>>
# ldap-master02,ldap-master01,0.00
# ldap-master02,ldap-master03,0.00

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

def parse_slapd_syncrepl(string_table: StringTable):
    section = {}
    for line in string_table:
        if len(line) == 3:
            instance, master, value = line
            if not instance in section:
                section[instance] = {}
            section[instance][master] = value
        elif len(line) == 2:
            instance, error = line
            if not instance in section:
                section[instance] = {}
            section[instance]["error"] = error
    return section

agent_section_slapd_syncrepl = AgentSection(
    name="slapd_syncrepl",
    parse_function=parse_slapd_syncrepl,
)

def discover_slapd_syncrepl(section) -> DiscoveryResult:
    for instance in section:
        for master in section[instance]:
            yield Service(item="%s %s" % (instance, master))

def check_slapd_syncrepl(item: str, params, section) -> CheckResult:
    instance, master = item.split(" ")
    if instance in section:
        if "error" in section[instance]:
            yield Result(
                state=State.CRIT,
                summary=section[instance]["error"],
            )
        else:
            if master in section[instance]:
                value = section[instance][master]
                if value.startswith("ERROR"):
                    yield Result(state=State.CRIT,
                                summary=value)
                else:
                    yield from check_levels(
                        float(value),
                        levels_upper=params.get("levels"),
                        label="Difference with Provider %s" % master,
                        metric_name="time_difference",
                        render_func=render.timespan,
                    )

check_plugin_slapd_syncrepl = CheckPlugin(
    name="slapd_syncrepl",
    service_name="SLAPD %s syncrepl status",
    sections=["slapd_syncrepl"],
    discovery_function=discover_slapd_syncrepl,
    check_function=check_slapd_syncrepl,
    check_default_parameters={},
    check_ruleset_name="slapd_syncrepl",
)
