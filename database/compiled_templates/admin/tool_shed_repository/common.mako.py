# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501214155.048358
_enable_loop = True
_template_filename = u'templates/admin/tool_shed_repository/common.mako'
_template_uri = u'/admin/tool_shed_repository/common.mako'
_source_encoding = 'ascii'
_exports = ['repository_installation_status_updater', 'render_readme_section', 'browse_files', 'tool_dependency_installation_updater', 'repository_installation_updater', 'dependency_status_updater', 'render_dependencies_section']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f3534030810', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f3534030810')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_repository_installation_status_updater(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        // Tool shed repository status updater - used to update the installation status on the Repository Installation Grid.\n        // Looks for changes in repository installation status using an async request. Keeps calling itself (via setTimeout) until\n        // repository installation status is not one of: \'New\', \'Cloning\', \'Setting tool versions\', \'Installing tool dependencies\',\n        // \'Loading proprietary datatypes\'.\n        var tool_shed_repository_status_updater = function( repository_status_list ) {\n            // See if there are any items left to track\n            //alert( "repository_status_list start " + repository_status_list.toSource() );\n            var empty = true;\n            for ( var item in repository_status_list ) {\n                //alert( "item" + item.toSource() );\n                //alert( "repository_status_list[item] " + repository_status_list[item].toSource() );\n                //alert( "repository_status_list[item][\'status\']" + repository_status_list[item][\'status\'] );\n                if (repository_status_list[item][\'status\'] != \'Installed\'){\n                    empty = false;\n                    break;\n                }\n            }\n            if ( ! empty ) {\n                setTimeout( function() { tool_shed_repository_status_updater_callback( repository_status_list ) }, 3000 );\n            }\n        };\n        var tool_shed_repository_status_updater_callback = function( repository_status_list ) {\n            //alert( repository_status_list );\n            //alert( repository_status_list.toSource() );\n            var ids = [];\n            var status_list = [];\n            $.each( repository_status_list, function( index, repository_status ) {\n                //alert(\'repository_status \'+ repository_status.toSource() );\n                //alert(\'id \'+ repository_status[\'id\'] );\n                //alert( \'status\'+ repository_status[\'status\'] );\n                ids.push( repository_status[ \'id\' ] );\n                status_list.push( repository_status[ \'status\' ] );\n            });\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='repository_installation_status_updates' )))
        __M_writer(u'",\n                dataType: "json",\n                data: { ids: ids.join( "," ), status_list: status_list.join( "," ) },\n                success : function( data ) {\n                    $.each( data, function( index, val ) {\n                        // Replace HTML\n                        var cell1 = $( "#RepositoryStatus-" + val[ \'id\' ] );\n                        cell1.html( val[ \'html_status\' ] );\n                        repository_status_list[ index ] = val;\n                    });\n                    tool_shed_repository_status_updater( repository_status_list );\n                },\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_readme_section(context,containers_dict):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        render_folder = _import_ns.get('render_folder', context.get('render_folder', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
        
        readme_files_root_folder = containers_dict.get( 'readme_files', None )
            
        
        __M_writer(u'\n')
        if readme_files_root_folder:
            __M_writer(u'        <p/>\n        <div class="form-row">\n            ')
            row_counter = RowCounter() 
            
            __M_writer(u'\n            <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table">\n                ')
            __M_writer(unicode(render_folder( readme_files_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
            __M_writer(u'\n            </table>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_browse_files(context,title_text,directory_path):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            // --- Initialize sample trees\n            $("#tree").dynatree({\n                title: "')
        __M_writer(filters.html_escape(unicode(title_text)))
        __M_writer(u'",\n                minExpandLevel: 1,\n                persist: false,\n                checkbox: true,\n                selectMode: 3,\n                onPostInit: function(isReloading, isError) {\n                    // Re-fire onActivate, so the text is updated\n                    this.reactivate();\n                },\n                fx: { height: "toggle", duration: 200 },\n                // initAjax is hard to fake, so we pass the children as object array:\n                initAjax: {url: "')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='open_folder' )))
        __M_writer(u'",\n                           dataType: "json",\n                           data: { folder_path: "')
        __M_writer(filters.html_escape(unicode(directory_path)))
        __M_writer(u'",\n                                   repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'" },\n                },\n                onLazyRead: function(dtnode){\n                    dtnode.appendAjax({\n                        url: "')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='open_folder' )))
        __M_writer(u'",\n                        dataType: "json",\n                        data: { folder_path: dtnode.data.key,\n                                repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'" },\n                    });\n                },\n                onSelect: function(select, dtnode) {\n                    // Display list of selected nodes\n                    var selNodes = dtnode.tree.getSelectedNodes();\n                    // convert to title/key array\n                    var selKeys = $.map(selNodes, function(node) {\n                        return node.data.key;\n                    });\n                },\n                onActivate: function(dtnode) {\n                    var cell = $("#file_contents");\n                    var selected_value;\n                     if (dtnode.data.key == \'root\') {\n                        selected_value = "')
        __M_writer(filters.html_escape(unicode(directory_path)))
        __M_writer(u'/";\n                    } else {\n                        selected_value = dtnode.data.key;\n                    };\n                    if (selected_value.charAt(selected_value.length-1) != \'/\') {\n                        // Make ajax call\n                        $.ajax( {\n                            type: "POST",\n                            url: "')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='get_file_contents' )))
        __M_writer(u'",\n                            dataType: "json",\n                            data: { file_path: selected_value, repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'" },\n                            success : function( data ) {\n                                cell.html( \'<label>\'+data+\'</label>\' )\n                            }\n                        });\n                    } else {\n                        cell.html( \'\' );\n                    };\n                },\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tool_dependency_installation_updater(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        can_update = False
        if query.count():
            # Get the first tool dependency to get to the tool shed repository.
            tool_dependency = query[0]
            tool_shed_repository = tool_dependency.tool_shed_repository
            can_update = tool_shed_repository.tool_dependencies_being_installed or tool_shed_repository.missing_tool_dependencies
            
        
        __M_writer(u'\n')
        if can_update:
            __M_writer(u'        <script type="text/javascript">\n            // Tool dependency installation status updater\n            tool_dependency_status_updater( [')
            __M_writer(unicode( ",".join( [ '{"id" : "%s", "status" : "%s"}' % ( trans.security.encode_id( td.id ), td.status ) for td in query ] ) ))
            __M_writer(u' ] );\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_repository_installation_updater(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        can_update = False
        if query.count():
            for tool_shed_repository in query:
                if tool_shed_repository.status not in [ trans.install_model.ToolShedRepository.installation_status.INSTALLED,
                                                        trans.install_model.ToolShedRepository.installation_status.ERROR,
                                                        trans.install_model.ToolShedRepository.installation_status.DEACTIVATED,
                                                        trans.install_model.ToolShedRepository.installation_status.UNINSTALLED ]:
                    can_update = True
                    break
            
        
        __M_writer(u'\n')
        if can_update:
            __M_writer(u'        <script type="text/javascript">\n            // Tool shed repository installation status updater\n            tool_shed_repository_status_updater( [')
            __M_writer(unicode( ",".join( [ '{"id" : "%s", "status" : "%s"}' % ( trans.security.encode_id( tsr.id ), tsr.status ) for tsr in query ] ) ))
            __M_writer(u' ] );\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dependency_status_updater(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        // Tool dependency status updater - used to update the installation status on the Tool Dependencies Grid.\n        // Looks for changes in tool dependency installation status using an async request. Keeps calling itself\n        // (via setTimeout) until dependency installation status is neither \'Installing\' nor \'Building\'.\n        var tool_dependency_status_updater = function( dependency_status_list ) {\n            // See if there are any items left to track\n            var empty = true;\n            for ( var item in dependency_status_list ) {\n                //alert( "item" + item.toSource() );\n                //alert( "dependency_status_list[item] " + dependency_status_list[item].toSource() );\n                //alert( "dependency_status_list[item][\'status\']" + dependency_status_list[item][\'status\'] );\n                if ( dependency_status_list[item][\'status\'] != \'Installed\' ) {\n                    empty = false;\n                    break;\n                }\n            }\n            if ( ! empty ) {\n                setTimeout( function() { tool_dependency_status_updater_callback( dependency_status_list ) }, 3000 );\n            }\n        };\n        var tool_dependency_status_updater_callback = function( dependency_status_list ) {\n            var ids = [];\n            var status_list = [];\n            $.each( dependency_status_list, function( index, dependency_status ) {\n                ids.push( dependency_status[ \'id\' ] );\n                status_list.push( dependency_status[ \'status\' ] );\n            });\n            // Make ajax call\n            $.ajax( {\n                type: "POST",\n                url: "')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='tool_dependency_status_updates' )))
        __M_writer(u'",\n                dataType: "json",\n                data: { ids: ids.join( "," ), status_list: status_list.join( "," ) },\n                success : function( data ) {\n                    $.each( data, function( index, val ) {\n                        // Replace HTML\n                        var cell1 = $( "#ToolDependencyStatus-" + val[ \'id\' ] );\n                        cell1.html( val[ \'html_status\' ] );\n                        dependency_status_list[ index ] = val;\n                    });\n                    tool_dependency_status_updater( dependency_status_list );\n                },\n            });\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_dependencies_section(context,install_resolver_dependencies_check_box,repository_dependencies_check_box,install_tool_dependencies_check_box,containers_dict,revision_label=None,export=False,requirements_status=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f3534030810')._populate(_import_ns, [u'*'])
        render_folder = _import_ns.get('render_folder', context.get('render_folder', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        repository = _import_ns.get('repository', context.get('repository', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <style type="text/css">\n        #dependency_table{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px;\n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n    </style>\n    <script type="text/javascript">\n         $(function(){\n             $(".detail-section").hide();\n             var hidden = true;\n             $(".toggle-detail-section").click(function(e){\n                 e.preventDefault();\n                 hidden = !hidden;\n                 if (hidden === true){\n                     $(".toggle-detail-section").text(\'Display Details\');\n                 } else{\n                     $(".toggle-detail-section").text(\'Hide Details\');\n                 }\n                 $(".detail-section").toggle();\n             })\n         });\n     </script>\n    ')

        from markupsafe import escape
        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
        
        repository_dependencies_root_folder = containers_dict.get( 'repository_dependencies', None )
        missing_repository_dependencies_root_folder = containers_dict.get( 'missing_repository_dependencies', None )
        tool_dependencies_root_folder = containers_dict.get( 'tool_dependencies', None )
        missing_tool_dependencies_root_folder = containers_dict.get( 'missing_tool_dependencies', None )
        env_settings_heaader_row_displayed = False
        package_header_row_displayed = False
        if revision_label:
            revision_label_str = ' revision <b>%s</b> of ' % escape( str( revision_label ) )
        else:
            revision_label_str = ' '
            
        
        __M_writer(u'\n    <div class="form-row">\n        <p>\n            By default Galaxy will install all needed dependencies for')
        __M_writer(unicode(revision_label_str))
        __M_writer(u'the repository. See the\n            <a target="_blank" href="https://docs.galaxyproject.org/en/master/admin/dependency_resolvers.html">\n                dependency resolver documentation\n            </a>.\n        </p>\n        <p>\n            You can control how dependencies are installed (this is an advanced option, if in doubt, use the default)\n            <button class="toggle-detail-section">\n                Display Details\n            </button>\n        </p>\n        <p>\n        </p>\n     </div>\n')
        if export:
            __M_writer(u'    <div class="form-row">\n        <div class="toolParamHelp" style="clear: both;">\n            <p>\n                The following additional repositories are required by')
            __M_writer(unicode(revision_label_str))
            __M_writer(u'the <b>')
            __M_writer(filters.html_escape(unicode(repository.name)))
            __M_writer(u'</b> repository and they can be exported as well.\n            </p>\n        </div>\n    </div>\n')
        __M_writer(u'    <div style="clear: both"></div>\n    <div class="detail-section">\n')
        if repository_dependencies_root_folder or missing_repository_dependencies_root_folder:
            if repository_dependencies_check_box:
                __M_writer(u'            <div class="form-row">\n')
                if export:
                    __M_writer(u'                    <label>Export repository dependencies?</label>\n')
                else:
                    __M_writer(u'                    <label>Handle repository dependencies?</label>\n')
                __M_writer(u'                ')
                __M_writer(unicode(repository_dependencies_check_box.get_html()))
                __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n')
                if export:
                    __M_writer(u'                        Select to export the following additional repositories that are required by this repository.\n')
                else:
                    __M_writer(u'                        Select to automatically install these additional Tool Shed repositories required by this repository.\n')
                __M_writer(u'                </div>\n            </div>\n            <div style="clear: both"></div>\n')
            if repository_dependencies_root_folder:
                __M_writer(u'            <div class="form-row">\n                <p/>\n                ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table">\n                    ')
                __M_writer(unicode(render_folder( repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                </table>\n                <div style="clear: both"></div>\n            </div>\n')
            if missing_repository_dependencies_root_folder:
                __M_writer(u'            <div class="form-row">\n                <p/>\n                ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table">\n                    ')
                __M_writer(unicode(render_folder( missing_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                </table>\n                <div style="clear: both"></div>\n            </div>\n')
        if tool_dependencies_root_folder or missing_tool_dependencies_root_folder:
            if install_tool_dependencies_check_box is not None:
                __M_writer(u'            <div class="form-row">\n                <label>When available, install Tool Shed managed tool dependencies?</label>\n                ')
                disabled = trans.app.config.tool_dependency_dir is None 
                
                __M_writer(u'\n                ')
                __M_writer(unicode(install_tool_dependencies_check_box.get_html( disabled=disabled )))
                __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n')
                if disabled:
                    __M_writer(u'                        Set the tool_dependency_dir configuration value in your Galaxy config to automatically handle tool dependencies.\n')
                else:
                    __M_writer(u'                        Select to automatically handle tool dependencies via Tool Shed.\n')
                __M_writer(u'                </div>\n            <div style="clear: both"></div>\n')
            if tool_dependencies_root_folder:
                __M_writer(u'            <div class="form-row">\n                <p/>\n                ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="dependency_table">\n                    ')
                __M_writer(unicode(render_folder( tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                </table>\n                <div style="clear: both"></div>\n            </div>\n')
            if missing_tool_dependencies_root_folder:
                __M_writer(u'            <div class="form-row">\n                <p/>\n                ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="dependency_table">\n                    ')
                __M_writer(unicode(render_folder( missing_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True )))
                __M_writer(u'\n                </table>\n                <div style="clear: both"></div>\n            </div>\n')
            __M_writer(u'    </div>\n')
        __M_writer(u'    <div style="clear: both"></div>\n')
        if requirements_status and install_resolver_dependencies_check_box:
            __M_writer(u'    <div class="form-row">\n        <label>When available, install <a href="https://docs.galaxyproject.org/en/master/admin/conda_faq.html" target="_blank">Conda</a> managed tool dependencies?</label>\n        ')
            __M_writer(unicode(install_resolver_dependencies_check_box.get_html()))
            __M_writer(u'\n        <div class="toolParamHelp" style="clear: both;">\n            Select to automatically install tool dependencies via Conda.\n        </div>\n    </div>\n')
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 1, "26": 0, "33": 1, "34": 66, "35": 231, "36": 254, "37": 302, "38": 357, "39": 374, "40": 394, "46": 304, "53": 304, "54": 342, "55": 342, "61": 233, "68": 233, "69": 234, "81": 244, "82": 245, "83": 246, "84": 248, "86": 248, "87": 250, "88": 250, "94": 3, "103": 3, "104": 8, "105": 8, "106": 19, "107": 19, "108": 21, "109": 21, "110": 22, "111": 22, "112": 26, "113": 26, "114": 29, "115": 29, "116": 44, "117": 44, "118": 52, "119": 52, "120": 54, "121": 54, "127": 359, "135": 359, "136": 360, "145": 367, "146": 368, "147": 369, "148": 371, "149": 371, "155": 376, "163": 376, "164": 377, "176": 387, "177": 388, "178": 389, "179": 391, "180": 391, "186": 256, "193": 256, "194": 287, "195": 287, "201": 68, "211": 68, "212": 95, "234": 115, "235": 118, "236": 118, "237": 132, "238": 133, "239": 136, "240": 136, "241": 136, "242": 136, "243": 141, "244": 143, "245": 144, "246": 145, "247": 146, "248": 147, "249": 148, "250": 149, "251": 151, "252": 151, "253": 151, "254": 153, "255": 154, "256": 155, "257": 156, "258": 158, "259": 162, "260": 163, "261": 165, "263": 165, "264": 167, "265": 167, "266": 172, "267": 173, "268": 175, "270": 175, "271": 177, "272": 177, "273": 183, "274": 184, "275": 185, "276": 187, "278": 187, "279": 188, "280": 188, "281": 190, "282": 191, "283": 192, "284": 193, "285": 195, "286": 198, "287": 199, "288": 201, "290": 201, "291": 203, "292": 203, "293": 208, "294": 209, "295": 211, "297": 211, "298": 213, "299": 213, "300": 218, "301": 220, "302": 221, "303": 222, "304": 224, "305": 224, "306": 230, "312": 306}, "uri": "/admin/tool_shed_repository/common.mako", "filename": "templates/admin/tool_shed_repository/common.mako"}
__M_END_METADATA
"""
