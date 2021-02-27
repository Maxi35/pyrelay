# EXALT CLIENT HTTP HEADERS
EXALT_HEADERS(fromLauncher = False) {
    "User-Agent": "UnityPlayer/2019.4.9f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
    "X-Unity-Version": fromLauncher ? "2019.3.14f1" : "2019.4.9f1";
}

# RESOURCES
VERSION = "https://api.rotmg.network/exalt/buildVersion.txt";
EQUIP = "https://api.rotmg.network/exalt/xml/equip.xml";
PACKETS = "https://api.rotmg.network/exalt/packets.xml";

# ACCOUNT DATA
CHAR_LIST = "https://www.realmofthemadgod.com/char/list?do_login=true&guid={}&password={}&game_net=Unity&play_platform=Unity&game_net_user_id=";

# ANTIBOT BYPASS
VERIFY_ACCESS_TOKEN = "https://realmofthemadgod.com/account/verifyAccessTokenClient";
EXTEND_ACCESS_TOKEN = "https://realmofthemadgod.com/account/extendAccessToken";

# PLAYERDATA
GET_EXALTATION_DATA = "https://realmofthemadgod.com/app/publicStaticData";
GET_POWERUP_STATS = "https://realmofthemadgod.com/account/listPowerUpStats";
GET_OWNED_PET_SKINS = "https://realmofthemadgod.com/account/getOwnedPetSkins";
