# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501214155.56649
_enable_loop = True
_template_filename = u'templates/webapps/tool_shed/repository/common.mako'
_template_uri = u'/webapps/tool_shed/repository/common.mako'
_source_encoding = 'ascii'
_exports = ['render_dependency_status', 'render_tool_dependency_successful_installation', 'render_tool_dependency', 'render_not_tested', 'render_missing_test_component', 'render_folder', 'render_tool', 'render_resolver_dependencies', 'render_clone_str', 'render_test_environment', 'container_javascripts', 'render_readme', 'render_tool_dependency_installation_error', 'render_tool_dependency_resolver', 'render_repository_dependency', 'render_repository_successful_installation', 'render_datatype', 'render_failed_test', 'common_javascripts', 'render_valid_data_manager', 'render_repository_installation_error', 'render_invalid_repository_dependency', 'render_invalid_tool', 'render_workflow', 'render_repository_type_select_field', 'render_passed_test', 'render_repository_items', 'render_invalid_data_manager', 'render_sharable_str', 'render_table_wrap_style', 'render_invalid_tool_dependency']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
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


def render_render_dependency_status(context,dependency,prepare_for_install=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <td>')
        __M_writer(filters.html_escape(unicode(dependency['name'] )))
        __M_writer(u'</td>\n    <td>')
        __M_writer(filters.html_escape(unicode(dependency['version'] )))
        __M_writer(u'</td>\n')
        if not prepare_for_install:
            if dependency['dependency_type']:
                __M_writer(u'            <td>')
                __M_writer(filters.html_escape(unicode(dependency['dependency_type'].title() )))
                __M_writer(u'</td>\n')
            else:
                __M_writer(u'            <td>')
                __M_writer(filters.html_escape(unicode(dependency['dependency_type'] )))
                __M_writer(u'</td>\n')
            __M_writer(u'        <td>')
            __M_writer(filters.html_escape(unicode(dependency['exact'] )))
            __M_writer(u'</td>\n')
        if dependency['dependency_type'] == None:
            __M_writer(u'        <td>\n           <img src="')
            __M_writer(unicode(h.url_for('/static')))
            __M_writer(u'/images/icon_error_sml.gif" title=\'Dependency not resolved\'/>\n')
            if prepare_for_install:
                __M_writer(u'               Not Installed\n')
            __M_writer(u'        </td>\n')
        elif not dependency['exact']:
            __M_writer(u'        <td>\n            <img src="')
            __M_writer(unicode(h.url_for('/static')))
            __M_writer(u'/images/icon_warning_sml.gif" title=\'Dependency resolved, but version ')
            __M_writer(unicode(dependency['version']))
            __M_writer(u" not found'/>\n        </td>\n")
        else:
            __M_writer(u'        <td>\n            <img src="')
            __M_writer(unicode(h.url_for('/static')))
            __M_writer(u'/june_2007_style/blue/ok_small.png"/>\n')
            if prepare_for_install:
                __M_writer(u'                Installed through ')
                __M_writer(filters.html_escape(unicode(dependency['dependency_type'].title() )))
                __M_writer(u'\n')
            __M_writer(u'        </td>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( successful_installation.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rtdsi-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        __M_writer(filters.html_escape(unicode(successful_installation.name )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(successful_installation.type )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(successful_installation.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Installation directory</th></tr>\n                <tr><td colspan="3">')
        __M_writer(filters.html_escape(unicode(successful_installation.installation_directory )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import string_as_bool
        encoded_id = trans.security.encode_id( tool_dependency.id )
        is_missing = tool_dependency.installation_status not in [ 'Installed' ]
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rtd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        if row_is_header:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
        elif trans.webapp.name == 'galaxy' and tool_dependency.tool_dependency_id:
            if tool_dependency.repository_id and tool_dependency.installation_status in [ trans.install_model.ToolDependency.installation_status.INSTALLED ]:
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_dependency', id=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n                    </a>\n')
            elif tool_dependency.installation_status not in [ trans.install_model.ToolDependency.installation_status.UNINSTALLED ]:
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository_tool_dependencies', tool_dependency_ids=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                __M_writer(unicode(tool_dependency.name))
                __M_writer(u'\n                    </a>\n')
            else:
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n')
        else:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n            ')

        if tool_dependency.version:
            version_str = tool_dependency.version
        else:
            version_str = ''
                    
        
        __M_writer(u'\n            ')
        __M_writer(filters.html_escape(unicode(version_str )))
        __M_writer(u'\n        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool_dependency.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        if trans.webapp.name == 'galaxy':
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.installation_status )))
            __M_writer(u'\n')
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_not_tested(context,not_tested,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( not_tested.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rnt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td>')
        __M_writer(filters.html_escape(unicode(not_tested.reason )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( missing_test_component.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rmtc-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool guid:</b> ')
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_guid )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Missing components:</b> <br/>')
        __M_writer(filters.html_escape(unicode(missing_test_component.missing_components )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_folder(context,folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_datatype(datatype,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        h = context.get('h', UNDEFINED)
        def render_tool_dependency(tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_repository_dependency(invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for)
        def render_invalid_tool_dependency(invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for)
        def render_readme(readme,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_readme(context,readme,pad,parent,row_counter,render_repository_actions_for)
        def render_valid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_tool(invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid,render_repository_actions_for)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        def render_missing_test_component(missing_test_component,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        trans = context.get('trans', UNDEFINED)
        def render_repository_dependency(repository_dependency,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_tool(tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_workflow(workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( folder.id )
        
        if is_root_folder:
            pad = folder_pad
            expander = h.url_for("/static/images/silk/resultset_bottom.png")
            folder_img = h.url_for("/static/images/silk/folder_page.png")
        else:
            pad = folder_pad + 20
            expander = h.url_for("/static/images/silk/resultset_next.png")
            folder_img = h.url_for("/static/images/silk/folder.png")
        my_row = None
            
        
        __M_writer(u'\n')
        if not is_root_folder:
            __M_writer(u'        ')

            if parent is None:
                bg_str = 'bgcolor="#D8D8D8"'
            else:
                bg_str = ''
                    
            
            __M_writer(u'\n        <tr id="folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'" ')
            __M_writer(unicode(bg_str))
            __M_writer(u' class="folderRow libraryOrFolderRow"\n')
            if parent is not None:
                __M_writer(u'                parent="')
                __M_writer(unicode(parent))
                __M_writer(u'"\n                style="display: none;"\n')
            __M_writer(u'            >\n            ')

            col_span_str = ''
            folder_label = str( folder.label )
            if folder.datatypes:
                col_span_str = 'colspan="4"'
            elif folder.label == 'Missing tool dependencies':
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these missing dependencies</i>" % folder_label
                col_span_str = 'colspan="5"'
            elif folder.label in [ 'Installed repository dependencies', 'Repository dependencies', 'Missing repository dependencies' ]:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                elif folder.label not in [ 'Installed repository dependencies' ] and folder.parent.label not in [ 'Installation errors' ]:
                    folder_label = "%s<i> - installation of these additional repositories is required</i>" % folder_label
                if trans.webapp.name == 'galaxy':
                    col_span_str = 'colspan="4"'
            elif folder.label == 'Invalid repository dependencies':
                folder_label = "%s<i> - click the repository dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Invalid tool dependencies':
                folder_label = "%s<i> - click the tool dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Valid tools':
                col_span_str = 'colspan="3"'
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to preview the tool and use the pop-up menu to inspect all metadata</i>" % folder_label
            elif folder.invalid_tools:
                if trans.webapp.name == 'tool_shed':
                    folder_label = "%s<i> - click the tool config file name to see why the tool is invalid</i>" % folder_label
            elif folder.tool_dependencies:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these dependencies</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.workflows:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to view an SVG image of the workflow</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.valid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="3"'
            elif folder.invalid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="2"'
                        
            
            __M_writer(u'\n            <td ')
            __M_writer(unicode(col_span_str))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(folder_pad))
            __M_writer(u'px;">\n                <span class="expandLink folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                    <div style="float: left; margin-left: 2px;" class="expandLink folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                        <a class="folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click" href="javascript:void(0);">\n                            ')
            __M_writer(unicode(folder_label))
            __M_writer(u'\n                        </a>\n                    </div>\n                </span>\n            </td>\n        </tr>\n        ')

            my_row = row_counter.count
            row_counter.increment()
                    
            
            __M_writer(u'\n')
        for sub_folder in folder.folders:
            __M_writer(u'        ')
            __M_writer(unicode(render_folder( sub_folder, pad, parent=my_row, row_counter=row_counter, is_root_folder=False, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for readme in folder.readme_files:
            __M_writer(u'        ')
            __M_writer(unicode(render_readme( readme, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for invalid_repository_dependency in folder.invalid_repository_dependencies:
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_repository_dependency( invalid_repository_dependency, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for index, repository_dependency in enumerate( folder.repository_dependencies ):
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            __M_writer(unicode(render_repository_dependency( repository_dependency, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for invalid_tool_dependency in folder.invalid_tool_dependencies:
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool_dependency( invalid_tool_dependency, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for index, tool_dependency in enumerate( folder.tool_dependencies ):
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            __M_writer(unicode(render_tool_dependency( tool_dependency, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        if folder.valid_tools:
            for index, tool in enumerate( folder.valid_tools ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_tool( tool, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        for invalid_tool in folder.invalid_tools:
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool( invalid_tool, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        if folder.workflows:
            for index, workflow in enumerate( folder.workflows ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_workflow( workflow, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.datatypes:
            for index, datatype in enumerate( folder.datatypes ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_datatype( datatype, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.valid_data_managers:
            for index, data_manager in enumerate( folder.valid_data_managers ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_valid_data_manager( data_manager, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.invalid_data_managers:
            for index, data_manager in enumerate( folder.invalid_data_managers ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_invalid_data_manager( data_manager, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.missing_test_components:
            for missing_test_component in folder.missing_test_components:
                __M_writer(u'            ')
                __M_writer(unicode(render_missing_test_component( missing_test_component, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( tool.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        if row_is_header:
            __M_writer(u'            <th style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">')
            __M_writer(filters.html_escape(unicode(tool.name )))
            __M_writer(u'</th>\n')
        else:
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            if tool.repository_id:
                if trans.webapp.name == 'tool_shed':
                    __M_writer(u'                        <div style="float:left;" class="menubutton split popup" id="tool-')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="view-info" href="')
                    __M_writer(unicode(h.url_for( controller='repository', action='display_tool', repository_id=trans.security.encode_id( tool.repository_id ), tool_config=tool.tool_config, changeset_revision=tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'</a>\n                        </div>\n                        <div popupmenu="tool-')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='repository', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">View tool metadata</a>\n                        </div>\n')
                elif trans.webapp.name == 'galaxy':
                    if tool.repository_installation_status == trans.install_model.ToolShedRepository.installation_status.INSTALLED:
                        __M_writer(u'                            <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id )))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                            ')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'\n')
                else:
                    __M_writer(u'                        ')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'\n')
            else:
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool.name )))
                __M_writer(u'\n')
            __M_writer(u'            </td>\n')
        __M_writer(u'        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.description )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        __M_writer(u'    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_resolver_dependencies(context,requirements_status):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_tool_dependency_resolver(requirements_status,prepare_for_install=False):
            return render_render_tool_dependency_resolver(context,requirements_status,prepare_for_install)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if requirements_status:
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Dependency Resolver Details</div>\n            <div class="toolFormBody">\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="module_resolvers">\n                    ')
            __M_writer(unicode(render_tool_dependency_resolver( requirements_status )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_clone_str(context,repository):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()

        from tool_shed.util.common_util import generate_clone_url_for_repository_in_tool_shed
        clone_str = generate_clone_url_for_repository_in_tool_shed( trans.user, repository )
            
        
        __M_writer(u'hg clone ')
        __M_writer(unicode( clone_str ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_test_environment(context,test_environment,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        encoded_id = trans.security.encode_id( test_environment.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rte-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table class="grid" id="test_environment">\n                <tr><td><b>Time tested:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.time_tested )))
        __M_writer(u'</td></tr>\n                <tr><td><b>System:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.system )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Architecture:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.architecture )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Python version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.python_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy revision:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy database version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed revision:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed database version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed mercurial version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_mercurial_version )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        repository = context.get('repository', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        var init_dependencies = function() {\n            var storage_id = "library-expand-state-')
        __M_writer(unicode(trans.security.encode_id(10000)))
        __M_writer(u'";\n            var restore_folder_state = function() {\n                var state = $.jStorage.get(storage_id);\n                if (state) {\n                    for (var id in state) {\n                        if (state[id] === true) {\n                            var row = $("#" + id),\n                                index = row.parent().children().index(row);\n                            row.addClass("expanded").show();\n                            row.siblings().filter("tr[parent=\'" + index + "\']").show();\n                        }\n                    }\n                }\n            };\n            var save_folder_state = function() {\n                var state = {};\n                $("tr.folderRow").each( function() {\n                    var folder = $(this);\n                    state[folder.attr("id")] = folder.hasClass("expanded");\n                });\n                $.jStorage.set(storage_id, state);\n            };\n            $(".container-table").each(function() {\n                //var container_id = this.id.split( "-" )[0];\n                //alert( container_id );\n                var child_of_parent_cache = {};\n                // Recursively fill in children and descendants of each row\n                var process_row = function(q, parents) {\n                    // Find my index\n                    var parent = q.parent(),\n                        this_level = child_of_parent_cache[parent] || (child_of_parent_cache[parent] = parent.children());\n                    var index = this_level.index(q);\n                    // Find my immediate children\n                    var children = $(par_child_dict[index]);\n                    // Recursively handle them\n                    var descendants = children;\n                    children.each( function() {\n                        child_descendants = process_row( $(this), parents.add(q) );\n                        descendants = descendants.add(child_descendants);\n                    });\n                    // Set up expand / hide link\n                    var expand_fn = function() {\n                        if ( q.hasClass("expanded") ) {\n                            descendants.hide();\n                            descendants.removeClass("expanded");\n                            q.removeClass("expanded");\n                        } else {\n                            children.show();\n                            q.addClass("expanded");\n                        }\n                        save_folder_state();\n                    };\n                    $("." + q.attr("id") + "-click").click(expand_fn);\n                    // return descendants for use by parent\n                    return descendants;\n                }\n                // Initialize dict[parent_id] = rows_which_have_that_parent_id_as_parent_attr\n                var par_child_dict = {},\n                    no_parent = [];\n                $(this).find("tbody tr").each( function() {\n                    if ( $(this).attr("parent")) {\n                        var parent = $(this).attr("parent");\n                        if (par_child_dict[parent] !== undefined) {\n                            par_child_dict[parent].push(this);\n                        } else {\n                            par_child_dict[parent] = [this];\n                        }\n                    } else {\n                        no_parent.push(this);\n                    }\n                });\n                $(no_parent).each( function() {\n                    descendants = process_row( $(this), $([]) );\n                    descendants.hide();\n               });\n            });\n            restore_folder_state();\n        };\n\n        var init_clipboard = function() {\n')
        if hasattr( repository, 'clone_url' ):
            __M_writer(u'                    $(\'#clone_clipboard\').on(\'click\', function( event ) {\n                        event.preventDefault();\n                        window.prompt("Copy to clipboard: Ctrl+C, Enter", "hg clone ')
            __M_writer(unicode( repository.clone_url ))
            __M_writer(u'");\n                    });\n')
        if hasattr( repository, 'share_url' ):
            __M_writer(u'                    $(\'#share_clipboard\').on(\'click\', function( event ) {\n                        event.preventDefault();\n                        window.prompt("Copy to clipboard: Ctrl+C, Enter", "')
            __M_writer(unicode( repository.share_url ))
            __M_writer(u'");\n                    });\n')
        __M_writer(u'        };\n\n        $(function() {\n            init_dependencies();\n            init_clipboard();\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_readme(context,readme,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        encoded_id = trans.security.encode_id( readme.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rr-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="readme_files">\n                <tr><td>')
        __M_writer(unicode( readme.text ))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import unicodify
        encoded_id = trans.security.encode_id( installation_error.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rtdie-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        __M_writer(filters.html_escape(unicode(installation_error.name )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(installation_error.type )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(installation_error.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Error</th></tr>\n                <tr><td colspan="3">')
        __M_writer(filters.html_escape(unicode(unicodify( installation_error.error_message ) )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_resolver(context,requirements_status,prepare_for_install=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_dependency_status(dependency,prepare_for_install=False):
            return render_render_dependency_status(context,dependency,prepare_for_install)
        __M_writer = context.writer()
        __M_writer(u'\n    <tr class="datasetRow">\n        <td style="padding-left: 20 px;">\n            <table class="grid" id="module_resolver_environment">\n                <head>\n                    <tr>\n                        <th>Dependency</th>\n                        <th>Version</th>\n')
        if not prepare_for_install:
            __M_writer(u'                            <th>Resolver</th>\n                            <th>Exact version</th>\n')
        __M_writer(u'                        <th>Current Installation Status<th>\n                    </tr>\n                </head>\n                <body>\n')
        for dependency in requirements_status:
            __M_writer(u'                        ')
            __M_writer(unicode(render_dependency_status(dependency, prepare_for_install)))
            __M_writer(u'\n                        <tr>\n')
        __M_writer(u'                </body>\n            </table>\n        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import asbool
        from tool_shed.util.repository_util import get_repository_by_name_and_owner
        encoded_id = trans.security.encode_id( repository_dependency.id )
        if trans.webapp.name == 'galaxy':
            if repository_dependency.tool_shed_repository_id:
                encoded_required_repository_id = trans.security.encode_id( repository_dependency.tool_shed_repository_id )
            else:
                encoded_required_repository_id = None
            if repository_dependency.installation_status:
                installation_status = str( repository_dependency.installation_status )
            else:
                installation_status = None
        repository_name = str( repository_dependency.repository_name )
        repository_owner = str( repository_dependency.repository_owner )
        changeset_revision = str( repository_dependency.changeset_revision )
        if asbool( str( repository_dependency.prior_installation_required ) ):
            prior_installation_required_str = " <i>(prior install required)</i>"
        else:
            prior_installation_required_str = ""
        if trans.webapp.name == 'galaxy':
            if row_is_header:
                cell_type = 'th'
            else:
                cell_type = 'td'
            rd = None
        else:
            # We're in the tool shed.
            cell_type = 'td'
            rd = get_repository_by_name_and_owner( trans.app, repository_name, repository_owner )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rrd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        if trans.webapp.name == 'galaxy':
            __M_writer(u'            <')
            __M_writer(unicode(cell_type))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            if row_is_header:
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'\n')
            elif encoded_required_repository_id:
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=encoded_required_repository_id )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</a>\n')
            else:
                __M_writer(u'                   ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'\n')
            __M_writer(u'            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            __M_writer(filters.html_escape(unicode(changeset_revision )))
            __M_writer(u'\n            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            __M_writer(filters.html_escape(unicode(repository_owner )))
            __M_writer(u'\n            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            __M_writer(unicode(installation_status))
            __M_writer(u'\n            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n')
        else:
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            if render_repository_actions_for == 'tool_shed' and rd:
                __M_writer(u'                    <a class="view-info" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='view_or_manage_repository', id=trans.security.encode_id( rd.id ), changeset_revision=changeset_revision )))
                __M_writer(u'">Repository <b>')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</b> revision <b>')
                __M_writer(filters.html_escape(unicode(changeset_revision )))
                __M_writer(u'</b> owned by <b>')
                __M_writer(filters.html_escape(unicode(repository_owner )))
                __M_writer(u'</b></a>')
                __M_writer(unicode(prior_installation_required_str))
                __M_writer(u'\n')
            else:
                __M_writer(u'                    Repository <b>')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</b> revision <b>')
                __M_writer(filters.html_escape(unicode(changeset_revision )))
                __M_writer(u'</b> owned by <b>')
                __M_writer(filters.html_escape(unicode(repository_owner )))
                __M_writer(u'</b>')
                __M_writer(unicode(prior_installation_required_str))
                __M_writer(u'\n')
            __M_writer(u'            </td>\n')
        __M_writer(u'    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( successful_installation.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rrsi-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n')
        if not is_current_repository:
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.name )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.owner )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
        __M_writer(u'            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( datatype.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(datatype.extension )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.mimetype )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.subclass )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_failed_test(context,failed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.basic_util import to_html_string
        encoded_id = trans.security.encode_id( failed_test.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rft-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        __M_writer(filters.html_escape(unicode(failed_test.test_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Stderr:</b> <br/>')
        __M_writer(unicode( to_html_string( failed_test.stderr ) ))
        __M_writer(u'</td></tr>\n                <tr><td><b>Traceback:</b> <br/>')
        __M_writer(unicode( to_html_string( failed_test.traceback ) ))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_common_javascripts(context,repository):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n\n            // --- Initialize sample trees\n            $("#tree").dynatree({\n                title: "')
        __M_writer(unicode(repository.name))
        __M_writer(u'",\n                minExpandLevel: 1,\n                persist: false,\n                checkbox: true,\n                selectMode: 3,\n                onPostInit: function(isReloading, isError) {\n                    // Re-fire onActivate, so the text is updated\n                    this.reactivate();\n                },\n                fx: { height: "toggle", duration: 200 },\n                // initAjax is hard to fake, so we pass the children as object array:\n                initAjax: {url: "')
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'",\n                           dataType: "json",\n                           data: { folder_path: "')
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'", repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'"  },\n                },\n                onLazyRead: function(dtnode){\n                    dtnode.appendAjax({\n                        url: "')
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'",\n                        dataType: "json",\n                        data: { folder_path: dtnode.data.key, repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'"  },\n                    });\n                },\n                onSelect: function(select, dtnode) {\n                    // Display list of selected nodes\n                    var selNodes = dtnode.tree.getSelectedNodes();\n                    // convert to title/key array\n                    var selKeys = $.map(selNodes, function(node) {\n                        return node.data.key;\n                    });\n                    if (document.forms["select_files_to_delete"]) {\n                        // The following is used only ~/templates/webapps/tool_shed/repository/browse_repository.mako.\n                        document.select_files_to_delete.selected_files_to_delete.value = selKeys.join(",");\n                    }\n                    // The following is used only in ~/templates/webapps/tool_shed/repository/upload.mako.\n                    if (document.forms["upload_form"]) {\n                        document.upload_form.upload_point.value = selKeys.slice(-1);\n                    }\n                },\n                onActivate: function(dtnode) {\n                    var cell = $("#file_contents");\n                    var selected_value;\n                     if (dtnode.data.key == \'root\') {\n                        selected_value = "')
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'/";\n                    } else {\n                        selected_value = dtnode.data.key;\n                    };\n                    if (selected_value.charAt(selected_value.length-1) != \'/\') {\n                        // Make ajax call\n                        $.ajax( {\n                            type: "POST",\n                            url: "')
        __M_writer(unicode(h.url_for( controller='repository', action='get_file_contents' )))
        __M_writer(u'",\n                            dataType: "json",\n                            data: { file_path: selected_value, repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'" },\n                            success : function ( data ) {\n                                cell.html( \'<label>\'+data+\'</label>\' )\n                            }\n                        });\n                    } else {\n                        cell.html( \'\' );\n                    };\n                },\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rvdm-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.name )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.data_tables )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import unicodify
        encoded_id = trans.security.encode_id( installation_error.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rrie-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n')
        if not is_current_repository:
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.name )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.owner )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
        __M_writer(u'                <tr><th>Error</th></tr>\n                <tr><td colspan="4">')
        __M_writer(filters.html_escape(unicode(unicodify( installation_error.error_message ) )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( invalid_repository_dependency.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rird-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            ')
        __M_writer(filters.html_escape(unicode( invalid_repository_dependency.error )))
        __M_writer(u'\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        encoded_id = trans.security.encode_id( invalid_tool.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rit-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        if trans.webapp.name == 'tool_shed' and invalid_tool.repository_id and invalid_tool.tool_config and invalid_tool.changeset_revision:
            __M_writer(u'                <a class="view-info" href="')
            __M_writer(unicode(h.url_for( controller='repository', action='load_invalid_tool', repository_id=trans.security.encode_id( invalid_tool.repository_id ), tool_config=invalid_tool.tool_config, changeset_revision=invalid_tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">\n                    ')
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n                </a>\n')
        else:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n')
        __M_writer(u'        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.encoding_util import tool_shed_encode
        encoded_id = trans.security.encode_id( workflow.id )
        encoded_workflow_name = tool_shed_encode( workflow.workflow_name )
        if trans.webapp.name == 'tool_shed':
            encoded_repository_metadata_id = trans.security.encode_id( workflow.repository_metadata_id )
            encoded_repository_id = None
        else:
            encoded_repository_metadata_id = None
            encoded_repository_id = trans.security.encode_id( workflow.repository_id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rw-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        if row_is_header:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
        elif trans.webapp.name == 'tool_shed' and encoded_repository_metadata_id:
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_workflow', workflow_name=encoded_workflow_name, repository_metadata_id=encoded_repository_metadata_id, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
        elif trans.webapp.name == 'galaxy' and encoded_repository_id:
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_workflow', workflow_name=encoded_workflow_name, repository_id=encoded_repository_id )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
        else:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.steps )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.format_version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.annotation )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_type_select_field(context,repository_type_select_field,render_help=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="form-row">\n        <label>Repository type:</label>\n        ')

        from tool_shed.repository_types import util
        options = repository_type_select_field.options
        repository_types = []
        for option_tup in options:
            repository_types.append( option_tup[ 1 ] )
        render_as_text = len( options ) == 1
        if render_as_text:
            repository_type = options[ 0 ][ 0 ]
                
        
        __M_writer(u'\n')
        if render_as_text:
            __M_writer(u'            ')
            __M_writer(filters.html_escape(unicode(repository_type )))
            __M_writer(u'\n')
            if render_help:
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    This repository\'s type cannot be changed because its contents are valid only for its current type or it has been cloned.\n                </div>\n')
        else:
            __M_writer(u'            ')
            __M_writer(unicode(repository_type_select_field.get_html()))
            __M_writer(u'\n')
            if render_help:
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    Select the repository type based on the following criteria.\n                    <ul>\n')
                if util.UNRESTRICTED in repository_types:
                    __M_writer(u'                            <li><b>Unrestricted</b> - contents can be any set of valid Galaxy utilities or files\n')
                if util.REPOSITORY_SUITE_DEFINITION in repository_types:
                    __M_writer(u'                            <li><b>Repository suite definition</b> - contents will always be restricted to one file named repository_dependencies.xml\n')
                if util.TOOL_DEPENDENCY_DEFINITION in repository_types:
                    __M_writer(u'                            <li><b>Tool dependency definition</b> - contents will always be restricted to one file named tool_dependencies.xml\n')
                __M_writer(u'                    </ul>\n                </div>\n')
        __M_writer(u'        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_passed_test(context,passed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( passed_test.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rpt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        __M_writer(filters.html_escape(unicode(passed_test.test_id )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_items(context,metadata,containers_dict,can_set_metadata=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_table_wrap_style(table_id):
            return render_render_table_wrap_style(context,table_id)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.encoding_util import tool_shed_encode
        
        has_datatypes = metadata and 'datatypes' in metadata
        has_readme_files = metadata and 'readme_files' in metadata
        has_workflows = metadata and 'workflows' in metadata
        
        datatypes_root_folder = containers_dict.get( 'datatypes', None )
        invalid_data_managers_root_folder = containers_dict.get( 'invalid_data_managers', None )
        invalid_repository_dependencies_root_folder = containers_dict.get( 'invalid_repository_dependencies', None )
        invalid_tool_dependencies_root_folder = containers_dict.get( 'invalid_tool_dependencies', None )
        invalid_tools_root_folder = containers_dict.get( 'invalid_tools', None )
        missing_repository_dependencies_root_folder = containers_dict.get( 'missing_repository_dependencies', None )
        missing_tool_dependencies_root_folder = containers_dict.get( 'missing_tool_dependencies', None )
        readme_files_root_folder = containers_dict.get( 'readme_files', None )
        repository_dependencies_root_folder = containers_dict.get( 'repository_dependencies', None )
        test_environment_root_folder = containers_dict.get( 'test_environment', None )
        tool_dependencies_root_folder = containers_dict.get( 'tool_dependencies', None )
        tool_test_results_root_folder = containers_dict.get( 'tool_test_results', None )
        valid_data_managers_root_folder = containers_dict.get( 'valid_data_managers', None )
        valid_tools_root_folder = containers_dict.get( 'valid_tools', None )
        workflows_root_folder = containers_dict.get( 'workflows', None )
        
        has_contents = datatypes_root_folder or invalid_tools_root_folder or valid_tools_root_folder or workflows_root_folder
        has_dependencies = \
            invalid_repository_dependencies_root_folder or \
            invalid_tool_dependencies_root_folder or \
            missing_repository_dependencies_root_folder or \
            repository_dependencies_root_folder or \
            tool_dependencies_root_folder or \
            missing_tool_dependencies_root_folder
        
        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
            
        
        __M_writer(u'\n')
        if readme_files_root_folder:
            __M_writer(u'        ')
            __M_writer(unicode(render_table_wrap_style( "readme_files" )))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Repository README files - may contain important installation or license information</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="readme_files">\n                    ')
            __M_writer(unicode(render_folder( readme_files_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
        if has_dependencies:
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Dependencies of this repository</div>\n            <div class="toolFormBody">\n')
            if invalid_repository_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_repository_dependencies">\n                        ')
                __M_writer(unicode(render_folder( invalid_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if missing_repository_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_repository_dependencies">\n                        ')
                __M_writer(unicode(render_folder( missing_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if repository_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="repository_dependencies">\n                        ')
                __M_writer(unicode(render_folder( repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if invalid_tool_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tool_dependencies">\n                        ')
                __M_writer(unicode(render_folder( invalid_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if tool_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="tool_dependencies">\n                        ')
                __M_writer(unicode(render_folder( tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if missing_tool_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_tool_dependencies">\n                        ')
                __M_writer(unicode(render_folder( missing_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            __M_writer(u'            </div>\n        </div>\n')
        if has_contents:
            __M_writer(u'        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Contents of this repository</div>\n            <div class="toolFormBody">\n')
            if valid_tools_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_tools">\n                        ')
                __M_writer(unicode(render_folder( valid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if invalid_tools_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tools">\n                        ')
                __M_writer(unicode(render_folder( invalid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if valid_data_managers_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_data_managers">\n                        ')
                __M_writer(unicode(render_folder( valid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if invalid_data_managers_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_data_managers">\n                        ')
                __M_writer(unicode(render_folder( invalid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if workflows_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="workflows">\n                        ')
                __M_writer(unicode(render_folder( workflows_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if datatypes_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="datatypes">\n                        ')
                __M_writer(unicode(render_folder( datatypes_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            __M_writer(u'            </div>\n        </div>\n')
        if tool_test_results_root_folder and trans.app.config.display_legacy_test_results:
            __M_writer(u'        ')
            __M_writer(unicode(render_table_wrap_style( "test_environment" )))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Automated tool test results</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="test_environment">\n                    ')
            __M_writer(unicode(render_folder( tool_test_results_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-ridm-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.index )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.error )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_sharable_str(context,repository,changeset_revision=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.repository_util import generate_sharable_link_for_repository_in_tool_shed
        sharable_link = generate_sharable_link_for_repository_in_tool_shed( repository, changeset_revision=changeset_revision )
            
        
        __M_writer(u'\n    <a href="')
        __M_writer(unicode( sharable_link ))
        __M_writer(u'" target="_blank">')
        __M_writer(unicode( sharable_link ))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_table_wrap_style(context,table_id):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <style type="text/css">\n        table.')
        __M_writer(unicode(table_id))
        __M_writer(u'{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px;\n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n        ul{ list-style-type: disc;\n            padding-left: 20px; }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( invalid_tool_dependency.id )
            
        
        __M_writer(u'\n    <style type="text/css">\n        #invalid_td_table{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px;\n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n    </style>\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-ritd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="invalid_td_table">\n                <tr><td>')
        __M_writer(filters.html_escape(unicode( invalid_tool_dependency.error )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "21": 71, "22": 175, "23": 218, "24": 226, "25": 231, "26": 385, "27": 409, "28": 435, "29": 457, "30": 476, "31": 499, "32": 530, "33": 554, "34": 573, "35": 645, "36": 660, "37": 691, "38": 721, "39": 755, "40": 786, "41": 807, "42": 830, "43": 879, "44": 935, "45": 962, "46": 985, "47": 1027, "48": 1059, "49": 1085, "50": 1098, "51": 1268, "57": 1029, "62": 1029, "63": 1030, "64": 1030, "65": 1031, "66": 1031, "67": 1032, "68": 1033, "69": 1034, "70": 1034, "71": 1034, "72": 1035, "73": 1036, "74": 1036, "75": 1036, "76": 1038, "77": 1038, "78": 1038, "79": 1040, "80": 1041, "81": 1042, "82": 1042, "83": 1043, "84": 1044, "85": 1046, "86": 1047, "87": 1048, "88": 1049, "89": 1049, "90": 1049, "91": 1049, "92": 1051, "93": 1052, "94": 1053, "95": 1053, "96": 1054, "97": 1055, "98": 1055, "99": 1055, "100": 1057, "106": 693, "111": 693, "112": 694, "116": 696, "117": 698, "118": 699, "119": 699, "120": 699, "121": 701, "122": 701, "123": 701, "124": 702, "125": 702, "126": 708, "127": 708, "128": 709, "129": 709, "130": 710, "131": 710, "132": 713, "133": 713, "134": 717, "139": 720, "145": 881, "151": 881, "152": 882, "162": 890, "163": 892, "164": 893, "165": 893, "166": 893, "167": 895, "168": 895, "169": 895, "170": 896, "171": 896, "172": 896, "173": 896, "174": 897, "175": 898, "176": 898, "177": 898, "178": 899, "179": 900, "180": 901, "181": 901, "182": 901, "183": 902, "184": 902, "185": 904, "186": 905, "187": 905, "188": 905, "189": 906, "190": 906, "191": 908, "192": 909, "193": 909, "194": 909, "195": 911, "196": 912, "197": 912, "198": 912, "199": 914, "200": 914, "201": 914, "202": 915, "203": 915, "204": 916, "211": 921, "212": 922, "213": 922, "214": 923, "215": 923, "216": 924, "217": 924, "218": 924, "219": 924, "220": 924, "221": 924, "222": 925, "223": 925, "224": 926, "225": 927, "226": 927, "227": 927, "228": 929, "229": 929, "230": 929, "231": 931, "236": 934, "242": 788, "247": 788, "248": 789, "252": 791, "253": 793, "254": 794, "255": 794, "256": 794, "257": 796, "258": 796, "259": 796, "260": 797, "261": 797, "262": 799, "263": 799, "264": 803, "269": 806, "275": 532, "280": 532, "281": 533, "285": 535, "286": 537, "287": 538, "288": 538, "289": 538, "290": 540, "291": 540, "292": 540, "293": 541, "294": 541, "295": 543, "296": 543, "297": 544, "298": 544, "299": 545, "300": 545, "301": 546, "302": 546, "303": 550, "308": 553, "314": 233, "348": 233, "349": 234, "363": 246, "364": 247, "365": 248, "366": 248, "373": 253, "374": 254, "375": 254, "376": 254, "377": 254, "378": 255, "379": 256, "380": 256, "381": 256, "382": 259, "383": 260, "436": 311, "437": 312, "438": 312, "439": 312, "440": 312, "441": 313, "442": 313, "443": 314, "444": 314, "445": 315, "446": 315, "447": 316, "448": 316, "449": 322, "454": 325, "455": 327, "456": 328, "457": 328, "458": 328, "459": 330, "460": 331, "461": 331, "462": 331, "463": 333, "464": 334, "465": 334, "466": 334, "467": 336, "468": 337, "469": 337, "471": 337, "472": 338, "473": 338, "474": 340, "475": 341, "476": 341, "477": 341, "478": 343, "479": 344, "480": 344, "482": 344, "483": 345, "484": 345, "485": 347, "486": 348, "487": 349, "488": 349, "490": 349, "491": 350, "492": 350, "493": 353, "494": 354, "495": 354, "496": 354, "497": 356, "498": 357, "499": 358, "500": 358, "502": 358, "503": 359, "504": 359, "505": 362, "506": 363, "507": 364, "508": 364, "510": 364, "511": 365, "512": 365, "513": 368, "514": 369, "515": 370, "516": 370, "518": 370, "519": 371, "520": 371, "521": 374, "522": 375, "523": 376, "524": 376, "526": 376, "527": 377, "528": 377, "529": 380, "530": 381, "531": 382, "532": 382, "533": 382, "539": 832, "545": 832, "546": 833, "554": 839, "555": 841, "556": 842, "557": 842, "558": 842, "559": 844, "560": 844, "561": 844, "562": 845, "563": 846, "564": 846, "565": 846, "566": 846, "567": 846, "568": 847, "569": 848, "570": 848, "571": 848, "572": 849, "573": 850, "574": 851, "575": 851, "576": 851, "577": 852, "578": 852, "579": 852, "580": 852, "581": 854, "582": 854, "583": 855, "584": 855, "585": 857, "586": 858, "587": 859, "588": 859, "589": 859, "590": 859, "591": 859, "592": 860, "593": 861, "594": 861, "595": 861, "596": 863, "597": 864, "598": 864, "599": 864, "600": 866, "601": 867, "602": 867, "603": 867, "604": 869, "605": 871, "606": 871, "607": 871, "608": 871, "609": 871, "610": 871, "611": 871, "612": 872, "613": 872, "614": 872, "615": 872, "616": 872, "617": 872, "618": 874, "619": 875, "624": 878, "630": 1087, "636": 1087, "637": 1088, "638": 1089, "639": 1093, "640": 1093, "646": 228, "651": 228, "656": 231, "657": 231, "663": 937, "668": 937, "669": 938, "671": 938, "672": 940, "673": 941, "674": 941, "675": 941, "676": 943, "677": 943, "678": 943, "679": 944, "680": 944, "681": 946, "682": 946, "683": 947, "684": 947, "685": 948, "686": 948, "687": 949, "688": 949, "689": 950, "690": 950, "691": 951, "692": 951, "693": 952, "694": 952, "695": 953, "696": 953, "697": 954, "698": 954, "699": 958, "704": 961, "710": 73, "717": 73, "718": 76, "719": 76, "720": 156, "721": 157, "722": 159, "723": 159, "724": 162, "725": 163, "726": 165, "727": 165, "728": 168, "734": 556, "739": 556, "740": 557, "742": 557, "743": 559, "744": 560, "745": 560, "746": 560, "747": 562, "748": 562, "749": 562, "750": 563, "751": 563, "752": 565, "753": 565, "754": 569, "759": 572, "765": 662, "770": 662, "771": 663, "776": 666, "777": 668, "778": 669, "779": 669, "780": 669, "781": 671, "782": 671, "783": 671, "784": 672, "785": 672, "786": 678, "787": 678, "788": 679, "789": 679, "790": 680, "791": 680, "792": 683, "793": 683, "794": 687, "799": 690, "805": 1061, "811": 1061, "812": 1069, "813": 1070, "814": 1073, "815": 1077, "816": 1078, "817": 1078, "818": 1078, "819": 1081, "825": 575, "832": 575, "833": 576, "865": 606, "866": 608, "867": 609, "868": 609, "869": 609, "870": 611, "871": 611, "872": 611, "873": 612, "874": 613, "875": 613, "876": 613, "877": 613, "878": 613, "879": 614, "880": 615, "881": 615, "882": 615, "883": 616, "884": 617, "885": 617, "886": 617, "887": 617, "888": 617, "889": 618, "890": 619, "891": 619, "892": 619, "893": 621, "894": 621, "895": 621, "896": 622, "897": 622, "898": 623, "899": 623, "900": 624, "901": 624, "902": 625, "903": 625, "904": 626, "905": 626, "906": 627, "907": 627, "908": 628, "909": 628, "910": 629, "911": 629, "912": 630, "913": 630, "914": 631, "915": 632, "916": 632, "917": 632, "918": 633, "919": 634, "920": 634, "921": 634, "922": 634, "923": 634, "924": 634, "925": 634, "926": 634, "927": 634, "928": 634, "929": 634, "930": 635, "931": 636, "932": 636, "933": 636, "934": 636, "935": 636, "936": 636, "937": 636, "938": 636, "939": 636, "940": 638, "941": 640, "942": 641, "947": 644, "953": 757, "958": 757, "959": 758, "963": 760, "964": 762, "965": 763, "966": 763, "967": 763, "968": 765, "969": 765, "970": 765, "971": 766, "972": 766, "973": 768, "974": 769, "975": 773, "976": 773, "977": 774, "978": 774, "979": 775, "980": 775, "981": 776, "982": 776, "983": 779, "984": 782, "989": 785, "995": 387, "1000": 387, "1001": 388, "1009": 394, "1010": 396, "1011": 397, "1012": 397, "1013": 397, "1014": 399, "1015": 399, "1016": 399, "1017": 400, "1018": 400, "1019": 400, "1020": 400, "1021": 400, "1022": 400, "1023": 400, "1024": 400, "1025": 401, "1026": 401, "1027": 401, "1028": 401, "1029": 401, "1030": 401, "1031": 402, "1032": 402, "1033": 402, "1034": 402, "1035": 402, "1036": 402, "1037": 403, "1038": 403, "1039": 403, "1040": 403, "1041": 403, "1042": 403, "1043": 405, "1048": 408, "1054": 411, "1059": 411, "1060": 412, "1065": 415, "1066": 417, "1067": 418, "1068": 418, "1069": 418, "1070": 420, "1071": 420, "1072": 420, "1073": 421, "1074": 421, "1075": 423, "1076": 423, "1077": 424, "1078": 424, "1079": 425, "1080": 425, "1081": 426, "1082": 426, "1083": 427, "1084": 427, "1085": 431, "1090": 434, "1096": 1, "1102": 1, "1103": 7, "1104": 7, "1105": 18, "1106": 18, "1107": 20, "1108": 20, "1109": 20, "1110": 20, "1111": 24, "1112": 24, "1113": 26, "1114": 26, "1115": 49, "1116": 49, "1117": 57, "1118": 57, "1119": 59, "1120": 59, "1126": 964, "1131": 964, "1132": 965, "1140": 971, "1141": 973, "1142": 974, "1143": 974, "1144": 974, "1145": 976, "1146": 976, "1147": 976, "1148": 977, "1149": 977, "1150": 977, "1151": 977, "1152": 977, "1153": 977, "1154": 977, "1155": 977, "1156": 978, "1157": 978, "1158": 978, "1159": 978, "1160": 978, "1161": 978, "1162": 979, "1163": 979, "1164": 979, "1165": 979, "1166": 979, "1167": 979, "1168": 981, "1173": 984, "1179": 723, "1184": 723, "1185": 724, "1190": 727, "1191": 729, "1192": 730, "1193": 730, "1194": 730, "1195": 732, "1196": 732, "1197": 732, "1198": 733, "1199": 733, "1200": 735, "1201": 736, "1202": 740, "1203": 740, "1204": 741, "1205": 741, "1206": 742, "1207": 742, "1208": 743, "1209": 743, "1210": 746, "1211": 747, "1212": 747, "1213": 751, "1218": 754, "1224": 459, "1229": 459, "1230": 460, "1234": 462, "1235": 464, "1236": 465, "1237": 465, "1238": 465, "1239": 467, "1240": 467, "1241": 467, "1242": 468, "1243": 468, "1244": 469, "1245": 469, "1246": 472, "1251": 475, "1257": 478, "1263": 478, "1264": 479, "1266": 479, "1267": 481, "1268": 482, "1269": 482, "1270": 482, "1271": 484, "1272": 484, "1273": 484, "1274": 485, "1275": 485, "1276": 486, "1277": 487, "1278": 487, "1279": 487, "1280": 488, "1281": 488, "1282": 490, "1283": 491, "1284": 491, "1285": 491, "1286": 493, "1287": 495, "1292": 498, "1298": 987, "1304": 987, "1305": 988, "1321": 1002, "1322": 1004, "1323": 1005, "1324": 1005, "1325": 1005, "1326": 1007, "1327": 1007, "1328": 1007, "1329": 1008, "1330": 1008, "1331": 1008, "1332": 1008, "1333": 1009, "1334": 1010, "1335": 1010, "1336": 1010, "1337": 1011, "1338": 1012, "1339": 1012, "1340": 1012, "1341": 1012, "1342": 1012, "1343": 1013, "1344": 1014, "1345": 1014, "1346": 1014, "1347": 1014, "1348": 1014, "1349": 1015, "1350": 1016, "1351": 1016, "1352": 1016, "1353": 1018, "1354": 1018, "1355": 1018, "1356": 1019, "1357": 1019, "1358": 1019, "1359": 1019, "1360": 1019, "1361": 1019, "1362": 1020, "1363": 1020, "1364": 1020, "1365": 1020, "1366": 1020, "1367": 1020, "1368": 1021, "1369": 1021, "1370": 1021, "1371": 1021, "1372": 1021, "1373": 1021, "1374": 1023, "1379": 1026, "1385": 177, "1390": 177, "1391": 180, "1402": 189, "1403": 190, "1404": 191, "1405": 191, "1406": 191, "1407": 192, "1408": 193, "1409": 197, "1410": 198, "1411": 198, "1412": 198, "1413": 199, "1414": 200, "1415": 203, "1416": 204, "1417": 206, "1418": 207, "1419": 209, "1420": 210, "1421": 212, "1422": 216, "1428": 809, "1433": 809, "1434": 810, "1438": 812, "1439": 814, "1440": 815, "1441": 815, "1442": 815, "1443": 817, "1444": 817, "1445": 817, "1446": 818, "1447": 818, "1448": 820, "1449": 820, "1450": 821, "1451": 821, "1452": 822, "1453": 822, "1454": 826, "1459": 829, "1465": 1100, "1474": 1100, "1475": 1101, "1516": 1140, "1517": 1141, "1518": 1142, "1519": 1142, "1520": 1142, "1521": 1148, "1523": 1148, "1524": 1150, "1525": 1150, "1526": 1155, "1527": 1156, "1528": 1159, "1529": 1160, "1530": 1161, "1532": 1161, "1533": 1163, "1534": 1163, "1535": 1166, "1536": 1167, "1537": 1168, "1539": 1168, "1540": 1170, "1541": 1170, "1542": 1173, "1543": 1174, "1544": 1175, "1546": 1175, "1547": 1177, "1548": 1177, "1549": 1180, "1550": 1181, "1551": 1182, "1553": 1182, "1554": 1184, "1555": 1184, "1556": 1187, "1557": 1188, "1558": 1189, "1560": 1189, "1561": 1191, "1562": 1191, "1563": 1194, "1564": 1195, "1565": 1196, "1567": 1196, "1568": 1198, "1569": 1198, "1570": 1201, "1571": 1204, "1572": 1205, "1573": 1209, "1574": 1210, "1575": 1211, "1577": 1211, "1578": 1213, "1579": 1213, "1580": 1216, "1581": 1217, "1582": 1218, "1584": 1218, "1585": 1220, "1586": 1220, "1587": 1223, "1588": 1224, "1589": 1225, "1591": 1225, "1592": 1227, "1593": 1227, "1594": 1230, "1595": 1231, "1596": 1232, "1598": 1232, "1599": 1234, "1600": 1234, "1601": 1237, "1602": 1238, "1603": 1239, "1605": 1239, "1606": 1241, "1607": 1241, "1608": 1244, "1609": 1245, "1610": 1246, "1612": 1246, "1613": 1248, "1614": 1248, "1615": 1251, "1616": 1254, "1617": 1255, "1618": 1255, "1619": 1255, "1620": 1261, "1622": 1261, "1623": 1263, "1624": 1263, "1630": 437, "1635": 437, "1636": 438, "1644": 444, "1645": 446, "1646": 447, "1647": 447, "1648": 447, "1649": 449, "1650": 449, "1651": 449, "1652": 450, "1653": 450, "1654": 450, "1655": 450, "1656": 450, "1657": 450, "1658": 450, "1659": 450, "1660": 451, "1661": 451, "1662": 451, "1663": 451, "1664": 451, "1665": 451, "1666": 453, "1671": 456, "1677": 220, "1681": 220, "1682": 221, "1687": 224, "1688": 225, "1689": 225, "1690": 225, "1691": 225, "1697": 647, "1701": 647, "1702": 649, "1703": 649, "1709": 501, "1714": 501, "1715": 502, "1719": 504, "1720": 516, "1721": 517, "1722": 517, "1723": 517, "1724": 519, "1725": 519, "1726": 519, "1727": 520, "1728": 520, "1729": 522, "1730": 522, "1731": 526, "1736": 529, "1742": 1736}, "uri": "/webapps/tool_shed/repository/common.mako", "filename": "templates/webapps/tool_shed/repository/common.mako"}
__M_END_METADATA
"""
