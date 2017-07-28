# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501213875.616172
_enable_loop = True
_template_filename = 'templates/user/login.mako'
_template_uri = '/user/login.mako'
_source_encoding = 'ascii'
_exports = ['body', 'init', 'render_openid_form', 'center_panel', 'render_login_form']



#This is a hack, we should restructure templates to avoid this.
def inherit(context):
    if context.get('trans').webapp.name == 'galaxy' and context.get( 'use_panels', True ):
        return '/webapps/galaxy/base_panels.mako'
    elif context.get('trans').webapp.name == 'tool_shed' and context.get( 'use_panels', True ):
        return '/webapps/tool_shed/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f29582d45d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f29582d45d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f29582d45d0')._populate(_import_ns, [u'render_msg'])
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


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f29582d45d0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        redirect = _import_ns.get('redirect', context.get('redirect', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        redirect_url = _import_ns.get('redirect_url', context.get('redirect_url', UNDEFINED))
        def render_openid_form(redirect,auto_associate,openid_providers):
            return render_render_openid_form(context,redirect,auto_associate,openid_providers)
        def render_login_form(form_action=None):
            return render_render_login_form(context,form_action)
        openid_providers = _import_ns.get('openid_providers', context.get('openid_providers', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if redirect_url:
            __M_writer(u'        <script type="text/javascript">  \n            top.location.href = \'')
            __M_writer(filters.html_escape(unicode(redirect_url )))
            __M_writer(u"';\n        </script>\n")
        __M_writer(u'\n')
        if context.get('use_panels'):
            __M_writer(u'        <div style="margin: 1em;">\n')
        else:
            __M_writer(u'        <div>\n')
        __M_writer(u'\n')
        if message:
            __M_writer(u'        ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n')
        if not trans.user:
            __M_writer(u'\n        ')
            __M_writer(unicode(render_login_form()))
            __M_writer(u'\n\n')
            if trans.app.config.enable_openid:
                __M_writer(u'            <br/>\n            ')
                __M_writer(unicode(render_openid_form( redirect, False, openid_providers )))
                __M_writer(u'\n')
            __M_writer(u'\n')
            if trans.app.config.get( 'terms_url', None ) is not None:
                __M_writer(u'            <br/>\n            <p>\n                <a href="')
                __M_writer(unicode(trans.app.config.get('terms_url', None)))
                __M_writer(u'">Terms and Conditions for use of this service</a>\n            </p>\n')
            __M_writer(u'\n')
        __M_writer(u'\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f29582d45d0')._populate(_import_ns, [u'render_msg'])
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


def render_render_openid_form(context,redirect,auto_associate,openid_providers):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f29582d45d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="toolForm">\n        <div class="toolFormTitle">OpenID Login</div>\n        <form name="openid" id="openid" action="')
        __M_writer(unicode(h.url_for( controller='user', action='openid_auth' )))
        __M_writer(u'" method="post" target="_parent" >\n            <div class="form-row">\n                <label>OpenID URL:</label>\n                <input type="text" name="openid_url" size="60" style="background-image:url(\'')
        __M_writer(unicode(h.url_for( '/static/images/openid-16x16.gif' )))
        __M_writer(u'\' ); background-repeat: no-repeat; padding-right: 20px; background-position: 99% 50%;"/>\n                <input type="hidden" name="redirect" value="')
        __M_writer(filters.html_escape(unicode(redirect )))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                Or, authenticate with your <select name="openid_provider">\n')
        for provider in openid_providers:
            __M_writer(u'                    <option value="')
            __M_writer(unicode(provider.id))
            __M_writer(u'">')
            __M_writer(unicode(provider.name))
            __M_writer(u'</option>\n')
        __M_writer(u'                </select> account.\n            </div>\n            <div class="form-row">\n                <input type="submit" name="login_button" value="Login"/>\n            </div>\n        </form>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f29582d45d0')._populate(_import_ns, [u'render_msg'])
        def body():
            return render_body(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_login_form(context,form_action=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f29582d45d0')._populate(_import_ns, [u'render_msg'])
        redirect = _import_ns.get('redirect', context.get('redirect', UNDEFINED))
        header = _import_ns.get('header', context.get('header', UNDEFINED))
        login = _import_ns.get('login', context.get('login', UNDEFINED))
        use_panels = _import_ns.get('use_panels', context.get('use_panels', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')

        if form_action is None:
            form_action = h.url_for( controller='user', action='login', use_panels=use_panels )
            
        
        __M_writer(u'\n\n')
        if header:
            __M_writer(u'        ')
            __M_writer(unicode(header))
            __M_writer(u'\n')
        __M_writer(u'    <div class="toolForm">\n        <div class="toolFormTitle">Login</div>\n        <form name="login" id="login" action="')
        __M_writer(unicode(form_action))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Username / Email Address:</label>\n                <input type="text" name="login" value="')
        __M_writer(filters.html_escape(unicode(login or '')))
        __M_writer(u'" size="40"/>\n                <input type="hidden" name="redirect" value="')
        __M_writer(filters.html_escape(unicode(redirect )))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Password:</label>\n                <input type="password" name="password" value="" size="40"/>\n                <div class="toolParamHelp" style="clear: both;">\n                    <a href="')
        __M_writer(unicode(h.url_for( controller='user', action='reset_password', use_panels=use_panels )))
        __M_writer(u'">Forgot password? Reset here</a>\n                </div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="login_button" value="Login"/>\n            </div>\n        </form>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"129": 20, "213": 207, "135": 102, "142": 102, "143": 105, "16": 1, "145": 108, "146": 108, "144": 105, "148": 109, "149": 113, "150": 114, "151": 114, "152": 114, "153": 114, "154": 114, "155": 116, "161": 25, "34": 23, "207": 91, "177": 69, "40": 0, "169": 25, "170": 26, "171": 26, "47": 10, "48": 12, "49": 21, "50": 23, "51": 27, "52": 67, "53": 100, "54": 124, "60": 29, "189": 71, "194": 74, "195": 76, "196": 77, "197": 77, "198": 77, "199": 79, "200": 81, "201": 81, "202": 84, "203": 84, "204": 85, "77": 29, "78": 31, "79": 32, "80": 33, "81": 33, "82": 36, "83": 37, "84": 38, "85": 39, "86": 40, "87": 42, "88": 43, "89": 44, "90": 44, "91": 44, "92": 46, "93": 47, "94": 48, "95": 49, "96": 49, "97": 51, "98": 52, "99": 53, "100": 53, "101": 55, "102": 56, "103": 57, "104": 59, "105": 59, "106": 62, "107": 64, "113": 14, "147": 109, "205": 85, "121": 14, "122": 15, "206": 91, "188": 69}, "uri": "/user/login.mako", "filename": "templates/user/login.mako"}
__M_END_METADATA
"""
