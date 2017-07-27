# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500952991.753891
_enable_loop = True
_template_filename = 'templates/admin/tool_shed_repository/repository_installation_status.mako'
_template_uri = 'admin/tool_shed_repository/repository_installation_status.mako'
_source_encoding = 'ascii'
_exports = ['render_repository_status']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def render_repository_status(repository):
            return render_render_repository_status(context._locals(__M_locals),repository)
        repository = context.get('repository', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(unicode(render_repository_status( repository )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_status(context,repository):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from markupsafe import escape
        if repository.status in [ trans.install_model.ToolShedRepository.installation_status.CLONING,
                                  trans.install_model.ToolShedRepository.installation_status.SETTING_TOOL_VERSIONS,
                                  trans.install_model.ToolShedRepository.installation_status.INSTALLING_TOOL_DEPENDENCIES,
                                  trans.install_model.ToolShedRepository.installation_status.LOADING_PROPRIETARY_DATATYPES ]:
            bgcolor = trans.install_model.ToolShedRepository.states.INSTALLING
        elif repository.status in [ trans.install_model.ToolShedRepository.installation_status.NEW,
                                    trans.install_model.ToolShedRepository.installation_status.UNINSTALLED ]:
            bgcolor = trans.install_model.ToolShedRepository.states.UNINSTALLED
        elif repository.status in [ trans.install_model.ToolShedRepository.installation_status.ERROR ]:
            bgcolor = trans.install_model.ToolShedRepository.states.ERROR
        elif repository.status in [ trans.install_model.ToolShedRepository.installation_status.DEACTIVATED ]:
            bgcolor = trans.install_model.ToolShedRepository.states.WARNING
        elif repository.status in [ trans.install_model.ToolShedRepository.installation_status.INSTALLED ]:
            if repository.missing_tool_dependencies or repository.missing_repository_dependencies:
                bgcolor = trans.install_model.ToolShedRepository.states.WARNING
            else:
                bgcolor = trans.install_model.ToolShedRepository.states.OK
        else:
            bgcolor = trans.install_model.ToolShedRepository.states.ERROR
        rval = '<div class="count-box state-color-%s" id="RepositoryStatus-%s">' % ( bgcolor, trans.security.encode_id( repository.id ) )
        rval += '%s</div>' % escape( repository.status )
        return rval
            
        
        __M_writer(u'    \n    ')
        __M_writer(unicode(rval))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 1, "64": 26, "66": 27, "37": 1, "38": 2, "65": 27, "72": 66, "16": 0, "24": 28, "25": 30, "26": 30}, "uri": "admin/tool_shed_repository/repository_installation_status.mako", "filename": "templates/admin/tool_shed_repository/repository_installation_status.mako"}
__M_END_METADATA
"""
