# algorithm-teach

使用 Python 制作可直接运行的算法教学动画。

## 环境

- Python 3.12.10
- Manim Community 0.22.0

## 运行遍历动画

在 PyCharm 中打开 `findMedianSortedArrays/move.py`，使用项目的 `.venv` 解释器，点击运行即可看到动画窗口。

也可以在项目目录运行：

```bash
.venv/bin/python findMedianSortedArrays/move.py
```

上下两个数组各有 8 个元素。窗口覆盖连续的 8 个格子，沿“上排从左到右 → 下排从右到左 → 回到上排”的顺时针路径循环移动。窗口内的格子背景变绿，离开窗口后恢复原色。

先点击动画窗口，让窗口获得键盘焦点。按 `1` 顺时针，按 `2` 逆时针，无需按回车。切换后从当前位置继续；如果正在移动，会先完成当前这一步。

当前示例使用 Manim 的 OpenGL 窗口实时显示动画，不生成视频。动画持续循环，关闭窗口即可退出。

## 运行有序数组合并动画

在 PyCharm 中打开 `findMedianSortedArrays/merge.py`，点击运行。

程序比较两个有序数组尚未取出的第一个元素，每次把较小的数移动到下方的结果数组。一边取完后，继续放入另一边的剩余元素。合并完成后保留结果，关闭窗口退出。

## 安装依赖

`requirements.txt` 中记录了 Manim Community 0.22.0。
macOS 安装 Manim 前需要准备 Cairo 和 pkg-config，例如通过 Homebrew 安装：

```bash
brew install cairo pkg-config
.venv/bin/python -m pip install -r requirements.txt
```

使用 `Tex`、`MathTex` 时还需要安装 LaTeX；普通图形和 `Text` 文字动画无需 LaTeX。

虚拟环境、IDE 配置以及生成的 `media/` 文件不提交到 Git。
