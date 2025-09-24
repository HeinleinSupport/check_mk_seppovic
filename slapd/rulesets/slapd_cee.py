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
    Integer,
    InputHint,
    List,
    migrate_to_integer_simple_levels,
    migrate_to_password,
    Password,
    String,
    validators,
)
from cmk.rulesets.v1.rule_specs import (
    AgentConfig,
    Topic,
)

def _migrate_from_list_to_dict(param):
    if isinstance(param, list):
        newparam = {"deploy": True}
        newparam["instances"] = []
        for instance, config in param:
            newparam["instances"].append({
                "instance": instance,
                "config": config,
            })
    elif isinstance(param, dict):
        newparam = param
    else:
        newparam = {"deploy": False}
    return newparam

def _migrate_password(model):
    if isinstance(model, str):
        model = ("password", model)
    model = migrate_to_password(model)
    return model

def _valuespec_agent_config_slapd():
    return Dictionary(
        migrate=_migrate_from_list_to_dict,
        elements={
            "deploy": DictElement(
                required=True,
                parameter_form=BooleanChoice(
                    label=Label("Deploy plugin for slapd"),
                    prefill=DefaultValue(True),
                )),
            "instances": DictElement(
                parameter_form=List(
                    title=Title("LDAP server instances to query"),
                    add_element_label=Label("Add new instance"),
                    element_template=Dictionary(
                        elements={
                            "instance": DictElement(
                                required=True,
                                parameter_form=String(
                                    title=Title("Instance name"),
                                )),
                            "config": DictElement(
                                required=True,
                                parameter_form=Dictionary(
                                    title=Title("Instance configuration"),
                                    elements={
                                        "uri": DictElement(
                                            required=True,
                                            parameter_form=String(
                                                title=Title("LDAP URI"),
                                                custom_validate=[validators.Url(["ldap+tls", "ldaps", "ldap", "ldapi"])],
                                            )),
                                        "server": DictElement(
                                            parameter_form=String(
                                                title=Title("Hostname"),
                                                custom_validate=[validators.HostAddress()],
                                            )),
                                        "binddn": DictElement(
                                            required=True,
                                            parameter_form=String(
                                                title=Title("Bind DN"),
                                            )),
                                        "bindpw": DictElement(
                                            required=True,
                                            parameter_form=Password(
                                                title=Title("Bind Password"),
                                                migrate=_migrate_password,
                                            )),
                                        "version": DictElement(
                                            parameter_form=Integer(
                                                title=Title("LDAP version"),
                                                prefill=DefaultValue(3),
                                                custom_validate=[validators.NumberInRange(min_value=2, max_value=3)],
                                            )),
                                        "suffix": DictElement(
                                            parameter_form=String(
                                                title=Title("LDAP Suffix"),
                                                help_text=Help("is taken from LDAP Monitoring DB; you can override it here if it is not reliable determined or if you want to save the time of one ldap query"),
                                            )),
                                        "syncrepl": DictElement(
                                            parameter_form=List(
                                                title=Title("Syncrepl Tests"),
                                                add_element_label=Label("Add syncrepl config"),
                                                element_template=Dictionary(
                                                    elements={
                                                        "serverid": DictElement(
                                                            required=True,
                                                            parameter_form=String(
                                                                title=Title("Server ID"),
                                                                help_text=Help("you need to specify your local serverid here if you are in a Multi-Master environment"),
                                                                prefill=InputHint("000"),
                                                            )),
                                                        "uri": DictElement(
                                                            parameter_form=String(
                                                                title=Title("LDAP URI"),
                                                                help_text=Help("also taken from LDAP Monitoring DB; you can override it here if it is not reliable determined or if you want to save the time of one ldap query"),
                                                                custom_validate=[validators.Url(["ldap+tls", "ldaps", "ldap", "ldapi"])],
                                                            )),
                                                        "server": DictElement(
                                                            parameter_form=String(
                                                                title=Title("Hostname"),
                                                                custom_validate=[validators.HostAddress()],
                                                            )),
                                                        "binddn": DictElement(
                                                            required=True,
                                                            parameter_form=String(
                                                                title=Title("Bind DN"),
                                                            )),
                                                        "bindpw": DictElement(
                                                            required=True,
                                                            parameter_form=Password(
                                                                title=Title("Bind Password"),
                                                                migrate=_migrate_password,
                                                            )),
                                                        "version": DictElement(
                                                            parameter_form=Integer(
                                                                title=Title("LDAP version"),
                                                                prefill=DefaultValue(3),
                                                                custom_validate=[validators.NumberInRange(min_value=2, max_value=3)],
                                                            )),
                                                        "suffix": DictElement(
                                                            parameter_form=String(
                                                                title=Title("LDAP Suffix"),
                                                                help_text=Help("is taken from LDAP Monitoring DB; you can override it here if it is not reliable determined or if you want to save the time of one ldap query"),
                                                            )),
                                                    },
                                                ),
                                            )),
                                    },
                                )),
                        },
                    ),
                )),
        },
    )

rule_spec_slapd_bakery = AgentConfig(
    name="slapd",
    title=Title("slapd (Linux)"),
    help_text=Help("This will deploy the agent plugin <tt>slapd.pl</tt> and create a configuration in <tt>/etc/check_mk/slapd.cfg</tt> for it."),
    topic=Topic.APPLICATIONS,
    parameter_form=_valuespec_agent_config_slapd,
)
