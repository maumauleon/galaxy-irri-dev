# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500952927.838967
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/admin/tool_sheds.mako'
_template_uri = '/webapps/galaxy/admin/tool_sheds.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f81885b7c10', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f81885b7c10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81885b7c10')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Accessible Galaxy tool sheds</div>\n    <div class="toolFormBody">\n        <div class="form-row">\n            <table class="grid">\n                ')
        shed_id = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shed_id'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        for name, url in trans.app.tool_shed_registry.tool_sheds.items():
            __M_writer(u'                    <tr class="libraryTitle">\n                        <td>\n                            <div style="float: left; margin-left: 1px;" class="menubutton split popup" id="dataset-')
            __M_writer(unicode(shed_id))
            __M_writer(u'-popup">\n                                <a class="view-info" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_shed', tool_shed_url=url )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(name)))
            __M_writer(u'</a>\n                            </div>\n                            <div popupmenu="dataset-')
            __M_writer(unicode(shed_id))
            __M_writer(u'-popup">\n                                <a class="action-button" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_shed', tool_shed_url=url )))
            __M_writer(u'">Browse valid repositories</a>\n                                <a class="action-button" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='find_tools_in_tool_shed', tool_shed_url=url )))
            __M_writer(u'">Search for valid tools</a>\n                                <a class="action-button" href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='find_workflows_in_tool_shed', tool_shed_url=url )))
            __M_writer(u'">Search for workflows</a>\n                            </div>\n                        </td>\n                    </tr>\n                    ')
            shed_id += 1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shed_id'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'                </tr>\n            </table>\n        </div>\n        <div style="clear: both"></div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81885b7c10')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css( "library" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81885b7c10')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'Configured Galaxy tool sheds')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "41": 1, "42": 2, "43": 4, "44": 9, "45": 11, "46": 12, "47": 12, "48": 12, "49": 14, "50": 20, "54": 20, "55": 21, "56": 22, "57": 24, "58": 24, "59": 25, "60": 25, "61": 25, "62": 25, "63": 27, "64": 27, "65": 28, "66": 28, "67": 29, "68": 29, "69": 30, "70": 30, "71": 34, "75": 34, "76": 36, "82": 6, "90": 6, "91": 7, "92": 7, "93": 8, "94": 8, "100": 4, "106": 4, "112": 106}, "uri": "/webapps/galaxy/admin/tool_sheds.mako", "filename": "templates/webapps/galaxy/admin/tool_sheds.mako"}
__M_END_METADATA
"""
