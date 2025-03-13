"""
The typical example of Hello World but using Actors.
"""

import thespian.actors as thea


class Hello(thea.Actor):
    def receiveMessage(self, message, sender):
        # Remember, in this example, the incoming `message` is
        # **ignored**. The `sender` parameter is the "actor address"
        # of the `Actor` that sent the message to this Actor. It is
        # an opaque type.
        self.send(sender, 'Hello, Thespian World!')
        # When execution exits the `receiveMessage()` method,
        # this `Actor` **sleeps** until it receives another message.
        # Each `Actor` processes **exactly one` message at a time.


def say_hello():
    # The following line performs **two** actions
    # - Start the Actor System (`ActorSystem()`)
    # - Create an instance of the `Hello` Actor.
    #
    # The result of the call to `creatActor()` is an **Actor Address**.
    #
    # Remember, the call, `ActorSystem()`, returns a **singleton**
    # instance of the specified `ActorSystem`. Once the Actor System
    # is no longer needed, one may call its `shutdown()` method to
    # release all associated resources. When an Actor System is shutdown,
    # any Actors running in that Actor System **will also be terminated**.
    hello = thea.ActorSystem(systemBase='multiprocTCPBase').createActor(Hello)

    # The call to the `ask()` method sends a message and then waits
    # for a response message. The message is the query text (a `string`):
    # 'are you there?'; however, as mentioned earlier, the content of
    # this particular message is **ignored** by the `Hello` Actor.
    #
    # The additional argument, the value 1.5, specifies a timeout period
    # in **seconds**. If no response is received, the `ask()` method
    # returns the value, `None`, to indicate a timeout.
    print(thea.ActorSystem().ask(hello, 'are you there?', 1.5))

    # Note, the response of an Actor to a message is **completely up to the
    # Actor implementation**. There is no requirement that a response must
    # be generated for each received message. In fact, an Actor may send
    # **several responses** or **no response at all**.

    # Shutdown the "hello" actor.
    thea.ActorSystem().tell(hello, thea.ActorExitRequest)


if __name__ == "__main__":
    say_hello()
