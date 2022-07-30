import native_ui
import sys

native_ui.set_runtime_platform("gnome", "org.surferlul.native-ui.ExampleApp")
from native_ui import native, abstract


def main():
    window = native.Window()
    window.set(
        child=None
    )

    app = native.Application(
        window=native.Window(
            child=native.Container(
                layout=abstract.Layout.VERTICAL,
            )
        )
    )
    cont = app.window.child

    def on_pressed(button, container):
        print("Hello world")
        container.call("add_child",
                       native.Button(
                           label="Hello",
                           pressed=on_pressed,
                           pressed_args=[container]
                       ))

    cont.add_child(native.Button(
        label="Hello",
        pressed=on_pressed,
        pressed_args=[cont],
    ))

    app.build()
    app.run(sys.argv)


if __name__ == "__main__":
    main()
