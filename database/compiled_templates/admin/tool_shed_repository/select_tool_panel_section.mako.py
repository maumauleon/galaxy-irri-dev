# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500952962.86718
_enable_loop = True
_template_filename = 'templates/admin/tool_shed_repository/select_tool_panel_section.mako'
_template_uri = '/admin/tool_shed_repository/select_tool_panel_section.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f81885b7c10', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f81885b7c10')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f81885b7090', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f81885b7090')] = ns

    ns = runtime.TemplateNamespace('__anon_0xbdf30d0', context._clean_inheritance_tokens(), templateuri=u'/webapps/tool_shed/repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0xbdf30d0')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f81885b7fd0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f81885b7fd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81885b7c10')._populate(_import_ns, [u'render_readme_section'])
        _mako_get_namespace(context, '__anon_0x7f81885b7090')._populate(_import_ns, [u'render_dependencies_section'])
        _mako_get_namespace(context, '__anon_0xbdf30d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f81885b7fd0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        encoded_updated_metadata = _import_ns.get('encoded_updated_metadata', context.get('encoded_updated_metadata', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        render_readme_section = _import_ns.get('render_readme_section', context.get('render_readme_section', UNDEFINED))
        install_repository_dependencies_check_box = _import_ns.get('install_repository_dependencies_check_box', context.get('install_repository_dependencies_check_box', UNDEFINED))
        shed_tool_conf = _import_ns.get('shed_tool_conf', context.get('shed_tool_conf', UNDEFINED))
        encoded_repo_info_dicts = _import_ns.get('encoded_repo_info_dicts', context.get('encoded_repo_info_dicts', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        includes_tool_dependencies = _import_ns.get('includes_tool_dependencies', context.get('includes_tool_dependencies', UNDEFINED))
        updating_repository_id = _import_ns.get('updating_repository_id', context.get('updating_repository_id', UNDEFINED))
        install_resolver_dependencies_check_box = _import_ns.get('install_resolver_dependencies_check_box', context.get('install_resolver_dependencies_check_box', UNDEFINED))
        render_tool_dependency_resolver = _import_ns.get('render_tool_dependency_resolver', context.get('render_tool_dependency_resolver', UNDEFINED))
        tool_shed_url = _import_ns.get('tool_shed_url', context.get('tool_shed_url', UNDEFINED))
        containers_dict = _import_ns.get('containers_dict', context.get('containers_dict', UNDEFINED))
        has_repository_dependencies = _import_ns.get('has_repository_dependencies', context.get('has_repository_dependencies', UNDEFINED))
        includes_tools_for_display_in_tool_panel = _import_ns.get('includes_tools_for_display_in_tool_panel', context.get('includes_tools_for_display_in_tool_panel', UNDEFINED))
        shed_tool_conf_select_field = _import_ns.get('shed_tool_conf_select_field', context.get('shed_tool_conf_select_field', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        updating_to_changeset_revision = _import_ns.get('updating_to_changeset_revision', context.get('updating_to_changeset_revision', UNDEFINED))
        tool_panel_section_select_field = _import_ns.get('tool_panel_section_select_field', context.get('tool_panel_section_select_field', UNDEFINED))
        includes_tools = _import_ns.get('includes_tools', context.get('includes_tools', UNDEFINED))
        requirements_status = _import_ns.get('requirements_status', context.get('requirements_status', UNDEFINED))
        install_tool_dependencies_check_box = _import_ns.get('install_tool_dependencies_check_box', context.get('install_tool_dependencies_check_box', UNDEFINED))
        updating = _import_ns.get('updating', context.get('updating', UNDEFINED))
        render_dependencies_section = _import_ns.get('render_dependencies_section', context.get('render_dependencies_section', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        new_tool_panel_section_label = _import_ns.get('new_tool_panel_section_label', context.get('new_tool_panel_section_label', UNDEFINED))
        updating_to_ctx_rev = _import_ns.get('updating_to_ctx_rev', context.get('updating_to_ctx_rev', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

    # Handle the case where an uninstalled repository encountered errors during the process of being reinstalled.  In
    # this case, the repository metadata is an empty dictionary, but one or both of has_repository_dependencies
    # and includes_tool_dependencies may be True.  If either of these are True but we have no metadata, we cannot install
    # repository dependencies on this pass.
        if has_repository_dependencies:
            repository_dependencies = containers_dict[ 'repository_dependencies' ]
            missing_repository_dependencies = containers_dict[ 'missing_repository_dependencies' ]
            if repository_dependencies or missing_repository_dependencies:
                can_display_repository_dependencies = True
            else:
                can_display_repository_dependencies = False
        else:
            can_display_repository_dependencies = False
        if includes_tool_dependencies:
            tool_dependencies = containers_dict[ 'tool_dependencies' ]
            missing_tool_dependencies = containers_dict[ 'missing_tool_dependencies' ]
            if tool_dependencies or missing_tool_dependencies:
                can_display_tool_dependencies = True
            else:
                can_display_tool_dependencies = False
        else:
            can_display_tool_dependencies = False
        can_display_resolver_installation = install_resolver_dependencies_check_box is not None
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_display_tool_dependencies','missing_tool_dependencies','missing_repository_dependencies','repository_dependencies','can_display_repository_dependencies','can_display_resolver_installation','tool_dependencies'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n<div class="warningmessage">\n    <p>\n        The Galaxy development team does not maintain the contents of many Galaxy Tool Shed repositories.  Some\n        repository tools may include code that produces malicious behavior, so be aware of what you are installing.\n    </p>\n    <p>\n        If you discover a repository that causes problems after installation, contact <a href="https://galaxyproject.org/support" target="_blank">Galaxy support</a>,\n        sending all necessary information, and appropriate action will be taken.\n    </p>\n    <p>\n        <a href="https://galaxyproject.org/toolshed/repository-features/#contact-repository-owner" target="_blank">Contact the repository owner</a> for\n        general questions or concerns.\n    </p>\n</div>\n<div class="toolForm">\n    <div class="toolFormBody">\n        <form name="select_tool_panel_section" id="select_tool_panel_section" action="')
        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='prepare_for_install' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <input type="hidden" name="includes_tools" value="')
        __M_writer(unicode(includes_tools))
        __M_writer(u'" />\n                <input type="hidden" name="includes_tool_dependencies" value="')
        __M_writer(unicode(includes_tool_dependencies))
        __M_writer(u'" />\n                <input type="hidden" name="requirements_status" value="')
        __M_writer(unicode(requirements_status))
        __M_writer(u'" />\n                <input type="hidden" name="includes_tools_for_display_in_tool_panel" value="')
        __M_writer(unicode(includes_tools_for_display_in_tool_panel))
        __M_writer(u'" />\n                <input type="hidden" name="tool_shed_url" value="')
        __M_writer(unicode(tool_shed_url))
        __M_writer(u'" />\n                <input type="hidden" name="encoded_repo_info_dicts" value="')
        __M_writer(unicode(encoded_repo_info_dicts))
        __M_writer(u'" />\n                <input type="hidden" name="updating" value="')
        __M_writer(unicode(updating))
        __M_writer(u'" />\n                <input type="hidden" name="updating_repository_id" value="')
        __M_writer(unicode(updating_repository_id))
        __M_writer(u'" />\n                <input type="hidden" name="updating_to_ctx_rev" value="')
        __M_writer(unicode(updating_to_ctx_rev))
        __M_writer(u'" />\n                <input type="hidden" name="updating_to_changeset_revision" value="')
        __M_writer(unicode(updating_to_changeset_revision))
        __M_writer(u'" />\n                <input type="hidden" name="encoded_updated_metadata" value="')
        __M_writer(unicode(encoded_updated_metadata))
        __M_writer(u'" />\n            </div>\n            <div style="clear: both"></div>\n            ')
        readme_files_dict = containers_dict.get( 'readme_files', None ) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['readme_files_dict'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if readme_files_dict:
            __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <th bgcolor="#EBD9B2">Repository README file - may contain important installation or license information</th>\n                    </table>\n                </div>\n                ')
            __M_writer(unicode(render_readme_section( containers_dict )))
            __M_writer(u'\n                <div style="clear: both"></div>\n')
        __M_writer(u'            ')

        if requirements_status and install_resolver_dependencies_check_box or includes_tool_dependencies:
            display_dependency_confirmation = True
        else:
            display_dependency_confirmation = False
                    
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['display_dependency_confirmation'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if requirements_status:
            if not install_resolver_dependencies_check_box and not includes_tool_dependencies:
                __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <head>\n                            <th>\n                                <img src="')
                __M_writer(unicode(h.url_for('/static')))
                __M_writer(u'/images/icon_error_sml.gif" title=\'Cannot install dependencies\'/>\n                                This repository requires dependencies that cannot be installed through the Tool Shed\n                            </th>\n                        </head>\n                    </table>\n                </div>\n                <div class="form-row">\n                     <p>This repository defines tool requirements that cannot be installed through the Tool Shed.</p>\n                     <p>Please activate Conda dependency resolution, activate Docker dependency resolution, setup Environment Modules\nor manually satisfy the dependencies listed below.</p>\n                     <p>For details see <a target="_blank" href="https://docs.galaxyproject.org/en/latest/admin/dependency_resolvers.html">the dependency resolver documentation.</a></p>\n                </div>\n')
            __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <th bgcolor="#EBD9B2">The following tool dependencies are required by the current repository</th>\n                    </table>\n                </div>\n                <div class="form-row">\n                    ')
            __M_writer(unicode(render_tool_dependency_resolver( requirements_status, prepare_for_install=True )))
            __M_writer(u'\n                </div>\n                <div style="clear: both"></div>\n')
        if can_display_repository_dependencies or display_dependency_confirmation:
            __M_writer(u'                <div class="form-row">\n                    <table class="colored" width="100%">\n                        <th bgcolor="#EBD9B2">Confirm dependency installation</th>\n                    </table>\n                </div>\n                ')
            __M_writer(unicode(render_dependencies_section( install_resolver_dependencies_check_box, install_repository_dependencies_check_box, install_tool_dependencies_check_box, containers_dict, revision_label=None, export=False, requirements_status=requirements_status )))
            __M_writer(u'\n                <div style="clear: both"></div>\n')
        if shed_tool_conf_select_field:
            if includes_tools_for_display_in_tool_panel:
                __M_writer(u'                    <div class="form-row">\n                        <table class="colored" width="100%">\n                            <th bgcolor="#EBD9B2">Choose the tool panel section to contain the installed tools (optional)</th>\n                        </table>\n                    </div>\n                <div class="detail-section">\n')
            __M_writer(u'                ')

            if len( shed_tool_conf_select_field.options ) == 1:
                select_help = "Your Galaxy instance is configured with 1 shed-related tool configuration file, so repositories will be "
                select_help += "installed using its <b>tool_path</b> setting."
            else:
                select_help = "Your Galaxy instance is configured with %d shed-related tool configuration files, " % len( shed_tool_conf_select_field.options )
                select_help += "so select the file whose <b>tool_path</b> setting you want used for installing repositories."
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['select_help'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                <div class="form-row">\n                    <label>Shed tool configuration file:</label>\n                    ')
            __M_writer(unicode(shed_tool_conf_select_field.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        ')
            __M_writer(filters.html_escape(unicode(select_help)))
            __M_writer(u'\n                    </div>\n                </div>\n                <div style="clear: both"></div>\n                </div>\n')
        else:
            __M_writer(u'                <input type="hidden" name="shed_tool_conf" value="')
            __M_writer(filters.html_escape(unicode(shed_tool_conf)))
            __M_writer(u'"/>\n')
        if includes_tools_for_display_in_tool_panel:
            __M_writer(u'                <div class="form-row">\n                    <label>Add new tool panel section:</label>\n                    <input name="new_tool_panel_section_label" type="textfield" value="')
            __M_writer(filters.html_escape(unicode(new_tool_panel_section_label)))
            __M_writer(u'" size="40"/>\n                    <div class="toolParamHelp" style="clear: both;">\n                        Add a new tool panel section to contain the installed tools (optional).\n                    </div>\n                </div>\n                <div class="form-row">\n                    <label>Select existing tool panel section:</label>\n                    ')
            __M_writer(unicode(tool_panel_section_select_field.get_html()))
            __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        Choose an existing section in your tool panel to contain the installed tools (optional).\n                    </div>\n                </div>\n')
        __M_writer(u'            <div class="form-row">\n                <input type="submit" name="select_tool_panel_section_button" value="Install"/>\n                <div class="toolParamHelp" style="clear: both;">\n')
        if includes_tools_for_display_in_tool_panel:
            __M_writer(u'                        Clicking <b>Install</b> without selecting a tool panel section will load the installed tools into the tool panel outside of any sections.\n')
        __M_writer(u'                </div>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81885b7c10')._populate(_import_ns, [u'render_readme_section'])
        _mako_get_namespace(context, '__anon_0x7f81885b7090')._populate(_import_ns, [u'render_dependencies_section'])
        _mako_get_namespace(context, '__anon_0xbdf30d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f81885b7fd0')._populate(_import_ns, [u'render_msg'])
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


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f81885b7c10')._populate(_import_ns, [u'render_readme_section'])
        _mako_get_namespace(context, '__anon_0x7f81885b7090')._populate(_import_ns, [u'render_dependencies_section'])
        _mako_get_namespace(context, '__anon_0xbdf30d0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f81885b7fd0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        container_javascripts = _import_ns.get('container_javascripts', context.get('container_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js("libs/jquery/jquery.rating", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        __M_writer(unicode(container_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 4, "26": 3, "29": 5, "32": 2, "38": 0, "76": 1, "77": 2, "78": 3, "79": 4, "80": 5, "81": 10, "82": 16, "83": 18, "111": 42, "112": 44, "113": 45, "114": 45, "115": 45, "116": 47, "117": 64, "118": 64, "119": 66, "120": 66, "121": 67, "122": 67, "123": 68, "124": 68, "125": 69, "126": 69, "127": 70, "128": 70, "129": 71, "130": 71, "131": 72, "132": 72, "133": 73, "134": 73, "135": 74, "136": 74, "137": 75, "138": 75, "139": 76, "140": 76, "141": 79, "145": 79, "146": 80, "147": 81, "148": 86, "149": 86, "150": 89, "151": 89, "160": 94, "161": 95, "162": 96, "163": 97, "164": 101, "165": 101, "166": 114, "167": 120, "168": 120, "169": 124, "170": 125, "171": 130, "172": 130, "173": 133, "174": 134, "175": 135, "176": 142, "177": 142, "188": 149, "189": 152, "190": 152, "191": 154, "192": 154, "193": 159, "194": 160, "195": 160, "196": 160, "197": 162, "198": 163, "199": 165, "200": 165, "201": 172, "202": 172, "203": 178, "204": 181, "205": 182, "206": 184, "212": 7, "223": 7, "224": 8, "225": 8, "226": 9, "227": 9, "233": 12, "245": 12, "246": 13, "247": 13, "248": 14, "249": 14, "250": 15, "251": 15, "257": 251}, "uri": "/admin/tool_shed_repository/select_tool_panel_section.mako", "filename": "templates/admin/tool_shed_repository/select_tool_panel_section.mako"}
__M_END_METADATA
"""
