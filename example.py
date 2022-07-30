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
            title="Example native-ui app",
            width=350,
            height=200,
            child=native.Container(
                layout=abstract.Layout.VERTICAL,
            )
        )
    )
    cont = app.window.child

    def window_update(self, container):
        splt = self.title.split()
        if self.title[-1].isdigit():
            splt = splt[:-1]
        else:
            splt.append("Buttons:")
        splt.append(str(len(container.children)))
        self.title = " ".join(splt)

    app.window.update = window_update
    app.window.update_args = [cont]

    def on_pressed(self, container, window):
        print("Hello world")
        self.label = f"Clicked {self.runtime_data.get('clicked', 1)}"
        self.runtime_data["clicked"] = self.runtime_data.get('clicked', 1) + 1
        container.add_child(
                       native.Button(
                           label="Hello",
                           pressed=on_pressed,
                           pressed_args=[container, window]
                       ))
        # test removing container children feature
        container.children = container.children
        window.update()

    cont.add_child(native.Button(
        label="Hello",
        pressed=on_pressed,
        pressed_args=[cont, app.window],
    ))

    app.build()
    app.run(sys.argv)


if __name__ == "__main__":
    main()
