#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

try:
    from cmk.gui.plugins.wato import (
        HostRulespec,
        rulespec_registry,
        IndividualOrStoredPassword,
    )

    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import RulespecGroupMonitoringAgentsAgentPlugins

    from cmk.gui.valuespec import (
        Dictionary,
        Hostname,
        Integer,
        LDAPDistinguishedName,
        ListOf,
        Password,
        TextAscii,
        Tuple,
        Url,
    )

    def _valuespec_agent_config_slapd():
        return ListOf(
            Tuple(elements=[
                Hostname(
                    title=_("Instance name"),
                ),
                Dictionary(elements=[
                    ('uri', Url(title=_("LDAP URI"), default_scheme="ldap+tls", allowed_schemes=["ldap+tls", "ldaps", "ldap", "ldapi"], default_value="ldap+tls://localhost:389/")),
                    ('server', Hostname(title=_("Hostname"), help=_("taken from LDAP URI if not specified"))),
                    ('binddn', LDAPDistinguishedName(title=_("Bind DN"))),
                    ('bindpw', Password(title=_("Bind Password"))),
                    ('version', Integer(title=_("LDAP Version"), default_value=3, minvalue=2, maxvalue=3)),
                    ("suffix", LDAPDistinguishedName(title=_("LDAP Suffix"), help=_("is taken from LDAP Monitoring DB; you can override it here if it is not reliable determined or if you want to save the time of one ldap query"))),
                    ("syncrepl", ListOf(Dictionary(elements=[
                        ('serverid', TextAscii(title=_("Server ID"), help=_("you need to specify your local serverid here if you are in a Multi-Master environment"), default_value="000")),
                        ('uri', Url(title=_("LDAP URI"), default_scheme="ldap+tls", allowed_schemes=["ldap+tls", "ldaps", "ldap", "ldapi"], help=_("also taken from LDAP Monitoring DB; you can override it here if it is not reliable determined or if you want to save the time of one ldap query"))),
                        ('server', Hostname(title=_("Hostname"), help=_("taken from LDAP URI if not specified; default value from Monitoring DB"))),
                        ('binddn', LDAPDistinguishedName(title=_("Bind DN"))),
                        ('bindpw', Password(title=_("Bind Password"))),
                        ('version', Integer(title=_("LDAP Version"), default_value=3, minvalue=2, maxvalue=3)),
                        ("suffix", LDAPDistinguishedName(title=_("LDAP Suffix"), help=_("if not specified suffix entry is taken from LDAP of the master server; you can override it here if it is not reliable determined or if you want to save the time of one ldap query"))),
                        ],
                        optional_keys=["uri", "server", "version", "suffix"],
                        ),
                        title=_("Syncrepl Tests"),
                        add_label=_("Add syncrepl config"),
                        )),
                    ],
                    title=_("Instance config"),
                    optional_keys=["server", "version", "suffix", "syncrepl"],
                ),
            ]),
            add_label=_("Add slapd Instance"),
            title=_("slapd (Linux)"),
            help=_("This will deploy the agent plugin <tt>slapd.pl</tt> and create a configuration in <tt>/etc/check_mk/slapd.cfg</tt> for it."),
        )

    rulespec_registry.register(
        HostRulespec(
            group=RulespecGroupMonitoringAgentsAgentPlugins,
            name="agent_config:slapd",
            valuespec=_valuespec_agent_config_slapd,
        ))

except ModuleNotFoundError:
    # RAW edition
    pass
