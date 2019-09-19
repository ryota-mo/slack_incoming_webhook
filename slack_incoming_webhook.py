import requests, json

WEB_HOOK_URL = "get Webhook URL from Incoming WebHooks in apps/manage/custom-integrations"
requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': 'message',  # requirement
    'username': 'test',  # option
    # 'icon_emoji': ':smile_cat:',  # option
    # 'channel': '',  # option
    'link_names': 1,  # make name link, option
}))
