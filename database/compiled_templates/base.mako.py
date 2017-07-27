# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500952922.07087
_enable_loop = True
_template_filename = 'templates/base.mako'
_template_uri = '/base.mako'
_source_encoding = 'ascii'
_exports = ['title', 'stylesheets', 'init', 'javascript_app', 'javascripts', 'metas']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'galaxy_client', context._clean_inheritance_tokens(), templateuri=u'/galaxy_client_app.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'galaxy_client')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        self.js_app = None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<!DOCTYPE HTML>\n<html>\n    <!--base.mako-->\n    ')
        __M_writer(unicode(self.init()))
        __M_writer(u'\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n')
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n\n        <title>')
        __M_writer(unicode(self.title()))
        __M_writer(u'</title>\n')
        __M_writer(u'        <link rel="index" href="')
        __M_writer(unicode( h.url_for( '/' ) ))
        __M_writer(u'"/>\n        ')
        __M_writer(unicode(self.metas()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.javascript_app()))
        __M_writer(u'\n    </head>\n    <body class="inbound">\n        ')
        __M_writer(unicode(next.body()))
        __M_writer(u'\n    </body>\n</html>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css('base')))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css('bootstrap-tour')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode( galaxy_client.load( app=self.js_app ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        form_input_auto_focus = context.get('form_input_auto_focus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if app.config.sentry_dsn:
            __M_writer(u'        ')
            __M_writer(unicode(h.js( "libs/raven" )))
            __M_writer(u"\n        <script>\n            Raven.config('")
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            if trans.user:
                __M_writer(u'                Raven.setUser( { email: "')
                __M_writer(filters.html_escape(unicode(trans.user.email)))
                __M_writer(u'" } );\n')
            __M_writer(u'        </script>\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js(
        ## TODO: remove when all libs are required directly in modules
        'bundled/libs.bundled',
        'libs/require',
        "libs/bootstrap-tour",
    )))
        __M_writer(u'\n\n    <script type="text/javascript">\n')
        __M_writer(u"        window.Galaxy = window.Galaxy || {};\n        window.Galaxy.root = '")
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u'\';\n        window.Galaxy.config = {};\n\n        // configure require\n        // due to our using both script tags and require, we need to access the same jq in both for plugin retention\n        // source http://www.manuel-strehl.de/dev/load_jquery_before_requirejs.en.html\n        define( \'jquery\', [], function(){ return jQuery; })\n        // TODO: use one system\n\n        // shims and paths\n        require.config({\n            baseUrl: "')
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": {\n                    exports: "_"\n                },\n                "libs/backbone": {\n                    deps: [ \'jquery\', \'libs/underscore\' ],\n                    exports: "Backbone"\n                }\n            },\n            // cache busting using time server was restarted\n            urlArgs: \'v=')
        __M_writer(unicode(app.server_starttime))
        __M_writer(u"'\n        });\n    </script>\n\n")
        if not form_input_auto_focus is UNDEFINED and form_input_auto_focus:
            __M_writer(u'        <script type="text/javascript">\n            $(document).ready( function() {\n                // Auto Focus on first item on form\n                if ( $("*:focus").html() == null ) {\n                    $(":input:not([type=hidden]):visible:enabled:first").focus();\n                }\n            });\n        </script>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"131": 42, "132": 44, "133": 45, "134": 45, "135": 45, "136": 47, "137": 47, "138": 48, "139": 49, "140": 49, "141": 49, "142": 51, "143": 53, "144": 54, "150": 59, "23": 1, "152": 65, "153": 65, "26": 0, "155": 76, "156": 87, "154": 76, "158": 91, "159": 92, "160": 101, "35": 1, "36": 2, "166": 109, "40": 2, "41": 4, "45": 4, "46": 8, "47": 8, "48": 12, "49": 14, "50": 16, "51": 16, "52": 18, "53": 18, "54": 18, "55": 19, "56": 19, "57": 20, "58": 20, "59": 21, "60": 21, "61": 22, "62": 22, "63": 25, "64": 25, "65": 30, "66": 33, "67": 39, "68": 102, "69": 106, "70": 109, "175": 166, "76": 30, "85": 36, "90": 36, "91": 37, "92": 37, "93": 38, "94": 38, "151": 64, "100": 33, "109": 104, "157": 87, "115": 104, "116": 105, "117": 105, "123": 42}, "uri": "/base.mako", "filename": "templates/base.mako"}
__M_END_METADATA
"""
