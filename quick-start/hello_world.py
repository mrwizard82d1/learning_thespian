from thespian.actors import (
    Actor,
    ActorExitRequest,
    ActorSystem,
)


class Hello(Actor):
    def receiveMessage(self, msg, sender):
        # NOTE: The Hello Actor sends the same message to `sender`
        # in response to **all** messages.
        self.send(sender, 'Hello, Thespian World!')


def main():
    hello = ActorSystem().createActor(Hello)
    print(ActorSystem().ask(hello, 'hi', 1))
    ActorSystem().tell(hello, ActorExitRequest())


if __name__ == "__main__":
    main()
