import os
import random


from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler


from secret import BOT_ID


from ..base import Base
from .helpers import get_user


def needed_exp(level, karma):
    if level == 0:
        return 0
    # Dirty hack
    if level == 1:
        return 5
    return int((level ** 3.14) * (1 - (karma / (level ** 3.14))))


class Exp(Base):
    def __init__(self, logger=None, table=None):
        commandhandlers = [
            MessageHandler(~Filters.command, self.add_message),
            CommandHandler(["level", "mylevel"], self.get_level),
            CommandHandler(["levels", "leaderboard"], self.get_leaderboard),
        ]
        super().__init__(logger, commandhandlers, table, mediafolder="./media/levelup")

    def add_message(self, update: Update, context: CallbackContext):
        user = update.effective_user
        dbuser = get_user(self.table, user.id, update.message.chat.id)
        dbuser.num_messages += 1
        dbuser.userfirstname = user.first_name

        change = dbuser.level
        while dbuser.num_messages > needed_exp(dbuser.level, dbuser.karma):
            dbuser.level += 1

        if change != dbuser.level:
            filename = os.path.join(self._media(), random.choice(os.listdir(self._media())))
            with open(filename, "rb") as file:
                update.message.reply_document(
                    document=file,
                    caption="LEVEL UP!\n{} -> {}\n{} messages for {} karma.".format(
                        change, dbuser.level, dbuser.num_messages, dbuser.karma
                    ),
                )

        dbuser.save()

    def get_level(self, update: Update, context: CallbackContext):
        if update.message.reply_to_message:
            user = update.message.reply_to_message.from_user
            if user.id == BOT_ID:
                update.message.reply_text("I don't level up, silly ~")
                return
            dbuser = get_user(self.table, user.id, update.message.chat.id)
        else:
            user = update.effective_user
            dbuser = get_user(self.table, user.id, update.message.chat.id)

        update.message.reply_text(
            "LEVEL {} ({} messages)".format(dbuser.level, dbuser.num_messages)
        )

    def get_leaderboard(self, update: Update, context: CallbackContext):
        try:
            _, num_people = update.message.text.split(" ", 1)
            num_people = int(num_people)
            if num_people < 1:
                num_people = 10
        except ValueError:
            num_people = 10

        users = (
            self.table.select()
            .where(self.table.chatid == update.message.chat.id)
            .order_by(self.table.level.desc())
            .order_by(self.table.num_messages.desc())
            .limit(num_people)
        )

        levels = {
            user.userid: [user.userfirstname, user.level, user.num_messages] for user in users
        }
        _ = levels.pop(BOT_ID)
        num_people = min(len(levels), num_people)

        all_people = []
        for i, (userid, data) in enumerate(levels.items()):
            if i < num_people:
                username, level, num_messages = data
                if not username:
                    username = "<No registered username>"
                all_people.append(
                    "{}. {}: level {} ({} messages).".format(i + 1, username, level, num_messages)
                )
            else:
                break

        update.message.reply_text("\n".join(all_people))

    def reset_from_history(self, update: Update, context: CallbackContext):
        pass


# TODO
# state (start or stop)(if admin?)
# reset/import chat (with or without file)