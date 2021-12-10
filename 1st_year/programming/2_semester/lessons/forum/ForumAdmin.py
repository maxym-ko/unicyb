from ForumUser import ForumUser


class Admin(ForumUser):
    def __init__(self, nick=''):
        super().__init__(nick)

    @classmethod
    def _process_nick(cls, nick):
        nick = super(cls)._process_nick(nick)
        if nick[0] != 'A':
            raise ValueError('Admin\'s nick should start from "A"')
        return nick

    def can_message(self):
        return True

    def _can_ban(self):
        pass

    def _can_be_banned(self):
        pass
