from manim import (
    DOWN, LEFT, RIGHT, UP, RoundedRectangle, Scene, Text, VGroup, config,
)


class ArrayMergeScene(Scene):
    def construct(self):
        a = [1, 4, 7, 9]
        b = [2, 4, 6, 8]

        # 画格子的代码只写一次。
        def make_row(values):
            row = VGroup()
            for value in values:
                box = RoundedRectangle(
                    width=0.9, height=0.9, corner_radius=0.12,
                    stroke_color="#34445E", stroke_width=1.5,
                    fill_color="#1B2940", fill_opacity=1,
                )
                cell = VGroup(box)
                if value is not None:
                    cell.add(Text(str(value), font_size=26).move_to(box))
                row.add(cell)
            return row.arrange(RIGHT, buff=0.12)

        row_a = make_row(a).shift(LEFT * 2.7 + UP * 0.7)
        row_b = make_row(b).shift(RIGHT * 2.7 + UP * 0.7)
        result = make_row([None] * (len(a) + len(b))).shift(DOWN * 1.6)

        self.add(Text("合并两个有序数组", font_size=34).shift(UP * 3))
        self.add(Text("比较两边尚未取出的第一个数，每次取较小的一个", font_size=18,
                      color="#94A3B8").shift(UP * 2.4))
        self.add(Text("数组 A", font_size=20, color="#94A3B8").next_to(row_a, UP))
        self.add(Text("数组 B", font_size=20, color="#94A3B8").next_to(row_b, UP))
        self.add(Text("合并结果", font_size=20, color="#94A3B8").next_to(result, DOWN))
        # result 只记录落点，不加入画面；结果方块随合并逐个出现。
        self.add(row_a, row_b)
        status = Text("从两个数组的开头开始", font_size=22).shift(DOWN * 0.4)
        self.add(status)
        self.wait(0.8)

        # i、j 分别记录两个数组取到哪里，每次把较小的数移到结果中。
        i = j = 0
        for slot in result:
            if j == len(b) or (i < len(a) and a[i] <= b[j]):
                cell = row_a[i]
                i += 1
            else:
                cell = row_b[j]
                j += 1

            status.become(Text(f"当前最小值：{cell[1].text}，移入结果数组", font_size=22)
                          .move_to(status))
            cell[0].set_fill("#237F72")
            self.play(cell.animate.move_to(slot), run_time=0.7)
            self.wait(0.3)

        status.become(Text("合并完成，结果仍然从小到大排列", font_size=22,
                           color="#5EEAD4").move_to(status))


if __name__ == "__main__":
    config.update({
        "renderer": "opengl", "live_preview": True, "format": "none",
        "background_color": "#101827", "window_size": (960, 540), "progress_bar": "none",
    })
    Text.set_default(font="Hiragino Sans GB")
    scene = ArrayMergeScene()
    scene.render()

    # 合并结束后保留结果，关闭窗口即可退出。
    window = scene.renderer.window
    while not window.is_closing:
        scene.renderer.update_frame(scene)
        window.swap_buffers()
