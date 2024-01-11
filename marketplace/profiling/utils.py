from django.contrib import messages


def error_messages(request, *args: str):
    fields = {}

    for field in args:
        fields.update({field.capitalize(): request.POST[field.lower()]})

    fields = [err[0] for err in fields.items() if not err[1]]

    return messages.error(
        request,
        f"Please, do not leave required fields blank -> {', '.join(fields)}",
    )
