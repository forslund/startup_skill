from mycroft.skills.core import MycroftSkill
from subprocess import Popen

class StartupSkill(MycroftSkill):
    def __init__(self):
        super(StartupSkill, self).__init__('StartupSkill')

    def initialize(self):
        self.procs = {}
        for pair in self.config.get('commands', []):
            self.procs[pair[0]] = Popen(pair[1].split(' '))

    def stop():
        for keys in self.procs:
            self.procs.kill()


def create_skill():
    return StartupSkill()
