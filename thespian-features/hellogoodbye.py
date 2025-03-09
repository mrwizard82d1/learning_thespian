"""Dynamic Actor Creation"""

import thespian.actors as thea
from thespian.actors import ActorSystem


class Hello(thea.Actor):
    def receiveMessage(self, message, sender):
        if message == 'are you there?':
            if not hasattr(self, 'world'):
                self.world = self.createActor(World)
            world_msg = (sender, 'Hello,')
            self.send(self.world, world_msg)


class World(thea.Actor):
    def receiveMessage(self, message, sender):
        if isinstance(message, tuple):
            original_sender, pre_world_text = message
            self.send(original_sender, pre_world_text + ' Thespian World!')


class Goodbye(thea.Actor):
    def receiveMessage(self, message, sender):
        self.send(sender, 'Goodbye!')


def run_example(systembase=None):
    goodbye = thea.ActorSystem().createActor(Goodbye)
    hello = thea.ActorSystem(systembase).createActor(Hello)
    # First message to an instance
    greeting = ActorSystem().ask(hello, 'are you there?', 1.5)
    print(greeting + '\n' + ActorSystem().ask(goodbye, None, 0.1))

    # Second message to the same insntance
    greeting = ActorSystem().ask(hello, 'are you there?', 1.5)
    print(greeting + '\n' + ActorSystem().ask(goodbye, None, 0.1))
    ActorSystem().shutdown()


if __name__ == '__main__':
    import sys
    run_example(sys.argv[1] if len(sys.argv) > 1 else None)
