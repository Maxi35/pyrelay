
VERSION = "https://static.drips.pw/rotmg/production/current/version.txt"
EQUIP = "https://static.drips.pw/rotmg/production/current/xml/Equip.xml"
VERIFY = "https://www.realmofthemadgod.com/account/verify"
VERIFYTOKEN = "https://www.realmofthemadgod.com/account/verifyAccessTokenClient?clientToken={}&accessToken={}&game_net=Unity&play_platform=Unity&game_net_user_id"
CHAR = "https://www.realmofthemadgod.com/char/list?do_login=true&accessToken={}&game_net=Unity&play_platform=Unity&game_net_user_id="

exaltHeaders = {
    "User-agent": "UnityPlayer/2019.4.9f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
    "X-Unity-Version": "2019.4.9f1"
    }

exaltVerifyData = {
    'game_net': 'Unity',
    'play_platform': 'Unity',
    'game_net_user_id': '',
    'guid': {},
    'password': {},
    'clientToken': {}
}
