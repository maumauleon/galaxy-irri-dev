# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501214133.125163
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/admin/index.mako'
_template_uri = '/webapps/galaxy/admin/index.mako'
_source_encoding = 'ascii'
_exports = ['left_panel', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f3534044c10', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3534044c10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        installing_repository_ids = _import_ns.get('installing_repository_ids', context.get('installing_repository_ids', UNDEFINED))
        is_repo_installed = _import_ns.get('is_repo_installed', context.get('is_repo_installed', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>Administration</div>\n    </div>\n    <div class="unified-panel-body">\n        <div class="toolMenu">\n            <div class="toolSectionList">\n                <div class="toolSectionTitle">Server</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='view_datatypes_registry' )))
        __M_writer(u'" target="galaxy_main">Data types registry</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='view_tool_data_tables' )))
        __M_writer(u'" target="galaxy_main">Data tables registry</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='display_applications' )))
        __M_writer(u'" target="galaxy_main">Display applications</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='jobs' )))
        __M_writer(u'" target="galaxy_main">Manage jobs</a></div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Tools and Tool Shed</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n')
        if trans.app.tool_shed_registry and trans.app.tool_shed_registry.tool_sheds:
            __M_writer(u'                        <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_sheds' )))
            __M_writer(u'" target="galaxy_main">Search Tool Shed</a></div>\n')
            if trans.app.config.enable_beta_ts_api_install:
                __M_writer(u'                            <div class="toolTitle"><a href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_toolsheds' )))
                __M_writer(u'" target="galaxy_main">Search Tool Shed (Beta)</a></div>\n')
        if installing_repository_ids:
            __M_writer(u'                        <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='monitor_repository_installation', tool_shed_repository_ids=installing_repository_ids )))
            __M_writer(u'" target="galaxy_main">Monitor installing repositories</a></div>\n')
        if is_repo_installed:
            __M_writer(u'                        <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_repositories' )))
            __M_writer(u'" target="galaxy_main">Manage installed tools</a></div>\n                        <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='reset_metadata_on_selected_installed_repositories' )))
            __M_writer(u'" target="galaxy_main">Reset metadata</a></div>\n')
        __M_writer(u'                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='package_tool' )))
        __M_writer(u'" target="galaxy_main">Download local tool</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='tool_versions' )))
        __M_writer(u'" target="galaxy_main">Tool lineage</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='reload_tool' )))
        __M_writer(u'" target="galaxy_main">Reload a tool\'s configuration</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='review_tool_migration_stages' )))
        __M_writer(u'" target="galaxy_main">Review tool migration stages</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='tool_errors' )))
        __M_writer(u'" target="galaxy_main">View Tool Error Logs</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='sanitize_whitelist' )))
        __M_writer(u'" target="galaxy_main">Manage Display Whitelist</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='manage_tool_dependencies' )))
        __M_writer(u'" target="galaxy_main">Manage Tool Dependencies</a></div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">User Management</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='users' )))
        __M_writer(u'" target="galaxy_main">Users</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='groups' )))
        __M_writer(u'" target="galaxy_main">Groups</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='admin', action='roles' )))
        __M_writer(u'" target="galaxy_main">Roles</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='userskeys', action='all_users' )))
        __M_writer(u'" target="galaxy_main">API keys</a></div>\n')
        if trans.app.config.allow_user_impersonation:
            __M_writer(u'                            <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin', action='impersonate' )))
            __M_writer(u'" target="galaxy_main">Impersonate a user</a></div>\n')
        __M_writer(u'                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Data</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n')
        if trans.app.config.enable_quotas:
            __M_writer(u'                            <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin', action='quotas' )))
            __M_writer(u'" target="galaxy_main">Quotas</a></div>\n')
        __M_writer(u'                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='library_admin', action='browse_libraries' )))
        __M_writer(u'" target="galaxy_main">Data libraries</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='data_manager' )))
        __M_writer(u'" target="galaxy_main">Local data</a></div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Form Definitions</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='forms', action='browse_form_definitions' )))
        __M_writer(u'" target="galaxy_main">Form definitions</a></div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Sample Tracking</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='external_service', action='browse_external_services' )))
        __M_writer(u'" target="galaxy_main">Sequencers and external services</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='request_type', action='browse_request_types' )))
        __M_writer(u'" target="galaxy_main">Request types</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='requests_admin', action='browse_requests' )))
        __M_writer(u'" target="galaxy_main">Sequencing requests</a></div>\n                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='requests_common', action='find_samples', cntrller='requests_admin' )))
        __M_writer(u'" target="galaxy_main">Find samples</a></div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'Galaxy Administration')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        center_url = h.url_for( controller='admin', action='center', message=message, status=status ) 
        
        __M_writer(u'\n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        __M_writer(unicode(center_url))
        __M_writer(u'"> </iframe>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging" )))
        __M_writer(u'\n\n')
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n        body { margin: 0; padding: 0; overflow: hidden; }\n        #left {\n            background: #C1C9E5 url(')
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n        }\n\n        .unified-panel-body {\n            overflow: auto;\n        }\n        .toolMenu {\n            margin: 8px 0 0 10px;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        self.has_left_panel=True
        self.has_right_panel=False
        self.active_view="admin"
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534044c10')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "36": 1, "37": 2, "38": 5, "39": 28, "40": 32, "41": 40, "42": 128, "43": 133, "49": 42, "59": 42, "60": 52, "61": 52, "62": 53, "63": 53, "64": 54, "65": 54, "66": 55, "67": 55, "68": 62, "69": 63, "70": 63, "71": 63, "72": 64, "73": 65, "74": 65, "75": 65, "76": 68, "77": 69, "78": 69, "79": 69, "80": 71, "81": 72, "82": 72, "83": 72, "84": 73, "85": 73, "86": 75, "87": 75, "88": 75, "89": 76, "90": 76, "91": 77, "92": 77, "93": 78, "94": 78, "95": 79, "96": 79, "97": 80, "98": 80, "99": 81, "100": 81, "101": 88, "102": 88, "103": 89, "104": 89, "105": 90, "106": 90, "107": 91, "108": 91, "109": 92, "110": 93, "111": 93, "112": 93, "113": 95, "114": 101, "115": 102, "116": 102, "117": 102, "118": 104, "119": 104, "120": 104, "121": 105, "122": 105, "123": 112, "124": 112, "125": 119, "126": 119, "127": 120, "128": 120, "129": 121, "130": 121, "131": 122, "132": 122, "138": 5, "144": 5, "150": 130, "159": 130, "160": 131, "162": 131, "163": 132, "164": 132, "170": 7, "178": 7, "179": 8, "180": 8, "181": 10, "182": 10, "183": 10, "184": 13, "185": 13, "186": 13, "187": 18, "188": 18, "194": 34, "201": 34, "202": 35, "208": 39, "214": 30, "221": 30, "222": 31, "223": 31, "229": 223}, "uri": "/webapps/galaxy/admin/index.mako", "filename": "templates/webapps/galaxy/admin/index.mako"}
__M_END_METADATA
"""
