# oppia/local_settings.py

def modify(settings):
    
    settings['INSTALLED_APPS'] += ('oppia.quiz', 
                                   'oppia.viz',
                                   'oppia.preview',
                                   'oppia.av',
                                   'oppia.profile',
                                   'oppia.reports',
                                   'oppia.summary',
                                   'crispy_forms',
                                   'tastypie',)
    settings['MIDDLEWARE_CLASSES'] += ('oppia.middleware.LoginRequiredMiddleware',)

    context_processors = (
            'oppia.context_processors.get_points',
            'oppia.context_processors.get_version',
            'oppia.context_processors.get_settings',)

    if 'TEMPLATES' in settings and settings['TEMPLATES'][0]: #Django 1.8+ template settings
        settings['TEMPLATES'][0]['OPTIONS']['context_processors'] += context_processors
    elif 'TEMPLATE_CONTEXT_PROCESSORS' in settings: #Fallback for the old template settings
        settings['TEMPLATE_CONTEXT_PROCESSORS'] += context_processors

    settings['LOGIN_EXEMPT_URLS'] = (
         r'^server/$',
         r'^profile/login/$',
         r'^profile/register/',
         r'^profile/reset/',
         r'^profile/setlang/$',
         r'^mobile/scorecard/$',        # - auth handled by api_key
         r'^mobile/monitor/',           # - auth handled by api_key
         r'^$',
         r'^about/$',
         r'^terms/$',
         r'^api/',                      # allow any URL under api/* - auth handled by api_key
         r'^modules/api/',              # allow any URL under modules/api/* - auth handled by api_key
         r'^badges/api/',                # allow any URL under badges/api/* - auth handled by api_key

         r'^content/video-embed-helper/$',
         r'^media/temp/',
    )

    settings['CRISPY_TEMPLATE_PACK'] = 'bootstrap3'

    settings['OPPIA_POINTS'] = {
        'REGISTER':100,                             # given when user first registers
        'QUIZ_ATTEMPT_OWNER':5,                     # given to the quiz owner when another user attempts their quiz
        'QUIZ_FIRST_ATTEMPT':20,                    # for the first attempt at a quiz
        'QUIZ_ATTEMPT':10,                          # for any subsequent attempts at a quiz
        'QUIZ_FIRST_ATTEMPT_THRESHOLD':100,         # Threshold for getting bonus points for first attempt at quiz (must be 0-100)
        'QUIZ_FIRST_ATTEMPT_BONUS':50,              # Bonus points for getting over the threshold on first attempt at quiz
        'QUIZ_CREATED':200,                         # for creating a quiz
        'ACTIVITY_COMPLETED':10,                    # for completing an activity
        'MEDIA_STARTED':20,                         # for starting media
        'MEDIA_PLAYING_INTERVAL':30,                # interval in seconds for which points are given
        'MEDIA_PLAYING_POINTS_PER_INTERVAL':5,      # no points per interval media is playing
        'MEDIA_MAX_POINTS':200,                     # the maximum number of points available for any single media play
        'COURSE_DOWNLOADED':50,                     # for downloading a course
    }

    settings['OPPIA_METADATA'] = {
        'NETWORK':True, #
        'DEVICE_ID': True,
        'SIM_SERIAL': True,
        'WIFI_ON': True,
        'NETWORK_CONNECTED': True,
        'BATTERY_LEVEL': True,
        'GPS':False,
    }

    settings['OPPIA_ALLOW_SELF_REGISTRATION'] = True    # turns on/off ability for users to self register

    settings['OPPIA_SHOW_GRAVATARS'] = True

    settings['OPPIA_STAFF_ONLY_UPLOAD'] = True          # prevents anyone without is_staff status being able to upload courses,
                                                        # setting to False allows any registered user to upload a course

    settings['OPPIA_POINTS_ENABLED'] = True            # determines if the points system is enabled
    # if OPPIA POINTS_ENABLED is false, then the next 3 settings are ignored
    settings['OPPIA_STAFF_EARN_POINTS'] = False         # prevent staff from earning points
    settings['OPPIA_COURSE_OWNERS_EARN_POINTS'] = False # stops owners of courses earning points
    settings['OPPIA_TEACHERS_EARN_POINTS'] = False      # stops teachers of courses earning points

    settings['OPPIA_BADGES_ENABLED'] = True            # determines if the badges system is enabled

    settings['BADGE_AWARD_METHOD_ALL_ACTIVITIES'] = 'all activities'
    settings['BADGE_AWARD_METHOD_FINAL_QUIZ'] = 'final quiz'
    settings['BADGE_AWARD_METHOD_ALL_QUIZZES'] = 'all quizzes'

    settings['BADGE_AWARDING_METHOD'] = settings['BADGE_AWARD_METHOD_ALL_ACTIVITIES']

    settings['OPPIA_GOOGLE_ANALYTICS_ENABLED'] = True
    settings['OPPIA_GOOGLE_ANALYTICS_CODE'] = 'UA-3609005-11'
    settings['OPPIA_GOOGLE_ANALYTICS_DOMAIN'] = 'oppia-mobile.org'

    settings['OPPIA_MAX_UPLOAD_SIZE'] = 5242880         # max course file upload size - in bytes

    settings['OPPIA_MEDIA_FILE_TYPES'] = ("video/m4v","video/mp4","audio/mpeg","video/3gp","video/3gpp")
    settings['OPPIA_MEDIA_IMAGE_FILE_TYPES'] = ()
    
    settings['OPPIA_EXPORT_LOCAL_MINVERSION'] = 2017011400 # min version of the export block to process the quizzes locally

    settings['API_LIMIT_PER_PAGE'] = 0

    settings['DEVICE_ADMIN_ENABLED'] = True

    if settings['DEVICE_ADMIN_ENABLED']:
        settings['INSTALLED_APPS'] += ('oppia.deviceadmin', 'gcm',)
        settings['GCM_APIKEY'] = 'OPPIA_GOOGLEAPIKEY'
        settings['GCM_DEVICE_MODEL'] = 'oppia.deviceadmin.models.UserDevice'
