# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501749548.810149
_enable_loop = True
_template_filename = 'config/plugins/visualizations/scatterplot/templates/scatterplot.mako'
_template_uri = 'scatterplot.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        embedded = context.get('embedded', UNDEFINED)
        title = context.get('title', UNDEFINED)
        h = context.get('h', UNDEFINED)
        saved_visualization = context.get('saved_visualization', UNDEFINED)
        visualization_id = context.get('visualization_id', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        visualization_display_name = context.get('visualization_display_name', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        config = context.get('config', UNDEFINED)
        __M_writer = context.writer()

        default_title = "Scatterplot of '" + hda.name + "'"
        info = hda.name
        if hda.info:
            info += ' : ' + hda.info
        
        # optionally bootstrap data from dprov
        ##data = list( hda.datatype.dataset_column_dataprovider( hda, limit=10000 ) )
        
        # Use root for resource loading.
        root = h.url_for( '/' )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['info','root','default_title'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n<!DOCTYPE HTML>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>')
        __M_writer(filters.html_escape(unicode(title or default_title )))
        __M_writer(u' | ')
        __M_writer(unicode(visualization_display_name))
        __M_writer(u'</title>\n\n')
        __M_writer(unicode(h.css( 'base', 'jquery-ui/smoothness/jquery-ui')))
        __M_writer(u'\n')
        __M_writer(unicode(h.stylesheet_link( root + 'plugins/visualizations/scatterplot/static/scatterplot.css' )))
        __M_writer(u'\n\n')
        __M_writer(u'<script type="text/javascript">\n// TODO: blah\nwindow.Galaxy = { root: \'')
        __M_writer(unicode( root ))
        __M_writer(u"' };\n</script>\n")
        __M_writer(unicode(h.js( 'libs/jquery/jquery',
        'libs/jquery/jquery.migrate',
        'libs/jquery/jquery-ui',
        'libs/bootstrap',
        'libs/underscore',
        'libs/backbone',
        'libs/d3',
        'ui/peek-column-selector',
        'ui/pagination',
        'mvc/visualization/visualization-model' )))
        __M_writer(u'\n\n')
        __M_writer(unicode(h.javascript_link( root + 'plugins/visualizations/scatterplot/static/scatterplot-edit.js' )))
        __M_writer(u'\n\n<script type="text/javascript">\nfunction getModel(){\n    return new ScatterplotModel({\n        id      : ')
        __M_writer(unicode(h.dumps( visualization_id )))
        __M_writer(u' || undefined,\n        title   : "')
        __M_writer(unicode(title or default_title))
        __M_writer(u'",\n        config  : ')
        __M_writer(unicode(h.dumps( config, indent=2 )))
        __M_writer(u'\n    });\n}\nfunction getHDAJSON(){\n    return ')
        __M_writer(unicode(h.dumps( trans.security.encode_dict_ids( hda.to_dict() ), indent=2 )))
        __M_writer(u';\n}\n</script>\n\n</head>\n\n')
        __M_writer(u'<body>\n')
        if embedded and saved_visualization:
            __M_writer(u'        <figcaption>\n            <span class="title">')
            __M_writer(unicode(title))
            __M_writer(u'</span>\n            <span class="title-info">')
            __M_writer(unicode(info))
            __M_writer(u'</span>\n        </figcaption>\n        <figure class="scatterplot-display"></figure>\n\n        <script type="text/javascript">\n        $(function(){\n            var display = new ScatterplotDisplay({\n                    el      : $( \'.scatterplot-display\' ).attr( \'id\', \'scatterplot-display-\' + \'')
            __M_writer(unicode(visualization_id))
            __M_writer(u'\' ),\n                    model   : getModel(),\n                    dataset : getHDAJSON(),\n                    embedded: "')
            __M_writer(unicode(embedded))
            __M_writer(u'"\n                }).render();\n            display.fetchData();\n            //window.model = model;\n            //window.display = display;\n        });\n        </script>\n\n')
        else:
            __M_writer(u'        <div class="chart-header">\n            <h2>')
            __M_writer(unicode(title or default_title))
            __M_writer(u'</h2>\n            <p>')
            __M_writer(unicode(info))
            __M_writer(u'</p>\n        </div>\n\n        <div class="scatterplot-editor"></div>\n        <script type="text/javascript">\n        $(function(){\n            var model = getModel(),\n                hdaJSON = getHDAJSON(),\n                editor  = new ScatterplotConfigEditor({\n                    el      : $( \'.scatterplot-editor\' ).attr( \'id\', \'scatterplot-editor-hda-\' + hdaJSON.id ),\n                    model   : model,\n                    dataset : hdaJSON\n                }).render();\n            window.editor = editor;\n\n            $( \'.chart-header h2\' ).click( function(){\n                var returned = prompt( \'Enter a new title:\' );\n                if( returned ){\n                    model.set( \'title\', returned );\n                }\n            });\n            model.on( \'change:title\', function(){\n                $( \'.chart-header h2\' ).text( model.get( \'title\' ) );\n                document.title = model.get( \'title\' ) + \' | \' + \'')
            __M_writer(unicode(visualization_display_name))
            __M_writer(u"';\n            })\n        });\n        </script>\n")
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "30": 1, "45": 12, "46": 14, "47": 19, "48": 19, "49": 19, "50": 19, "51": 22, "52": 22, "53": 23, "54": 23, "55": 26, "56": 28, "57": 28, "58": 30, "68": 39, "69": 41, "70": 41, "71": 46, "72": 46, "73": 47, "74": 47, "75": 48, "76": 48, "77": 52, "78": 52, "79": 59, "80": 60, "81": 61, "82": 62, "83": 62, "84": 63, "85": 63, "86": 70, "87": 70, "88": 73, "89": 73, "90": 81, "91": 82, "92": 83, "93": 83, "94": 84, "95": 84, "96": 107, "97": 107, "98": 112, "104": 98}, "uri": "scatterplot.mako", "filename": "config/plugins/visualizations/scatterplot/templates/scatterplot.mako"}
__M_END_METADATA
"""
