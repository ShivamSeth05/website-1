def setup_module(nav):
    nav['base'].items.append(nav.Item('Log in', 'auth.login', constraints=[nav.Item.REQUIRELOGOUT]))
    nav['base'].items.append(nav.Item('Log out', 'auth.logout', constraints=[nav.Item.REQUIRELOGIN]))
