# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501654462.772447
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/dataset/large_file.mako'
_template_uri = '/dataset/large_file.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f4bc4364c90', context._clean_inheritance_tokens(), templateuri=u'/dataset/display.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f4bc4364c90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f4bc4364c90')._populate(_import_ns, [u'render_deleted_data_message'])
        truncated_data = _import_ns.get('truncated_data', context.get('truncated_data', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        render_deleted_data_message = _import_ns.get('render_deleted_data_message', context.get('render_deleted_data_message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode( render_deleted_data_message( data ) ))
        __M_writer(u'\n\n<div class="warningmessagelarge">\n    This dataset is large and only the first megabyte is shown below.<br />\n    <a href="')
        __M_writer(unicode(h.url_for( controller='dataset', action='display', dataset_id=trans.security.encode_id( data.id ), filename='' )))
        __M_writer(u'">Show all</a> |\n    <a href="')
        __M_writer(unicode(h.url_for( controller='dataset', action='display', dataset_id=trans.security.encode_id( data.id ), to_ext=data.ext )))
        __M_writer(u'">Save</a>\n</div>\n\n<pre>\n')
        __M_writer(filters.html_escape(unicode( util.unicodify( truncated_data ) )))
        __M_writer(u'\n</pre>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"42": 1, "43": 2, "44": 4, "45": 4, "46": 8, "47": 8, "48": 9, "49": 9, "50": 13, "51": 13, "23": 2, "57": 51, "29": 0}, "uri": "/dataset/large_file.mako", "filename": "templates/webapps/galaxy/dataset/large_file.mako"}
__M_END_METADATA
"""
