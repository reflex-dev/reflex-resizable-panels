"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_resizable_panels import resizable_panels as rzp

filename = f"{config.app_name}/{config.app_name}.py"


def lorem():
    return rx.vstack(
        rx.section(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""",
            size="2",
        ),
        rx.section(
            """Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
            size="2",
        ),
    )


def panels():
    return rx.box(
        rzp.group(
            rzp.panel(
                background_color=rx.color("black", 10),
                min_size=20,
                default_size=20,
            ),
            rzp.handle(),
            rzp.panel(
                rx.container(lorem()),
                background_color=rx.color("gray", 10),
                min_size=30,
                on_collapse=rx.toast("Panel collapsed"),
                on_expand=rx.toast("Panel expanded"),
                on_resize=lambda size: rx.toast(f"Panel resized to {size}%"),
            ),
            direction="horizontal",
        ),
        width="100%",
        height="100%",
    )


def index() -> tuple:
    return rx.box(
        panels(),
        height="100vh",
    ), rx.color_mode.button(position="top-right")


# Add state and page to the app.
app = rx.App()
app.add_page(index)
