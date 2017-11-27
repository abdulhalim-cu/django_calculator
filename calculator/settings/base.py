DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
	    'NAME': get_env_variable('django_calc'),
	    'USER': get_env_variable('djangoadmin'),
	    'PASSWORD': get_env_variable('mysqladmin'),
	    'HOST': '',
	    'PORT': '',
    }
}