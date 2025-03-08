from thespian.actors import (
    Actor,
    ActorSystem,
    ActorExitRequest,
)


class Greeting:
    def __init__(self, msg):
        self.message = msg
        self.sendTo = []

    def  __str__(self):
        return self.message


class Hello(Actor):
    def receiveMessage(self, message, sender):
        if message == 'hi':
           greeting = Greeting('Hello')
           world = self.createActor(World)
           punctuate = self.createActor(Punctuate)
           greeting.sendTo = [punctuate, sender]
           self.send(world, greeting)


class World(Actor):
    def receiveMessage(self, message, sender):
        if isinstance(message, Greeting):
            message.message += ', World'
            next_to = message.sendTo.pop(0)
            self.send(next_to, message)


class Punctuate(Actor):
    def receiveMessage(self, message, sender):
        if isinstance(message, Greeting):
            message.message += '!'
            next_to = message.sendTo.pop(0)
            self.send(next_to, message)


if __name__ == '__main__':
    hello = ActorSystem().createActor(Hello)
    print(ActorSystem().ask(hello, 'hi', 0.2))
    print(ActorSystem().ask(hello, 'hi', 0.2))
    ActorSystem().tell(hello, ActorExitRequest())
    print('Sending a message after an `ActorExitRequest`.')
    print(f'results in: {ActorSystem().ask(hello, 'hi', 0.2)=}')
