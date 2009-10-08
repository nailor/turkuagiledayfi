def load_settings():
    import os
    del globals()['load_settings']

    path = os.environ.get('DJANGO_SETTINGS_FILE',
                          os.path.expanduser('~/.settings.py'))
    if not os.path.exists(path):
        raise RuntimeError('Django settings file %s not found' % path)

    execfile(path, globals())

load_settings()
