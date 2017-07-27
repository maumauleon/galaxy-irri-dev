# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500952924.595323
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/admin/center.mako'
_template_uri = '/webapps/galaxy/admin/center.mako'
_source_encoding = 'ascii'
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f818c17bf50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f818c17bf50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f818c17bf50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        tool_shed_repository_ids = _import_ns.get('tool_shed_repository_ids', context.get('tool_shed_repository_ids', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        is_repo_installed = _import_ns.get('is_repo_installed', context.get('is_repo_installed', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<h2>Administration</h2>\nPlease visit <a href="https://galaxyproject.org/admin" target="_blank">the Galaxy administration hub</a> to learn how to keep your Galaxy in best shape.\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        else:
            __M_writer(u'        <h4>Server</h4>\n            <ul>\n                <li>\n                    <strong>Data types registry</strong> - See all datatypes available in this Galaxy.\n                </li>\n                <li>\n                    <strong>Data tables registry</strong> - See all data tables available in this Galaxy.\n                </li>\n                <li>\n                    <strong>Display applications</strong> - See all display applications configured in this Galaxy.\n                </li>\n                <li>\n                    <strong>Manage jobs</strong> - Display all jobs that are currently not finished (i.e., their state is new, waiting, queued, or running).  Administrators are able to cleanly stop long-running jobs. \n                </li>\n            </ul>\n\n        <h4>Tools and Tool Shed</h4>\n            <ul>\n')
            if trans.app.tool_shed_registry and trans.app.tool_shed_registry.tool_sheds:
                __M_writer(u'                <li>\n                    <strong>Search Tool Shed</strong> - Search and install new tools and other Galaxy utilities from the Tool Shed. See <a href="https://galaxyproject.org/admin/tools/add-tool-from-toolshed-tutorial" target="_blank">the tutorial</a>.\n                </li>\n')
            if tool_shed_repository_ids:
                __M_writer(u'                <li>\n                    <strong>Monitor installing repositories</strong> - View the status of tools that are being currently installed.\n                </li>\n')
            if is_repo_installed:
                __M_writer(u'                <li>\n                    <strong>Manage installed tools</strong> - View and administer installed tools and utilities on this Galaxy.\n                </li>\n                <li>\n                    <strong>Reset metadata</strong> - Select on which repositories you want to reset metadata.\n                </li>\n')
            __M_writer(u"                <li>\n                    <strong>Download local tool</strong> - Download a tarball with a tool from this Galaxy.\n                </li>\n                <li>\n                    <strong>Reload a tool's configuration</strong> - Allows a new version of a tool to be loaded while the server is running.\n                </li>\n                <li>\n                    <strong>Tool lineage</strong> - A view of a version lineages for all installed tools. Useful for debugging.\n                </li>\n                <li>\n                    <strong>Review tool migration stages</strong> - See the list of migration stages that moved sets of tools from the distribution to the Tool Shed.\n                </li>\n            </ul>\n\n        <h4>User Management</h4>\n            <ul>\n                <li>\n                    <strong>Users</strong> - A view of all users and all groups and non-private roles associated with each user.  \n                </li>\n                <li>\n                    <strong>Groups</strong> - A view of all groups along with the members of the group and the roles associated with each group.\n                </li>\n                <li>\n                    <strong>Roles</strong> - A view of all non-private roles along with the role type, and the users and groups that are associated with the role.\n                    Also includes a view of the data library datasets that are associated with the role and the permissions applied to each dataset.\n                </li>\n                <li>\n                    <strong>API keys</strong> - A view of all generated API keys with an option to re-generate.\n                </li>\n")
            if trans.app.config.allow_user_impersonation:
                __M_writer(u'                <li>\n                    <strong>Impersonate a user</strong> - Allows to view Galaxy as another user in order to help troubleshoot issues.\n                </li>\n')
            __M_writer(u'            </ul>\n\n        <h4>Data</h4>\n            <ul>\n')
            if trans.app.config.enable_quotas:
                __M_writer(u'                <li>\n                    <strong>Quotas</strong> - Manage user space quotas. See <a href="https://galaxyproject.org/admin/disk-quotas" target="_blank">wiki</a> for details.\n                </li>\n')
            __M_writer(u'                <li>\n                    <strong>Data libraries</strong> - Data libraries enable authorized Galaxy users to share datasets with other groups or users. Only administrators can create data libraries. See <a href="https://galaxyproject.org/data-libraries" target="_blank">wiki</a> for details.\n                </li>\n                <li>\n                    <strong>Local data</strong> - Manage the reference (and other) data that is stored within Tool Data Tables. See <a href="https://galaxyproject.org/admin/tools/data-managers" target="_blank">wiki</a> for details.\n                </li>\n            </ul>\n        <h4>Form definitions</h4>\n            <ul>\n                <li>\n                    <strong>Form definitions</strong> - Manage local form definitions.\n                </li>\n            </ul>\n\n        <h4>Sample tracking</h4>\n            <ul>\n                <li>\n                    Please see the <a href="https://galaxyproject.org/archive/library-sample-tracking" target="_blank">sample tracking tutorial</a>.\n                </li>\n            </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f818c17bf50')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'Galaxy Administration')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "42": 1, "43": 2, "44": 4, "45": 8, "46": 9, "47": 9, "48": 9, "49": 10, "50": 11, "51": 29, "52": 30, "53": 34, "54": 35, "55": 39, "56": 40, "57": 47, "58": 76, "59": 77, "60": 81, "61": 85, "62": 86, "63": 90, "69": 4, "75": 4, "81": 75}, "uri": "/webapps/galaxy/admin/center.mako", "filename": "templates/webapps/galaxy/admin/center.mako"}
__M_END_METADATA
"""
