{
	'description': 'Emote Collector curates emotes from any server and lets you use them without Nitro.',
	'prefixes': ['ec/'],

	'decay': {
		'enabled': False,  # whether to enable the deletion of old emotes
		'cutoff': {  # emotes older than 4 weeks old that were not used 3 times will be removed automatically
			'usage': 2,
			'time': datetime.timedelta(weeks=4),
		},
	},

	# your instance of the website code located at https://github.com/EmoteCollector/website
	# if this is left blank, the ec/list command will not advertise the online version of the list.
	'website': 'https://ec.emote.bot',

	# change this user agent if you change the code
	'user_agent': 'EmoteCollectorBot (https://github.com/EmoteBot/EmoteCollector)',

	'repo': 'https://github.com/EmoteBot/EmoteCollector',

	# related to your instance of https://github.com/EmoteCollector/website
	# if this dict is left empty, the API related commands will be disabled.
	'api': {
		'docs_url': 'https://ec.emote.bot/api/v0/docs',
	},

	# the contents of this file will be sent to the user when they run the "copyright" command
	# as provided by bot_bin
	'copyright_license_file': 'data/short-license.txt',

	'support_server': {  # a guild where users can get help using the bot
		'id': None,  # the ID of the guild itself
		# where should users be invited to when they need help? the bot must have Create Instant Invites permission
		# for this channel
		'invite_channel_id': None,  # if set to None, the ec/support command will be disabled
	},

	# a user ID of someone to send logs to
	# note: currently nothing is sent except a notification of the bot's guild count being a power of 2
	'send_logs_to': None,

	'ignore_bots': {
		'default': True,
		'overrides': {
			'guilds': frozenset({
				# put guild IDs in here for which you want to override the default behavior
			}),
			'channels': frozenset({
				# put channel IDs in here for which you want to override the default behavior
			}),
		}
	},

	# this is a dict mapping log channel IDs to settings for that channel
	# each settings dict looks like this:
	# {
	# 	'include_nsfw_emotes': True,  # optional, if not specified, it defaults to False
	# 	'actions': {  # a set of actions to log to this channel
	# 		# possible action strings:
	# 		'add',
	# 		'remove',
	# 		'force_remove',  # when an emote is removed by a moderator
	# 		'preserve',  # when an emote is preserved (excluded from the emote decay)
	# 		'unpreserve',  # when an emote is un-preserved (included in the emote decay)
	# 		'nsfw',  # when an emote is marked as NSFW
	# 		'sfw',  # when an emote is marked as SFW
	# 		'decay',  # when an emote is removed by the automatic emote decay
	# 	}
	# }
	# multiple channels can be configured. all of them will be used for logging.
	'logs': {
	},

	# User IDs of accounts that own the backend guilds. This is required for the bot to function.
	'backend_user_accounts': [
	],

	# postgresql connection info
	# any fields left None will use defaults or environment variables
	'database': {
		'user': None,
		'password': None,
		'database': None,
		'host': None,
		'port': None,
	},

	'tokens': {
		'discord': 'sek.rit.token',  # get this from https://discordapp.com/developers/applications/me
		'stats': {  # keep these set to None unless your bot is listed on any of these sites
			'bots.discord.pw': None,
			'discordbots.org': None,
			'botsfordiscord.com': None
		}
	},

	'success_or_failure_emojis': {False: '❌', True: '✅'},
}
