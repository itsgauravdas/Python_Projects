"""
This Python script uses the plyer library to display a simple notification on your desktop, which shows a title and message, then disappears after a specified timeout. Here's a quick overview:

title: Sets the title of the notification.
message: Displays the content of the notification.
timeout: Determines how long (in seconds) the notification should remain visible.
"""
from plyer import notification

notification.notify(
    title="email Notification",
    message="You have 3 unread messages",
    timeout=10,
)