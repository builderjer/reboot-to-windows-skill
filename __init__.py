import os

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class RebootToWindowsSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.default_os = 0
        self.reboot_os = 2

    def initialize(self):
        os.system('sudo grub-set-default {}'.format(self.default_os))

    @intent_handler('RebootOS.intent')
    def handle_reboot_intent(self, message):
        should_reboot = self.ask_yesno('ask.to.reboot')
        if should_reboot:
            os.system('sudo grub-reboot {}'.format(self.reboot_os))
            os.system('sudo reboot')

def create_skill():
    return RebootToWindowsSkill()
