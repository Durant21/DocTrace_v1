from pyramid.view import view_config


@view_config(route_name='home', renderer="templates/mytemplate.jinja2")
def my_view(request):
    return {'project': 'DocTrace'}

# @view_config(route_name='home', renderer="templates/mytemplate.pt")
# def my_view(request):
#     return {'project': 'iMii_v9'}


@view_config(route_name='main', renderer='templates/main_template.jinja2')
def main_view1(request):
    return {'project': 'DocTrace'}
