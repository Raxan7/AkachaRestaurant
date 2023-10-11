from .models import Messages


def send_message(sender, sender_category, receiver, receiver_category, message,
                 message_type):
    """
        This function creates the message object and then the message is
        accessed by a user of a certain category, the user who sends the
        message is also identified by their category
        Message sending is completely automatic, users can't send messages
        like it is a chatting app. Messages are tied to the actions that are
        carried out by the users

        CEO can view all messages that are being sent
        StoreKeeper can send messages to the CEO based on the activities done
        Chef can send messages to the StoreKeeper when requesting goods

        Message Types
            --> Authorization
            --> Request
            --> Denial
    """
    message_object = Messages.objects.create(
        sender=sender,
        sender_category=sender_category,
        receiver=receiver,
        receiver_category=receiver_category,
        message=message,
        message_type=message_type,
    )
    message_object.save()
