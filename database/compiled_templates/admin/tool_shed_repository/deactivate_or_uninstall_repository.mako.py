# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500964096.078382
_enable_loop = True
_template_filename = 'templates/admin/tool_shed_repository/deactivate_or_uninstall_repository.mako'
_template_uri = '/admin/tool_shed_repository/deactivate_or_uninstall_repository.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0xbe73a90', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0xbe73a90')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7faba0162910', context._clean_inheritance_tokens(), templateuri=u'/admin/tool_shed_repository/repository_actions_menu.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7faba0162910')] = ns

    ns = runtime.TemplateNamespace('__anon_0xbe73210', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0xbe73210')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xbe73a90')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7faba0162910')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0xbe73210')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        map = _import_ns.get('map', context.get('map', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        list = _import_ns.get('list', context.get('list', UNDEFINED))
        render_galaxy_repository_actions = _import_ns.get('render_galaxy_repository_actions', context.get('render_galaxy_repository_actions', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        remove_from_disk_check_box = _import_ns.get('remove_from_disk_check_box', context.get('remove_from_disk_check_box', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        repository = context.get( 'repository', None )
        if isinstance( repository, list ):
            repositories = repository
        else:
            repositories = [ repository ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['repositories','repository'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if len( repositories ) == 1:
            __M_writer(u'    ')
            __M_writer(unicode(render_galaxy_repository_actions( repositories[0] )))
            __M_writer(u'\n')
        __M_writer(u'\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n<div class="toolForm">\n<form name="deactivate_or_uninstall_repository" id="deactivate_or_uninstall_repository" action="')
        __M_writer(unicode( h.url_for( controller='admin_toolshed', action='deactivate_or_uninstall_repository' ) ))
        __M_writer(u'" method="post" >\n')
        for repository in repositories:
            __M_writer(u'    <input type="hidden" name="id" value="')
            __M_writer(filters.html_escape(unicode( trans.security.encode_id( repository.id ) )))
            __M_writer(u'" />\n    <div class="toolFormTitle">')
            __M_writer(filters.html_escape(unicode(repository.name)))
            __M_writer(u'</div>\n    <div class="toolFormBody">\n            <div class="form-row">\n                <label>Description:</label>\n                ')
            __M_writer(filters.html_escape(unicode(repository.description)))
            __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Revision:</label>\n                ')
            __M_writer(filters.html_escape(unicode(repository.changeset_revision)))
            __M_writer(u'</a>\n            </div>\n            <div class="form-row">\n                <label>Tool shed:</label>\n                ')
            __M_writer(filters.html_escape(unicode(repository.tool_shed)))
            __M_writer(u'\n                <div style="clear: both"></div>\n            </div>\n            <div class="form-row">\n                <label>Owner:</label>\n                ')
            __M_writer(filters.html_escape(unicode(repository.owner)))
            __M_writer(u'\n            </div>\n            <div class="form-row">\n                <label>Deleted:</label>\n                ')
            __M_writer(filters.html_escape(unicode(repository.deleted)))
            __M_writer(u'\n            </div>\n            <div class="form-row">\n                ')

            can_deactivate_repository = repository.can_deactivate
            can_uninstall_repository = repository.can_uninstall
                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_uninstall_repository','can_deactivate_repository'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if can_deactivate_repository:
                __M_writer(u'                    <table width="100%" border="0" cellpadding="0" cellspacing="0">\n                        <tr>\n                            <td bgcolor="#D8D8D8">\n                                <label>Deactivating this repository will result in the following:</label>\n                            </td>\n                        </tr>\n                    </table>\n                    <div class="toolParamHelp" style="clear: both;">\n                            * The repository and all of its contents will remain on disk and can still be used by dependent items.\n                    </div>\n')
                if repository.includes_tools_for_display_in_tool_panel:
                    __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s tools will not be loaded into the tool panel.\n                        </div>\n')
                if repository.includes_tool_dependencies:
                    __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s installed tool dependencies will remain on disk.\n                        </div>\n')
                if repository.includes_datatypes:
                    __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s datatypes, datatype converters and display applications will be eliminated from the datatypes registry.\n                        </div>\n')
                __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository record\'s deleted column in the tool_shed_repository database table will be set to True.\n                    </div>\n                    <br/>\n')
            if can_uninstall_repository:
                __M_writer(u'                    <table width="100%" border="0" cellpadding="0" cellspacing="0">\n                        <tr>\n                            <td bgcolor="#D8D8D8">\n                                <label>Uninstalling this repository will result in the following:</label>\n                            </td>\n                        </tr>\n                    </table>\n                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository and all of its contents will be removed from disk and can no longer be used by dependent items.\n                    </div>\n')
                if repository.includes_tools_for_display_in_tool_panel:
                    __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s tool tag sets will be removed from the tool config file in which they are defined.\n                        </div>\n')
                if repository.includes_tool_dependencies:
                    __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s installed tool dependencies will be removed from disk and can no longer be used by dependent items.\n                        </div>\n                        <div class="toolParamHelp" style="clear: both;">\n                            * Each associated tool dependency record\'s status column in the tool_dependency database table will be set to \'Uninstalled\'.\n                        </div>\n')
                if repository.includes_datatypes:
                    __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                            * The repository\'s datatypes, datatype converters and display applications will be eliminated from the datatypes registry.\n                        </div>\n')
                __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository record\'s deleted column in the tool_shed_repository database table will be set to True.\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        * The repository record\'s uninstalled column in the tool_shed_repository database table will be set to True.\n                    </div>\n                    <div style="clear: both"></div>\n                    <br/>\n                    ')
                        
                irm = trans.app.installed_repository_manager
                repository_tup = irm.get_repository_tuple_for_installed_repository_manager( repository )
                
                # Get installed repositories that this repository requires.
                installed_dependent_repositories = []
                installed_runtime_dependent_tool_dependencies = []
                installed_dependent_repositories = irm.installed_dependent_repositories_of_installed_repositories.get( repository_tup, [] )
                
                # Get this repository's installed tool dependencies.
                installed_tool_dependencies = irm.installed_tool_dependencies_of_installed_repositories.get( repository_tup, [] )
                
                # Get installed runtime dependent tool dependencies of this repository's installed tool dependencies.
                installed_runtime_dependent_tool_dependencies = []
                for itd_tup in installed_tool_dependencies:
                    installed_dependent_td_tups = \
                                irm.installed_runtime_dependent_tool_dependencies_of_installed_tool_dependencies.get( itd_tup, [] )
                    if installed_dependent_td_tups:
                        installed_runtime_dependent_tool_dependencies.extend( installed_dependent_td_tups )
                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['itd_tup','installed_tool_dependencies','installed_runtime_dependent_tool_dependencies','installed_dependent_td_tups','repository_tup','irm','installed_dependent_repositories'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                if installed_dependent_repositories or installed_runtime_dependent_tool_dependencies:
                    __M_writer(u'                        <table width="100%" border="0" cellpadding="0" cellspacing="0">\n                            <tr>\n                                <td bgcolor="#D8D8D8">\n                                    <label>Uninstalling this repository will affect the following dependent items:</label>\n                                </td>\n                            </tr>\n                        </table>\n')
                    if installed_dependent_repositories:
                        __M_writer(u'                            <label>Dependent repositories:</label>\n                            <ul>\n')
                        for installed_dependent_repository_tup in installed_dependent_repositories:
                            __M_writer(u'                                ')

                            tool_shed, name, owner, installed_changeset_revision = installed_dependent_repository_tup
                                                            
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['owner','name','tool_shed','installed_changeset_revision'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n                                <li>Revision <b>')
                            __M_writer(filters.html_escape(unicode( installed_changeset_revision )))
                            __M_writer(u'</b> of repository <b>')
                            __M_writer(filters.html_escape(unicode(name )))
                            __M_writer(u'</b> owned by <b>')
                            __M_writer(filters.html_escape(unicode(owner )))
                            __M_writer(u'</b></li>\n')
                        __M_writer(u'                            </ul>\n')
                    if installed_runtime_dependent_tool_dependencies:
                        __M_writer(u"                            <label>Runtime dependent tool dependencies of this repository's tool dependencies:</label>\n                            <ul>\n")
                        for td_tup in installed_runtime_dependent_tool_dependencies:
                            __M_writer(u'                                    ')

                            tool_shed_repository_id, name, version, type = td_tup
                            containing_repository = irm.get_containing_repository_for_tool_dependency( td_tup )
                            repository_name = containing_repository.name
                            changeset_revision = containing_repository.changeset_revision
                            owner = containing_repository.owner
                                                                
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['repository_name','name','tool_shed_repository_id','containing_repository','version','owner','changeset_revision','type'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n                                    <li>\n                                        Version <b>')
                            __M_writer(filters.html_escape(unicode(version )))
                            __M_writer(u'</b> of ')
                            __M_writer(filters.html_escape(unicode(type )))
                            __M_writer(u' <b>')
                            __M_writer(filters.html_escape(unicode(name )))
                            __M_writer(u'</b> contained in revision \n                                        <b>')
                            __M_writer(filters.html_escape(unicode(changeset_revision )))
                            __M_writer(u'</b> of repository <b>')
                            __M_writer(filters.html_escape(unicode(repository_name )))
                            __M_writer(u'</b> owned by <b>')
                            __M_writer(filters.html_escape(unicode(owner )))
                            __M_writer(u'</b>\n                                    </li>\n')
                        __M_writer(u'                            </ul>\n')
                    __M_writer(u'                        <br/>\n')
            __M_writer(u'            </div>\n        </div>\n')
        __M_writer(u'            <div class="form-row">\n                ')

        can_deactivate_repository = True in map( lambda x: x.can_deactivate, repositories )
        can_uninstall_repository = True in map( lambda x: x.can_uninstall, repositories )
                        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['can_uninstall_repository','can_deactivate_repository'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if can_deactivate_repository and can_uninstall_repository:
            __M_writer(u'                    ')
            deactivate_uninstall_button_text = "Deactivate or Uninstall" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['deactivate_uninstall_button_text'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                    ')
            __M_writer(unicode(remove_from_disk_check_box.get_html()))
            __M_writer(u'\n                    <label for="remove_from_disk" style="display: inline;font-weight:normal;">Check to uninstall or leave blank to deactivate</label>\n                    <br/><br/>\n')
        elif can_deactivate_repository:
            __M_writer(u'                    ')
            deactivate_uninstall_button_text = "Deactivate" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['deactivate_uninstall_button_text'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        else:
            __M_writer(u'                    ')
            deactivate_uninstall_button_text = "Uninstall" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['deactivate_uninstall_button_text'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            __M_writer(u'                    <input type="hidden" name="remove_from_disk" value="true"/><input type="hidden" name="remove_from_disk" value="true"/>\n')
        __M_writer(u'                <input type="submit" name="deactivate_or_uninstall_repository_button" value="')
        __M_writer(filters.html_escape(unicode(deactivate_uninstall_button_text)))
        __M_writer(u'"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 3, "26": 4, "29": 2, "35": 0, "55": 1, "56": 2, "57": 3, "58": 4, "59": 6, "69": 12, "70": 14, "71": 15, "72": 15, "73": 15, "74": 17, "75": 18, "76": 19, "77": 19, "78": 19, "79": 21, "80": 23, "81": 23, "82": 24, "83": 25, "84": 25, "85": 25, "86": 26, "87": 26, "88": 30, "89": 30, "90": 35, "91": 35, "92": 39, "93": 39, "94": 44, "95": 44, "96": 48, "97": 48, "98": 51, "105": 54, "106": 55, "107": 56, "108": 66, "109": 67, "110": 71, "111": 72, "112": 76, "113": 77, "114": 81, "115": 86, "116": 87, "117": 97, "118": 98, "119": 102, "120": 103, "121": 110, "122": 111, "123": 115, "124": 123, "147": 142, "148": 143, "149": 144, "150": 151, "151": 152, "152": 154, "153": 155, "154": 155, "160": 157, "161": 158, "162": 158, "163": 158, "164": 158, "165": 158, "166": 158, "167": 160, "168": 162, "169": 163, "170": 165, "171": 166, "172": 166, "182": 172, "183": 174, "184": 174, "185": 174, "186": 174, "187": 174, "188": 174, "189": 175, "190": 175, "191": 175, "192": 175, "193": 175, "194": 175, "195": 178, "196": 180, "197": 183, "198": 186, "199": 187, "206": 190, "207": 191, "208": 192, "209": 192, "213": 192, "214": 193, "215": 193, "216": 196, "217": 197, "218": 197, "222": 197, "223": 198, "224": 199, "225": 199, "229": 199, "230": 201, "231": 203, "232": 203, "233": 203, "239": 233}, "uri": "/admin/tool_shed_repository/deactivate_or_uninstall_repository.mako", "filename": "templates/admin/tool_shed_repository/deactivate_or_uninstall_repository.mako"}
__M_END_METADATA
"""
