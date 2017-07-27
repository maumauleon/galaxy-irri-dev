# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500952987.185399
_enable_loop = True
_template_filename = 'templates/admin/tool_shed_repository/initiate_repository_installation.mako'
_template_uri = 'admin/tool_shed_repository/initiate_repository_installation.mako'
_source_encoding = 'ascii'
_exports = ['repository_installation_javascripts', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f81840e7e90', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f81840e7e90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81840e7e90')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        tool_shed_repositories = _import_ns.get('tool_shed_repositories', context.get('tool_shed_repositories', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if tool_shed_repositories:
            __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Monitor installing tool shed repositories</div>\n        <div class="toolFormBody">\n            <table class="grid">\n                <tr>\n                    <td>Name</td>\n                    <td>Description</td>\n                    <td>Owner</td>\n                    <td>Revision</td>\n                    <td>Status</td>\n                </tr>\n')
            for tool_shed_repository in tool_shed_repositories:
                __M_writer(u'                    ')

                encoded_repository_id = trans.security.encode_id( tool_shed_repository.id )
                ids_of_tool_dependencies_missing_or_being_installed = [ trans.security.encode_id( td.id ) for td in tool_shed_repository.tool_dependencies_missing_or_being_installed ]
                link_to_manage_tool_dependencies = tool_shed_repository.status in [ trans.install_model.ToolShedRepository.installation_status.INSTALLING_TOOL_DEPENDENCIES ]
                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['td','ids_of_tool_dependencies_missing_or_being_installed','link_to_manage_tool_dependencies','encoded_repository_id'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                    <tr>\n                        <td>\n')
                if link_to_manage_tool_dependencies:
                    __M_writer(u'                                <a class="view-info" href="')
                    __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_tool_dependencies', tool_dependency_ids=ids_of_tool_dependencies_missing_or_being_installed )))
                    __M_writer(u'">\n                                    ')
                    __M_writer(filters.html_escape(unicode(tool_shed_repository.name)))
                    __M_writer(u'\n                                </a>\n')
                else:
                    __M_writer(u'                                <a class="view-info" href="')
                    __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=encoded_repository_id )))
                    __M_writer(u'">\n                                    ')
                    __M_writer(filters.html_escape(unicode(tool_shed_repository.name)))
                    __M_writer(u'\n                                </a>\n')
                __M_writer(u'                        </td>\n                        <td>')
                __M_writer(unicode(tool_shed_repository.description))
                __M_writer(u'</td>\n                        <td>')
                __M_writer(unicode(tool_shed_repository.owner))
                __M_writer(u'</td>\n                        <td>')
                __M_writer(unicode(tool_shed_repository.changeset_revision))
                __M_writer(u'</td>\n                        <td><div id="RepositoryStatus-')
                __M_writer(unicode(encoded_repository_id))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(tool_shed_repository.status)))
                __M_writer(u'</div></td>\n                    </tr>\n')
            __M_writer(u'            </table>\n            <br clear="left"/>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_repository_installation_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81840e7e90')._populate(_import_ns, [u'*'])
        reinstalling = _import_ns.get('reinstalling', context.get('reinstalling', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        initiate_repository_installation_ids = _import_ns.get('initiate_repository_installation_ids', context.get('initiate_repository_installation_ids', UNDEFINED))
        encoded_kwd = _import_ns.get('encoded_kwd', context.get('encoded_kwd', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        $(document).ready(function( ){\n            initiate_repository_installation( "')
        __M_writer(unicode(initiate_repository_installation_ids))
        __M_writer(u'", "')
        __M_writer(unicode(encoded_kwd))
        __M_writer(u'", "')
        __M_writer(unicode(reinstalling))
        __M_writer(u'" );\n        });\n        var initiate_repository_installation = function ( iri_ids, encoded_kwd, reinstalling ) {\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repositories' )))
        __M_writer(u'",\n                dataType: "html",\n                data: { operation: "install", tool_shed_repository_ids: iri_ids, encoded_kwd: encoded_kwd, reinstalling: reinstalling },\n                success : function ( data ) {\n                    console.log( "Initializing repository installation succeeded" );\n                },\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81840e7e90')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        repository_installation_status_updater = _import_ns.get('repository_installation_status_updater', context.get('repository_installation_status_updater', UNDEFINED))
        repository_installation_updater = _import_ns.get('repository_installation_updater', context.get('repository_installation_updater', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n   ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n   ')
        __M_writer(unicode(repository_installation_status_updater()))
        __M_writer(u'\n   ')
        __M_writer(unicode(repository_installation_updater()))
        __M_writer(u'\n   ')
        __M_writer(unicode(self.repository_installation_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"133": 127, "23": 2, "29": 0, "39": 1, "40": 2, "41": 9, "42": 29, "43": 31, "44": 32, "45": 43, "46": 44, "47": 44, "55": 48, "56": 51, "57": 52, "58": 52, "59": 52, "60": 53, "61": 53, "62": 55, "63": 56, "64": 56, "65": 56, "66": 57, "67": 57, "68": 60, "69": 61, "70": 61, "71": 62, "72": 62, "73": 63, "74": 63, "75": 64, "76": 64, "77": 64, "78": 64, "79": 67, "85": 11, "95": 11, "96": 14, "97": 14, "98": 14, "99": 14, "100": 14, "101": 14, "102": 20, "103": 20, "109": 4, "119": 4, "120": 5, "121": 5, "122": 6, "123": 6, "124": 7, "125": 7, "126": 8, "127": 8}, "uri": "admin/tool_shed_repository/initiate_repository_installation.mako", "filename": "templates/admin/tool_shed_repository/initiate_repository_installation.mako"}
__M_END_METADATA
"""
