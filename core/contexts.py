# context for all templates

NAV_LINKS = [{"name": "Home", "path": "/"}, {"name": "About", "path": "/about/"}]


def shared_context(request):
    return {"navbar_links": NAV_LINKS}
