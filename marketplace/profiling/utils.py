from django.contrib import messages
from main.models import Events


def error_messages(request, *args: str):
    fields = {}

    for field in args:
        fields.update({field.capitalize(): request.POST[field.lower()]})

    fields = [err[0] for err in fields.items() if not err[1]]

    return messages.error(
        request,
        f"Please, do not leave required fields blank -> {', '.join(fields)}",
    )


def check_if_like(request, item):
    event = Events.objects.filter(user=request.user, object=item)
    if event.exists():
        event = event.last()
        if event.event == "Like":
            return True
        else:
            return False
    else:
        return False
