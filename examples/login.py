
""" This is an example of the information needed in the src/login.py file """
def get_user() -> str:
	return "<USER EMAIL>"

def get_passwd() -> str:
	return "<USER PASSWORD>"

def get_cookies() -> dict(str, str):
	return "<DICT OF COOKIES>"

"""
COOKIES EXAMPLE
	"datr":<STRING>,
	"sb":<STRING>",
	"dpr":<STRING>,
	"locale":<STRING>,
	"c_user":<STRING>,
	"xs":<STRING>,
	"oo":<STRING>,
	"presence":<STRING>,
	"fr":<STRING>,
	"m_page_voice":<STRING>,
	"m_pixel_ratio":<STRING>,
	"wd":<STRING>


"""
def get_thread() -> int:
	return 123123123123123 # The thread id -> in the group-chat url

