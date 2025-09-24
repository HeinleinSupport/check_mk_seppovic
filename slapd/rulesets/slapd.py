#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.rulesets.v1 import (
    Help,
    Title,
)
from cmk.rulesets.v1.form_specs import (
    DictElement,
    Dictionary,
    Float,
    Integer,
    InputHint,
    LevelDirection,
    SimpleLevels,
    String,
    migrate_to_float_simple_levels,
    migrate_to_integer_simple_levels,
)
from cmk.rulesets.v1.rule_specs import (
    Topic,
    HostAndItemCondition,
    CheckParameters,
)

_item_spec_slapd=HostAndItemCondition(
    item_title=Title("Instance"),
    item_form=String(),
)

def _parameter_valuespec_slapd_instance():
    return Dictionary(
        elements={
            "maxConnectionTime": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("Max. response time"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="seconds"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint(value=(0.0, 0.0)),
                ))})

rule_spec_slapd_instance = CheckParameters(
    name="slapd_instance",
    title=Title("slapd Instance"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_instance,
    condition=_item_spec_slapd,
)


def _parameter_valuespec_slapd_stats_connections():
    return Dictionary(
        elements={
            "Current": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Current Connections"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="connections"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint(value=(0, 0)),
                )),
            "Total": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Total Connections"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="connections"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint(value=(0, 0)),
                )),
            "rate": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Connection rate"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="per second"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint(value=(0.0, 0.0)),
                )),
        }
    )

rule_spec_slapd_stats_connections = CheckParameters(
    name="slapd_stats_connections",
    title=Title("slapd Connections"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_connections,
    condition=_item_spec_slapd,
)


def _parameter_valuespec_slapd_stats_operations():
    elements = {
        "deviance": DictElement(
            parameter_form=SimpleLevels(
                title=Title("Max. Deviance"),
                migrate=migrate_to_integer_simple_levels,
                form_spec_template=Integer(unit_symbol="ops"),
                level_direction=LevelDirection.UPPER,
                prefill_fixed_levels=InputHint((0, 0)),
            ))
    }
    for parameter in ["Bind", "Delete", "Add", "Abandon", "Extended", "Search", "Modify", "Unbind", "Modrdn", "Compare"]:
        elements[parameter] = DictElement(
            required=False,
            parameter_form=SimpleLevels(
                title=Title(parameter),
                migrate=migrate_to_integer_simple_levels,
                level_direction=LevelDirection.UPPER,
                form_spec_template=Integer(unit_symbol="ops/s"),
                prefill_fixed_levels=InputHint(value=(0, 0)),
            ))
    return Dictionary(
        elements=elements,
    )

rule_spec_slapd_stats_operations = CheckParameters(
    name="slapd_stats_operations",
    title=Title("slapd Operations"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_operations,
    condition=_item_spec_slapd,
)


def _parameter_valuespec_slapd_stats_statistics():
    elements = {}
    for parameter in ["Entries", "Referrals", "PDU", "Bytes"]:
        elements[parameter] = DictElement(
            parameter_form=SimpleLevels(
                title=Title(f"{parameter} rate"),
                migrate=migrate_to_float_simple_levels,
                level_direction=LevelDirection.UPPER,
                form_spec_template=Float(unit_symbol="per second"),
                prefill_fixed_levels=InputHint(value=(0.0, 0.0)),
            ))
    return Dictionary(
        elements=elements,
    )

rule_spec_slapd_stats_statistics = CheckParameters(
    name="slapd_stats_statistics",
    title=Title("slapd Network Statistics"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_statistics,
    condition=_item_spec_slapd,
)


def _parameter_valuespec_slapd_stats_waiters():
    elements = {}
    for parameter in ["Read", "Write"]:
        elements[parameter] = DictElement(
            parameter_form=SimpleLevels(
                title=Title(f"{parameter} Waiters"),
                migrate=migrate_to_integer_simple_levels,
                level_direction=LevelDirection.UPPER,
                form_spec_template=Integer(),
                prefill_fixed_levels=InputHint(value=(0, 0)),
            ))
    return Dictionary(
        elements=elements,
    )

rule_spec_slapd_stats_waiters = CheckParameters(
    name="slapd_stats_waiters",
    title=Title("slapd Waiters"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_waiters,
    condition=_item_spec_slapd,
)


def _parameter_valuespec_slapd_syncrepl():
    return Dictionary(
        elements={
            "levels": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("deltatime between Consumer and Provider"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="seconds"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint(value=(0.0, 0.0)),
                ))
        }
    )

rule_spec_slapd_syncrepl = CheckParameters(
    name="slapd_syncrepl",
    title=Title("slapd Syncrepl status"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_syncrepl,
    condition=_item_spec_slapd,
)
