# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501214439.814476
_enable_loop = True
_template_filename = 'templates/admin/tool_shed_repository/repository_installation_grid.mako'
_template_uri = 'admin/tool_shed_repository/repository_installation_grid.mako'
_source_encoding = 'ascii'
_exports = ['javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f354019c090', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f354019c090')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/grid_base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f354019c090')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f354019c090')._populate(_import_ns, [u'*'])
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
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"65": 59, "36": 1, "37": 2, "38": 8, "55": 5, "44": 4, "53": 4, "54": 5, "23": 2, "56": 6, "57": 6, "58": 7, "59": 7, "29": 0}, "uri": "admin/tool_shed_repository/repository_installation_grid.mako", "filename": "templates/admin/tool_shed_repository/repository_installation_grid.mako"}
__M_END_METADATA
"""
