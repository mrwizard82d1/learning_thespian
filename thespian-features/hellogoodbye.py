"""Dynamic Actor Creation"""

import thespian.actors as thea
from thespian.actors import ActorSystem, ActorExitRequest


class Hello(thea.Actor):
    def receiveMessage(self, message, sender):
        if message == 'are you there?':
            world = self.createActor(World)
            world_msg = (sender, 'Hello,')
            self.send(world, world_msg)


class World(thea.Actor):
    def receiveMessage(self, message, sender):
        if isinstance(message, tuple):
            original_sender, pre_world_text = message
            self.send(original_sender, pre_world_text + ' Thespian World!')
            self.send(self.myAddress, ActorExitRequest())


class Goodbye(thea.Actor):
    def receiveMessage(self, message, sender):
        self.send(sender, 'Goodbye!')


def run_example(systembase=None):
    hello = thea.ActorSystem(systembase).createActor(Hello)
    goodbye = thea.ActorSystem().createActor(Goodbye)
    greeting = ActorSystem().ask(hello, 'are you there?', 1.5)
    print(greeting + '\n' + ActorSystem().ask(goodbye, None, 0.1))
    ActorSystem().shutdown()


if __name__ == '__main__':
    import sys
    run_example(sys.argv[1] if len(sys.argv) > 1 else None)
