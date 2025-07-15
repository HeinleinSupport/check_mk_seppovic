#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Float,
    Integer,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    rulespec_registry,
    CheckParameterRulespecWithItem,
    RulespecGroupCheckParametersApplications,
)

def _item_spec_slapd():
    return TextAscii(
        title = _("Instance"),
        help = _("Only needed if multiple SLAPD Instances on one server available"),
    )


def _parameter_valuespec_slapd_instance():
    return Dictionary(
	help = _("test"),
        elements = [
            ( "maxConnectionTime",
              Tuple(
                  title = _("Max. response time"),
                  elements = [
                      Float(title = _("Warning: "), default_value = 0.0, unit = _("seconds") ),
                      Float(title = _("Critical: "), default_value = 0.0, unit = _("seconds") ),
                  ]
              )
            ),
        ]
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_instance",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_slapd,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_slapd_instance,
        title=lambda: _("slapd Instance"),
    ))


def _parameter_valuespec_slapd_stats_connections():
    return Dictionary(
        elements = [
            ( "Current",
              Tuple(
                  title = _("Current Connections"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Total",
              Tuple(
                  title = _("Total Connections"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "rate",
              Tuple(
                  title = _("Connection rate"),
                  elements = [
                      Float(title = _("Warning: "), default_value = 0.0 ),
                      Float(title = _("Critical: "), default_value = 0.0 ),
                  ]
              )
            ),
        ]
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_connections",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_slapd,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_slapd_stats_connections,
        title=lambda: _("slapd Connections"),
    ))


def _parameter_valuespec_slapd_stats_operations():
    return Dictionary(
        elements = [
            ( "Bind",
              Tuple(
                  title = _("Bind"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Delete",
              Tuple(
                  title = _("Delete"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Add",
              Tuple(
                  title = _("Add"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Abandon",
              Tuple(
                  title = _("Abandon"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Extended",
              Tuple(
                  title = _("Extended"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Search",
              Tuple(
                  title = _("Search"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Modify",
              Tuple(
                  title = _("Modify"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Unbind",
              Tuple(
                  title = _("Unbind"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Modrdn",
              Tuple(
                  title = _("Modrdn"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "Compare",
              Tuple(
                  title = _("Compare"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
            ( "deviance",
              Tuple(
                  title = _("Max. Deviance"),
                  elements = [
                      Integer(title = _("Warning: "), default_value = 0 ),
                      Integer(title = _("Critical: "), default_value = 0 ),
                  ]
              )
            ),
        ]
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_operations",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_slapd,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_slapd_stats_operations,
        title=lambda: _("slapd Operations"),
    ))


def _parameter_valuespec_slapd_stats_statistics():
    return Dictionary(
        elements = [
            ( "Entries",
                Tuple(
                    title = _("Entries rate"),
                    elements = [
                        Float(title = _("Warning: "), default_value = 0.0 ),
                        Float(title = _("Critical: "), default_value = 0.0 ),
                    ]
                )
            ),
            ( "Referarals",
                Tuple(
                    title = _("Referarals rate"),
                    elements = [
                        Float(title = _("Warning: "), default_value = 0.0 ),
                        Float(title = _("Critical: "), default_value = 0.0 ),
                    ]
                )
            ),
            ( "PDU",
                Tuple(
                    title = _("PDUs rate"),
                    elements = [
                        Float(title = _("Warning: "), default_value = 0.0 ),
                        Float(title = _("Critical: "), default_value = 0.0 ),
                    ]
                )
            ),
             ( "Bytes",
                Tuple(
                    title = _("Bytes rate"),
                    elements = [
                        Float(title = _("Warning: "), default_value = 0.0 ),
                        Float(title = _("Critical: "), default_value = 0.0 ),
                    ]
                )
            ),
       ]
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_statistics",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_slapd,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_slapd_stats_statistics,
        title=lambda: _("slapd Network Statistics"),
    ))


def _parameter_valuespec_slapd_stats_waiters():
    return Dictionary(
        elements = [
            ( "Read",
                Tuple(
                    title = _("Read Waiters"),
                    elements = [
                        Integer(title = _("Warning: "), default_value = 0 ),
                        Integer(title = _("Critical: "), default_value = 0 ),
                    ]
                )
            ),
             ( "Write",
                Tuple(
                    title = _("Write Waiters"),
                    elements = [
                        Integer(title = _("Warning: "), default_value = 0 ),
                        Integer(title = _("Critical: "), default_value = 0 ),
                    ]
                )
            ),
       ]
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_waiters",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_slapd,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_slapd_stats_waiters,
        title=lambda: _("slapd Waiters"),
    ))


def _parameter_valuespec_slapd_syncrepl():
    return Dictionary(
        elements = [
            ( "levels",
                Tuple(
                    title = _("deltatime between Consumer and Provider"),
                    elements = [
                        Float(title = _("Warning: "), default_value = 0.0, unit = _("seconds") ),
                        Float(title = _("Critical: "), default_value = 0.0, unit = _("seconds") ),
                    ]
                )
            ),
        ]
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_syncrepl",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_slapd,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_slapd_syncrepl,
        title=lambda: _("slapd Syncrepl status"),
    ))
