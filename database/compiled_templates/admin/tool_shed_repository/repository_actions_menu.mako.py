# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500964096.17007
_enable_loop = True
_template_filename = u'templates/admin/tool_shed_repository/repository_actions_menu.mako'
_template_uri = u'/admin/tool_shed_repository/repository_actions_menu.mako'
_source_encoding = 'ascii'
_exports = ['render_galaxy_repository_actions']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_galaxy_repository_actions(context,repository=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        workflow_name = context.get('workflow_name', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.encoding_util import tool_shed_encode
        in_error_state = repository.in_error_state
        tool_dependency_ids = [ trans.security.encode_id( td.id ) for td in repository.tool_dependencies ]
        if repository.status in [ trans.install_model.ToolShedRepository.installation_status.DEACTIVATED,
                                  trans.install_model.ToolShedRepository.installation_status.ERROR,
                                  trans.install_model.ToolShedRepository.installation_status.INSTALLED ]:
            can_administer = True
        else:
            can_administer = False
            
        
        __M_writer(u'\n    <br/><br/>\n    <ul class="manage-table-actions">\n        <li><a class="action-button" id="repository-')
        __M_writer(unicode(repository.id))
        __M_writer(u'-popup" class="menubutton">Repository Actions</a></li>\n        <div popupmenu="repository-')
        __M_writer(unicode(repository.id))
        __M_writer(u'-popup">\n')
        if workflow_name:
            __M_writer(u'                <li><a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='import_workflow', workflow_name=tool_shed_encode( workflow_name ), repository_id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Import workflow to Galaxy</a></li>\n')
        if repository.can_reinstall_or_activate:
            __M_writer(u'                <a class="action-button" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_repositories', operation='activate or reinstall', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Activate or reinstall repository</a>\n')
        if in_error_state:
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='reset_to_install', id=trans.security.encode_id( repository.id ), reset_repository=True )))
            __M_writer(u'">Reset to install</a>\n')
        elif repository.can_install:
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=trans.security.encode_id( repository.id ), operation='install' )))
            __M_writer(u'">Install</a>\n')
        elif can_administer:
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Manage repository</a>\n                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Browse repository files</a>\n                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='check_for_updates', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Get repository updates</a>\n')
            if repository.can_reset_metadata:
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='reset_repository_metadata', id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Reset repository metadata</a>\n')
            if repository.includes_tools:
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='set_tool_versions', id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Set tool versions</a>\n')
            if tool_dependency_ids:
                __M_writer(u'                    <a class="action-button" target="galaxy_main" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository_tool_dependencies', tool_dependency_ids=tool_dependency_ids, repository_id=trans.security.encode_id( repository.id ) )))
                __M_writer(u'">Manage tool dependencies</a>\n')
            __M_writer(u'                <a class="action-button" target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='deactivate_or_uninstall_repository', id=trans.security.encode_id( repository.id ) )))
            __M_writer(u'">Deactivate or uninstall repository</a>\n')
        __M_writer(u'            <a class="action-button" target="galaxy_main" href="')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='repair_repository', id=trans.security.encode_id( repository.id ) )))
        __M_writer(u'">Repair repository</a>\n        </div>\n    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "32": 1, "33": 47, "39": 3, "46": 3, "47": 4, "59": 14, "60": 17, "61": 17, "62": 18, "63": 18, "64": 19, "65": 20, "66": 20, "67": 20, "68": 22, "69": 23, "70": 23, "71": 23, "72": 25, "73": 26, "74": 26, "75": 26, "76": 27, "77": 28, "78": 28, "79": 28, "80": 29, "81": 30, "82": 30, "83": 30, "84": 31, "85": 31, "86": 32, "87": 32, "88": 33, "89": 34, "90": 34, "91": 34, "92": 36, "93": 37, "94": 37, "95": 37, "96": 39, "97": 40, "98": 40, "99": 40, "100": 42, "101": 42, "102": 42, "103": 44, "104": 44, "105": 44, "111": 105}, "uri": "/admin/tool_shed_repository/repository_actions_menu.mako", "filename": "templates/admin/tool_shed_repository/repository_actions_menu.mako"}
__M_END_METADATA
"""
