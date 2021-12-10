class ForumUser:
    _noname_name = "noname"

    def __init__(self, nick=''):
        if not isinstance(nick, str):
            raise TypeError('The only argument should be string')

        self._nick = self._process_nick(nick)
        self._ban = 0
        self._n = 0

    def _process_nick(cls, nick):
        nick = nick.strip()
        if not nick:
            nick = cls._noname_name
        return nick

    def can_message(self):
        return not self.ban and not self._is_noname()

    def message(self, text):
        if self.can_message():
            self._message(text)
        else:
            if self.ban:
                self._ban -= 1
        return self

    def _message(self, text):
        print(self.nick, text)

    def _is_noname(self):
        return self.nick == self._noname_name

    def do_ban(self, other):
        if self._can_ban() and other._can_be_banned():
            self._ban(other)

    def _can_ban(self):
        pass

    def _can_be_banned(self):
        pass

    def _ban(self, other):
        pass

    @property
    def nick(self):
        return self._nick

    @property
    def ban(self):
        return self._ban
