#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.rulesets.v1 import (
    Help,
    Label,
    Title,
)
from cmk.rulesets.v1.form_specs import (
    BooleanChoice,
    DefaultValue,
    DictElement,
    Dictionary,
    Float,
    Integer,
    InputHint,
    LevelDirection,
    migrate_to_float_simple_levels,
    migrate_to_integer_simple_levels,
    SingleChoice,
    SingleChoiceElement,
    SimpleLevels,
)
from cmk.rulesets.v1.rule_specs import (
    AgentConfig,
    CheckParameters,
    DiscoveryParameters,
    HostAndItemCondition,
    Topic,
)

def _parameter_valuespec_slapd_instance():
    return Dictionary(
        elements = {
            "maxConnectionTime": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("Max. response time"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="seconds"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
        }
    )

rule_spec_slapd_instance = CheckParameters(
    name="slapd_instance",
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_instance,
    title=Title("slapd Instance"),
    condition=HostAndItemCondition(item_title=Title("Instance")),
)


def _parameter_valuespec_slapd_stats_connections():
    return Dictionary(
        elements = {
            "Current": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Current Connections"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="connections"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Total": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Total Connections"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="connections"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "rate": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Connection rate"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="per second"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
        }
    )

rule_spec_slapd_stats_connections = CheckParameters(
    name="slapd_stats_connections",
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_connections,
    title=Title("slapd Connections"),
    condition=HostAndItemCondition(item_title=Title("Instance")),
)


def _parameter_valuespec_slapd_stats_operations():
    return Dictionary(
        elements = {
            "Bind": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Bind"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Delete": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Delete"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Add": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Add"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Abandon": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Abandon"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Extended": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Extended"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Search": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Search"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Modify": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Modify"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Unbind": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Unbind"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Modrdn": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Modrdn"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Compare": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Compare"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops/s"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "deviance": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Max. Deviance"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(unit_symbol="ops"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
        }
    )

rule_spec_slapd_stats_operations = CheckParameters(
    name="slapd_stats_operations",
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_operations,
    title=Title("slapd Operations"),
    condition=HostAndItemCondition(item_title=Title("Instance")),
)

def _parameter_valuespec_slapd_stats_statistics():
    return Dictionary(
        elements = {
            "Entries": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("Entries rate"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="per second"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
            "Referarals": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("Referrals rate"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="per second"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
            "PDU": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("PDUs rate"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="per second"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
            "Bytes": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("Bytes rate"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="per second"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
        }
    )

rule_spec_slapd_stats_statistics = CheckParameters(
    name="slapd_stats_statistics",
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_statistics,
    title=Title("slapd Network Statistics"),
    condition=HostAndItemCondition(item_title=Title("Instance")),
)

def _parameter_valuespec_slapd_stats_waiters():
    return Dictionary(
        elements = {
            "Read": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Read Waiters"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
            "Write": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Write Waiters"),
                    migrate=migrate_to_integer_simple_levels,
                    form_spec_template=Integer(),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0, 0)),
                )),
        }
    )

rule_spec_slapd_stats_waiters = CheckParameters(
    name="slapd_stats_waiters",
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_stats_waiters,
    title=Title("slapd Waiters"),
    condition=HostAndItemCondition(item_title=Title("Instance")),
)

def _parameter_valuespec_slapd_syncrepl():
    return Dictionary(
        elements = {
            "levels": DictElement(
                required=True,
                parameter_form=SimpleLevels(
                    title=Title("deltatime between Consumer and Provider"),
                    migrate=migrate_to_float_simple_levels,
                    form_spec_template=Float(unit_symbol="seconds"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=InputHint((0.0, 0.0)),
                )),
        }
    )

rule_spec_slapd_syncrepl = CheckParameters(
    name="slapd_syncrepl",
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec_slapd_syncrepl,
    title=Title("slapd Syncrepl status"),
    condition=HostAndItemCondition(item_title=Title("Instance and Syncrepl partner")),
)
