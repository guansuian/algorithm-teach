from manim import (
    DOWN, RIGHT, UP, RoundedRectangle, Scene, Text, VGroup, config,
)


class ArrayTraversalScene(Scene):
    def on_key_press(self, symbol, modifiers):
        if symbol == ord("1"):
            self.direction = 1
        elif symbol == ord("2"):
            self.direction = -1

    def construct(self):
        self.direction = 1
        window_size = 8
        base_color = "#1B2940"
        active_color = "#237F72"
        rows = VGroup()

        # 先画两行数组，每行 8 个格子。
        for values in (range(1, 9), range(9, 17)):
            row = VGroup()
            for value in values:
                box = RoundedRectangle(
                    width=1, height=1, corner_radius=0.12,
                    stroke_color="#34445E", stroke_width=1.5,
                    fill_color=base_color, fill_opacity=1,
                )
                number = Text(str(value), font_size=26, color="#F1F5F9").move_to(box)
                row.add(VGroup(box, number))
            rows.add(row.arrange(RIGHT, buff=0.14))
        rows.arrange(DOWN, buff=0.6).shift(DOWN * 0.25)

        self.add(Text("环形滑动窗口", font_size=34).shift(UP * 2.6))
        self.add(Text("按 1 顺时针 · 按 2 逆时针 · 窗口长度 8", font_size=18,
                      color="#94A3B8").shift(UP * 2))
        self.add(rows)

        # 把两行按顺时针顺序接起来，最初亮起上排的 8 个格子。
        path = list(rows[0]) + list(rows[1])[::-1]
        for cell in path[:window_size]:
            cell[0].set_fill(active_color)
        self.wait(0.8)

        # 每走一格：尾部退出一个，前方进入一个，窗口始终覆盖 8 个格子。
        start = 0
        while not self.renderer.window.is_closing:
            # 先记住这一步的方向，途中按键会从下一步生效。
            direction = self.direction
            if direction == 1:
                leaving = start
                entering = (start + window_size) % len(path)
            else:
                leaving = (start + window_size - 1) % len(path)
                entering = (start - 1) % len(path)
            self.play(
                path[leaving][0].animate.set_fill(base_color),
                path[entering][0].animate.set_fill(active_color),
                run_time=0.35,
            )
            start = (start + direction) % len(path)
            self.wait(0.3)


if __name__ == "__main__":
    # OpenGL 直接显示动画窗口，format="none" 关闭视频输出。
    config.update({
        "renderer": "opengl", "live_preview": True, "format": "none",
        "background_color": "#101827", "window_size": (960, 540), "progress_bar": "none",
    })
    Text.set_default(font="Hiragino Sans GB")
    ArrayTraversalScene().render()
