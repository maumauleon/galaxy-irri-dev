# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501213875.693667
_enable_loop = True
_template_filename = u'templates/message.mako'
_template_uri = u'/message.mako'
_source_encoding = 'ascii'
_exports = ['body', 'render_msg', 'center_panel', 'init', 'render_large_message', 'javascripts']



def inherit(context):
    if context.get('use_panels'):
        if context.get('webapp'):
            app_name = context.get('webapp')
        elif context.get('app'):
            app_name = context.get('app').name
        else:
            app_name = 'galaxy'
        return '/webapps/%s/base_panels.mako' % app_name
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f295422c750', context._clean_inheritance_tokens(), templateuri=u'/refresh_frames.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f295422c750')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        def render_large_message(message,status):
            return render_render_large_message(context,message,status)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(render_large_message( message, status )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_msg(context,msg,status='done'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="')
        __M_writer(unicode(status))
        __M_writer(u'message">')
        __M_writer(unicode(_(msg)))
        __M_writer(u'</div>\n    <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        def render_large_message(message,status):
            return render_render_large_message(context,message,status)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(render_large_message( message, status )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        active_view = _import_ns.get('active_view', context.get('active_view', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view=active_view
        self.message_box_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_large_message(context,message,status):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="')
        __M_writer(unicode(status))
        __M_writer(u'messagelarge" style="margin: 1em">')
        __M_writer(unicode(_(message)))
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f295422c750')._populate(_import_ns, [u'handle_refresh_frames'])
        handle_refresh_frames = _import_ns.get('handle_refresh_frames', context.get('handle_refresh_frames', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        __M_writer(unicode(handle_refresh_frames()))
        __M_writer(u'\n    <script type="text/javascript">\n        if ( parent.handle_minwidth_hint )\n        {\n            parent.handle_minwidth_hint( -1 );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"171": 29, "132": 20, "133": 21, "140": 26, "16": 1, "146": 53, "153": 53, "154": 54, "155": 54, "156": 54, "157": 54, "163": 29, "37": 16, "43": 0, "172": 30, "173": 30, "174": 31, "175": 31, "51": 13, "52": 14, "53": 16, "54": 18, "58": 18, "59": 27, "60": 38, "61": 43, "62": 46, "63": 50, "64": 55, "65": 61, "181": 175, "71": 48, "81": 48, "82": 49, "83": 49, "89": 58, "96": 58, "97": 59, "98": 59, "99": 59, "100": 59, "106": 44, "116": 44, "117": 45, "118": 45, "124": 20}, "uri": "/message.mako", "filename": "templates/message.mako"}
__M_END_METADATA
"""
