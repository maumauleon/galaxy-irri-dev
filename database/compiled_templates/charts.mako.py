# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501749232.110997
_enable_loop = True
_template_filename = 'config/plugins/visualizations/charts/templates/charts.mako'
_template_uri = 'charts.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        config = context.get('config', UNDEFINED)
        visualization_name = context.get('visualization_name', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        visualization_id = context.get('visualization_id', UNDEFINED)
        __M_writer = context.writer()

        root            = h.url_for( "/" )
        app_root        = root + "plugins/visualizations/charts/static/client"
        repository_root = root + "plugins/visualizations/charts/static/repository"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['app_root','root','repository_root'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<!DOCTYPE HTML>\n<html>\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        <title>')
        __M_writer(filters.html_escape(unicode(hda.name )))
        __M_writer(u' | ')
        __M_writer(unicode(visualization_name))
        __M_writer(u'</title>\n        ')
        __M_writer(unicode(h.js( 'libs/jquery/jquery',
                'libs/jquery/jquery-ui',
                'libs/jquery/select2',
                'libs/bootstrap',
                'libs/underscore',
                'libs/backbone',
                'libs/d3',
                'libs/require')))
        __M_writer(u'\n        ')
        __M_writer(unicode(h.css( 'base', 'jquery-ui/smoothness/jquery-ui' )))
        __M_writer(u'\n        ')
        __M_writer(unicode(h.stylesheet_link( app_root + "/app.css" )))
        __M_writer(u'\n    </head>\n    <body>\n        <script type="text/javascript">\n            var app_root = \'')
        __M_writer(unicode(app_root))
        __M_writer(u"';\n            var repository_root = '")
        __M_writer(unicode(repository_root))
        __M_writer(u"';\n            var Galaxy = Galaxy || parent.Galaxy || {\n                root    : '")
        __M_writer(unicode(root))
        __M_writer(u'\',\n                emit    : {\n                    debug: function() {}\n                }\n            };\n            window.console = window.console || {\n                log     : function(){},\n                debug   : function(){},\n                info    : function(){},\n                warn    : function(){},\n                error   : function(){},\n                assert  : function(){}\n            };\n            require.config({\n                baseUrl: Galaxy.root + "static/scripts/",\n                paths: {\n                    "plugin"        : "')
        __M_writer(unicode(app_root))
        __M_writer(u'",\n                    "d3"            : "libs/d3",\n                    "repository"    : "')
        __M_writer(unicode(repository_root))
        __M_writer(u'"\n                },\n                shim: {\n                    "libs/underscore": { exports: "_" },\n                    "libs/backbone": { exports: "Backbone" },\n                    "d3": { exports: "d3" }\n                }\n            });\n            $(function() {\n                require( [ \'plugin/app\' ], function( App ) {\n                    var config = ')
        __M_writer(unicode( h.dumps( config ) ))
        __M_writer(u';\n                    var app = new App({\n                        visualization_id : ')
        __M_writer(unicode( h.dumps( visualization_id ) ))
        __M_writer(u" || undefined,\n                        dataset_id       : config.dataset_id,\n                        chart_dict       : config.chart_dict\n                    });\n                    $( 'body' ).append( app.$el );\n                });\n            });\n        </script>\n    </body>\n</html>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "26": 1, "34": 5, "35": 11, "36": 11, "37": 11, "38": 11, "39": 12, "47": 19, "48": 20, "49": 20, "50": 21, "51": 21, "52": 25, "53": 25, "54": 26, "55": 26, "56": 28, "57": 28, "58": 44, "59": 44, "60": 46, "61": 46, "62": 56, "63": 56, "64": 58, "65": 58, "71": 65}, "uri": "charts.mako", "filename": "config/plugins/visualizations/charts/templates/charts.mako"}
__M_END_METADATA
"""
