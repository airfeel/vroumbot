"""
Text spam! Yay!
"""
import random


from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
import requests


from ..base import Base


class Text(Base):
    """
    Text spam! Yay!
    """

    def __init__(self, logger=None):
        commandhandlers = [
            CommandHandler("vroum", self.vroum),
            CommandHandler("vroom", self.vroom),
            CommandHandler(["dad", "dadjoke"], self.dad),
            CommandHandler(["beep", "boop"], self.boop),
            CommandHandler("tut", self.tut),
            CommandHandler(["keysmash", "bottom", "helo"], self.keysmash),
            CommandHandler(["oh", "ooh", "oooh"], self.oh),
            CommandHandler(["ay", "ayy", "ayyy", "xd", "xdd", "xddd"], self.xd),
            CommandHandler(["pep", "peptalk", "motivation", "motivational"], self.peptalk),
        ]
        super().__init__(logger, commandhandlers)

    def vroum(self, update: Update, context: CallbackContext) -> None:
        """
        Vroum!
        """
        update.message.reply_text("Vroum!")

        self.logger.info("{} gets a Vroum!".format(update.effective_user.first_name))

    def vroom(self, update: Update, context: CallbackContext) -> None:
        """
        nO.
        """
        update.message.reply_text("😠")

        self.logger.info("{} gets a 😠!".format(update.effective_user.first_name))

    def dad(self, update: Update, context: CallbackContext) -> None:
        """
        Random dad joke
        """
        endpoint = "http://dadjokes.online/noecho"
        resp = requests.get(url=endpoint)
        try:
            data = resp.json()
            opener, punchline, _ = data["Joke"].values()
        except:
            update.message.reply_text("No more dad jokes )':.")
            return

        update.message.reply_text(opener).reply_text(punchline)

        self.logger.info("{} gets a dad joke!".format(update.effective_user.first_name))

    def boop(self, update: Update, context: CallbackContext) -> None:
        """
        boop/beep/beep/boop
        """
        if "/beep" in update.message.text:
            text = "boop"
        elif "/boop" in update.message.text:
            text = "beep"
        else:
            text = "..."

        update.message.reply_text(text)

        self.logger.info("{} gets a {}!".format(update.effective_user.first_name, text))

    def tut(self, update: Update, context: CallbackContext) -> None:
        """
        tut
        """
        update.message.reply_text("tut")

        self.logger.info("{} gets a tut!".format(update.effective_user.first_name))

    def keysmash(self, update: Update, context: CallbackContext) -> None:
        """
        Bottom generator
        """
        letters_normal = ["j", "h", "l", "r", "d", "s", "m", "J", "f", "k", "g"]
        letters_frustration = ["l", "h", "r", "m", "g"]

        letters = letters_frustration if random.randint(1, 9) == 1 else letters_normal

        mu = 12.777777777778
        sigma = 2.1998877636915
        length = int(random.gauss(mu, sigma))
        result = oldletter = newletter = random.choice(letters)

        for _ in range(length):
            while oldletter == newletter:
                newletter = random.choice(letters)
            result += newletter
            oldletter = newletter

        update.message.reply_text(result)

        self.logger.info("{} is keysmashing!".format(update.effective_user.first_name))

    def oh(self, update: Update, context: CallbackContext) -> None:
        """
        Oooh
        """
        mu = 3
        sigma = 2
        length = -1
        while length < 1:
            length = int(random.gauss(mu, sigma))

        result = "o" * length + "h"
        result = "".join([l.upper() if random.randint(1, 6) == 1 else l for l in result])

        update.message.reply_text(result)

        self.logger.info("{} is in awe!".format(update.effective_user.first_name))

    def xd(self, update: Update, context: CallbackContext) -> None:
        """
        XDDD
        """
        mu = 3
        sigma = 2
        length = -1
        while length < 1:
            length = int(random.gauss(mu, sigma))

        if random.randint(1, 2) == 1:
            result = "X" + "D" * length
        else:
            result = "a" + "y" * length

        update.message.reply_text(result)

        self.logger.info("{} is in XDing real hard!".format(update.effective_user.first_name))

    def peptalk(self, update: Update, context: CallbackContext) -> None:
        """
        When you need a bit of motivation!
        """
        first = [
            "Champ,",
            "Fact:",
            "Everybody says",
            "Dang...",
            "Check it:",
            "Just saying...",
            "Superstar,",
            "Tiger,",
            "Self,",
            "Know this:",
            "News alert:",
            "Girl,",
            "Ace,",
            "Excuse me but",
            "Experts agree",
            "In my opinion,",
            "Hear ye, hear ye:",
            "Okay, listen up:",
        ]

        second = [
            "the mere idea of you",
            "your soul",
            "your hair today",
            "everything you do",
            "your personal style",
            "every thought you have",
            "that sparkle in your eye",
            "your presence here",
            "what you got going on",
            "the essential you",
            "your life's journey",
            "that saucy personlity",
            "your DNA",
            "that brain of yours",
            "your choice of attire",
            "the way you roll",
            "whatever your secret is",
            "all of y'all",
        ]

        third = [
            "has serious game,",
            "rains magic,",
            "deserves the Nobel Prize,",
            "raises the roof,",
            "breeds miracles,",
            "is paying off big time,",
            "shows mad skills,",
            "just shimmers,",
            "is a national treasure,",
            "gets the party hopping,",
            "is the next big thing,",
            "roars like a lion,",
            "is a rainbow factory,",
            "is made of diamonds,",
            "makes birds sing,",
            "should be taught in school,",
            "makes my world go 'round,",
            "is 100% legit,",
        ]

        fourth = [
            "24/7.",
            "can I get an amen?",
            "and that's a fact.",
            "so treat yourself.",
            "you feel me?",
            "that's just science.",
            "would I lie?",
            "for reals.",
            "mic drop.",
            "you hidden gem.",
            "snuggle bear.",
            "period.",
            "now let's dance.",
            "high five.",
            "say it again!",
            "according to CNN.",
            "so get used to it.",
        ]

        update.message.reply_text(
            "{} {} {} {}".format(
                random.choice(first),
                random.choice(second),
                random.choice(third),
                random.choice(fourth),
            )
        )

        self.logger.info("{} gets a little motivation!".format(update.effective_user.first_name))
