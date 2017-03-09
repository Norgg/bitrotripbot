import irc.bot
import irc.strings
from random import choice
irc.client.ServerConnection.buffer_class.errors = u'replace'

rip = [
    u"Kountdown",
    u"Eye_of_Jeb",
    u"checkpoint",
    u"Lizzie",
    u"SpaceCore",
    u"FactSphere",
    u"AdventureSphere",
    u"Technicality",
    u"hatbot",
    u"DMPBot",
    u"Malcolm",
]

missed = [
    u"you will be missed.",
    u"we will remember you.",
    u"you were faithful 'til the end.",
    u"sleep well.",
    u"you are where good bots go."
]

nick = u'bitrotripbot'
server = u'irc.esper.net'
port = 6667
channels = [u'#bottorture']


class RipBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channels, nick, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nick, nick)
        self.channels_to_join = channels
        self.nick = nick

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        for channel in self.channels_to_join:
            c.join(channel)

    def on_notify(selc, ctx, evt):
        print(evt.arguments[0])

    def on_privmsg(self, ctx, evt):
        pass

    def on_pubmsg(self, ctx, evt):
        msg = evt.arguments[0]
        was_cmd = msg.startswith(u"!rip")
        channel = evt.target

        if was_cmd:
            response = "Rest in peace {}, {}".format(
                choice(rip),
                choice(missed)
            )
            self.connection.privmsg(channel, response)
            return


def main():
    RipBot(channels, nick, server, port).start()


if __name__ == u"__main__":
    main()
