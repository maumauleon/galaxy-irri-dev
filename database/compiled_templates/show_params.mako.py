# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501221697.604619
_enable_loop = True
_template_filename = 'templates/show_params.mako'
_template_uri = 'show_params.mako'
_source_encoding = 'ascii'
_exports = ['inputs_recursive_indent', 'inputs_recursive']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x8f11990', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x8f11990')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8f11990')._populate(_import_ns, [u'render_msg'])
        upgrade_messages = _import_ns.get('upgrade_messages', context.get('upgrade_messages', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        inherit_chain = _import_ns.get('inherit_chain', context.get('inherit_chain', UNDEFINED))
        tool = _import_ns.get('tool', context.get('tool', UNDEFINED))
        def inputs_recursive(input_params,param_values,depth=1,upgrade_messages=None):
            return render_inputs_recursive(context._locals(__M_locals),input_params,param_values,depth,upgrade_messages)
        filter = _import_ns.get('filter', context.get('filter', UNDEFINED))
        job = _import_ns.get('job', context.get('job', UNDEFINED))
        set = _import_ns.get('set', context.get('set', UNDEFINED))
        hda = _import_ns.get('hda', context.get('hda', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        params_objects = _import_ns.get('params_objects', context.get('params_objects', UNDEFINED))
        has_parameter_errors = _import_ns.get('has_parameter_errors', context.get('has_parameter_errors', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        from galaxy.util import listify, nice_size, unicodify 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['nice_size','listify','unicodify'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<style>\n    .inherit {\n        border: 1px solid #bbb;\n        padding: 15px;\n        text-align: center;\n        background-color: #eee;\n    }\n\n    table.info_data_table {\n        table-layout: fixed;\n        word-break: break-word;\n    }\n    table.info_data_table td:nth-child(1) {\n        width: 25%;\n    }\n\n    .code {\n        white-space: pre-wrap;\n        background: #1d1f21;\n        color: white;\n        padding: 1em;\n    }\n</style>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<h2>\n')
        if tool:
            __M_writer(u'    ')
            __M_writer(filters.html_escape(unicode(tool.name )))
            __M_writer(u'\n')
        else:
            __M_writer(u'    Unknown Tool\n')
        __M_writer(u'</h2>\n\n<h3>Dataset Information</h3>\n<table class="tabletip" id="dataset-details">\n    <tbody>\n        ')

        encoded_hda_id = trans.security.encode_id( hda.id )
        encoded_history_id = trans.security.encode_id( hda.history_id )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['encoded_hda_id','encoded_history_id'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n        <tr><td>Number:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.hid )))
        __M_writer(u'</td></tr>\n        <tr><td>Name:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.name )))
        __M_writer(u'</td></tr>\n        <tr><td>Created:</td><td>')
        __M_writer(unicode(unicodify(hda.create_time.strftime(trans.app.config.pretty_datetime_format))))
        __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>Filesize:</td><td>')
        __M_writer(unicode(nice_size(hda.dataset.file_size)))
        __M_writer(u'</td></tr>\n        <tr><td>Dbkey:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.dbkey )))
        __M_writer(u'</td></tr>\n        <tr><td>Format:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.ext )))
        __M_writer(u'</td></tr>\n    </tbody>\n</table>\n\n<h3>Job Information</h3>\n<table class="tabletip">\n    <tbody>\n')
        if job:
            __M_writer(u'            <tr><td>Galaxy Tool ID:</td><td>')
            __M_writer(filters.html_escape(unicode( job.tool_id )))
            __M_writer(u'</td></tr>\n            <tr><td>Galaxy Tool Version:</td><td>')
            __M_writer(filters.html_escape(unicode( job.tool_version )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>Tool Version:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.tool_version )))
        __M_writer(u'</td></tr>\n        <tr><td>Tool Standard Output:</td><td><a href="')
        __M_writer(unicode(h.url_for( controller='dataset', action='stdout', dataset_id=encoded_hda_id )))
        __M_writer(u'">stdout</a></td></tr>\n        <tr><td>Tool Standard Error:</td><td><a href="')
        __M_writer(unicode(h.url_for( controller='dataset', action='stderr', dataset_id=encoded_hda_id )))
        __M_writer(u'">stderr</a></td></tr>\n')
        if job:
            __M_writer(u'            <tr><td>Tool Exit Code:</td><td>')
            __M_writer(filters.html_escape(unicode( job.exit_code )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>History Content API ID:</td><td>')
        __M_writer(unicode(encoded_hda_id))
        __M_writer(u'</td></tr>\n')
        if job:
            __M_writer(u'            <tr><td>Job API ID:</td><td>')
            __M_writer(unicode(trans.security.encode_id( job.id )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>History API ID:</td><td>')
        __M_writer(unicode(encoded_history_id))
        __M_writer(u'</td></tr>\n')
        if hda.dataset.uuid:
            __M_writer(u'        <tr><td>UUID:</td><td>')
            __M_writer(unicode(hda.dataset.uuid))
            __M_writer(u'</td></tr>\n')
        if trans.user_is_admin() or trans.app.config.expose_dataset_path:
            __M_writer(u'            <tr><td>Full Path:</td><td>')
            __M_writer(filters.html_escape(unicode(hda.file_name )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'    </tbody>\n</table>\n\n<h3>Tool Parameters</h3>\n<table class="tabletip" id="tool-parameters">\n    <thead>\n        <tr>\n            <th>Input Parameter</th>\n            <th>Value</th>\n            <th>Note for rerun</th>\n        </tr>\n    </thead>\n    <tbody>\n')
        if params_objects and tool:
            __M_writer(u'            ')
            __M_writer(unicode( inputs_recursive( tool.inputs, params_objects, depth=1, upgrade_messages=upgrade_messages ) ))
            __M_writer(u'\n')
        elif params_objects is None:
            __M_writer(u'            <tr><td colspan="3">Unable to load parameters.</td></tr>\n')
        else:
            __M_writer(u'            <tr><td colspan="3">No parameters.</td></tr>\n')
        __M_writer(u'    </tbody>\n</table>\n')
        if has_parameter_errors:
            __M_writer(u'    <br />\n    ')
            __M_writer(unicode( render_msg( 'One or more of your original parameters may no longer be valid or displayed properly.', status='warning' ) ))
            __M_writer(u'\n')
        __M_writer(u'\n\n<h3>Inheritance Chain</h3>\n<div class="inherit" style="background-color: #fff; font-weight:bold;">')
        __M_writer(filters.html_escape(unicode(hda.name )))
        __M_writer(u'</div>\n\n')
        for dep in inherit_chain:
            __M_writer(u'    <div style="font-size: 36px; text-align: center; position: relative; top: 3px">&uarr;</div>\n    <div class="inherit">\n        \'')
            __M_writer(filters.html_escape(unicode(dep[0].name )))
            __M_writer(u"' in ")
            __M_writer(unicode(dep[1]))
            __M_writer(u'<br/>\n    </div>\n')
        __M_writer(u'\n\n\n')
        if job and job.command_line and (trans.user_is_admin() or trans.app.config.expose_dataset_path):
            __M_writer(u'<h3>Command Line</h3>\n<pre class="code">\n')
            __M_writer(filters.html_escape(unicode( job.command_line )))
            __M_writer(u'</pre>\n')
        __M_writer(u'\n')
        if job and (trans.user_is_admin() or trans.app.config.expose_potentially_sensitive_job_metrics):
            __M_writer(u'<h3>Job Metrics</h3>\n')
            job_metrics = trans.app.job_metrics 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['job_metrics'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            plugins = set([metric.plugin for metric in job.metrics]) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['metric','plugins'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            for plugin in sorted(plugins):
                if trans.user_is_admin() or plugin != 'env':
                    __M_writer(u'    <h4>')
                    __M_writer(filters.html_escape(unicode( plugin )))
                    __M_writer(u'</h4>\n    <table class="tabletip info_data_table">\n        <tbody>\n        ')

                    plugin_metrics = filter(lambda x: x.plugin == plugin, job.metrics)
                    plugin_metric_displays = [job_metrics.format( metric.plugin, metric.metric_name, metric.metric_value ) for metric in plugin_metrics]
                    plugin_metric_displays = sorted(plugin_metric_displays, key=lambda pair: pair[0])  # Sort on displayed title
                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['plugin_metric_displays','metric','plugin_metrics'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    for metric_title, metric_value in plugin_metric_displays:
                        __M_writer(u'                <tr><td>')
                        __M_writer(filters.html_escape(unicode( metric_title )))
                        __M_writer(u'</td><td>')
                        __M_writer(filters.html_escape(unicode( metric_value )))
                        __M_writer(u'</td></tr>\n')
                    __M_writer(u'        </tbody>\n    </table>\n')
        __M_writer(u'\n')
        if job and job.dependencies:
            __M_writer(u'<h3>Job Dependencies</h3>\n    <table class="tabletip">\n        <thead>\n        <tr>\n            <th>Dependency</th>\n            <th>Dependency Type</th>\n            <th>Version</th>\n        </tr>\n        </thead>\n        <tbody>\n\n')
            for dependency in job.dependencies:
                __M_writer(u'                <tr><td>')
                __M_writer(filters.html_escape(unicode( dependency['name'] )))
                __M_writer(u'</td>\n                    <td>')
                __M_writer(filters.html_escape(unicode( dependency['dependency_type'] )))
                __M_writer(u'</td>\n                    <td>')
                __M_writer(filters.html_escape(unicode( dependency['version'] )))
                __M_writer(u'</td>\n                </tr>\n')
            __M_writer(u'\n        </tbody>\n    </table>\n')
        __M_writer(u'\n\n\n<script type="text/javascript">\n$(function(){\n    $( \'.input-dataset-show-params\' ).on( \'click\', function( ev ){\n')
        __M_writer(u"        if( window.parent.Galaxy && window.parent.Galaxy.currHistoryPanel ){\n            window.parent.Galaxy.currHistoryPanel.scrollToId( 'dataset-' + $( this ).data( 'hda-id' ) );\n        }\n    })\n});\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inputs_recursive_indent(context,text,depth):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8f11990')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'\n    <td style="padding-left: ')
        __M_writer(unicode( ( depth - 1 ) * 10 ))
        __M_writer(u'px">\n        ')
        __M_writer(filters.html_escape(unicode(text )))
        __M_writer(u'\n    </td>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inputs_recursive(context,input_params,param_values,depth=1,upgrade_messages=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x8f11990')._populate(_import_ns, [u'render_msg'])
        listify = _import_ns.get('listify', context.get('listify', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def inputs_recursive_indent(text,depth):
            return render_inputs_recursive_indent(context,text,depth)
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        def inputs_recursive(input_params,param_values,depth=1,upgrade_messages=None):
            return render_inputs_recursive(context,input_params,param_values,depth,upgrade_messages)
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        if upgrade_messages is None:
            upgrade_messages = {}
            
        
        __M_writer(u'\n')
        for input_index, input in enumerate( input_params.itervalues() ):
            if input.name in param_values:
                if input.type == "repeat":
                    for i in range( len(param_values[input.name]) ):
                        __M_writer(u'                    ')
                        __M_writer(unicode( inputs_recursive(input.inputs, param_values[input.name][i], depth=depth+1) ))
                        __M_writer(u'\n')
                elif input.type == "section":
                    __M_writer(u'                <tr>\n')
                    __M_writer(u'                    ')
                    __M_writer(unicode(inputs_recursive_indent( text=input.name, depth=depth )))
                    __M_writer(u'\n                    <td></td>\n                </tr>\n                ')
                    __M_writer(unicode( inputs_recursive( input.inputs, param_values[input.name], depth=depth+1, upgrade_messages=upgrade_messages.get( input.name ) ) ))
                    __M_writer(u'\n')
                elif input.type == "conditional":
                    __M_writer(u'                ')

                    try:
                        current_case = param_values[input.name]['__current_case__']
                        is_valid = True
                    except:
                        current_case = None
                        is_valid = False
                    
                    
                    __M_writer(u'\n')
                    if is_valid:
                        __M_writer(u'                    <tr>\n                        ')
                        __M_writer(unicode( inputs_recursive_indent( text=input.test_param.label, depth=depth )))
                        __M_writer(u'\n')
                        __M_writer(u'                        <td>')
                        __M_writer(filters.html_escape(unicode(input.cases[current_case].value )))
                        __M_writer(u'</td>\n                        <td></td>\n                    </tr>\n                    ')
                        __M_writer(unicode( inputs_recursive( input.cases[current_case].inputs, param_values[input.name], depth=depth+1, upgrade_messages=upgrade_messages.get( input.name ) ) ))
                        __M_writer(u'\n')
                    else:
                        __M_writer(u'                    <tr>\n                        ')
                        __M_writer(unicode( inputs_recursive_indent( text=input.name, depth=depth )))
                        __M_writer(u'\n                        <td><em>The previously used value is no longer valid</em></td>\n                        <td></td>\n                    </tr>\n')
                elif input.type == "upload_dataset":
                    __M_writer(u'                    <tr>\n                        ')
                    __M_writer(unicode(inputs_recursive_indent( text=input.group_title( param_values ), depth=depth )))
                    __M_writer(u'\n                        <td>')
                    __M_writer(unicode( len( param_values[input.name] ) ))
                    __M_writer(u' uploaded datasets</td>\n                        <td></td>\n                    </tr>\n')
                elif input.type == "data":
                    __M_writer(u'                    <tr>\n                        ')
                    __M_writer(unicode(inputs_recursive_indent( text=input.label, depth=depth )))
                    __M_writer(u'\n                        <td>\n')
                    for i, element in enumerate(listify(param_values[input.name])):
                        if i > 0:
                            __M_writer(u'                            ,\n')
                        if element.history_content_type == "dataset":
                            __M_writer(u'                                ')

                            hda = element
                            encoded_id = trans.security.encode_id( hda.id )
                            show_params_url = h.url_for( controller='dataset', action='show_params', dataset_id=encoded_id )
                                                            
                            
                            __M_writer(u'\n                                <a class="input-dataset-show-params" data-hda-id="')
                            __M_writer(unicode(encoded_id))
                            __M_writer(u'"\n                                       href="')
                            __M_writer(unicode(show_params_url))
                            __M_writer(u'">')
                            __M_writer(unicode(hda.hid))
                            __M_writer(u': ')
                            __M_writer(filters.html_escape(unicode(hda.name )))
                            __M_writer(u'</a>\n\n')
                        else:
                            __M_writer(u'                                ')
                            __M_writer(unicode(element.hid))
                            __M_writer(u': ')
                            __M_writer(filters.html_escape(unicode(element.name )))
                            __M_writer(u'\n')
                    __M_writer(u'                        </td>\n                        <td></td>\n                    </tr>\n')
                elif input.visible:
                    __M_writer(u'                ')

                    if  hasattr( input, "label" ) and input.label:
                        label = input.label
                    else:
                        #value for label not required, fallback to input name (same as tool panel)
                        label = input.name
                    
                    
                    __M_writer(u'\n                <tr>\n                    ')
                    __M_writer(unicode(inputs_recursive_indent( text=label, depth=depth )))
                    __M_writer(u'\n                    <td>')
                    __M_writer(filters.html_escape(unicode(input.value_to_display_text( param_values[input.name] ) )))
                    __M_writer(u'</td>\n                    <td>')
                    __M_writer(filters.html_escape(unicode( upgrade_messages.get( input.name, '' ) )))
                    __M_writer(u'</td>\n                </tr>\n')
            else:
                __M_writer(u'            <tr>\n                ')

                    # Get parameter label.
                if input.type == "conditional":
                    label = input.test_param.label
                elif input.type == "repeat":
                    label = input.label()
                else:
                    label = input.label or input.name
                                
                
                __M_writer(u'\n                ')
                __M_writer(unicode(inputs_recursive_indent( text=label, depth=depth )))
                __M_writer(u'\n                <td><em>not used (parameter was added after this job was run)</em></td>\n                <td></td>\n            </tr>\n')
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "51": 1, "52": 2, "53": 3, "57": 3, "58": 135, "59": 142, "60": 145, "61": 146, "62": 146, "63": 146, "64": 147, "65": 148, "66": 150, "67": 155, "74": 158, "75": 159, "76": 159, "77": 160, "78": 160, "79": 161, "80": 161, "81": 163, "82": 163, "83": 163, "84": 164, "85": 164, "86": 165, "87": 165, "88": 172, "89": 173, "90": 173, "91": 173, "92": 174, "93": 174, "94": 176, "95": 176, "96": 176, "97": 177, "98": 177, "99": 178, "100": 178, "101": 179, "102": 180, "103": 180, "104": 180, "105": 182, "106": 182, "107": 182, "108": 183, "109": 184, "110": 184, "111": 184, "112": 186, "113": 186, "114": 186, "115": 187, "116": 188, "117": 188, "118": 188, "119": 190, "120": 191, "121": 191, "122": 191, "123": 193, "124": 206, "125": 207, "126": 207, "127": 207, "128": 208, "129": 209, "130": 210, "131": 211, "132": 213, "133": 215, "134": 216, "135": 217, "136": 217, "137": 219, "138": 222, "139": 222, "140": 224, "141": 225, "142": 227, "143": 227, "144": 227, "145": 227, "146": 230, "147": 233, "148": 234, "149": 236, "150": 236, "151": 238, "152": 239, "153": 240, "154": 241, "158": 241, "159": 242, "163": 242, "164": 243, "165": 244, "166": 245, "167": 245, "168": 245, "169": 248, "177": 252, "178": 253, "179": 254, "180": 254, "181": 254, "182": 254, "183": 254, "184": 256, "185": 261, "186": 262, "187": 263, "188": 274, "189": 275, "190": 275, "191": 275, "192": 276, "193": 276, "194": 277, "195": 277, "196": 280, "197": 284, "198": 291, "204": 138, "210": 138, "211": 139, "212": 139, "213": 140, "214": 140, "220": 29, "237": 29, "238": 30, "243": 33, "244": 34, "245": 35, "246": 36, "247": 37, "248": 38, "249": 38, "250": 38, "251": 40, "252": 41, "253": 43, "254": 43, "255": 43, "256": 46, "257": 46, "258": 47, "259": 48, "260": 48, "269": 55, "270": 56, "271": 57, "272": 58, "273": 58, "274": 60, "275": 60, "276": 60, "277": 63, "278": 63, "279": 64, "280": 65, "281": 66, "282": 66, "283": 71, "284": 72, "285": 73, "286": 73, "287": 74, "288": 74, "289": 78, "290": 79, "291": 80, "292": 80, "293": 82, "294": 83, "295": 84, "296": 86, "297": 87, "298": 87, "304": 91, "305": 92, "306": 92, "307": 93, "308": 93, "309": 93, "310": 93, "311": 93, "312": 93, "313": 95, "314": 96, "315": 96, "316": 96, "317": 96, "318": 96, "319": 99, "320": 102, "321": 103, "322": 103, "330": 109, "331": 111, "332": 111, "333": 112, "334": 112, "335": 113, "336": 113, "337": 116, "338": 118, "339": 119, "349": 127, "350": 128, "351": 128, "352": 133, "358": 352}, "uri": "show_params.mako", "filename": "templates/show_params.mako"}
__M_END_METADATA
"""
