import Networking.Packets.Outgoing as outgoing
import Networking.Packets.Incoming as incoming
import Networking.Packets.PacketTypes as PacketTypes

types = PacketTypes.PacketTypes()

def CreatePacket(packet_type):
    if type(packet_type) != str:
        raise ValueError("Packet type have to be of type str not " + str(type(packet_type)))
    packet_type = packet_type.upper()
    if not isValidPacket(packet_type):
        raise ValueError("Invalid Packet type: "+packet_type)
    if packet_type == types.ACCEPTTRADE:
        return outgoing.AcceptTradePacket()
    if packet_type == types.ACTIVEPETUPDATEREQUEST:
        return outgoing.ActivePetUpdateRequestPacket()
    if packet_type == types.AOEACK:
        return outgoing.AoeAckPacket()
    if packet_type == types.BUY:
        return outgoing.BuyPacket()
    if packet_type == types.CANCELTRADE:
        return outgoing.CancelTradePacket()
    if packet_type == types.CHANGEGUILDRANK:
        return outgoing.ChangeGuildRankPacket()
    if packet_type == types.CHANGEPETSKIN:
        return outgoing.ChangePetSkinPacket()
    if packet_type == types.CHANGETRADE:
        return outgoing.ChangeTradePacket()
    if packet_type == types.CHECKCREDITS:
        return outgoing.CheckCreditsPacket()
    if packet_type == types.CHOOSENAME:
        return outgoing.ChooseNamePacket()
    if packet_type == types.CREATEGUILD:
        return outgoing.CreateGuildPacket()
    if packet_type == types.CREATE:
        return outgoing.CreatePacket()
    if packet_type == types.EDITACCOUNTLIST:
        return outgoing.EditAccountListPacket()
    if packet_type == types.ENEMYHIT:
        return outgoing.EnemyHitPacket()
    if packet_type == types.ESCAPE:
        return outgoing.EscapePacket()
    if packet_type == types.GOTOACK:
        return outgoing.GotoAckPacket()
    if packet_type == types.GOTOQUESTROOM:
        return outgoing.GoToQuestRoomPacket()
    if packet_type == types.GROUNDDAMAGE:
        return outgoing.GroundDamagePacket()
    if packet_type == types.GUILDINVITE:
        return outgoing.GuildInvitePacket()
    if packet_type == types.GUILDREMOVE:
        return outgoing.GuildRemovePacket()
    if packet_type == types.HELLO:
        return outgoing.HelloPacket()
    if packet_type == types.INVDROP:
        return outgoing.InvDropPacket()
    if packet_type == types.INVSWAP:
        return outgoing.InvSwapPacket()
    if packet_type == types.JOINGUILD:
        return outgoing.JoinGuildPacket()
    if packet_type == types.KEYINFOREQUEST:
        return outgoing.KeyInfoRequestPacket()
    if packet_type == types.LOAD:
        return outgoing.LoadPacket()
    if packet_type == types.MOVE:
        return outgoing.MovePacket()
    if packet_type == types.OTHERHIT:
        return outgoing.OtherHitPacket()
    if packet_type == types.PLAYERHIT:
        return outgoing.PlayerHitPacket()
    if packet_type == types.PLAYERSHOOT:
        return outgoing.PlayerShootPacket()
    if packet_type == types.PLAYERTEXT:
        return outgoing.PlayerTextPacket()
    if packet_type == types.PONG:
        return outgoing.PongPacket()
    if packet_type == types.REQUESTTRADE:
        return outgoing.RequestTradePacket()
    if packet_type == types.RESETDAILYQUESTS:
        return outgoing.ResetDailyQuestsPacket()
    if packet_type == types.RESKIN:
        return outgoing.ReskinPacket()
    if packet_type == types.SETCONDITION:
        return outgoing.SetConditionPacket()
    if packet_type == types.SHOOTACK:
        return outgoing.ShootAckPacket()
    if packet_type == types.SQUAREHIT:
        return outgoing.SquareHitPacket()
    if packet_type == types.TELEPORT:
        return outgoing.TeleportPacket()
    if packet_type == types.UPDATEACK:
        return outgoing.UpdateAckPacket()
    if packet_type == types.USEITEM:
        return outgoing.UseItemPacket()
    if packet_type == types.USEPORTAL:
        return outgoing.UsePortalPacket()
    if packet_type == types.ACCOUNTLIST:
        return incoming.AccountListPacket()
    if packet_type == types.ALLYSHOOT:
        return incoming.AllyShootPacket()
    if packet_type == types.AOE:
        return incoming.AoePacket()
    if packet_type == types.BUYRESULT:
        return incoming.BuyResultPacket()
    if packet_type == types.CLAIMDAILYREWARDRESPONSE:
        return incoming.ClaimDailyRewardResponsePacket()
    if packet_type == types.CLIENTSTAT:
        return incoming.ClientStatPacket()
    if packet_type == types.CREATESUCCESS:
        return incoming.CreateSuccessPacket()
    if packet_type == types.DAMAGE:
        return incoming.DamagePacket()
    if packet_type == types.DEATH:
        return incoming.DeathPacket()
    if packet_type == types.ENEMYSHOOT:
        return incoming.EnemyShootPacket()
    if packet_type == types.FAILURE:
        return incoming.FailurePacket()
    if packet_type == types.FILE:
        return incoming.FilePacket()
    if packet_type == types.GLOBALNOTIFICATION:
        return incoming.GlobalNotificationPacket()
    if packet_type == types.GOTO:
        return incoming.GotoPacket()
    if packet_type == types.GUILDRESULT:
        return incoming.GuildResultPacket()
    if packet_type == types.INVITEDTOGUILD:
        return incoming.InvitedToGuildPacket()
    if packet_type == types.INVRESULT:
        return incoming.InvResultPacket()
    if packet_type == types.KEYINFORESPONSE:
        return incoming.KeyInfoResponsePacket()
    if packet_type == types.MAPINFO:
        return incoming.MapInfoPacket()
    if packet_type == types.NAMERESULT:
        return incoming.NameResultPacket()
    if packet_type == types.NEWABILITY:
        return incoming.NewAbilityPacket()
    if packet_type == types.NEWCHARACTERINFORMATION:
        return incoming.NewCharacterInformationPacket()
    if packet_type == types.NEWTICK:
        return incoming.NewTickPacket()
    if packet_type == types.NOTIFICATION:
        return incoming.NotificationPacket()
    if packet_type == types.PASSWORDPROMPT:
        return incoming.PasswordPromptPacket()
    if packet_type == types.PIC:
        return incoming.PicPacket()
    if packet_type == types.PING:
        return incoming.PingPacket()
    if packet_type == types.PLAYSOUND:
        return incoming.PlaySoundPacket()
    if packet_type == types.QUESTOBJID:
        return incoming.QuestObjIdPacket()
    if packet_type == types.QUESTREDEEMRESPONSE:
        return incoming.QuestRedeemResponsePacket()
    if packet_type == types.QUEUEINFORMATION:
        return incoming.QueueInformationPacket()
    if packet_type == types.REALMHEROESRESPONSE:
        return incoming.RealmHeroesResponsePacket()
    if packet_type == types.RECONNECT:
        return incoming.ReconnectPacket()
    if packet_type == types.RESKINUNLOCK:
        return incoming.ReskinUnlockPacket()
    if packet_type == types.SERVERPLAYERSHOOT:
        return incoming.ServerPlayerShootPacket()
    if packet_type == types.SHOWEFFECT:
        return incoming.ShowEffectPacket()
    if packet_type == types.TEXT:
        return incoming.TextPacket()
    if packet_type == types.TRADEACCEPTED:
        return incoming.TradeAcceptedPacket()
    if packet_type == types.TRADECHANGED:
        return incoming.TradeChangedPacket()
    if packet_type == types.TRADEDONE:
        return incoming.TradeDonePacket()
    if packet_type == types.TRADEREQUESTED:
        return incoming.TradeRequestedPacket()
    if packet_type == types.TRADESTART:
        return incoming.TradeStartPacket()
    if packet_type == types.UPDATE:
        return incoming.UpdatePacket()
    if packet_type == types.VERIFYEMAIL:
        return incoming.VerifyEmailPacket()

def isValidPacket(packet_type):
    return packet_type in dir(types)
